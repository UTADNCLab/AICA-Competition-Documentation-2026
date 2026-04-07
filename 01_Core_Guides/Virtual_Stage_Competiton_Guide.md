# Virtual Stage Competition Guide 

Welcome to Virtual Stage (Stage 1) of the IEEE SMC AI-Powered Collaborative Autonomy Challenge (AICA).  
This guide explains what teams should prepare for virtual-stage evaluation.

---

## Navigation

- [Virtual Stage Objective](#1-virtual-stage-objective)
- [Virtual Stage Detailed Scenario](#2-virtual-stage-detailed-scenario)
- [Core Principles for Multimodal Delivery](#3-core-principles-for-multimodal-delivery)
- [Operational Guide](#4-operational-guide)
- [Scoring and Ranking](#5-scoring-and-ranking)
- [Resources](#6-resources)

---

## 1) Virtual Stage Objective

The objective of the Virtual Stage is to demonstrate your system’s ability to complete delivery missions in the QLabs simulation environment.

Your submission should clearly demonstrate:

- End-to-end mission completion  
- Efficient routing and navigation using provided maps and paths  
- Stable control and correct action sequencing  
- Effective coordination between QCar2 and QDrone2  

For full submission details, see: [Virtual Stage Submission Guide](../02_Participation/Submission_Guide.md)

This stage evaluates mission completion, system reliability, and coordination performance.

---

## 2) Virtual Stage Detailed Scenario

For the complete scenario description, see: [Virtual Stage Detailed Scenario](../01_Core_Guides/Virtual_Stage_Detailed_Scenario.md)

---

### Key Scenario Elements

- Central depot pickups for packages  
    - **QCar2** can carry: 2 small packages or 1 large package  
    - **QDrone2** can carry: 1 small package only  
- Coordination between QCar2 and QDrone2  
- Vehicle-to-vehicle transfers  
- Window delivery vs common drop 
- Delivery completion requirements  

> This section provides a high-level overview. Refer to the detailed scenario page for full rules and configurations.

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

The Operational Guide includes both the step-by-step mission workflow and the operational constraints for valid pickup, transfer, delivery, and mission execution.  

[Operational Guide](../01_Core_Guides/Operational_Guide.md)

---

## 5) Scoring and Ranking

This section defines how team performance is scored and how rankings are determined in the Virtual Stage.

### Scoring Method

- The mission clock starts at the official mission start  
- A delivery is counted when the delivery is successfully completed according to the scenario logic  

**Scoring formula:**

- **Delivery score = 1000 − current mission time + floor-based bonus**
- **Total Score = Sum of all delivery scores**

#### Not all deliveries receive a bonus. Only **window deliveries by QDrone2** are eligible for a floor-based bonus, and the bonus increases with the target floor level.

**Example floor-based bonus logic:**

- Floor 4 → **+400**
- Floor 3 → **+300**
- Floor 2 → **+200**

Higher scores correspond to faster delivery completion and more valuable delivery choices.

### Ranking

- Teams are ranked based on their total score  
- The team with the highest total score ranks first  

For a detailed explanation of scoring behavior and recommended strategies, see: [Scoring and Strategy](../01_Core_Guides/Scoring_and_Strategy.md)

---


## 6) Resources


[All Competition Resources](../04_Resources/All_Competition_Resources.md)

---


#### Back to: 

[Competition Objective](../01_Core_Guides/Competition_Objective.md)

[AICA Home Portal](../00_Portal/AICA_PORTAL.md)

