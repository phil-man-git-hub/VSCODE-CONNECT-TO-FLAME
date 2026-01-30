# Insight: Backburner Server Metadata

This document explains the information (Tags) attached to the individual computers (Servers) in your render farm.

**Target Audience:** Novice technical artists and system administrators.

---

## 1. Monitoring the Workers

Every server in the Backburner farm has an `info` stream that tells you its health and status:

- **`state`**: Is the computer **Idle** (waiting for work), **Active** (rendering), or **Absent** (turned off)?
- **`perfIndex`**: A score from 0 to 1. A score of 1.0 means this is the fastest machine in the building.
- **`plugins`**: A list of what this machine can do. For example, does it have **Burn** installed for rendering video?

---

## 2. Setting a Schedule

One of the coolest features of Backburner is the **`schedule`** stream. You can tell a machine exactly when it is allowed to work.

- **The Math:** The schedule is stored as a 24-bit number (one bit for every hour of the day). 
- **Use Case:** You can set a rule that says: *"Machine #10 is a powerful artist workstation. It should only render between 7 PM and 7 AM when the artist is home sleeping."*

---

## 3. Why is this useful?

- **Efficiency:** You can ensure that heavy renders don't slow down artists while they are working.
- **Troubleshooting:** If a machine is constantly in an "Error" state, you can find it quickly in the metadata and fix it.
- **Description:** You can add custom notes like "Node under the window" or "Needs more RAM" to help you keep track of physical machines.

---

## 4. Key Takeaway for Beginners

Server Metadata is the **"Health Report"** for your computers. By reading the `state` and `perfIndex`, you can make sure your studio's hardware is being used to its full potential without interrupting the creative team.
