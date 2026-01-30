# Insight: Automating QuickTime Transcoding from Batch

This document explains the `batch_write_file_quicktime.py` script. It shows how to automatically create a QuickTime movie whenever a "Write File" node finishes rendering in Batch.

**Target Audience:** Novice Python programmers interested in render automation.

---

## 1. What is the Goal?

In Flame's Batch environment, a **Write File** node is often used to export image sequences (like OpenEXR). However, after the render is done, you might *also* need a QuickTime file for review.

**This script automates that second step.** As soon as the Write File node finishes its work, this script picks up the images and converts them into a QuickTime movie.

---

## 2. Key Concepts

### A. The `batch_export_end` Hook
This is the "trigger." Flame runs this function automatically when a Batch export completes. It provides an `info` dictionary containing the path to the newly rendered files.

### B. Dynamic Preset Paths
The script uses `flame.PyExporter.get_presets_dir()`. This is better than hardcoding a path because it asks Flame: *"Where do you keep your official Autodesk QuickTime presets?"* This makes the script work on any computer, regardless of where Flame is installed.

---

## 3. How the Script Works

1.  **Find the Media:** It uses `os.path.join` to combine the export folder and the filename into one full path.
2.  **Import:** It tells Flame to "look" at those new files using `flame.import_clips(full_path)`.
3.  **Setup the Exporter:**
    - It creates an instance of `flame.PyExporter`.
    - It sets `exporter.foreground = True`. This means Flame will focus entirely on making the QuickTime until it is finished.
4.  **Export:** It runs the `export()` command using the official "8-bit Uncompressed" preset.

---

## 4. Why is this useful?

- **Saves Time:** You don't have to manually create a new export job after every render.
- **Consistency:** Every render automatically gets a matching QuickTime file in the same folder.
- **Simplicity:** For the artist, they just hit "Render" in Batch, and both the image sequence and the movie appear.

---

## 5. Key Takeaway for Beginners

This script is a perfect example of a **"Post-Process."** By using the information provided by a hook (`info["exportPath"]`), you can chain multiple Flame operations together into a single automated workflow.
