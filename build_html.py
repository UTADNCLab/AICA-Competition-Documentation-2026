import re
import html
from pathlib import Path
import markdown

ROOT = Path(__file__).parent.resolve()

EXCLUDE = {"TODO.md"}
STYLE_PATH_FROM_ROOT = "/styles.css"

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text or "section"

def convert_md_links(md_text: str) -> str:
    # Convert markdown links pointing to .md into .html
    # [Text](path/file.md#anchor) -> [Text](path/file.html#anchor)
    pattern = re.compile(r"(\[[^\]]+\]\()([^)]+?\.md)(#[^)]+)?(\))")
    def repl(m):
        start, link, anchor, end = m.groups()
        return f"{start}{link[:-3]}.html{anchor or ''}{end}"
    return pattern.sub(repl, md_text)

def convert_html_links(html_text: str) -> str:
    # Convert generated HTML hrefs with .md to .html
    html_text = re.sub(r'href="([^"]+?)\.md(#.*?)?"', lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', html_text)
    return html_text

def page_template(title: str, body_html: str, rel_css: str, source_md: str) -> str:
    safe_title = html.escape(title)
    source_md_escaped = html.escape(source_md)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{safe_title}</title>
  <link rel="stylesheet" href="{rel_css}" />
</head>
<body>
  <div class="page-wrap">
    <main class="portal-card">
      <header class="hero hero-no-banner">
        <div class="hero-content">
          <p class="hero-kicker">IEEE SMC 2026 • Quanser • UTA</p>
          <h1>{safe_title}</h1>
          <p class="hero-sub">Rendered from: {source_md_escaped}</p>
        </div>
      </header>
      <section class="content markdown-content">
        {body_html}
      </section>
    </main>
  </div>
</body>
</html>
"""

def first_heading(md_text: str, fallback: str) -> str:
    for line in md_text.splitlines():
        m = re.match(r"^\s*#{1,6}\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return fallback

def build_one(md_path: Path):
    rel_md = md_path.relative_to(ROOT)
    out_path = md_path.with_suffix(".html")
    rel_out = out_path.relative_to(ROOT)

    raw = md_path.read_text(encoding="utf-8", errors="replace")
    raw = raw.replace("\ufeff", "")
    raw = convert_md_links(raw)

    md = markdown.Markdown(extensions=["fenced_code", "tables", "toc"])
    body = md.convert(raw)
    body = convert_html_links(body)

    title = first_heading(raw, rel_md.stem)

    rel_css = STYLE_PATH_FROM_ROOT

    final_html = page_template(title, body, rel_css, str(rel_md).replace("\\", "/"))
    out_path.write_text(final_html, encoding="utf-8")
    print(f"Built: {rel_out}")

def main():
    md_files = sorted(ROOT.rglob("*.md"))
    for md_path in md_files:
        if md_path.name in EXCLUDE:
            continue
        if ".git" in md_path.parts:
            continue
        build_one(md_path)

    # Ensure root index mirrors 00_Portal/AICA_PORTAL.html
    portal_html = ROOT / "00_Portal" / "AICA_PORTAL.html"
    index_html = ROOT / "index.html"
    if portal_html.exists():
        index_html.write_text(portal_html.read_text(encoding="utf-8"), encoding="utf-8")
        print("Built: index.html (mirrored from 00_Portal/AICA_PORTAL.html)")

if __name__ == "__main__":
    main()
