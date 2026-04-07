# Development Guide

This guide shows a simple way to build your system for the virtual stage.

---

## 1. How to Start

1. Decide what the car and drone will do  
2. Plan routes using the provided map and nodes  
3. Add logic for pickup, transfer, and delivery  
4. Run the full mission in simulation  
5. Improve speed and reliability  

---

## 2. Basic System Structure

You can organize your system like this:

- Mission logic (what to do next)  
- Car controller (QCar2 movement)  
- Drone controller (QDrone2 movement)  
- Transfer logic (car ↔ drone interaction)  
- Simple logging (time, score, errors)  

---

## 3. What Your System Should Show

Your final system should:

- Start and run the mission correctly  
- Complete at least one full delivery cycle  
- Move smoothly (no unstable behavior) 

---

## 4. What You Should Test

Try different approaches:

- Only using the car  
- Using drone for window delivery  
- Using both with transfers  

Check:

- Total time  
- Score  

---

### Back to: 

[All Competition Resources](../04_Resources/All_Competition_Resources.md)  

[AICA Portal](../00_Portal/AICA_PORTAL.md)