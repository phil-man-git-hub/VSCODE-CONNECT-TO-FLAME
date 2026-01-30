# Insight: Injecting Metadata into OpenEXR Files

This document explains the `inject_metadata_write_file_exr.py` script. It shows how to embed important information (like the project name and user) directly into the headers of your rendered files.

**Target Audience:** Novice Python programmers interested in pipeline data and metadata.

---

## 1. Why Inject Metadata?

When you render a shot as an OpenEXR sequence, the files go onto a server where other artists (like compositors or colorists) pick them up. If they have a problem with a file, they need to know:
- Which project did this come from?
- Which version of Flame rendered it?
- Who was the artist?

**This script automates that bookkeeping.** It "tags" every frame with this info invisibly inside the file header.

---

## 2. Key Concepts

### A. The `batch_export_begin` Hook
Unlike the `end` hook, this one runs *before* the first frame is written. This is the perfect time to set the "Rules" for the render.

### B. Targeting the "Write File" Node
The script finds the specific node doing the work:
```python
write_file = flame.batch.get_node(info.get("nodeName"))
```

### C. Channel-Specific Metadata
OpenEXR files can have many channels (Red, Green, Blue, Alpha, Depth). The script iterates through every channel and injects the same metadata into all of them so the info is never lost.
```python
write_file.set_metadata_value(channel_name, key, value)
```

---

## 3. What Information is Saved?

The script currently saves:
- **`flame/version`**: The version of Flame used.
- **`flame/project`**: The name of the project.
- **`flame/workspace`**: The artist's workspace.
- **`flame/user`**: The artist's name.

---

## 4. Why is this useful?

- **Traceability:** You can always find the source of a file, even years later.
- **Automation:** Other software (like ShotGrid or Deadline) can read these headers to automatically organize files.
- **Accuracy:** It removes the need for artists to manually type notes into the render settings.

---

## 5. Key Takeaway for Beginners

Metadata is the **"DNA"** of a digital file. By using the `set_metadata_value` function, you are ensuring that your files carry their history with them wherever they go.
