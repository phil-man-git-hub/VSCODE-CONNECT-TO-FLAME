# Insight: Managing Archived Clips

This document explains the `managed_archived_clips.py` script. It shows how to use Python to quickly see which of your clips have been safely backed up and which ones are still sitting on your local storage.

**Target Audience:** Novice Python programmers interested in data management and visual feedback.

---

## 1. The Challenge: What is Archived?

When working on a large project, you often archive (back up) clips to a tape or a server. Once they are archived, you might want to:
1. **Identify** them quickly without looking at a list.
2. **Delete** them to save local space, but *only* if you're sure they are safe.

---

## 2. Key Concepts: Archive Properties

Flame objects have hidden "Archive" properties that Python can read:
- **`item.archive_date`**: Tells you *when* the clip was successfully backed up.
- **`item.archive_error`**: Tells you if the backup failed.

---

## 3. How the Script Works

The script provides two professional tools:

### A. Visual Audit (Color Coding)
It goes through your selection and changes the color of the clips in the Media Panel:
- **Green:** Successfully Archived.
- **Red:** Archive Failed (Error).
- **Default:** Not yet archived.
```python
if item.archive_error:
    item.colour = (1.0, 0.0, 0.0) # Red
elif item.archive_date:
    item.colour = (0.0, 1.0, 0.0) # Green
```

### B. Safe Cleanup
It removes clips from your project, but it uses a safety check:
```python
if item.archive_date and not item.archive_error:
    flame.delete(item)
```
This ensures you **never** delete a clip that hasn't been successfully backed up first.

---

## 4. Why is this useful?

- **Confidence:** You can see at a glance that your work is safe.
- **Organization:** It makes it easy to keep your local project "lean" by removing old files.
- **Troubleshooting:** Red clips immediately show you where a backup failed, so you can fix it.

---

## 5. Key Takeaway for Beginners

Using `item.colour` is a great way to give **Visual Feedback** to the user. Instead of just printing a text list, changing the UI colors makes your script much more intuitive and "integrated" into the Flame experience.
