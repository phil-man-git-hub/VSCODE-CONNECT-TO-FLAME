# Insight: Managing Clips

This document explains how to handle the most important part of Flame: the **Clips**.

**Target Audience:** Novice programmers interested in media ingestion and organization.

---

## 1. Anatomy of a Clip Node

In Wiretap, a "Clip" is actually a container that holds different versions of the same video:

- **`HIRES`**: The full-quality original images.
- **`LOWRES`**: The small "Proxy" versions used for fast playback.
- **`SLATE`**: A shortcut to the smallest version available.
- **`AUDIOSTREAM`**: The sound attached to the video.

---

## 2. Ingesting Media (Three Methods)

How do you get a movie into a Flame clip via the API?

### Method A: Writing Frames (The "Copy" way)
You manually write raw pixels to a new clip. 
- *Use case:* Creating a new clip from scratch inside a script.

### Method B: Soft-Importing (The "Reference" way)
You tell Flame where the file is on your server. Flame doesn't copy the file; it just "Points" to it.
- *Use case:* The standard way to bring camera footage (like R3D or ProRes) into a project.

### Method C: Path Linking (The "Direct" way)
You give Flame a list of file paths. This is the fastest way to build a clip from a sequence of images (like 10,000 DPX files).

---

## 3. The "No Overwrite" Rule

Flame is very protective of its media. You **cannot** overwrite the frames of an existing clip via the API.
- **The Workflow:** If you want to change a clip, you must create a NEW clip, write the new frames to it, and then delete the old one.

---

## 4. Key Takeaway for Beginners

Clips are the "Leaves" of the Flame tree. By using `WireTapClipFormat`, you define the technical specs, and by using `createClipNode`, you build the container. Remember: always prefer "Soft-Importing" (Method B) to save disk space and time!
