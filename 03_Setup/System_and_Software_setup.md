# System and Software Setup

## Hardware Requirements

Recommended hardware specifications for the SMC AICA 2026 competition.


| Tier | CPU | RAM | GPU |
|---|---|---|---|
| Minimum Specifications | Intel Core Ultra 5 / Intel Core i5 / Ryzen 5 | 8GB | Intel Iris Xe or Intel Arc integrated GPU |
| Recommended Specifications | Intel Core Ultra 7 / Intel Core i7 / Ryzen 7 | 16GB | Intel Arc integrated GPU or discrete GPU (e.g., NVIDIA GeForce RTX 3050) |
| Recommended Research Specifications | Intel Core Ultra 7 / Intel Core i7 / Ryzen 7 | 32GB | Discrete GPU (e.g., NVIDIA GeForce RTX 3050) |


## Software Setup & Installation

Required software installation and configuration before running the SMC AICA 2026 Competition Files Package.


## Step 1 - Download 

Download the SMC AICA 2026 Competition Files Package to the system. This can be done using `Git` or by downloading the files as a `.zip` archive. It is recommended to store the files in `C:\Users\<YourUsername>\Documents\Quanser`.


### With Git

1. Install [Git](https://git-scm.com/downloads).
2. Open a windows terminal in `C:\Users\<YourUsername>\Documents`.
3. Run the following command to create the Quanser directory and copy the contents of this repo in there.

```text
git clone https://github.com/UTADNCLab/IEEE-SMC-AICA-Competition-2026.git Quanser
```

### Without Git (ZIP)

1. Create a folder named Quanser under Documents on the system. The directory should be `C:\Users\<Username>\Documents\Quanser`. Then open the repository on GitHub: [IEEE SMC AICA Competition 2026](https://github.com/UTADNCLab/IEEE-SMC-AICA-Competition-2026.git).
2. Click the green Code button at the top of the GitHub page, then select Download ZIP from the menu.
3. Unzip the folder in the system.
4. Open `IEEE-SMC-AICA-Competition-2026-main` (containing folders`0_libraries`, `1_setup`, `2_SMC_AICA_2026_Competition_Files`). Copy all contents into the newly created `C:\Users\<Username>\Documents\Quanser` folder.


### Expected Local Layout

```text

C:\Users\<YourUsername>\Documents\Quanser\
    0_libraries\
    1_setup\
    2_SMC_AICA_2026_Competition_Files\

```

For additional information on Quanser Academic resources refer: [Quanser_Academic_Resources](https://github.com/quanser/Quanser_Academic_Resources)


## Step 2 - Install Required Software

### Install Python

Download Python (Python 3.12 recommended): [Python Official Downloads](https://www.python.org/downloads/). On the first screen of the installer, make sure to check **Add Python to PATH**. If you download Python from the official Python website, do not use the Python Install Manager.

Install NumPy using the following command:

```text
python -m pip install numpy
```

### Install Quanser SDK

Download the Quanser SDK for Windows from the following GitHub repository: [Quanser SDK](https://github.com/quanser/quanser_sdk_win64)


### If using  MATLAB/Simulink

Download MATLAB (2023a or later): [MATLAB for Windows](https://www.mathworks.com/downloads/)

In MATLAB, download Quanser Interactive Labs for MATLAB via Add-On Explorer.

<figure class="small-ui-figure">
  <img src="../images/Matlab_Get_Add_on.png" alt="MATLAB Add-Ons menu">
</figure>

![Quanser Interactive Labs for MATLAB](../images/Quanser_Interactive_lab_for_matlab_.png)

Follow the instructions in the Getting Started section of Quanser Interactive Labs for MATLAB to properly install Quanser Interactive Labs. Run `QLabs.setup` and complete the installation process before continuing with this guide.



### Install Quanser Interactive Labs (QLabs)

If the QLabs has been properly installed in previous section, skip this step.

Download the QLabs: [QLabs Get Started](https://qlabs.quanserdocs.com/en/latest/Get%20Started.html)


## Step 3 - Check System Requirements

Navigate to:

```text
C:\Users\<YourUsername>\Documents\Quanser\1_setup\
```

Run `step_1_check_requirements` and select your mode:

|Selection| Software you want to use |Device Usuage |
|-----|------|-----------|
|If only using Python| Python Only (Option 1) |  Virtual Only (Option 1) |
|If only using MATLAB| MATLAB Only (Option 2) |  Virtual Only (Option 1) |
|If using both | Both Python + MATLAB (Option 3)| Virtual Only (Option 1)|


| Workflow | Software Selection | Device Usage Selection |
|---|---|---|
| Python Only | ![Python Software Option](../images/python_setup_selection_in_bat_file.png) | ![Python Device Option](../images/python_setup_selection_part_2_in_bat_file.png) |
| MATLAB Only | ![MATLAB Software Option](../images/matlab_setup_selection_in_bat_file.png) | ![MATLAB Device Option](../images/python_setup_selection_part_2_in_bat_file.png) |
| Python + MATLAB | ![Both Software Option](../images/botj_setup_selection_in_bat_file.png)   | ![Both Device Option](../images/python_setup_selection_part_2_in_bat_file.png) |


Make sure system diagnosis is complete before proceeding to Step 4. 


## Step 4 - Configure Environment

From `C:\Users\<YourUsername>\Documents\Quanser\1_setup\`:

- Run `configure_python.bat` for Python workflow only
- Run `configure_matlab.bat` for MATLAB workflow only
- Run both files if using Python and MATLAB

Restart your system after all configuration steps are complete.


### Back to [ AICA Home Portal](../00_Portal/AICA_PORTAL.md)

