# Insight: The OTIO Translation Engine

This document explains the `otio_reader.py` script. While the "Hook" script starts the process, this is the "Brain" that does the actual work of turning an OTIO file into a Flame sequence.

**Target Audience:** Novice Python programmers interested in object-oriented programming (OOP) and "Data Mapping."

---

## 1. What is a "Reader" Class?

This script uses a **Class** called `FlameOTIOReader`. 
- **The Concept:** Think of this class as a professional translator. It reads a book in one language (OTIO) and writes a new one in another language (Flame API).

---

## 2. Key Translation Steps

The script doesn't just "copy" the file. It has to map every OTIO concept to a Flame concept:

### A. The Timeline Map
- **OTIO Timeline** becomes a **Flame Sequence**.
- **OTIO Track** becomes a **Flame Track** (Video or Audio).
- **OTIO Clip** becomes a **Flame Segment**.

### B. Frame Rate Conversion
OTIO might say "23.98 fps," but Flame expects exactly `"23.976 fps"`. The function `_otio_rate_to_frame` handles this tricky math so the timing stays perfect.

### C. Finding Media
OTIO files often use "Relative Paths" (e.g., `../media/shot.mov`). The script is smart enough to find the real file on your hard drive by looking at where the OTIO file itself is saved.

---

## 3. Advanced Feature: "Pre" and "Post" Hooks

The reader is designed to be extensible. It uses its own internal hooks:
- **`pre_hook_Clip`**: Runs just before a clip is created.
- **`post_hook_Clip`**: Runs after the clip is in Flame.
This allows other programmers to add custom logic (like adding a specific Color FX) without changing the main reader code.

---

## 4. Why is this useful?

- **Robustness:** By putting all the logic in one Class, the code is easier to test and fix.
- **Complexity:** It handles nested structures (like stacks and gaps) that a simple script couldn't manage.
- **Accuracy:** It ensures that metadata, markers, and transitions are preserved during the move between software.

---

## 5. Key Takeaway for Beginners

Mapping data from one format to another is a common job for Python. The secret is to break the big problem into small pieces: first translate the Timeline, then the Tracks, then the Clips, then the Markers. 
