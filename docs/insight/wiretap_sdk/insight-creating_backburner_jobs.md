# Insight: Creating and Submitting Jobs

This document explains how your Python script can "Hire" Backburner to do a job for you.

**Target Audience:** Novice programmers interested in task automation.

---

## 1. The 5-Step Process

Submitting a job to the render farm follows a strict sequence:

1.  **Create the Node:** You build a new "Empty" job in the `/jobs` folder.
2.  **Add General Info:** You tell Backburner basic things like "What is the name of this job?" and "Which plugin should I use (e.g., Burn)?"
3.  **Add Detailed Instructions:** (Optional) You can give specific render settings, like "Use 4x Anti-Aliasing."
4.  **Attach Files:** (Optional) If the job needs a specific setup file to run, you can "push" that file directly into the job node.
5.  **Go!:** When you first create a job, it is **Suspended** (Sleeping). You must change its status to **Waiting** to tell the farm to start working.

---

## 2. Mandatory Info

Backburner won't work unless you provide two key details:
- **`pluginName`**: Which software should run this job?
- **`numTasks`**: How many pieces should this job be split into?

---

## 3. Why is this useful?

Normally, an artist has to hit "Render" manually inside Flame. With this API, you can write a script that says:
*"Every night at midnight, find all finished edits and submit them to Backburner to create review movies."* 

It turns manual "Clicking" into automatic "Processing."

---

## 4. Key Takeaway for Beginners

Creating a job is like **Filling out a Form**. You create the form (the node), fill in the blanks (the metadata), and then hand it to the manager (changing status to 'Waiting'). Once the manager has the form, the rest happens automatically!
