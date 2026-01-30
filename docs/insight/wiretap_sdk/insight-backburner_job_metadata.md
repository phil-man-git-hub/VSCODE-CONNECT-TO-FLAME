# Insight: Backburner Job Metadata

This document explains the information (Tags) attached to a render job in Backburner. Understanding these tags allows you to track exactly how your renders are performing.

**Target Audience:** Novice programmers interested in status monitoring and reporting.

---

## 1. The Four Metadata Streams

Every job in Backburner has four different "Folders" of information:

### A. `info` (The Overview)
This is the most important stream. It contains the basic "ID Card" for the job:
- **`percentTasksCompleted`**: How much of the render is done?
- **`submittedTime`**: When did the artist hit the button?
- **`lastError`**: If it failed, why?

### B. `state` (The Activity)
A simple tag that tells you what the job is doing right now:
- `waiting`: Ready to work.
- `active`: Currently rendering.
- `complete`: Successfully finished.
- `suspended`: On hold.

### C. `tasks` (The Granular View)
A job is often split into many small "Tasks" (like 10 frames each). This stream lists every single task, which machine worked on it, and how many milliseconds it took.

### D. `details` / `xmlDetails` (Custom Info)
A secret compartment for technical settings. This is where Flame stores specific render instructions like "Use Motion Blur" or "Output at 4K."

---

## 2. Why is this useful?

By reading the `info` and `tasks` streams, you can build a **Studio Report**. You can calculate exactly how many hours your render farm spent on a specific project, which machines are the fastest, and which artists are submitting the most jobs.

---

## 3. Key Takeaway for Beginners

Job Metadata is **"Live Intelligence."** Instead of guessing if a render will be done by lunch, your script can read the `percentTasksCompleted` tag and tell you exactly how much work is left!
