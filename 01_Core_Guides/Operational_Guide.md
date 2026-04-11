# Operational Guide

This guide explains how to run the AICA virtual stage and defines the operational conditions that must be satisfied during execution. It combines system startup, navigator usage, pickup/drop/transfer behavior, runtime checks, communication channels, and mission constraints into one practical document.

It includes operational guidance for both **QCar2** and **QDrone2**.

---

## Navigation

1. [System Execution Flow](#1-system-execution-flow)
2. [Before You Start](#2-before-you-start)
      - [Open QLabs and Load the Cityscape Map Manually](#open-qlabs-and-load-the-cityscape-map-manually)
      - [Run the Setup Environment File Manually](#run-the-setup-environment-file-manually)
3. [Automated System Startup](#3-automated-system-startup)
      - [Optional Manual Setup Before Running the BAT File](#optional-manual-setup-before-running-the-bat-file)
4. [Run the Game File (Mandatory)](#4-run-the-game-file-mandatory)
5. [Navigator Information](#5-navigator-information)
      - [QDrone2 Navigator](#51-qdrone2-navigator)
      - [QDrone2 Communication Channels and Ports](#511-qdrone2-communication-channels-and-ports)
      - [QCar2 Navigator](#52-qcar2-navigator)
      - [QCar2 Communication Channels and Ports](#521-qcar2-communication-channels-and-ports)
6. [Manual Control Details](#6-manual-control-details)
      - [QCar2 Manual Control](#61-qcar2-manual-control)
      - [QDrone2 Manual Control](#62-qdrone2-manual-control)
7. [Autonomous Control Details](#7-autonomous-control-details)
      - [QCar2 Autonomous Control](#71-qcar2-autonomous-control)
      - [QDrone2 Autonomous Control](#72-qdrone2-autonomous-control)
8. [Action Key Mapping and Intention Mapping](#8-action-key-mapping-and-intention-mapping)
      - [Python Action Keys for QDrone2](#81-python-action-keys-for-qdrone2)
      - [MATLAB / Simulink Intention Mapping](#82-matlab--simulink-intention-mapping)
9. [Pickup and Delivery Operations and Conditions](#9-pickup-and-delivery-operations-and-conditions)
      - [Drone Pickup](#91-drone-pickup)
      - [Car Pickup](#92-car-pickup)
      - [Drone Delivery](#93-drone-delivery)
      - [Car Delivery](#94-car-delivery)
10. [Transfer Operation and Conditions](#10-transfer-operation-and-conditions)
      - [Car to Drone Transfer](#101-car-to-drone-transfer)
      - [Drone to Car Transfer](#102-drone-to-car-transfer)
11. [Final Runtime Check, Mission Completion, and File Reference](#11-final-runtime-check-mission-completion-and-file-reference)
      - [Mission Timing and Completion](#mission-timing-and-completion)
      - [Final Runtime Check](#final-runtime-check)
      - [File Structure](#file-structure)
---

## 1) System Execution Flow

The overall execution flow is:

- **`setup_env.py`** or **`setup_env.m`** runs once at the beginning to prepare the simulation environment. These files should **NOT** be modified.
- **QLabs** loads the required map and acts as the shared simulation environment
- **Navigator Drone → Flight Stack Drone → RT Model Drone** controls the drone and updates it in QLabs.
- **Navigator Car → Drive Stack Car → RT Model Car** controls the car and updates it in QLabs
- **`game.py`** runs alongside QLabs and handles pickup logic, transfer timing, package behavior, and scoring. This should **NOT** be modified
- Together, these components run continuously until the mission is completed

---


## 2) Before You Start

Before running the system, make sure:

- all required software is installed
- your system meets the competition hardware requirements
- the required QLabs environment is available
- all competition files are placed in the correct folder
- the software setup steps have already been completed

For setup details, refer to: [System and Software Setup](../00_Portal/AICA_COMPETITION_GUIDE.md#system-and-software-setup)

### Open QLabs and Load the Cityscape Map Manually

1. Open **Quanser Interactive Labs** from the Windows Start menu, or go to `C:\Program Files\Quanser\Quanser Interactive Labs` and run the application.
2. Wait for QLabs to fully launch.
3. In QLabs, open **Self-Driving Car Studio**.
4. Select and load the **Cityscape** map.
5. Wait until the Cityscape environment finishes loading completely.
6. After the map is open, continue with the startup BAT file or run the required files manually.

### Important

- The virtual stage is designed to run in the **Cityscape** map.
- Make sure the Cityscape map is loaded before running the setup environment files for QCar2 and QDrone2.
- If the wrong map is open, the spawn locations, nodes, and delivery locations will not match the competition scenario.
- Always confirm the correct map is loaded before running `setup_env.py` or `setup_env.m`.

### Run the Setup Environment File Manually

If you do not want the BAT file to handle teh set up of vehicles, you can run the `setup environment` file manually after loading the Cityscape map.

Run one of the following depending on your workflow:

- **Python:** `python setup_env.py`
- **MATLAB:** run `setup_env.m`

This step spawns **QCar2** and **QDrone2** in the QLabs environment using the configured spawn location.

### Important

- Make sure QLabs is already open and the **Cityscape** map is loaded before running the spawn file.
- The setup environment file should be run only after the correct map is fully loaded.
- If vehicles are already spawned, avoid running the setup environment file again unless you want to reset the scenario.

---

## 3) Automated System Startup

A complete BAT launcher is provided for one-click startup.

Example: `run_all.bat`

This file is intended to:

1. open QLabs
2. load the required competition map
3. run the QCar2 and QDrone2 setup environment files (**Do not modify**)
4. start the RT models
    - `virtual_DriveStack.rt-win64` (**Do not modify**)
    - `virtual_FlightStack.rt-win64` (**Do not modify**)
5. arm both vehicles
6. command QDrone2 takeoff to hover altitude
7. run the selected navigator files or models
8. begin execution based on the selected mode

### Optional Manual Setup Before Running the BAT File

If QLabs is already open with the **Cityscape** map loaded, or if the vehicles have already been spawned manually, the corresponding steps in the BAT file may be commented out.

Examples:

- comment out the QLabs launch command if QLabs is already open
- comment out the map-loading step if the **Cityscape** map is already loaded
- comment out the setup environment step if `setup_env.py` or `setup_env.m` has already been run manually

### Important

- This launcher is intended to run the full startup workflow automatically, including the selected navigator files or models.
- It may be configured to use either **MATLAB / Simulink** or **Python**, depending on the version selected in the file.
- If you want to use the **Python** navigator files, make sure the Python commands are enabled in the BAT file.
- If you want to use the **MATLAB / Simulink** navigator files, make sure the MATLAB commands are enabled in the BAT file.
- By default, one version may be enabled and the other may be commented out, or you can start the navigator models separately by commenting out both versions in the BAT file.
- If manual setup steps have already been completed, users may comment out the corresponding BAT file lines before running it.
- Teams should review the BAT file before running to make sure it matches their intended workflow.

---

## 4) Run the Game File (**Mandatory — Do not modify**)

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

### Important

Without `game.py`:

- package pickup will not work correctly
- transfer operations will fail
- deliveries will not be tracked correctly
- scoring will not update

---

## 5) Navigator Information

### Performance Note

Commenting out unnecessary video subsystems can improve runtime performance and reduce computing resource requirements.

---

### 5.1 QDrone2 Navigator

The QDrone navigator supports:

- waypoint-based autonomous control
- manual control
- control mode switching
- intention mode switching
- camera streams, enabled as needed and disabled by default in the provided code and model

### Note

- **Manual control is available only in Python**
- **MATLAB / Simulink does not support manual control in the provided navigator files**

### QDrone2 Inputs

Users can provide:

- waypoints for autonomous control
- manual control commands
- autonomous or manual control mode
- autonomous or manual intention mode

### QDrone2 Intention List

- Nothing
- Pickup Small
- Drop
- Transfer from Car
- Transfer to Car

### 5.1.1 QDrone2 Communication Channels and Ports

QDrone2 uses fixed communication ports for the simulator, cameras, and game connection.

#### Camera and Sensor Ports

If camera support is enabled in Python, the following ports are used:

- **RealSense RGB + Depth Camera**
  - Address: `tcpip://localhost:18986`
  - Device ID: `0@tcpip://localhost:18986`
  - Mode: `RGB&DEPTH`
  - RGB resolution: `640 x 480`
  - Depth resolution: `640 x 480`

- **Right Camera**
  - Address: `tcpip://localhost:18982`
  - Camera ID: `0@tcpip://localhost:18982`
  - Resolution: `640 x 480`

- **Back Camera**
  - Address: `tcpip://localhost:18983`
  - Camera ID: `1@tcpip://localhost:18983`
  - Resolution: `640 x 480`

- **Left Camera**
  - Address: `tcpip://localhost:18984`
  - Camera ID: `2@tcpip://localhost:18984`
  - Resolution: `640 x 480`

- **Downward Camera**
  - Address: `tcpip://localhost:18985`
  - Camera ID: `3@tcpip://localhost:18985`
  - Resolution: `640 x 480`

#### Data and Game Ports

The provided QDrone2 Python code also uses:

- **Drone data stream**
  - Address: `tcpip://localhost:18373`
  - Agent mode: `C`
  - Send buffer size: `1460`
  - Receive buffer shape: `(1,16)` with `float64`
  - Receive buffer size: `1460`

- **Game stream**
  - Address: `tcpip://127.0.0.1:19001`
  - Agent mode: `C`
  - Send buffer size: `8`
  - Receive buffer shape: `(1,1)` with `float64`
  - Receive buffer size: `24`

#### Important

- These ports are part of the provided QDrone2 system used in the virtual stage.
- Teams should use these ports as documented.
- If camera streaming is not needed, disabling unused cameras can reduce runtime load.

#### Reference Python Section

For the Python section related to this communication setup, refer to: [QDrone2 Communication Python Section](QDrone2_communication.md)

---

### 5.2 QCar2 Navigator

The QCar navigator supports:

- node-based trajectory selection
- manual control
- velocity selection
- Intention commands
- camera stream, enabled as needed and disabled by default in the provided code and model

### Note

- **Manual control is available only in Python**
- **MATLAB / Simulink does not support manual control in the provided navigator files**

### QCar2 Inputs

Users can provide:

- start node
- end node
- velocity
- manual control commands
- intention commands

### QCar2 Intention List

- Nothing
- Pickup Small
- Pickup Large
- Drop
- Transfer from Drone
- Transfer to Drone

### 5.2.1 QCar2 Communication Channels and Ports

QCar2 uses fixed communication ports for simulator connection, sensors, and game connection.

#### Port Information

The QCar2 communication ports are documented below in the same format as QDrone2.

Example format:

- **Front Camera**
  - Address: `tcpip://localhost:PORT_NUMBER`
  - Resolution: `WIDTH x HEIGHT`
  - Frame rate: `VALUE`

- **Vehicle data stream**
  - Address: `tcpip://localhost:PORT_NUMBER`
  - Agent mode: `C`
  - Send buffer size: `VALUE`
  - Receive buffer size: `VALUE`

#### Important

- These ports are part of the provided QCar2 system used in the virtual stage.
- Teams should use the documented ports exactly as provided.
- If camera streaming is not needed, disabling unused sensors can reduce runtime load.

#### Reference Python Section

For the Python section related to this communication setup, refer to: [QCar2 Communication Python Section](QCar2_communication.md)

---

## 6) Manual Control Details

### 6.1 QCar2 Manual Control

QCar2 open-loop control uses two main inputs:

- **Velocity Command**
- **Steering Angle**

#### Input Limits

- velocity command range: `[-0.2, 0.2]`
- steering angle range: `[-0.6, 0.6]` rad

#### Keyboard Controls

- **Up Arrow** → positive velocity command
- **Down Arrow** → negative velocity command
- **No key pressed** → velocity command = `0`
- **Left Arrow** → negative steering angle
- **Right Arrow** → positive steering angle
- **M** → mode switch (Manual to Auto or Auto to Manual)

#### Manual Mode Summary for QCar2

Arrows:

- Up / Down → forward / backward velocity command
- Left / Right → steering command

---

### 6.2 QDrone2 Manual Control

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

## 7) Autonomous Control Details

This section describes how QCar2 and QDrone2 operate in autonomous mode.

### 7.1 QCar2 Autonomous Control

In autonomous mode, QCar2 uses node-based routing for path planning and motion execution.

Users can provide:

- start node
- end node
- desired velocity command

Based on the selected start node and end node, the controller computes:

- the path to follow through the node network
- steering commands
- velocity commands

#### QCar2 Node Map for Python

The following node map shows the node numbers that can be used for **QCar2 autonomous route planning in the Python version**.

**Pickup location:** Node **24**

<img src="../images/node_map_qcar2.png" alt="QCar2 Python node map" width="520">

#### Sample Autonomous Files

Sample files for autonomous operation are also provided in the `tools\` folder, including:

- `plan_path.py`
- `example.py`

For QCar2, `plan_path.py` provides a sample autonomous path-planning workflow in which a node-based route is generated and the QCar2 drives autonomously based on the selected node path.

#### Important

- Teams should use these node numbers when selecting QCar2 start and end nodes in Python.
- Node numbering may differ from MATLAB / Simulink, so always use the correct node reference for the selected workflow.
- The files in `tools\` are provided as sample references for autonomous planning and execution.

---

### 7.2 QDrone2 Autonomous Control

In autonomous mode, QDrone2 uses waypoint-based navigation to move between mission targets.

Users can provide:

- waypoint or target position
- desired autonomous motion target
- autonomous control mode
- autonomous intention mode

Based on the selected target, the controller computes:

- position tracking commands
- altitude control
- heading control
- motion toward the required pickup, drop, or transfer target

#### Sample Autonomous Files

Sample files for autonomous operation are also provided in the `tools\` folder, including:

- `city_voxel_map.npz`
- `occupancy_grid.txt`
- `profile_ramp.py`
- `qdrone2_plans.npz`
- `read_occupancy_grid.py`
- `example.py`

For QDrone2, these files provide sample references for map reading, waypoint generation, and autonomous motion planning.

#### Voxel Map and Occupancy Grid

The voxel map and occupancy grid files are provided as sample environment representations for autonomous planning.

- `city_voxel_map.npz` stores a sample 3D voxel representation of the environment
- `occupancy_grid.txt` provides a sample occupancy grid representation
- `read_occupancy_grid.py` can be used as a reference for reading and processing occupancy information
- `qdrone2_plans.npz` provides sample stored planning data for drone operation


---

## 8) Action Key Mapping and Intention Mapping

### 8.1 Python Action Keys for QDrone2

Default QDrone2 keys in Python:

- `6` → Pickup
- `7` → Drop
- `8` → Transfer from Car
- `9` → Transfer to Car
- `0` → Nothing / Reset intention

For QCar2, the same `0` key is used for resetting intention to Nothing.

---

### 8.2 MATLAB / Simulink Intention Mapping

In MATLAB / Simulink, intentions are set by changing the numeric constant going into the intention input.

This means:

- you do **not** press keyboard keys in the same way as Python
- instead, you manually set the desired numeric intention value in the model when running

#### Important Clarification

The Python keys and the MATLAB intention values are mapped to the same internal values used by `game.py`.

**For example**: Pressing **`6`** in Python may correspond to intention value `1` in MATLAB
  - Even though the visible key number is different, `game.py` interprets them as the same action.
  - Do not confuse **keyboard key number** with **internal intention value**. The behavior is the same in `game.py`. Only the way you trigger the intention differs between Python and MATLAB / Simulink.


---

## 9) Pickup and Delivery Operations and Conditions

Pickup and delivery actions are managed by `game.py` and require the vehicle to remain inside the valid region for the full action duration.

### Hold Time

- Pickup action duration: **3 seconds**
- Delivery action duration: **3 seconds**

### Note on Condition Checks

In the condition checks used in this guide, the term **target location** is used as a general meaning for the relevant task location.

Depending on the operation, the target location may refer to:

- the pickup location
- the drop location
- the transfer target location


---

### 9.1 QDrone2 Pickup

#### Exact Distance Requirement

A QDrone2 pickup is valid when all of the following are satisfied relative to the pickup location:

- horizontal distance must be **2.0 m or less**
- vertical offset must be between **0.0 m and 4.0 m**
- the condition must be maintained for the full **3 seconds**

#### Operational Description

If the QDrone2 is spawned near the central pickup or moved near a package:

1. move the QDrone2 into the valid pickup region
2. press the assigned pickup key
3. the timer starts in `game.py`
4. once the timer reaches **3 seconds**, the package attaches to the drone

#### QDrone2 Carry Capacity at a Time

QDrone2 can carry: **1 small package only**

#### Condition Interpretation

The QDrone2 condition check is based on horizontal distance and vertical offset between the QDrone1 and the target location.

#### Actual Condition Check

```python
np.hypot(dx, dy) <= 2.0 and 0.0 <= dz <= 4.0

```

where:

  - `dx` = difference in x-position between QDrone2 and the target location
  - `dy` = difference in y-position between QDrone2 and the target location
  - `dz` = difference in z-position between QDrone2 and the target location



### 9.2 QCar2 Pickup

#### Exact Distance Requirement

A QCar2 pickup is valid when all of the following are satisfied relative to the pickup location:

- distance from the QCar2 to the pickup point must be **less than 2.0 m**
- the condition must be maintained for the full **3 seconds**

#### Operational Description

For the QCar2:

1. stop the QCar2 near the pickup depot
2. press the assigned pickup key
3. the timer starts in `game.py`

The same pickup logic applies.

#### QCar2 Carry Capacity at a Time

QCar2 can carry:

- **2 small packages**
- or **1 large package**

#### Condition Interpretation

The QCar2 condition check is based on the distance between the current QCar2 position and the target location.

#### Actual Condition Check

```python
np.linalg.norm(loc_car - LOC_PICK) < 2.0
```

where:

  - `loc_car` = QCar2 current position
  - `LOC_PICK` = target location

### 9.3 QDrone2 Delivery

#### Exact Distance Requirement

A QDrone2 delivery is valid when all of the following are satisfied relative to the drop location:

- horizontal distance must be **2.0 m or less**
- vertical offset must be between **0.0 m and 4.0 m**
- the condition must be maintained for the full **3 seconds**

#### Operational Description

To deliver using the QDrone2:

1. move the QDrone2 into the valid drop region
2. hover in the required position range
3. press the assigned drop-off intention key
4. the timer begins in `game.py`
5. once the required time is completed, the package is dropped at the location

#### Window Delivery (QDrone2 Only)

Only **QDrone2** may perform window deliveries

---

### 9.4 QCar2 Delivery

#### Exact Distance Requirement

A QCar2 delivery is valid when all of the following are satisfied relative to the shared drop-off location:

- distance from the QCar2 to the shared drop-off location must be **less than 2.0 m**
- the QCar2 must remain stopped at the required location
- the condition must be maintained for the full **3 seconds**

#### Operational Description

To deliver using the QCar2:

1. move the QCar2 to the shared drop-off location
2. stop the QCar2 at the required location
3. press the assigned drop-off intention key
4. the timer begins in `game.py`
5. once the required time is completed, the package is dropped at the shared drop-off location

#### Shared Drop-Off Delivery

QCar2 and QDrone2 can both perform a shared drop-off delivery.

---

## 10) Transfer Operation and Conditions

Transfer can happen in both directions:

- **QCar2 → QDrone2**
- **QDrone2 → QCar2**

Both vehicles must use the correct intention values.

### Transfer Hold Time

- Transfer action duration: **3 seconds**

---

### 10.1 QCar2 to QDrone2 Transfer

#### Exact Distance Requirement

A QCar2 to QDrone2 transfer is valid when all of the following are satisfied relative to the car:

- horizontal distance from drone to car must be **2.0 m or less**
- vertical offset from drone to car must be between **0.0 m and 4.0 m**
- QCar2 must be stationary
- both vehicles must have the correct intention values set
- the condition must be maintained for the full **3 seconds**

#### Operational Description

To transfer from QCar2 to QDrone2:

1. stop the car at the desired transfer location
2. move the drone above or near the car within the valid transfer region
3. set the correct intention values on both vehicles

Now set intentions:

- QCar2 intention = **Transfer to Drone**
- QDrone2 intention = **Transfer from Car**

#### Important

Transfer will only work if:

- both vehicles are in the correct position
- both intention values are correctly set

If only one side is set, transfer will **not** occur.

#### Transfer Completion

- the timer begins in `game.py`
- after **3 seconds**, the package transfers from the QCar2 to QDrone2


---

### 10.2 QDrone2 to QCar2 Transfer

#### Exact Distance Requirement

A QDrone2 to QCar2 transfer is valid when all of the following are satisfied relative to the car:

- horizontal distance from QDrone2 to QCar2 must be **2.0 m or less**
- vertical offset from QDrone2 to QCar2 must be between **0.0 m and 4.0 m**
- QCar2 must be stationary
- both vehicles must have the correct intention values set
- the condition must be maintained for the full **3 seconds**

#### Operational Description

To transfer from QDrone2 to QCar2:

1. stop the QCar2 at the desired location
2. hover the QDrone2 above or near the QCar2 within the valid transfer region
3. set the correct intention values on both vehicles

Now set intentions:

- QDrone2 intention = **Transfer to Car**
- QCar2 intention = **Transfer from Drone**

#### Transfer Completion

- `game.py` starts the timer
- after **3 seconds**, the package transfers from the drone to the car

---

## 11) Final Runtime Check, Mission Completion, and File Reference

### Mission Timing and Completion

- Mission time begins at the official mission start.
- The mission objective is to minimize total completion time.
- If required deliveries are not completed, the mission is considered incomplete.

A delivery is considered complete only after the scenario logic confirms a valid delivery event.

### Important

- `game.py` manages pickup timing, transfer timing, delivery timing, and scoring.
- Teams should verify package completion behavior during runtime.

### Final Runtime Check

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

### Main File Types

The competition package includes the following types of files:

- **setup environment files** → prepare the QCar2 and QDrone2 simulation environment (**Do not modify**)
- **RT model files** → run the provided vehicle stack (**Do not modify**)
- **BAT files** → start the stack and automate execution
- **navigator files** → main files that teams run and modify for MATLAB / Simulink or Python operation
- **`game.py`** → backend mission logic, package handling, timing, and scoring (**Do not modify**)

### File Structure

```text
AICA_Competition_Files\
    setup_env.py                  (Do not modify)
    setup_env.m                   (Do not modify)
    QDrone2_Navigator.slx
    QDrone2_Navigator.py
    QCar2_Navigator.slx
    QCar2_Navigator.py
    run_all.bat
    spawn_location.txt
    virtual_DriveStack.rt-win64   (Do not modify)
    virtual_FlightStack.rt-win64  (Do not modify)
    game.py                       (Do not modify)
    tools\
        city_voxel_map.npz
        occupancy_grid.txt
        plan_path.py
        profile_ramp.py
        qdrone2_plans.npz
        read_occupancy_grid.py
        example.py    
```

#### Back to:

[Virtual Stage Competition Guide](../01_Core_Guides/Virtual_Stage_Competiton_Guide.md)

[AICA Home Portal](../00_Portal/AICA_PORTAL.md)