# Insight: Creating a "Watch Folder" in Flame

This document explains the `watch_folder.py` example script. It shows how to make Flame perform background tasks without freezing the user interface.

**Target Audience:** Novice Python programmers interested in automation and "Background Tasks."

---

## 1. What is a "Watch Folder"?

A Watch Folder is a folder on your computer that a script monitors. Whenever you drop a file into that folder, the script automatically "wakes up" and imports that file into Flame.

## 2. The Secret: `schedule_idle_event`

If you write a simple Python script that says `while True: look_for_files()`, Flame will **freeze**. This is because Python is taking up 100% of Flame's attention.

**The Solution:** Use Flame's "Idle" loop.
Flame has a special feature called `schedule_idle_event`. It tells Flame: *"Hey, next time the artist is NOT clicking anything, run this function for a split second."*

## 3. How the Script Works

1.  **Start on Startup:** The script uses the `app_initialized` hook to start looking for files as soon as Flame opens.
2.  **The Check:** It looks inside `/var/tmp/watch_folder`.
3.  **The Import:** If it finds a new file, it imports it into a library named "Watch Folder."
4.  **The Relay Race:** After importing *one* file, the script doesn't just keep going. It says: *"I'm done for now. Flame, please call me again in 1 second."*
    ```python
    flame.schedule_idle_event(do_watch_folder, delay=1)
    ```

---

## 4. Why is this powerful?

- **Zero Lag:** Because the script only runs during "Idle" time, the artist can keep working, editing, and color grading without noticing the script is running.
- **Workflow Speed:** You can have an external assistant or another software (like a 3D renderer) drop files into the folder, and they magically appear in Flame without any manual work.

---

## 5. Key Takeaway for Beginners

In Flame, **never use long `while` loops**. Instead, use `schedule_idle_event` to break your big task into tiny pieces that run only when Flame isn't busy. This keeps the software responsive and your workflow smooth!
