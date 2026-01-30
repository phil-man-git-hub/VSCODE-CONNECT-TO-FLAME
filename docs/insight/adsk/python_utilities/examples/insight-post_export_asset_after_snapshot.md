# Insight: Automating Snapshots with Post-Export Hooks

This document explains the `post_export_asset_using_snapshot.py` example script. It shows how Flame can "watch" its own export process and perform an action immediately after a file is saved.

**Target Audience:** Novice Python programmers interested in workflow automation and "Self-Healing" pipelines.

---

## 1. What is an "Export Snapshot"?

In Flame, a Snapshot is a quick way to save a single frame or a short clip as a file on your hard drive. Usually, once you hit export, the process is finished.

**The Goal:** Every time you take a snapshot in the Player, Flame should automatically **re-import** that file back onto your Desktop reels.

## 2. The `post_export_asset` Hook

Flame has a special "event" called `post_export_asset`. Every time *any* export finishes, Flame shouts: *"Hey! I just finished exporting something. Does anyone want to do anything with it?"*

Our script listens for that shout.

## 3. How the Script Works

The script follows three logic steps:

### Step 1: Filter the Noise
Since this hook runs for *every* export (even big renders), we first check if this was actually a Snapshot:
```python
if info["isSnapshot"]: # Is this a snapshot, or a regular export?
```

### Step 2: Find the Destination
The script looks at your project and finds the first reel on your Desktop:
```python
reel = flame.projects.current_project.current_workspace.desktop.reel_groups[0].reels[0]
```

### Step 3: Re-Import the File
Flame tells the script exactly where the file was saved using `info["destinationPath"]`. The script then tells Flame to import that path:
```python
clip_path = os.path.join(info["destinationPath"], info["resolvedPath"])
flame.import_clips(clip_path, reel)
```

---

## 4. Why is this powerful?

This creates a **Loop**. You can stay in the Player, take snapshots of different versions of a shot, and when you look back at your Desktop, they are all waiting for you in a neat reel. 

It eliminates the tedious manual task of:
1. Exporting.
2. Opening the MediaHub.
3. Browsing to the folder.
4. Dragging the file in.

---

## 5. Key Takeaway for Beginners

Hooks like `post_export_asset` allow Flame to talk to itself. By using the information Flame provides in the `info` dictionary, you can bridge the gap between "Saving a File" and "Using a File."
