# Insight: Chaining Complex Jobs with Export Dependencies

This document explains the `post_export_dependency.py` example script. This is an advanced script that shows how to make multiple tasks happen in a specific order, even if they take a long time.

**Target Audience:** Novice Python programmers interested in "Pipeline Engineering."

---

## 1. The Concept: "Wait For Me"

Sometimes, exporting a clip is only the first step. You might want to:
1. Export a clip as a sequence of images.
2. **THEN** Zip those images into one file.
3. **THEN** Send an email saying it's done.

The problem? Step 2 cannot start until Step 1 is 100% finished. If Step 1 is happening on **Backburner** (in the background), your script needs a way to wait.

## 2. Using Backburner Dependencies

The "Magic" in this script is the **Job ID**.
When Flame sends an export to Backburner, it gets back a unique ID number (e.g., Job #1234). 

Our script tells Backburner: *"I want to run a Zip command, but DO NOT START until Job #1234 is finished successfully."* This is called a **Dependency**.

## 3. Key Workflows in the Script

The script demonstrates several "Chain Reactions":

### A. Export & Zip
It exports files and then automatically sends a command to the computer's `zip` tool.

### B. Export & Transcode (FFmpeg)
It exports high-quality images and then triggers **FFmpeg** (a famous video tool) to create a small preview movie automatically.
- *Tip:* Look for `cmd = "/usr/local/bin/ffmpeg ..."`. This is how Flame talks to other software on your computer!

### C. Export & Re-Import
This is the most advanced. It uses an **Idle Loop** (`flame.schedule_idle_event`).
- The script checks every 1 second: *"Is the background job done yet?"*
- As soon as the answer is *"Yes"*, it automatically imports the file back into Batch.

---

## 4. Why Use `flame.execute_command`?

The script mentions a special function `flame.execute_command`. 
- **Beginner Tip:** In regular Python, people use `os.system` or `subprocess`.
- **Flame Tip:** In Flame, using `flame.execute_command` is much safer and faster because it doesn't "fork" (copy) the entire memory of Flame just to run a tiny command.

---

## 5. Key Takeaway for Beginners

This script shows that Flame isn't just a creative tool; it can be the **"Brain"** of your whole studio. By chaining jobs together using Dependencies, you can build complex, automated workflows that run while you sleep!
