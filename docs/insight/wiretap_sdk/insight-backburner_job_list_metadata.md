# Insight: Backburner Job List Metadata

This document explains how to get a detailed status report of all **Active** renders currently happening in your studio.

**Target Audience:** Novice programmers interested in high-performance data querying.

---

## 1. The Active Overview

Just like the archive, the active **`/jobs`** node has a "Super Query" feature. When you ask for its `info` metadata, it returns a list of every job currently waiting or rendering.

It includes live details like:
- **`percentTasksCompleted`**: How close is the job to being done?
- **`nbFailedServers`**: Are any computers struggling with this specific job?
- **`order`**: Where is this job in the "Lineup"?

---

## 2. Advanced Filtering (The "Fields" trick)

If you have 1,000 jobs, the XML file can get huge and slow. You can use **Filters** to ask for only the pieces you need.

- **Example:** *"I only want the Name and the ID, don't send me the whole description."*
- **The Filter Code:** `<Fields id='1' name='1'/>`

---

## 3. Comparison Queries

You can even ask complex questions using the `<Comparison>` tag:
- *"Show me all jobs that are 'complete'."*
- *"Show me all jobs submitted by user 'JohnDoe'."*

---

## 4. Why is this useful?

This is the power behind every professional "Render Monitor" dashboard. Instead of clicking through a slow interface, your script can ask for a tiny, filtered list of "Only failed jobs" and alert you instantly when a render hits a snag.

---

## 5. Key Takeaway for Beginners

The `/jobs` node is the **"Live Status Board"**. By using filters and comparisons, you can get exactly the data you need (like "Only show me the progress of V2 shots") without wasting time downloading information you don't care about.
