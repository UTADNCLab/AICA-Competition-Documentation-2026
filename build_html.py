from pathlib import Path
import markdown
import re
import html as html_lib

MD_EXT = ".md"


def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def title_from_markdown(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return fallback


def normalize_internal_href(href: str, source_md: Path) -> str:
    href = href.strip()
    if not href:
        return href

    if href.startswith(("http://", "https://", "mailto:", "#")):
        return href

    anchor = ""
    if "#" in href:
        href, anchor = href.split("#", 1)
        anchor = "#" + anchor

    if href == "":
        return anchor if anchor else href

    if href.endswith(".md"):
        href = href[:-3] + ".html"

    target = (source_md.parent / href).resolve()
    repo_root = Path(".").resolve()

    try:
        rel = target.relative_to(repo_root).as_posix()
        return rel + anchor
    except Exception:
        clean = href.lstrip("./")
        return clean + anchor


def rewrite_links_for_output(html: str, source_md: Path, output_path: Path) -> str:
    def repl(match):
        prefix, url, suffix = match.groups()

        if url.startswith(("http://", "https://", "mailto:")):
            return f'{prefix}{url}{suffix}'

        if url.startswith("#"):
            anchor_text = url[1:]
            return f'{prefix}#{slugify(anchor_text)}{suffix}'

        normalized = normalize_internal_href(url, source_md)

        if "#" in normalized:
            base, frag = normalized.split("#", 1)
            normalized = f"{base}#{slugify(frag)}"

        if output_path.parent == Path("."):
            final = normalized
        else:
            base = Path(normalized.split("#", 1)[0]).as_posix()
            depth = len(output_path.parent.parts)
            final = "../" * depth + base
            if "#" in normalized:
                final = final + "#" + normalized.split("#", 1)[1]

        return f'{prefix}{final}{suffix}'

    return re.sub(r'(href=")([^"]*)(")', repl, html)


def css_href_for(output_path: Path) -> str:
    depth = len(output_path.parent.parts)
    if depth == 0:
        return "styles.css"
    return "../" * depth + "styles.css"


def add_heading_ids(content_html: str) -> str:
    def repl(m):
        tag = m.group(1)
        inner = m.group(2)
        text = re.sub(r"<[^>]+>", "", inner).strip()
        hid = slugify(text)
        if not hid:
            return m.group(0)
        return f'<{tag} id="{hid}">{inner}</{tag}>'

    return re.sub(r"<(h[1-6])>(.*?)</\\1>", repl, content_html, flags=re.IGNORECASE | re.DOTALL)


def strip_first_h1(content_html: str, page_title: str) -> str:
    """
    Remove the first H1 from markdown body if it matches the page title.
    Works whether the H1 has an id attribute or not.
    """
    normalized_title = re.sub(r"\s+", " ", html_lib.escape(page_title).strip())
    pattern = re.compile(
        r'^\s*<h1(?:\s+[^>]*)?>\s*(.*?)\s*</h1>\s*',
        re.IGNORECASE | re.DOTALL
    )

    match = pattern.match(content_html)
    if not match:
        return content_html

    h1_inner = re.sub(r"<[^>]+>", "", match.group(1)).strip()
    h1_inner = re.sub(r"\s+", " ", h1_inner)

    if h1_inner == normalized_title:
        return content_html[match.end():]

    return content_html


def clean_html_text(text: str) -> str:
    """Strip tags and normalize whitespace."""
    text = re.sub(r"<[^>]+>", "", text)
    text = html_lib.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def color_package_type_tables(content_html: str) -> str:
    """
    Find tables with a 'Package Type' column and add CSS classes to those cells:
      Pickup -> package-pickup
      Small  -> package-small
      Large  -> package-large
    """

    def process_table(match):
        table_html = match.group(0)

        # Find all table rows
        rows = re.findall(r"<tr>(.*?)</tr>", table_html, flags=re.IGNORECASE | re.DOTALL)
        if not rows:
            return table_html

        # Find the header row that contains <th>
        header_row = None
        for row in rows:
            if "<th" in row.lower():
                header_row = row
                break

        if not header_row:
            return table_html

        headers = re.findall(r"<th[^>]*>(.*?)</th>", header_row, flags=re.IGNORECASE | re.DOTALL)
        header_texts = [clean_html_text(h).lower() for h in headers]

        try:
            package_idx = header_texts.index("package type")
        except ValueError:
            return table_html

        # Add table class
        table_html = re.sub(
            r"<table>",
            '<table class="package-type-table">',
            table_html,
            count=1,
            flags=re.IGNORECASE
        )

        def process_row(row_match):
            row_html = row_match.group(0)

            # Skip header rows
            if "<th" in row_html.lower():
                return row_html

            tds = re.findall(r"<td[^>]*>(.*?)</td>", row_html, flags=re.IGNORECASE | re.DOTALL)
            if package_idx >= len(tds):
                return row_html

            package_value = clean_html_text(tds[package_idx]).lower()

            css_class = None
            if package_value == "pickup":
                css_class = "package-pickup"
            elif package_value == "small":
                css_class = "package-small"
            elif package_value == "large":
                css_class = "package-large"

            if not css_class:
                return row_html

            td_pattern = re.compile(r"(<td[^>]*>)(.*?)(</td>)", re.IGNORECASE | re.DOTALL)

            td_matches = list(td_pattern.finditer(row_html))
            if package_idx >= len(td_matches):
                return row_html

            target_td = td_matches[package_idx]
            start_tag, inner_html, end_tag = target_td.groups()
            replacement = f'{start_tag}<span class="{css_class}">{inner_html}</span>{end_tag}'

            return row_html[:target_td.start()] + replacement + row_html[target_td.end():]

        table_html = re.sub(r"<tr>.*?</tr>", process_row, table_html, flags=re.IGNORECASE | re.DOTALL)
        return table_html

    return re.sub(r"<table>.*?</table>", process_table, content_html, flags=re.IGNORECASE | re.DOTALL)


def render_page(content_html: str, page_title: str, css_href: str) -> str:
    content_html = add_heading_ids(content_html)
    content_html = strip_first_h1(content_html, page_title)
    content_html = color_package_type_tables(content_html)

    banner_href = css_href_for(Path("index.html")) if css_href == "styles.css" else "../" * css_href.count("../") + "images/banner.png"
    if css_href == "styles.css":
        banner_href = "images/banner.png"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{page_title}</title>
  <link rel="stylesheet" href="{css_href}" />
  <style>
    .package-pickup {{
      color: #2e9b47;
      font-weight: 700;
    }}

    .package-small {{
      color: #c83a3a;
      font-weight: 700;
    }}

    .package-large {{
      color: #2f66d0;
      font-weight: 700;
    }}
  </style>
</head>
<body>
  <div class="page-wrap">
    <main class="portal-card">
      <header class="hero">
        <img src="{banner_href}" alt="AICA Competition Banner" class="hero-banner" />
        <div class="hero-content">
          <h1>{page_title}</h1>
        </div>
      </header>
      <section class="content markdown-body">
        {content_html}
      </section>
    </main>
  </div>
</body>
</html>
"""


def convert_markdown_file(md_path: Path):
    rel = md_path.as_posix()
    out_path = md_path.with_suffix(".html")
    md_text = md_path.read_text(encoding="utf-8")
    page_title = title_from_markdown(md_text, md_path.stem)

    raw_html = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    body_html = rewrite_links_for_output(raw_html, md_path, out_path)
    css_href = css_href_for(out_path)
    final_html = render_page(body_html, page_title, css_href)

    out_path.write_text(final_html, encoding="utf-8")
    print(f"generated: {rel} -> {out_path.as_posix()}")


def generate_root_index_from_portal():
    """
    Generate root index.html directly from 00_Portal/AICA_PORTAL.md
    so root-relative links and styles are correct.
    """
    portal_md = Path("00_Portal/AICA_PORTAL.md")
    if not portal_md.exists():
        return

    md_text = portal_md.read_text(encoding="utf-8")
    page_title = title_from_markdown(md_text, portal_md.stem)

    raw_html = markdown.markdown(md_text, extensions=["tables", "fenced_code"])
    body_html = rewrite_links_for_output(raw_html, portal_md, Path("index.html"))
    final_html = render_page(body_html, page_title, "styles.css")

    Path("index.html").write_text(final_html, encoding="utf-8")
    print("generated: index.html from 00_Portal/AICA_PORTAL.md")


def generate_all():
    root = Path(".")
    md_files = [p for p in root.rglob(f"*{MD_EXT}") if ".git" not in p.parts]

    for md_file in md_files:
        convert_markdown_file(md_file)

    # Generate root homepage directly from portal markdown
    generate_root_index_from_portal()


if __name__ == "__main__":
    generate_all()