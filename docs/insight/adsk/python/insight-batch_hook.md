# Insight: Mastering the Batch Lifecycle

This document explains the `batch_hook.py` file. It covers every stage of the Batch process—from saving your work to rendering the final images.

**Target Audience:** Novice Python programmers learning about render pipelines and automation.

---

## 1. What is a Batch Hook?

**Batch** is Flame's node-based compositing environment. Because Batch is where most of the "Heavy Lifting" (rendering) happens, it has many hooks to help you track progress and prevent mistakes.

---

## 2. Key Lifecycle Stages

The script breaks the Batch workflow into three main parts:

### A. Setup Management (`batch_setup_loaded` / `saved`)
These run when you open or save your Batch schematic.
- **Use case:** Keep a log of who is opening which Batch setup and when.

### B. Iterations (`batch_setup_iterated_pre` / `post`)
In Flame, an "Iteration" is a versioned save.
- **The "Pre" Hook:** Runs *before* the save happens. You can use this to **Abort** the save if the file name doesn't match studio standards.
- **The "Post" Hook:** Runs after the save. It tells you if it was successful.

### C. Rendering & Exporting (`begin` / `end` hooks)
This is where the images are actually created.
- **`batch_render_begin`**: Runs before a local render.
- **`batch_burn_begin`**: Runs before sending a job to a "Burn" render node.
- **`batch_export_begin`**: Runs before a "Write File" node starts exporting to disk.

---

## 3. The `info` and `userData` Pattern

Almost all these functions use two special parameters:

1.  **`info` [Dictionary]:** This is a read-only (and sometimes modifiable) "ID Card" for the task. It contains paths, frame rates, resolution, and job names.
2.  **`userData` [Dictionary]:** This is like a **"Sticky Note."** You can write something on it in the `_begin` hook (like a timestamp), and Flame will hand that same sticky note back to you in the `_end` hook. It's the best way to track how long a job took!

---

## 4. Why is this useful?

- **Quality Control:** Use the `begin` hooks to check if the render settings (like resolution) are correct before wasting hours on a render.
- **Custom Notifications:** Use the `end` hooks to trigger a Slack message or email when a long render is finished.
- **Path Redirection:** Use the `batch_export_begin` hook to dynamically change where files are saved based on the project name.

---

## 5. Key Takeaway for Beginners

Batch hooks allow you to **"Sandwich"** Flame's built-in actions with your own code. By putting logic at the "Start" and "End" of a render, you can build a highly controlled and intelligent production pipeline.
