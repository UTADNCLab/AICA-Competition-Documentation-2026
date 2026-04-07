# What Is Provided

This page gives a simple overview of the main files provided for the competition and explains how they work together.

---

## Overview

The competition package includes files for spawning the scenario, starting the vehicle stack, running the mission logic, and developing the team solution.

In general:

- The organizers provide the scenario setup and backend mission logic  
- Teams mainly work on the **navigator** files to implement their solution  
- Some files must run in the background for scoring, package handling, pickup, and transfer logic  

---

## Important Before You Start

Before using this guide, ensure that:

- All required software is installed  
- Your system meets the hardware requirements  
- The full setup process has been completed  

For complete setup instructions, refer to: [System and Software Setup](../00_Portal/AICA_COMPETITION_GUIDE_BLOCK_A.md#system-and-software-setup)

This page is a **quick overview guide**.  
For detailed steps, refer to the [Operational Guide](../01_Core_Guides/Execution_Guide.md).

---

## 1) Spawn Files

Spawn files are provided in both **Python (.py)** and **MATLAB (.m)**.

These files:

- spawn the vehicles in QLabs  
- load the scenario setup  
- place vehicles and packages at the required starting positions  
- start the required RT model  

These files only set up the environment. They do **not** execute the mission logic.

---

## 2) BAT Files / Startup Files

Two types of BAT files are provided:

### Complete Automation BAT

A fully automated BAT file is also provided.

This file will:

- open QLabs  
- load the required map  
- run the spawn file  
- start the virtual stack  
- launch the navigator files  
- begin execution based on the selected mode (manual or autonomous)  

This provides a one-step way to run the full system.

---

## 3) Navigator Files

The main files teams will modify are the navigator files.

Separate navigator files are provided for both vehicles and both environments:

- **MATLAB / Simulink**
  - `navigator_car.slx`
  - `navigator_drone.slx`

- **Python**
  - `navigator_car.py`
  - `navigator_drone.py`

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

## 4) Game File

The main backend mission file is:

- **`game.py`**

This file handles the core scenario logic and must be running during execution.

It is responsible for:

- pickup timing  
- transfer timing  
- delivery timing  
- package handling  
- intention/command execution  
- scenario progress  
- scoring display in the QLabs window  

### Important

- This file should **not be modified**  
- It must run together with the navigator files for correct system behavior  

Without this file:

- packages will not function correctly  
- transfers may fail  
- deliveries will not be tracked  
- scoring will not be displayed  

---

## 5) What Teams Need to Modify

Teams should mainly focus on the navigator files.

This is where teams develop their solution, including:

- path planning  
- vehicle control  
- mission logic  
- coordination strategy  
- pickup, transfer, and delivery behavior  

Once the system is running correctly, development should focus on improving the navigator logic.

---

## 6) Summary

In simple terms:

- **Spawn files** → set up the scenario  
- **BAT files** → start and automate execution  
- **Navigator files** → where teams build their solution  
- **`game.py`** → handles backend logic and scoring  

---

### Back to:

[All Competition Resources](../04_Resources/All_Competition_Resources.md)

[AICA Portal](../00_Portal/AICA_PORTAL.md)

