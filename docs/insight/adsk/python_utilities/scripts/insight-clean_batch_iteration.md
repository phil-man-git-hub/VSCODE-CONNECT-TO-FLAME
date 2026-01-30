# Insight: Deep-Cleaning Project Iterations

This document explains the `clean_batch_iteration.py` script. It shows how to save disk space by deleting old "Iterations" (saved versions) of your Batch work.

**Target Audience:** Novice Python programmers interested in project maintenance and "Recursion."

---

## 1. What are Batch Iterations?

Every time you save your work in Batch, Flame creates an "Iteration." Over a long project, these can add up to hundreds of files, taking up a lot of space on your storage.

**The Goal:** A "Nuclear Option" to delete all iterations from a specific Folder, Library, or even your entire Desktop.

---

## 2. Key Concept: Recursion

This script uses a very important programming technique called **Recursion**.

Imagine a Library contains a Folder, which contains another Folder, which finally contains a Batch Group. To find that Batch Group, the script has to "dig" through the folders.

The `find_batch_group` function does this:
1. It looks for Batch Groups in the current folder and cleans them.
2. It then looks for more folders inside the current one.
3. If it finds a folder, **it calls itself** to look inside that new folder.

```python
def find_batch_group(folder):
    # ... clean things here ...
    for folders in folder.folders:
        find_batch_group(folders) # Calling itself!
```

---

## 3. How the Script Works

- **Multiple Scopes:** The script is smart. It checks if you clicked on a Library, a Folder, or a Batch Group and uses the correct logic for each one.
- **Silent Delete:** It uses `flame.delete(iteration, confirm=False)`. 
  - *Warning:* Setting `confirm=False` means Flame won't ask "Are you sure?" It just deletes them instantly. This is fast, but dangerous!

---

## 4. Why is this useful?

- **Storage Management:** It's the fastest way to "slim down" a project before archiving it.
- **Organization:** It removes the clutter of old, failed experiments and keeps only the current work.
- **Workflow Speed:** Instead of opening 50 Batch Groups and deleting iterations manually, you click one button on the top-level Library.

---

## 5. Key Takeaway for Beginners

**Recursion** is the best way to deal with "Tree" structures (like folders inside folders). Instead of writing complex logic to guess how deep the folders go, you just tell the function to keep digging until it hits the bottom.
