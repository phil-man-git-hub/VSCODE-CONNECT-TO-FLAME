# Insight: Automating Motion Vector Caching

This document explains the `cache_motion_vectors.py` script. It shows how to programmatically build a "Node Tree" in Batch to calculate and save motion vectors.

**Target Audience:** Novice Python programmers learning how to manipulate the Batch Schematic.

---

## 1. What are Motion Vectors?

Motion vectors are data that describe how pixels move from one frame to the next. In Flame, calculating this can be slow, so we often "Cache" (save) the results. 

**The Goal:** Instead of manually adding an "Action" node, adding a "Motion Vectors Map," and clicking "Cache," this script does it all in one click.

---

## 2. Key Concepts

### A. Node Creation & Positioning
The script uses `flame.batch.create_node("Action")`. 
- **Coordinates:** It uses `pos_x` and `pos_y` to place the nodes neatly in the schematic. It adds `400` to the X-position so the new node doesn't overlap the old one.

### B. Connecting Nodes
To make the nodes work, they must be "wired" together.
```python
flame.batch.connect_nodes(clip, "Default", media, "Default")
```
This is like dragging a line between two dots in the Batch interface.

### C. Caching a Range
The script finds the start and end frame of the clip and tells the node to render exactly that range:
```python
motion_map.cache_range(start, end)
```

---

## 3. Two Ways to Use the Script

1.  **In Batch:** Right-click a clip node and select "Cache Motion Vectors Map."
2.  **From the Desktop:** Right-click your Desktop and select "Create Batch and Cache...".
    - This version is even more powerful! It opens a file browser, lets you pick a clip, creates a **brand new Batch Group**, imports the clip, and then sets up the motion vectors.

---

## 4. Why is this useful?

- **Standardization:** It ensures that every Motion Vector Map is set up exactly the same way every time.
- **Speed:** It handles all the tedious clicking and dragging of nodes automatically.
- **Batch Processing:** You can use the "Desktop" version to process a file without even having a Batch group open yet.

---

## 5. Key Takeaway for Beginners

When you use the Python API, you are basically a **"Ghost Operator."** Anything a human can do with a mouse (creating nodes, connecting them, clicking 'Cache'), you can do with code by calling the right functions.
