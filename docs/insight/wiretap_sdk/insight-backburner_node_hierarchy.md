# Insight: Backburner Node Hierarchy

This document explains the organizational map of the **Backburner Manager**. Just like Flame projects, Backburner uses a tree structure to keep track of computers and tasks.

**Target Audience:** Novice programmers interested in system organization.

---

## 1. The Map of the Manager

The Backburner hierarchy has four main branches:

### A. The Manager (`MANAGER/`)
The root of the whole tree. It holds the overall settings for the entire render farm.

### B. The Server List (`SERVERLIST/`)
A list of every computer (Render Node) that has introduced itself to the Manager. 
- Each computer has its own `SERVER` node.
- If a computer disappears (unplugged or crashed), it is marked as "Absent."

### C. The Server Group List (`SERVERGROUPLIST/`)
Where you can group computers together. 
- *Example:* You might create a group called "Super_Fast_Nodes" that only contains the newest computers in the studio.

### D. The Job List (`JOBLIST/`)
The most active part of the tree. It contains every `JOB` currently being processed.
- When a job is completely finished and old, it moves to the **Archive** branch.

---

## 2. Using Metadata

Each node in this tree has "Tags" (Metadata). 
- A **Job Node** has tags telling you the percentage finished.
- A **Server Node** has tags telling you if the computer is currently "Busy" or "Idle."

---

## 3. Why is this useful?

By "Walking" through this tree, your Python script can build its own dashboard. You can write a script that says: *"Find all servers in the 'Super_Fast' group and tell me how many of them are currently Idle."*

---

## 4. Key Takeaway for Beginners

Backburner's hierarchy is a **Live Status Map**. It gives you a birds-eye view of every worker and every task in your studio, organized into a simple tree that your code can easily read.
