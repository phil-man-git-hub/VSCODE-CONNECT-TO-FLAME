# Insight: Customizing the Export Pipeline

This document explains the `export_hook.py` file. It is one of the most powerful and complex hook files in Flame, allowing you to control exactly what happens when media is saved to disk.

**Target Audience:** Novice Python programmers interested in complex automation and data management.

---

## 1. The Export "Sandwich"

Exporting a clip in Flame isn't just one single action; it's a sequence of events. Flame allows you to "sandwich" your own code at every layer of this process.

### The Execution Order:
1.  **`pre_export`**: Runs once at the very beginning of the whole export job.
2.  **`pre_export_sequence`**: Runs for every Sequence in your export list.
3.  **`pre_export_asset`**: Runs for every individual file (Video, Audio, OpenClip) being created.
4.  **`post_export_asset`**: Runs as soon as a file is finished.
5.  **`post_export_sequence`**: Runs when all assets in a sequence are done.
6.  **`post_export`**: Runs once everything is finished.

---

## 2. Key Features

### A. The "Abort" Switch
Most `pre_` hooks allow you to cancel the export if something is wrong.
```python
if info["destinationPath"] == "/forbidden/path":
    info["abort"] = True
    info["abort_message"] = "You cannot export to this server!"
```

### B. Overwriting Files
The `export_overwrite_file` hook lets you decide what happens if a file already exists. 
- You can tell Flame to always `"overwrite"`, `"skip"`, or `"ask"` the user. This is perfect for avoiding those annoying pop-up boxes!

### C. `userData` Sharing
Like the Batch hooks, Export hooks use a `userData` dictionary. You can put info in at the `pre_export` stage and read it back at `post_export`. This is how you track total export time or gather a list of every file created.

---

## 3. Why is this useful?

- **Custom Naming:** You can use `pre_export_asset` to dynamically change the filename (`info["resolvedPath"]`) based on the shot name or project code.
- **Post-Processing:** Use `post_export_asset` to automatically trigger an external transcode (like making a low-res H.264 for the web) as soon as the high-res file is ready.
- **Security:** Ensure that exports only go to approved storage locations.

---

## 4. Key Takeaway for Beginners

The export pipeline is granular. If you want to change something for the *whole job*, use `pre_export`. If you want to change something for *one specific clip*, use `pre_export_asset`. Understanding this hierarchy is the key to building a professional studio pipeline.
