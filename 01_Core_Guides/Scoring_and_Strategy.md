# Scoring and Strategy

This page explains the scoring logic and key strategy considerations for the competition.

---

## 1) Scoring Concept

The competition score is based on mission time at the moment each delivery is completed.

### Scoring Formula

- **Standard delivery score = 1000 − current mission time**
- **Bonus delivery score = 1000 − current mission time + floor-based bonus**
- **Total Score = Sum of all delivery scores**

### Floor-Based Bonus

Some drone delivery locations provide additional bonus points based on floor level.

A higher floor corresponds to a higher bonus.

**Example bonus values:**

- **Floor 4 → +400**
- **Floor 3 → +300**
- **Floor 2 → +200**

> Note: Always follow the latest official release if scoring parameters are updated.

---

## 2) Impact of Delivery Methods

### Standard Delivery

- Standard deliveries score based on mission time only  
- Faster completion results in a higher score contribution  

### Bonus Drone Delivery

- Certain drone delivery locations provide additional bonus points  
- Higher-floor delivery locations provide larger bonuses  
- These locations can significantly increase total score if reached efficiently  

---

## 3) Strategy Trade-Offs

Teams should consider:

- Speed vs coordination overhead  
- Transfer benefit vs transfer dwell cost  
- Standard delivery vs higher-floor bonus delivery opportunities  
- Simplicity vs score-optimized strategies  

---

## 4) Strategy Evaluation

Teams are encouraged to compare different approaches, such as:

- Car-only baseline  
- Drone-priority delivery  
- Hybrid strategy with transfers  
- Bonus-focused drone strategy  

Evaluate based on:

- Total score  
- Mission completion time  
- Reliability across repeated runs  
- Efficiency of coordination between QCar2 and QDrone2  

---

## 5) Practical Recommendations

- Complete deliveries as early as possible to maximize score  
- Use higher-floor bonus delivery locations when they improve total mission efficiency  
- Avoid unnecessary delays during pickup, drop, and transfer operations  
- Minimize idle hover and stop time  
- Use clear and deterministic action logic  

---

Back to: 

[Virtual Stage Competition Guide](../01_Core_Guides/Virtual_Stage_Competiton_Guide.md)

[AICA Home Portal](../00_Portal/AICA_PORTAL.md)
