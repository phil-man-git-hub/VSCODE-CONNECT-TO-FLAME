# Insight: Global Application Hooks

This document explains the `hook.py` file. These are the "Global" events that happen at the highest level of Autodesk Flame.

**Target Audience:** Novice Python programmers interested in general automation and default settings.

---

## 1. What is a Global Hook?

While most hooks are about specific tasks (like rendering or exporting), Global Hooks are about the **Application** itself. They run when Flame starts, when you switch projects, or when you log in as a different user.

---

## 2. Key Global Events

### A. Lifecycle Hooks (`app_initialized` / `app_exited`)
- **`app_initialized`**: Runs as soon as Flame is ready for work.
  - *Use case:* Automatically open a specific library or print a "Welcome" message to the console.
- **`app_exited`**: Runs when you quit Flame.
  - *Use case:* Clean up temporary files or save a log of how long you worked.

### B. User Changes (`user_changed`)
Flame runs this when you switch from "Editor A" to "Editor B."
- *Use case:* Automatically load the user's preferred hotkeys or window layouts via Python.

### C. Default Naming Hooks
Flame uses several hooks to decide what the "Default Name" should be for things like Markers and Shots:
- `timeline_default_shot_name`
- `timeline_default_marker_name`
- `default_reference_name`

Instead of every shot being named "Shot 1", "Shot 2", you can write a script that names them based on the Date and the Project Name automatically.

---

## 3. Monitoring Performance

The `render_ended` hook in this file is different from the Batch render hook. It triggers for *any* render in Flame (Timeline, Effects, etc.) and tells you exactly how many seconds it took.
- **Use case:** Build a report showing which modules (like "Action" or "GMask") are taking the most time to render across your project.

---

## 4. Why is this useful?

- **Consistency:** You can enforce studio-wide naming standards for markers and shots so everyone's projects look the same.
- **Environment Setup:** You can prepare the Flame environment (like setting the Video Preview device) automatically every time the software starts.

---

## 5. Key Takeaway for Beginners

Global hooks are for **"Set it and Forget it"** logic. Once you write a hook here, it works across every project and every user, making it the best place for infrastructure-level automation.
