# Insight: Exporting the "Current Frame"

This document explains the `export_current_frame.py` script. It shows how to grab exactly what you are looking at in the player and save it as a high-quality Jpeg.

**Target Audience:** Novice Python programmers learning about non-destructive editing.

---

## 1. The Challenge: Single Frame Export

Flame's exporter usually wants to export a whole clip. If you only want the frame your playhead is on, you have to be clever.

**The Strategy:**
1. Find the current time.
2. **Duplicate** the clip (so we don't ruin the original).
3. Set the In/Out points of the duplicate to that single frame.
4. Export and then **Delete** the duplicate.

---

## 2. Key Concepts

### A. Clip Duplication
```python
duplicate_clip = flame.duplicate(clip)
```
**Why do this?** If you change the In/Out marks on the original clip, the artist will lose their edit! Duplicating creates a "disposable" copy that we can change safely.

### B. Mark Manipulation
```python
duplicate_clip.in_mark = clip.current_time.get_value()
duplicate_clip.out_mark = clip.current_time.get_value() + 1
```
This tells the duplicate clip: *"Your start is the current frame, and your end is one frame later."*

### C. The `try...finally` Block
This is a "Safety Net."
```python
try:
    # Do the export...
finally:
    flame.delete(duplicate_clip)
```
The `finally` part runs *no matter what*—even if the export crashes. This ensures that Flame's memory doesn't get cluttered with thousands of hidden duplicate clips.

---

## 3. Finding the Save Location

The script uses a neat trick to find where to save the file. It tries to use the path you currently have open in the **MediaHub**. This is very intuitive for the user!

---

## 4. Key Takeaway for Beginners

Always be **Non-Destructive**. If your script needs to change a clip's settings just for a moment, consider creating a duplicate, doing the work, and then cleaning up after yourself.
