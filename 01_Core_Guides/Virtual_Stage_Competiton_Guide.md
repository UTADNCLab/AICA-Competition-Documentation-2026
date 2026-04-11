# Virtual Stage Competition Guide 

Welcome to Virtual Stage (Stage 1) of the IEEE SMC AI-Powered Collaborative Autonomy Challenge (AICA).  
This guide explains what teams should prepare for virtual-stage evaluation.

---

## Navigation

- [Virtual Stage Submission](#1-virtual-stage-submission)
- [Virtual Stage Detailed Scenario](#2-virtual-stage-detailed-scenario)
- [Core Principles for Multimodal Delivery](#3-core-principles-for-multimodal-delivery)
- [Operational Guide](#4-operational-guide)
- [Scoring and Ranking](#5-scoring-and-ranking)
- [Resources](#6-resources)

---

## 1) Virtual Stage Submission

The objective of the Virtual Stage is to demonstrate each team’s ability to implement multimodal delivery in the Quanser Interactive Labs (**QLabs**) simulation environment.

For full submission details, see the [Virtual Stage Submission Guide](../02_Participation/Submission_Guide.md).

---

## 2) Virtual Stage Detailed Scenario

For the complete scenario description, see: [Virtual Stage Detailed Scenario](../01_Core_Guides/Virtual_Stage_Detailed_Scenario.md)

This document includes:

- Central pickup operations for delivery packages
  - **QCar2** can carry **2 small packages** or **1 large package**
  - **QDrone2** can carry **1 small package only**
- Vehicle-to-vehicle transfer operations
- **Window delivery** and **Shared drop-off** delivery options
- Delivery completion requirements
- Pickup and delivery location references
- **QCar2** node references and **QDrone2** coordinate references

---

## 3) Core Principles for Multimodal Delivery

### Planning and Decision-Making
- Use the provided maps and routes to plan efficient paths and delivery strategies  
- Select appropriate actions based on mission state (pickup, transfer, delivery)  
- Ensure correct sequencing of actions for complete mission execution  

### Control Systems
- Execute stable steering, velocity control, stopping, and hover behavior  
- Ensure smooth and reliable motion during navigation and task execution  
- QCar2 must follow lane-based navigation and remain within road boundaries  

### Localization and Navigation
- Use available position data to follow planned routes accurately  
- Maintain lane discipline and avoid invalid shortcuts outside defined paths  
- Adapt navigation based on mission progress and task requirements  

### Multi-Agent Coordination
- Coordinate QCar2 and QDrone2 actions for pickup, transfer, and delivery  
- Manage timing and interaction between vehicles for efficient mission execution  

### Mission Completion and Efficiency
- Ensure all deliveries are completed successfully  
- Optimize overall mission time and execution efficiency  

---

## 4) Operational Guide

See the [Operational Guide](../01_Core_Guides/Operational_Guide.md) for the step-by-step mission workflow and the operational constraints for valid pickup, transfer, delivery, and mission execution for both **QCar2** and **QDrone2** in the virtual stage.

---

## 5) Scoring and Ranking

This section defines how team performance is scored and how rankings are determined in the Virtual Stage.

### Scoring Method

- Mission time begins at the mission start time.
- When a delivery is successfully completed, the delivery score calculated from the scoring formula will be shown in the Quanser Interactive Labs (QLabs) window.

**Scoring formula:**

- **Score for each completed delivery = 1000 − delivery completion time + window delivery bonus**
- **Total Score = Sum of all delivery scores**

#### Delivery Completion Time

**Delivery completion time** is the time taken to complete a delivery, measured from the mission start time until the package is successfully delivered.

#### Window Delivery Bonus

Only **QDrone2** can perform window deliveries, and the bonus depends on the target floor level.

**Bonus by floor level:**

- Floor 4 → **+400**
- Floor 3 → **+300**
- Floor 2 → **+200**

Higher scores are earned by completing deliveries earlier and by choosing delivery methods that provide additional bonus points.


### Ranking

- Teams are ranked based on their total score
- The team with the highest total score ranks first

---


## 6) Resources


[All Competition Resources](../04_Resources/All_Competition_Resources.md)

---


#### Back to: 

[Competition Objective](../01_Core_Guides/Competition_Objective.md)

[AICA Home Portal](../00_Portal/AICA_PORTAL.md)

