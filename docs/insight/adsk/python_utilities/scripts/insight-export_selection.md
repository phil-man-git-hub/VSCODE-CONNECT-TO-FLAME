# Insight: Bulk Export & FFmpeg Integration

This document explains the `export_selection.py` script. This is a "Power User" script that handles everything from exporting thumbnails to talking to external software like **FFmpeg**.

**Target Audience:** Intermediate Python programmers interested in external integrations.

---

## 1. What does it do?

This script provides several professional export options for your selection:
1. **Thumbnail + Movie:** Saves a Jpeg of the first frame AND a QuickTime file.
2. **Recursive Export:** If you select a folder, it digs through and exports everything inside it, keeping your folder structure organized.
3. **FFmpeg Export:** This is the most advanced part. It bypasses Flame's built-in exporter and uses a third-party tool (FFmpeg) to create movies.

---

## 2. Key Concepts: The FFmpeg Bridge

How does Flame talk to FFmpeg? It's a three-step dance:

### Step 1: Named Pipes (`os.mkfifo`)
The script creates a "Pipe"—a virtual file that exists only in the computer's memory. It uses this to stream audio data from Flame directly into FFmpeg.

### Step 2: `read_frame` and `read_audio`
Autodesk provides "Command Line" versions of Flame's engine called `read_frame` and `read_audio`. The script runs these in the background to pull raw data out of Flame's database.

### Step 3: Subprocess Piping
The script "pipes" the video from `read_frame` into FFmpeg's input.
```python
ffmpeg_process = subprocess.Popen(..., stdin=read_frame_process.stdout)
```
This is like connecting a fire hose from one machine (Flame) to another (FFmpeg).

---

## 3. Foreground vs. Background

- **Foreground:** Your mouse turns into a wait cursor, and you wait for FFmpeg to finish.
- **Background:** The script creates a **Backburner** job. It actually writes a tiny Python script *on the fly* and tells Backburner to run it on a render node!

---

## 4. Why is this useful?

- **Custom Formats:** Flame's built-in exporter is great, but FFmpeg can do *anything* (like making tiny H.264 files for WhatsApp or adding custom text overlays).
- **Efficiency:** You can offload heavy transcoding to other computers on your network.

---

## 5. Key Takeaway for Beginners

Flame is an "Open" system. You aren't limited to the buttons inside the software. By using `subprocess` and external tools, you can bridge Flame to any other software on your computer.
