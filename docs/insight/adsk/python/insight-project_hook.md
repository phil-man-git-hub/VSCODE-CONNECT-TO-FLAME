# Insight: Automating the Project Lifecycle

This document explains the `project_hook.py` file. It gives you total control over how Flame projects are created, saved, and managed.

**Target Audience:** Novice Python programmers interested in project management and data safety.

---

## 1. What is a Project Hook?

In Flame, a "Project" is the container for all your work. Because projects are so important, Flame gives you hooks for every possible change that can happen to one.

---

## 2. Key Lifecycle Events

### A. Creation & Setup (`project_init_creation` / `pre_creation`)
- **`project_init_creation`**: Runs as soon as you open the "New Project" window.
  - *Use case:* Automatically fill in the Project Description or Nickname based on today's date.
- **`project_pre_creation`**: Runs right before the project is actually built.
  - *Use case:* **Abort** the creation if the name doesn't follow studio rules (e.g., must start with a job number).

### B. Project Changes (`project_changed` / `project_saved`)
- **`project_changed`**: Runs when you switch from Project A to Project B.
- **`project_saved`**: Runs every time you save.
  - *Tip:* It even tells you if it was an "Auto-Save" or a manual save by the artist!

### C. Conversion & Migration (`project_pre_conversion`)
When you upgrade Flame, you often have to convert old projects.
- *Use case:* Log which projects have been migrated to the new version for auditing.

### D. Deletion & Protection (`project_pre_delete`)
This is the "Security Guard" hook.
- *Use case:* Prevent anyone from deleting a project if it's currently marked as "Active" in your studio database.

---

## 3. The "Abort" Power

Just like Export hooks, Project hooks allow you to set `info["abort"] = True`. This is the ultimate safety feature. It stops Flame from doing anything until the project data meets your studio's standards.

---

## 4. Why is this useful?

- **Organization:** Ensure every project has a consistent folder structure and naming convention.
- **Safety:** Prevent accidental deletion of "Master" projects.
- **Automation:** Automatically link Flame projects to external systems like ShotGrid as soon as they are created.

---

## 5. Key Takeaway for Beginners

Project hooks are about **"Governance."** They allow you to turn Flame from a standalone tool into a part of a larger, managed studio ecosystem where rules are enforced automatically by code.
