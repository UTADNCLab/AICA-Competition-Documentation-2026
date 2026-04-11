# What Is Provided

This page gives a simple overview of the main files provided for the competition and explains how they work together.

---

## Overview

The competition package includes files for setting up the scenario, starting the vehicle stack, running the mission logic, and developing the team solution.

In general:

- The organizers provide the scenario setup and backend mission logic
- Teams mainly work on the **navigator** files to implement their solution
- Some files must run in the background for scoring, package handling, pickup, and transfer logic
- Sample autonomous planning files are also provided in the `tools\` folder for reference

---

## Important Before You Start

Before using this guide, ensure that:

- All required software is installed
- Your system meets the hardware requirements
- The full setup process has been completed

For complete setup instructions, refer to: [System and Software Setup](../03_Setup/Software_Setup_Instructions.md)

---

## 1) Setup Environment Files

`setup_env` files are provided in both **Python (.py)** and **MATLAB (.m)**.

These files:

- set up the vehicles in QLabs
- load the scenario setup
- place vehicles and packages at the required starting positions
- prepare the environment for execution

### Files

- `setup_env.py` **(Do not modify)**
- `setup_env.m` **(Do not modify)**

### Important

- These files are required to correctly initialize the competition environment.
- Run the appropriate setup environment file before starting the mission workflow.
- These files should **NOT** be modified.

---

## 2) RT Model Files

The following RT model files are provided for the virtual stack:

- `virtual_DriveStack.rt-win64` **(Do not modify)**
- `virtual_FlightStack.rt-win64` **(Do not modify)**

These files are used to run the provided drive stack and flight stack in the virtual-stage environment.

### Important

- These RT model files should **NOT** be modified.
- RT model execution is handled through the provided BAT file.
- No separate manual step is required to run these RT model files in the standard workflow.
- `virtual_DriveStack.rt-win64` is used for **QCar2**.
- `virtual_FlightStack.rt-win64` is used for **QDrone2**.

---

## 3) BAT Startup File

### Complete Automation BAT

A fully automated BAT file is also provided.

This file will:

- open QLabs
- load the required map
- run the setup environment file
- start the RT model files
- launch the navigator files
- begin execution based on the selected mode (manual or autonomous)

---

## 4) Navigator Files

The main files teams will modify are the navigator files.

Separate navigator files are provided for both vehicles and both environments:

- **MATLAB / Simulink**
  - `QCar2_Navigator.slx`
  - `QDrone2_Navigator.slx`

- **Python**
  - `QCar2_Navigator.py`
  - `QDrone2_Navigator.py`

These files control the actual movement and behavior of the vehicles.

They are used to implement:

- manual or autonomous movement
- route following
- delivery strategy
- coordination between QCar2 and QDrone2

### Notes

- The **Python version** supports both manual and autonomous operation
- The **MATLAB / Simulink version** is focused on autonomous control
- If manual control is required, **Python is recommended**

Once started, the vehicles operate based on the selected mode and implemented logic.

---

## 5) Sample Autonomous Files in `tools\`

Sample files are also provided in the `tools\` folder as references for autonomous planning and map-based navigation.

These include:

- `city_voxel_map.npz`
- `occupancy_grid.txt`
- `plan_path.py`
- `profile_ramp.py`
- `qdrone2_plans.npz`
- `read_occupancy_grid.py`
- `Example.py`

### What These Files Are Used For

- `city_voxel_map.npz` provides a sample voxel map of the environment
- `occupancy_grid.txt` provides a sample occupancy grid representation
- `read_occupancy_grid.py` can be used as a reference for reading occupancy data
- `plan_path.py` provides a sample autonomous planning workflow for **QCar2**, where a node-based path is generated and the car drives autonomously
- `qdrone2_plans.npz` provides sample planning data for **QDrone2**
- `profile_ramp.py` and `Example.py` provide additional sample references for testing and autonomous execution logic

These files are provided as **sample references only** and can help teams understand how autonomous planning may be implemented for the car and drone.

---

## 6) Game File

The main backend mission file is:

- `game.py` **(Do not modify)**

This file handles the core scenario logic and must be running during execution.

It is responsible for:

- pickup timing
- transfer timing
- delivery timing
- package handling
- intention and command execution
- scenario progress
- scoring display in the QLabs window

### Important

- This file should **NOT** be modified.
- It must run together with the navigator files for correct system behavior.
- It is required for scoring, package logic, pickup logic, transfer logic, and delivery tracking.

Without this file:

- packages will not function correctly
- transfers may fail
- deliveries will not be tracked
- scoring will not be displayed

---

## 7) What Teams Need to Modify

Teams should mainly focus on the navigator files.

This is where teams develop their solution, including:

- path planning
- vehicle control
- mission logic
- coordination strategy
- pickup, transfer, and delivery behavior

The sample files in `tools\` may also be used as references when developing autonomous planning logic.

---

## 8) Summary

In simple terms:

- **Setup environment files** → set up the scenario **(Do not modify)**
- **RT model files** → run the provided vehicle stack **(Do not modify)**
- **BAT file** → start and automate execution
- **Navigator files** → where teams build their solution
- **Sample files in `tools\`** → reference files for autonomous planning and map handling
- **`game.py`** → handles backend logic and scoring **(Do not modify)**

---

### Back to:

[All Competition Resources](../04_Resources/All_Competition_Resources.md)

[AICA Portal](../00_Portal/AICA_PORTAL.md)