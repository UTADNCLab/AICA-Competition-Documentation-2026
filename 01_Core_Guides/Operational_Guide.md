# Operational Guide

This guide explains how to run the AICA virtual stage and defines the operational conditions that must be satisfied during execution. It combines system startup, navigator usage, pickup/drop/transfer behavior, runtime checks, and mission constraints into one practical document.

---

## Navigation

- [System Execution Flow](#1-system-execution-flow)
- [Before You Start](#2-before-you-start)
- [Automated System Startup](#3-automated-system-startup)
- [Run the Game File (Mandatory)](#4-run-the-game-file-mandatory)
- [Navigator Information](#5-navigator-information)
- [Manual Control Details](#6-manual-control-details)
- [Action Key Mapping and Intention Mapping](#7-action-key-mapping-and-intention-mapping)
- [Pickup Operation and Conditions](#8-pickup-operation-and-conditions)
- [Delivery Operation and Conditions](#9-delivery-operation-and-conditions)
- [Transfer Operation and Conditions](#10-transfer-operation-and-conditions)
- [Mission Timing and Completion](#11-mission-timing-and-completion)
- [Runtime Validation Checklist](#12-runtime-validation-checklist)
- [Common Errors and Notes](#13-common-errors-and-notes)
- [Files Reference](#14-files-reference)
- Path planning voxel Map autonmous control working will be added with the final files.
---

## 1) System Execution Flow

The overall execution flow is:  Need to discuss with Porf Koru and add here 

In simple terms:

- **`spawn_competition.py`** runs once at the beginning to prepare the simulation environment  
- **QLabs** loads the required map and acts as the shared simulation environment  
- **Navigator Drone → Flight Stack Drone → RT Model Drone** controls the drone and updates it in QLabs  
- **Navigator Car → Drive Stack Car → RT Model Car** controls the car and updates it in QLabs  
- **`game.py`** runs alongside QLabs and handles pickup logic, transfer timing, package behavior, and scoring  
- Together, these components run continuously until the mission is completed  

---

## 2) Before You Start

Before running the system, make sure:

- all required software is installed  
- your system meets the competition hardware requirements  
- the required QLabs environment is available  
- all competition files are placed in the correct folder  
- the software setup steps have already been completed  

For setup details, refer to:

- [System and Software Setup](../00_Portal/AICA_COMPETITION_GUIDE.md#system-and-software-setup)
- [What Is Provided](../01_Core_Guides/What_Is_Provided.md)

### Workflow Choice

Teams may use the provided **MATLAB / Simulink** files, the provided **Python** files, or a combination of both, depending on their preferred development workflow. It is not necessary to use only one environment. Teams may run part of their solution in MATLAB / Simulink and part in Python, provided the full system is configured correctly.

---

### Scenario Configuration

To change the spawn position of QCar2 and QDrone2 : Edit `spawn_location.txt` . This file controls the initial spawn location used in QLabs.


## 3) Automated System Startup

A complete BAT launcher is provided for one-click startup.

Example: `launch_full_stack.bat`

This file is intended to:

1. open QLabs  
2. load the required competition map  
3. spawn QCar2 and QDrone2 (Execute the spawn file) 
4. start the RT models  
5. arm both vehicles  (Start the Stack files for Qcar2 and Qdrone2)
6. command QDrone2 takeoff to hover altitude  
7. run the selected navigator files or models  
8. begin execution based on the selected mode  

### Important

- This launcher is intended to run the full startup workflow automatically, including the selected navigator files or models.
- It may be configured to use either **MATLAB / Simulink** or **Python**, depending on the version selected in the file.
- If you want to use the **Python** navigator files, make sure the Python commands are enabled in the BAT file.
- If you want to use the **MATLAB / Simulink** navigator files, make sure the MATLAB commands are enabled in the BAT file.
- By default, one version may be enabled and the other may be commented out or you can start the navigator models seperately by commenting out both version in BAT file.
- Teams should review and update the BAT file as needed before running.

---

## 4) Run the Game File (Mandatory)

Run:

    python game.py

This file is required for the scenario to work properly.

It handles:

- pickup timing  
- transfer timing  
- delivery timing  
- package movement and visualization in QLabs  
- intention-based scenario logic  
- score display in the QLabs window  

#### Important

Without `game.py`:

- package pickup will not work correctly  
- transfer operations will fail  
- deliveries will not be tracked correctly  
- scoring will not update  

---

## 5) Navigator Information

#### Performance Note: Commenting out unnecessary video subsystems can improve runtime performance and reduce computing resource requirements.


### 5.1 QDrone2 Navigator

The QDrone navigator supports:

- waypoint-based autonomous control  
- manual control  
- control mode switching  
- intention mode switching  
- camera stream (enabled as needed; disabled by default in the provided code and model)  

#### Note:

- **Manual control is available only in Python**
- **MATLAB / Simulink does not support manual control in the provided navigator files**
#### QDrone2 Inputs

Users can provide:

- waypoints for autonomous control  
- manual control commands  
- autonomous or manual control mode  
- autonomous or manual intention mode  

#### QDrone2 Intention List

- Nothing  
- Pickup Small  
- Drop  
- Transfer from Car  
- Transfer to Car  

---

### 5.2 QCar2 Navigator

The QCar navigator supports:

- node-based trajectory selection  
- manual control  
- velocity selection  
- action commands  
- camera stream (enabled as needed; disabled by default in the provided code and model)  

#### Note:

- **Manual control is available only in Python**
- **MATLAB / Simulink does not support manual control in the provided navigator files**

#### QCar2 Inputs

Users can provide:

- start node  
- end node  
- velocity  
- manual control commands  
- action commands  

#### QCar2 Intention List

- Nothing  
- Pickup Small  
- Pickup Large  
- Drop  
- Transfer from Drone  
- Transfer to Drone  

---

## 6) Manual Control Details

### 6.1 QCar2 Manual Control

QCar2 open-loop control uses two main inputs:

- **Velocity**
- **Steering**

#### Velocity Input

- `-1` = full backward speed  
- `0` = stop  
- `1` = full forward speed  

Here, `1` corresponds to about **13 m/s**.

#### Steering Input

- steering range: `[-0.6, 0.6]`

#### Keyboard Controls

- **Up Arrow** → velocity = `1`  
- **Down Arrow** → velocity = `-1`  
- **No key pressed** → velocity = `0`  
- **Left Arrow** → steering = `-0.5`  
- **Right Arrow** → steering = `0.5`  
- **M** → mode switch (Manual to Auto or Auto to Manual)  

#### Manual Mode Summary for QCar2

Arrows:

- Up / Down → forward / backward  
- Left / Right → steer left / right  

---

### 6.2 QCar2 Autonomous Control

In autonomous mode, the car uses:

- start node  
- end node  
- desired velocity  

The controller then computes:

- steering commands  
- velocity commands  

This is based on the selected planner and controller, such as node-based planning with Pure Pursuit tracking.

---

### 6.3 QDrone2 Manual Control

QDrone2 manual mode uses the following default keyboard controls:

- **W / S** → pitch forward / backward  
- **A / D** → roll left / right  
- **E / Q** → altitude up / down  
- **Z / X** → yaw left / right  
- **M** → mode switch (Manual to Auto or Auto to Manual)  

#### Default Motion Rates

- Pitch: about **0.5 m/s**  
- Roll: about **0.5 m/s**  
- Altitude: about **0.5 m/s**  
- Yaw: about **π/6 rad/s**  

Maximum drone speed is about **2.5 m/s**.

---

## 7) Action Key Mapping and Intention Mapping

### 7.1 Python Action Keys for QDrone2

Default QDrone2 keys in Python:

- `6` → Pickup  
- `7` → Drop  
- `8` → Transfer from Car  
- `9` → Transfer to Car  
- `0` → Nothing / Reset intention  

For QCar2, the same `0` key is used for resetting intention to Nothing.

---

### 7.2 MATLAB / Simulink Intention Mapping

In MATLAB / Simulink, intentions are set by changing the numeric constant going into the intention input.

This means:

- you do **not** press keyboard keys in the same way as Python  
- instead, you manually set the desired numeric intention value in the model when running  

#### Important Clarification

The Python keys and the MATLAB intention values are mapped to the same internal values used by `game.py`.

For example:

- pressing `6` in Python may correspond to intention value `1` in MATLAB  
- even though the visible key number is different, `game.py` interprets them as the same action  

#### Important

Do not confuse **keyboard key number** with **internal intention value**

The behavior is the same in `game.py`. Only the way you trigger the intention differs between Python and MATLAB / Simulink.

---

### Vehicle Speed Limits

- **QCar2** must not exceed the maximum speed of **13 m/s** in the scenario  
- **QDrone2** must not exceed the maximum speed of **2.5 m/s** in the scenario  
- Teams may operate below the maximum speed limits for stability, safety, or strategy  

---

## 8) Pickup Operation and Conditions

### 8.1 Drone Pickup

If the drone is spawned near the depot or moved near a package:

1. move the drone **1 m** above the small package  
2. press the assigned pickup key  
3. the timer starts in `game.py`  
4. once the timer reaches **3 seconds**, the package attaches to the drone  

#### Drone Carry Capacity at a time

QDrone2 can carry: **1 small package only**

#### Constraint

A drone pickup is valid only when:

- QDrone2 remains at the required pickup position  
- QDrone2 maintains the hover of 1 m above the location.
- the pickup condition is held for the full **3 seconds**

---

### 8.2 Car Pickup

For the car:

1. stop the car near the pickup depot  
2. press the assigned pickup key  
3. the timer starts in `game.py`  

The same pickup logic applies.

#### Car Carry Capacity at a time

QCar2 can carry: **2 small packages**, or  **1 large package**

#### Constraint

A car pickup is valid only when:

- QCar2 remains stationary at the pickup location  
- the pickup condition is maintained for the full **3 seconds**

---

## 9) Delivery Operation and Conditions

### 9.1 Drone Delivery

To deliver using the drone:

1. move the drone above the drop-off location  
2. hover in the required position  
3. press the assigned drop-off intention key  
4. the timer begins in `game.py`  
5. once the required time is completed, the package is dropped at the location  

#### Constraint

A drone drop is valid only when:

- QDrone2 remains in the required delivery position  
- the required hover of **1 m** above the drop off location is maintained  
- the condition is held for the full **3 seconds**

#### Window Delivery (Drone Only)

- Only **QDrone2** may perform window deliveries

---

### 9.2 Car Delivery

For the car:

1. move the car to the drop-off location  
2. stop at the required position  
3. press the assigned drop-off intention  
4. once the timer completes in `game.py`, the package is dropped near the road or drop-off pad  

#### Constraint

A car drop is valid only when:

- QCar2 stops and holds at the drop location  
- the hold condition is maintained for the full **3 seconds**

#### Common Drop Delivery

- QCar2 or QDrone2 may perform a common drop depending on the scenario rules

---

## 10) Transfer Operation and Conditions

Transfer can happen in both directions:

- **Car → Drone**
- **Drone → Car**

Both vehicles must use the correct intention values.

---

### 10.1 Car to Drone Transfer

To transfer from car to drone:

1. stop the car at the desired transfer location  
2. move the drone directly above the car  
3. make sure the drone is hovering about **1 meter above the car**

Now set intentions:

- car intention = **Transfer to Drone**
- drone intention = **Transfer from Car**

#### Constraint

A car-to-drone transfer is valid only when:

- QCar2 is stationary  
- QDrone2 is positioned directly above QCar2  
- QDrone2 maintains the **1 m above the car **alititude
- both vehicles have the correct intention values set  
- the transfer configuration is maintained for the full **3 seconds**

#### Important

Transfer will only work if:

- both vehicles are in the correct position  
- both intention values are correctly set  

If only one side is set, transfer will **not** occur.

#### Transfer Completion

- the timer begins in `game.py`  
- after **3 seconds**, the package transfers from the car to the drone  

Then both vehicles can continue moving based on your design.

---

### 10.2 Drone to Car Transfer

To transfer from drone to car:

1. stop the car at the desired location  
2. hover the drone above the car  
3. keep the drone about **1 meter above the car**

Now set intentions:

- drone intention = **Transfer to Car**
- car intention = **Transfer from Drone**

#### Constraint

A drone-to-car transfer is valid only when:

- QCar2 is stationary  
- QDrone2 is positioned directly above QCar2  
- QDrone2 maintains the required transfer altitude  
- both vehicles have the correct intention values set  
- the transfer configuration is maintained for the full **3 seconds**

#### Transfer Completion

- `game.py` starts the timer  
- after **3 seconds**, the package transfers from the drone to the car  

Then both vehicles can continue moving.

---

## 11) Mission Timing and Completion

- Mission time begins at the official mission start  
- The mission objective is to minimize total completion time  
- If required deliveries are not completed, the mission is considered incomplete  

A delivery is considered complete only after the scenario logic confirms a valid delivery event.

### Important

- `game.py` manages pickup timing, transfer timing, delivery timing, and scoring
- Teams should verify package completion behavior during runtime

---

## 12) Runtime Validation Checklist

Before running a full mission, verify the following:

- both vehicles are spawned  
- both vehicles are armed  
- drone has taken off and is hovering stably  
- the virtual stack is running  
- the navigator files are running  
- `game.py` is running  
- pickup actions are working  
- drop actions are working  
- transfer actions are working  
- score display is visible in QLabs  

---

## 13) Common Errors and Notes

---

### Transfer Requires Both Sides

For transfer to work:

- both vehicles must be positioned correctly  
- both intention values must be set correctly  

If one is missing, transfer will fail.

---

### `game.py` Must Always Be Running

Without `game.py`:

- package timing will not work  
- scoring will not update  
- package movement will not be shown correctly  

---

## 14) Files Reference

### Main File Types

The competition package includes the following types of files:

- **spawn files** → set up the vehicles and scenario  
- **BAT files** → start the stack and automate execution  
- **navigator files** → these are the main files teams run and modify for MATLAB / Simulink or Python operation
- **`game.py`** → backend mission logic and scoring  

### File Structure

    Competition_Folder\
        spawn_competition.m
        spawn_competition.py
        Navigator.slx
        navigator.py
        navigator_QCar2.slx
        navigator_QCar2_python.py
        launch_full_stack.bat
        spawn_location.txt
        PATH PLANNING FILES
        VOXEL MAP FILES 
        game.py

---

#### Back to:

[Virtual Stage Competition Guide](Virtual_Stage_Competiton_Guide.md)

[AICA Home Portal](../00_Portal/AICA_PORTAL.md)
