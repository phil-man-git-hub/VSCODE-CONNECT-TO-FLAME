# Insight: Backburner Terminology

This document explains the specific "Vocabulary" used when talking about Flame's background rendering system.

**Target Audience:** Novice programmers learning about distributed rendering.

---

## 1. The Core Components

- **Backburner:** The name of the entire system that manages background jobs.
- **Job:** A specific task (like "Render the car commercial"). A job is made up of many small parts.
- **Backburner Manager:** The "Central Brain" that decides which computer does which job.
- **Backburner Server:** The program on each computer that actually does the work.

---

## 2. Technical Infrastructure

- **Renderer / Rendering Engine:** The "Machine" inside the computer that draws the pictures (e.g., **Burn**).
- **Processing Engine:** A machine that does non-picture tasks, like moving files or zipping folders.
- **Plug-in / Adapter:** The "Translator" that allows the Backburner Manager to talk to different software (like Flame, 3ds Max, or Maya).

---

## 3. Why is this useful?

Knowing these terms helps you understand where a problem is happening. 
- If your job won't start, the **Manager** might be down.
- If the frames are coming out black, the **Server** or the **Renderer** might have a problem.

---

## 4. Key Takeaway for Beginners

Backburner is like a **Construction Site**. The **Job** is the building, the **Manager** is the foreman with the clipboard, and the **Servers** are the individual workers. The **Adapters** are the specific tools (hammers, saws) they use to get the job done.
