# Insight: Bridging Flame and the OS

This document explains the `path_of_selected_clips.py` script. It shows how to jump from inside Flame's MediaHub directly into your computer's file browser (like Finder or Nautilus).

**Target Audience:** Novice Python programmers interested in Operating System (OS) integration.

---

## 1. What is the Goal?

Sometimes you see a clip in Flame's MediaHub and you think: *"I need to see this file on my hard drive to rename it or copy it."* Normally, you'd have to open a new window and manually browse to that folder.

**This script creates a shortcut.** You right-click the clip in Flame, and the folder pops open on your desktop instantly.

---

## 2. Key Concepts

### A. Detecting the OS
Computers work differently. A Mac uses `open`, while Linux usually uses `nautilus`. The script checks which system you are on using `os.uname()`.

### B. `flame.execute_command`
This is a high-performance way for Flame to talk to the rest of the computer. 
- **The "Old" way:** Using `subprocess.call`.
- **The "Flame" way:** `flame.execute_command`. This is better because it doesn't slow down Flame's memory while the external window is open.

---

## 3. How the Script Works

1. **Get the Path:** It looks at the selected item and finds its location on the server/hard drive.
2. **Handle Files vs Folders:** If you clicked a specific file, the script is smart enough to find the "Parent Folder" so it can open the right directory.
3. **Run the Browser:** It builds a command like `/usr/bin/open /Volumes/Media/Shots` and tells the OS to run it.

---

## 4. Why is this useful?

- **Speed:** It saves you from the "Deep Folder Dive" through your OS.
- **Verification:** It's the fastest way to confirm exactly where a file lives on the physical server.
- **Workflow Bridge:** It makes it easy to move between Flame and other software (like checking files in a text editor or a specialized player).

---

## 5. Key Takeaway for Beginners

Your Python scripts can be a **"Bridge"** between different worlds. By using a few simple OS commands, you can make Flame feel like it's deeply connected to the rest of your computer.
