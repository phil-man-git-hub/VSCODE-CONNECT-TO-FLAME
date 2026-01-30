# Insight: Managing Projects and Setups

This document explains how to use the API to automatically create, configure, and manage Flame projects.

**Target Audience:** Novice programmers interested in project administration.

---

## 1. Creating a New Project

Creating a project through the API is like using the "New Project" window in Flame, but much faster.
- **Default Settings:** If you just give it a name, Flame uses the standard studio defaults.
- **Custom Settings (XML):** You can provide an XML file to specify exactly how the project should look (e.g., "This job is 4K," or "Use this specific color policy").

---

## 2. Using Templates

If your studio has a standard "Master Template" for all jobs, you can tell the API to use it:
```xml
<Project>
    <Template>Studio_Commercial_Template</Template>
</Project>
```
This ensures every project starts with the right resolution and folder structure.

---

## 3. Managing "Setups"

A **Setup** is a small file that saves the settings for a specific Flame tool (like a GMask or a Color Correction).
- **Streaming:** Setups can be large. You use the `pushStream` and `pullStream` commands to upload or download these files from the project.

---

## 4. Deleting Projects

Deleting a project is a two-step process:
1.  **Empty the Project:** You must delete all Libraries inside the project first.
2.  **Destroy the Node:** Once empty, you can permanently remove the project from the workstation.

---

## 5. Key Takeaway for Beginners

The Project API is the **"Architect"** of your workflow. Instead of artists wasting time setting up folders and choosing resolutions, your script can prepare everything perfectly before they even arrive at their desk.
