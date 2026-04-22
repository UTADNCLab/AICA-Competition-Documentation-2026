# Virtual Stage Competition Guide 

Welcome to the Virtual Stage of the SMC AICA 2026.  
This guide explains what teams should prepare for Virtual Stage competition.

---

## Navigation

- [Virtual Stage Submission](#virtual-stage-submission)
- [Virtual Stage Detailed Scenario](#virtual-stage-detailed-scenario)
- [Core Principles for Multimodal Delivery](#core-principles-for-multimodal-delivery)
- [Operational Guide](#operational-guide)
- [Scoring and Ranking](#scoring-and-ranking)
- [Resources](#resources)

---

## Virtual Stage Submission

The objective of the Virtual Stage is to create a video that demonstrates a team's ability to implement algorithms for the multimodal autonomous delivery system in the QLabs simulation environment.

For the full submission details, see the [Virtual Stage Submission Guide](../02_Participation/Submission_Guide.md)

---

## Virtual Stage Detailed Scenario

For the complete scenario description, see the [Virtual Stage Detailed Scenario](../01_Core_Guides/Virtual_Stage_Detailed_Scenario.md)

This document includes:

- System Setup
- Central Pickup Operations
- Vehicle-to-Vehicle Package Transfer
- Delivery Options
- Pickup and Delivery Locations

---

## Core Principles for Multimodal Delivery

### Delivery Planning and Decision-Making
- Plan delivery tasks by assigning them to either QCar2, QDrone2, or their coordinated operation through vehicle-to-vehicle package transfer
- Develop delivery planning strategies to achieve a high score by considering the city map, vehicle capabilities, pickup and drop-off locations, and available delivery options

### Multi-Agent Coordination
- Coordinate QCar2 and QDrone2 actions for pickup, vehicle-to-vehicle package transfer, and delivery  
- Manage timing and interaction between vehicles for efficient mission execution  

### Control Systems and Navigation
- Develop smooth and safe trajectories for QDrone2, ensuring stable, high-performance flight while avoiding obstacles 
- [Optional] Design and implement a control algorithm to generate steering and velocity commands for the autonomous navigation of QCar2 within road boundaries while avoiding collisions

### Mission Completion and Efficiency
- Set an appropriate level of autonomy, ranging from fully manual control to fully autonomous operation
- Optimize overall mission time and execution efficiency  

---

## Operational Guide

See the [Operational Guide](../01_Core_Guides/Operational_Guide.md) for the step-by-step mission workflow and the operational constraints for valid pickup, vehicle-to-vehicle package transfer, delivery, and mission execution for both QCar2 and QDrone2 in the virtual stage

---

## Scoring and Ranking

This section defines how teams performance is scored and how rankings are determined in the Virtual Stage


### Scoring Formula

- Score for each completed delivery = 1000 − delivery completion time + window delivery bonus
- Total Score = Sum of all delivery scores


Delivery Completion Time is the time taken to complete a delivery, measured from the mission start time until the package is successfully delivered

Window Delivery Bonus: Only QDrone2 can perform window deliveries, and the bonus depends on the target floor level


Bonus by floor level:

- Floor 4 → +400
- Floor 3 → +300
- Floor 2 → +200


### Score Display

- When a delivery is successfully completed, a delivery score is calculated using the scoring formula
- The total score is displayed at the top of the QLabs window


### Ranking

Teams are ranked according to their total score, where a higher score corresponds to a higher rank.


---


## Resources


[All Competition Resources](../04_Resources/All_Competition_Resources.md)

---


#### Back to: 

[Competition Guide](../01_Core_Guides/Competition_Objective.md)

[AICA Home Portal](../00_Portal/AICA_PORTAL.md)

