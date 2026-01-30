# Insight: Backburner Network Architecture

This document explains the "Engine" behind Flame's background rendering and how it coordinates multiple computers to get work done faster.

**Target Audience:** Novice technical artists interested in render farms and distributed computing.

---

## 1. The Three Main Players

Backburner is a system that splits a big job into small pieces and sends them to different machines. It has three main components:

### A. The Backburner Manager (The Boss)
The Manager is the "Brain" of the operation. 
- It receives jobs from Flame artists.
- It looks at all the computers on the network and decides who is free to work.
- It keeps a list of every job—what is "Active," "Waiting," or "Done."

### B. The Backburner Server (The Worker)
This is a program running on one or more machines (Render Nodes).
- It waits for the Manager to give it a job.
- When it gets a job, it starts the rendering engine (like **Burn**) and creates the actual frames.

### C. The Backburner Monitor (The Dashboard)
This is the interface the humans use. 
- It allows you to see the progress of your renders.
- You can use it to "Pause," "Restart," or "Prioritize" certain jobs if you are in a rush.

---

## 2. How a Job Moves

1.  **Submit:** The artist hits "Render" in Flame.
2.  **Assign:** The Manager finds an available Server.
3.  **Execute:** The Server renders the frames.
4.  **Finish:** The frames are saved to the server, and the Manager marks the job as "Complete."

---

## 3. Why is this useful?

Backburner allows you to keep working in Flame while your computer renders in the background. Or, you can use 50 other computers on your network to render a long movie in minutes instead of hours!

---

## 4. Key Takeaway for Beginners

Backburner is a **"Traffic Cop"** for renders. It ensures that every computer in your studio is working as efficiently as possible, and it gives you a central place to track all that hard work.
