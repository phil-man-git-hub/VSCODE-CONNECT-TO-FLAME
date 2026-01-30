# Insight: The IFFFS Node Hierarchy

This document explains the tree-like structure inside a Flame project. Understanding this "Map" is essential for finding and modifying clips using the Wiretap API.

**Target Audience:** Novice programmers interested in database structures.

---

## 1. The Tree Analogy

Think of a Flame project like a tree. You start at the trunk and follow the branches until you find the "Leaves" (the actual frames of video).

**The Hierarchy:**
1.  **PROJECT:** The trunk. Contains everything for a specific job.
2.  **WORKSPACE:** A large branch. Usually one for every artist on the project.
3.  **DESKTOP:** A smaller branch. Where the current active work lives.
4.  **LIBRARY:** A folder where you store your clips.
5.  **REEL:** A group inside a library.
6.  **CLIP:** The final branch.
7.  **HIRES / VERSION:** The leaves. The actual images you see on the screen.

---

## 2. Important Node Types

- **`PROJECT`**: The top level.
- **`LIBRARY`**: The primary place where clips are organized.
- **`CLIP`**: This node doesn't hold the pictures itself; it is a container for **Versions**.
- **`HIRES`**: This is the child of a Clip that actually holds the high-resolution images.

---

## 3. The "Commit" Concept

When you make a change via the API (like renaming a clip), Wiretap doesn't save it to the hard drive immediately. It waits 2 seconds to see if you have more changes.
- **Manual Save:** You can force a save by sending a **`COMMIT`** command. This is like hitting "Ctrl+S" in a text editor.

---

## 4. Why is this useful?

By knowing this hierarchy, you can write a script that says:
*"Go to Project: 'Car_Ad', find Library: 'Daily_Renders', and list every CLIP inside it."*
Without this map, you'd be lost in thousands of files with no way to find the one you need.

---

## 5. Key Takeaway for Beginners

Everything in Flame is a **Node**. To find anything, you just start at the top (The Project) and "Walk" down the tree using Node IDs until you reach your destination.
