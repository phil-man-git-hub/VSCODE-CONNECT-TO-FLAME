# Insight: Backburner Overview

This document provides a high-level summary of **Backburner**, Flame's system for managing background work.

**Target Audience:** Novice programmers and studio artists.

---

## 1. What is Backburner?

Rendering a movie can take hours. If you did this inside Flame, your computer would be "Locked" and you couldn't keep working.

**Backburner** is the solution. It is a "Background Manager" that takes your render request and handles it on a different computer (or in the background of your own computer) so you can keep editing.

---

## 2. Why is it in the Wiretap SDK?

The Backburner Manager is actually a **Wiretap Server**. This is great news for programmers! It means you can use the same code you use to find clips to also find render jobs.

---

## 3. What can you do with it?

Using the API, you can build your own custom tools to:
- **Monitor:** See exactly which frame a render is on.
- **Control:** Pause a job if you need more bandwidth, or Restart a job if it failed.
- **Automate:** Submit hundreds of renders at once from a script.

---

## 4. Key Takeaway for Beginners

Backburner is the **"Task Manager"** for your entire studio. It coordinates the "Heavy Lifting" so that artists can stay focused on being creative. By mastering the Backburner API, you can build a pipeline that renders while you sleep.
