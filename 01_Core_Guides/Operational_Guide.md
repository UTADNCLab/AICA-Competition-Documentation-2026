# Operational Guide

This guide explains how to run the AICA virtual stage and defines the operational conditions that must be satisfied during execution. It combines system startup, navigator usage, pickup/drop/transfer behavior, runtime checks, communication channels, and mission constraints.

It includes operational guidance for both **QCar2** and **QDrone2**.

---

## Navigation

1. [System Execution Flow](#1-system-execution-flow)
2. [Before You Start](#2-before-you-start)
      - [Open QLabs and Load the Cityscape Map Manually](#open-qlabs-and-load-the-cityscape-map-manually)
3. [Automated System Startup](#3-automated-system-startup)
4. [Game File (Do not modify)](#4-game-file-do-not-modify)
5. [Navigator Information](#5-navigator-information)
      - [QDrone2 Navigator](#51-qdrone2-navigator)
      - [QDrone2 Communication Channels and Ports](#511-qdrone2-communication-channels-and-ports)
      - [QCar2 Navigator](#52-qcar2-navigator)
      - [QCar2 Communication Channels and Ports](#521-qcar2-communication-channels-and-ports)
6. [Autonomous Control Details](#6-autonomous-control-details)
      - [QCar2 Autonomous Control](#61-qcar2-autonomous-control)
      - [QDrone2 Autonomous Control](#62-qdrone2-autonomous-control)
7. [Pickup and Delivery Operations and Conditions](#7-pickup-and-delivery-operations-and-conditions)
      - [Drone Pickup](#71-drone-pickup)
      - [Car Pickup](#72-car-pickup)
      - [Drone Delivery](#73-drone-delivery)
      - [Car Delivery](#74-car-delivery)
8. [Transfer Operation and Conditions](#8-transfer-operation-and-conditions)
      - [Car to Drone Transfer](#81-car-to-drone-transfer)
      - [Drone to Car Transfer](#82-drone-to-car-transfer)
9. [Final Runtime Check, Mission Completion, and File Reference](#9-final-runtime-check-mission-completion-and-file-reference)
      - [Mission Timing and Completion](#mission-timing-and-completion)
      - [Final Runtime Check](#final-runtime-check)
      - [File Structure](#file-structure)
---

## 1) System Execution Flow

The overall execution flow is as follows:

- **QLabs** loads the required map and serves as the simulation environment.
- **`setup_env.py`** runs once at the start to load the vehicles and their corresponding real-time models **(RT models)**. This file should **NOT** be modified.

**Note:** This file reads the initial positions and headings of the vehicles from `spawn_locations.txt`. Competitors may modify `spawn_locations.txt` to set custom spawn locations.

- **RT Model QDrone2** simulates the actuators and sensors of the QDrone2. Competitors only need to load this model.
- **Virtual FlightStack** executes the controllers, sensor fusion algorithms, and core drone functions. Competitors only need to load this model.
- **QDrone2 Navigator** sends waypoints to the Virtual FlightStack, reads vehicle states from it, and sends the QDrone2 intention to `game.py`.

**Note:** Competitors are expected to develop the **QDrone2 Navigator**. Specifically, they must send the correct waypoints and intentions to execute their delivery plan. Example implementations in both Python and MATLAB/Simulink are provided in the Competition Package and may be used as a reference or modified as needed.

- **RT Model QCar2** simulates the actuators and sensors of the QCar2. Competitors only need to load this model.
- **Virtual DriveStack** executes the sensor fusion algorithms and core car functions. Competitors only need to load this model.
- **QCar2 Navigator** sends velocity and steering commands to the Virtual DriveStack, reads vehicle states from it, and sends the QCar2 intention to `game.py`.

**Note:** Competitors are expected to develop the **QCar2 Navigator**. Specifically, they must send the correct velocity commands, steering commands, and intentions to execute their delivery plan. A controller for autonomous driving must be implemented within the QCar2 Navigator. Example implementations in both Python and MATLAB/Simulink are provided in the Competition Package and may be used as a reference or modified as needed.

- The **QDrone2 Navigator** and **QCar2 Navigator** can each be developed in **Python** or **MATLAB/Simulink**.
- **`game.py`** enforces the game rules, handles pickup, vehicle-to-vehicle transfer, and drop-off logic, and tracks scoring. This file should **NOT** be modified.
- All components must be loaded and run continuously until the mission is complete. A batch file `run_all.bat` is provided to load all components for Python-based Navigator implementations, and `run_all.m` is provided for MATLAB/Simulink implementations.

---


## 2) Before You Start

Before running the system, make sure:

- all required software is installed
- your system meets the competition hardware requirements
- the required QLabs environment is available
- all competition files are placed in the correct folder
- the software setup steps have already been completed

For setup details, see the [System and Software Setup](../00_Portal/AICA_COMPETITION_GUIDE.md#system-and-software-setup)

### Open QLabs and Load the Cityscape Map Manually

1. Open **Quanser Interactive Labs** from the Windows Start menu, or go to `C:\Program Files\Quanser\Quanser Interactive Labs` and run the application.
2. Wait for QLabs to fully launch.
3. In QLabs, open **Self-Driving Car Studio**.
4. Select and load the **Cityscape** map.
5. Wait until the Cityscape environment finishes loading completely.
6. After the map is open, continue with `run_all.BAT` or `run_all.m` or run the required files manually.

### Important

- The virtual stage is designed to run in the **Cityscape** map.
- Make sure the Cityscape map is loaded.
- If the wrong map is open, the spawn locations, nodes, and delivery locations will not match the competition scenario.

---

## 3) Automated System Startup

A complete BAT launcher is provided for one-click startup.

Example: `run_all.bat`

This file is intended to:

1. run the setup environment file **(setup_env.py)**
2. start the models 
    - `virtual_DriveStack.rt-win64`
    - `virtual_FlightStack.rt-win64` 
3. start the models 
    - `QCar2_Navigator.py`
    - `QDrone2_Navigator.py`
4. run the game file **(game.py)**

Example: `run_all.m`

This file is intended to:

1. run the setup environment file **(setup_env.py)**
2. start the models 
    - `virtual_DriveStack.rt-win64`
    - `virtual_FlightStack.rt-win64` 
3. start the models 
    - `QCar2_Navigator.slx`
    - `QDrone2_Navigator.slx`
4. run the game file **(game.py)**

---

## 4) Game File (**Do not modify**)

Run:

    python game.py

**Note:** If you have several Python Versions you can use `py -3.12 game.py` which specifies the version. 

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
- publishing intention
- camera streams, enabled as needed and disabled by default in the provided code and model
- sensor readings


### QDrone2 Intention List

    0: Nothing

    1: Pickup Small

    2: Pickup Large

    3: Drop

    4: Transfer from Drone

    5: Transfer to Drone


### 5.1.1 QDrone2 Communication Channels and Ports

QDrone2 uses fixed communication ports for the simulator, cameras, and game connection.

---

#### Camera and Sensor Ports

If camera support is enabled in Python, the following ports are used:

| Camera | Address | Camera ID | Resolution |
|---|---|---|---|
| RealSense RGB + Depth | `tcpip://localhost:18986` | `0@tcpip://localhost:18986` | `640 x 480` (RGB + Depth) |
| Right Camera | `tcpip://localhost:18982` | `0@tcpip://localhost:18982` | `640 x 480` |
| Back Camera | `tcpip://localhost:18983` | `1@tcpip://localhost:18983` | `640 x 480` |
| Left Camera | `tcpip://localhost:18984` | `2@tcpip://localhost:18984` | `640 x 480` |
| Downward Camera | `tcpip://localhost:18985` | `3@tcpip://localhost:18985` | `640 x 480` |

> **Note:** The RealSense camera operates in `RGB & DEPTH` mode and provides both RGB and Depth streams on the same port.

---

**Data and Game Ports**


Drone Data Stream:

| Parameter | Value |
|---|---|
| Address | `tcpip://localhost:18373` |
| Agent Mode | `C` |
| Send Buffer Size | `1460` |
| Receive Buffer Shape | `(1, 16)` — `float64` |
| Receive Buffer Size | `1460` |

Received Data Layout:

| Index | Description | Unit |
|---|---|---|
| `[0]` | Stream connection flag | — |
| `[1:4]` | IMU gyroscope data | rad/s |
| `[4:7]` | IMU accelerometer data | m/s² |
| `[7:10]` | Estimated angular position | rad |
| `[10:13]` | Estimated angular rates | rad/s |
| `[13:16]` | Estimated angular acceleration | rad/s² |
| `[16:20]` | Pose — x, y, z, yaw | m, m, m, rad |

**Sent Data:** Waypoint as `[x, y, z, yaw]` vector.

---

**Drone Intention Stream**

| Parameter | Value |
|---|---|
| Address | `tcpip://127.0.0.1:19001` |
| Agent Mode | `C` |
| Send Buffer Size | `8` |
| Receive Buffer Shape | `(1, 1)` — `float64` |
| Receive Buffer Size | `24` |

**Received Data:** None.

**Sent Data:** QDrone2 intention value.

For the Python section related to this communication setup, see the [QDrone2 Communication Python Section](QDrone2_communication.md)

---

### 5.2 QCar2 Navigator

The QCar navigator supports:

- node-based trajectory selection
- velocity and steering 
- publishing intention
- camera stream, enabled as needed and disabled by default in the provided code and model

### QCar2 Inputs

Users can provide:

- start node
- end node
- velocity and steering 
- intention commands

### QCar2 Intention List

    0: Nothing

    1: Pickup Small

    2: Pickup Large

    3: Drop

    4: Transfer from Drone

    5: Transfer to Drone


### 5.2.1 QCar2 Communication Channels and Ports

QCar2 uses fixed communication ports for the simulator, cameras, and game connection.

---

#### Camera and Sensor Ports

If camera support is enabled in Python, the following ports are used:

| Camera | Address | Camera ID | Resolution |
|---|---|---|---|
| Right Camera | `tcpip://localhost:18961` | `0@tcpip://localhost:18961` | `640 x 480` |
| Back Camera | `tcpip://localhost:18962` | `1@tcpip://localhost:18962` | `640 x 480` |
| Front Camera | `tcpip://localhost:18963` | `2@tcpip://localhost:18963` | `640 x 480` |
| Left Camera | `tcpip://localhost:18964` | `3@tcpip://localhost:18964` | `640 x 480` |

> **Note:** All cameras operate at a frame rate of `30 fps` with a resolution of `640 x 480`.

---

#### **Data and Game Ports**

---

**QCar2 Data Stream**

| Parameter | Value |
|---|---|
| Address | `tcpip://localhost:18375` |
| Agent Mode | `C` |
| Send Buffer Size | `1460` |
| Receive Buffer Shape | `(1, 10)` — `float64` |
| Receive Buffer Size | `1460` |

**Received Data Layout:**

| Index | Description | Unit |
|---|---|---|
| `[0]` | Motor power consumption | W |
| `[1]` | Battery level | % |
| `[2]` | Car speed | m/s |
| `[3:6]` | Gyroscope data | rad/s |
| `[6:9]` | Accelerometer data | m/s² |
| `[9]` | Connection status flag | — |

**Sent Data:** Velocity and steering commands as `[velocity, steering]` vector.

---

**QCar2 Intention Stream**

| Parameter | Value |
|---|---|
| Address | `tcpip://localhost:19000` |
| Agent Mode | `C` |
| Send Buffer Size | `8` |
| Receive Buffer Shape | `(1, 3)` — `float64` |
| Receive Buffer Size | `24` |

**Received Data:** Vehicle pose as `[x, y, yaw]`.

**Sent Data:** QCar2 intention value.

For the Python section related to this communication setup, see the [QCar2 Communication Python Section](QCar2_communication.md)

---


## 6) Autonomous Control Details

This section describes how QCar2 and QDrone2 operate in autonomous mode.

### 6.1 QCar2 Autonomous Control

In autonomous mode, QCar2 uses node-based routing for path planning and motion execution.

Users can provide:

- start node
- end node
- desired velocity and steering command
- publishing intention

Based on the selected start node and end node, the controller computes:

- the path to follow through the node network
- steering commands
- velocity commands

#### QCar2 Node Map for Python

The following node map shows the node numbers that can be used for **QCar2 autonomous route planning in the Python version**.

**Pickup location:** Node **24**

<img src="../images/roadmap_Python.png" alt="QCar2 Python node map" width="520">

#### QCar2 Node Map for MATLAB/Simulink 

The following node map shows the node numbers that can be used for **QCar2 autonomous route planning in the MATLAB/Simulink version**.

**Pickup location:** Node **25**

<img src="../images/roadmap_Matlab.png" alt="QCar2 MATLAB/Simulink node map" width="520">

#### Sample Autonomous Files

Sample files for autonomous operation are also provided in the `tools\` folder, including:

- `plan_path.py`
- `example.py`

For QCar2, `plan_path.py` provides a sample autonomous path-planning workflow in which a node-based route is generated and the QCar2 drives autonomously based on the selected node path.

#### Important

- Teams should use these node numbers when selecting QCar2 start and end nodes in Python.
- The files in `tools\` are provided as sample references for autonomous planning and execution.

---

### 6.2 QDrone2 Autonomous Control

In autonomous mode, QDrone2 uses waypoint-based navigation to move between mission targets.

Users can provide:

- waypoint or target position
- desired autonomous motion target
- publishing intention

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


## 7) Pickup and Delivery Operations and Conditions

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

### 7.1 QDrone2 Pickup

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



### 7.2 QCar2 Pickup

#### Exact Distance Requirement

A QCar2 pickup is valid when all of the following are satisfied relative to the central pickup location:

- distance from the QCar2 to the central pickup point must be **less than 2.0 m**
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

### 7.3 QDrone2 Delivery

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

### 7.4 QCar2 Delivery

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

## 8) Transfer Operation and Conditions

Transfer can happen in both directions:

- **QCar2 → QDrone2**
- **QDrone2 → QCar2**

Both vehicles must use the correct intention values.

### Transfer Hold Time

- Transfer action duration: **3 seconds**

---

### 8.1 QCar2 to QDrone2 Transfer

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

### 8.2 QDrone2 to QCar2 Transfer

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

## 9) Final Runtime Check, Mission Completion, and File Reference

### Mission Timing and Completion

- Mission time begins at the official mission start.
- When a delivery is successfully completed, a delivery score is calculated using the scoring formula.
- The **total score** is displayed at the **top** of the QLabs window.

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

### File Structure

```text
AICA_Competition_Files\
    setup_env.py                  
    QDrone2_Navigator.slx
    QDrone2_Navigator.py
    QCar2_Navigator.slx
    QCar2_Navigator.py
    run_all.bat
    run_all.m
    spawn_location.txt
    virtual_DriveStack.rt-win64   
    virtual_FlightStack.rt-win64  
    game.py                       
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