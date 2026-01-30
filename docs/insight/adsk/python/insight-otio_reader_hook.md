# Insight: Importing OpenTimelineIO (OTIO)

This document explains the `otio_reader_hook.py` file. It shows how Flame can understand "OTIO" files—a universal format for sharing movie timelines between different software.

**Target Audience:** Novice Python programmers interested in cross-software compatibility.

---

## 1. What is OTIO?

Imagine you edited a video in Adobe Premiere or DaVinci Resolve and you want to bring that exact timeline (all the clips in the right order) into Flame. Usually, you would use an XML or AAF file. 

**OpenTimelineIO (OTIO)** is a modern, open-source way to do this. It's more reliable and easier for programmers to use.

---

## 2. How the Hook Works

This script acts as a **"Bridge."** 

1.  **The Trigger:** When you try to import an OTIO file, Flame runs the `import_otio` function.
2.  **The Engine:** It calls another script (`otio_reader.py`) to do the heavy lifting.
3.  **The Translation:** It takes the "Clips" and "Tracks" from the OTIO file and recreates them inside Flame as `PySequence` and `PySegment` objects.

---

## 3. Error Handling

Importing timelines is messy. Clips might be missing, or files might be corrupted. The script uses a **`try...except`** block:

```python
try:
    otio.read_otio_file(file_path, first_sel)
except Exception as e:
    return f"Caught exception: {e}"
```

This ensures that if the import fails, Flame doesn't crash. Instead, it "catches" the error and shows a helpful message to the user.

---

## 4. Why is this useful?

- **Interoperability:** It allows Flame to sit in the middle of a pipeline with many different editing tools.
- **Customization:** Because it's written in Python, you can customize *how* the import happens—for example, automatically looking for missing media in a specific studio folder.

---

## 5. Key Takeaway for Beginners

Hooks aren't just for small tasks; they can be used to add **Entire New Features** to Flame. By writing a reader hook, you are teaching Flame how to understand a file format it didn't know about when it was first built!
