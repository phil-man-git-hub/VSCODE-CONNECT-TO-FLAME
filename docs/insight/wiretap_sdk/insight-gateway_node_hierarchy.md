# Insight: The Gateway Node Hierarchy

This document explains how the **Wiretap Gateway** looks at your computer's hard drive and turns it into a neat, organized list of clips.

**Target Audience:** Novice programmers interested in file systems and media browsing.

---

## 1. What is the Gateway Hierarchy?

The Gateway is like a **Translator**. It looks at a messy folder full of DPX or ProRes files and translates them into standard Wiretap Nodes.

- **`DIR`**: A standard folder on your hard drive.
- **`CLIP`**: A "Smart" node that groups multiple frames (like `shot.001.dpx` to `shot.100.dpx`) into a single object.
- **`HIRES`**: The actual video data inside the clip.

---

## 2. Multi-Process Design

To keep everything fast, the Gateway uses two types of processes:
1.  **The Main Process:** The "Boss" that handles the startup.
2.  **The Session Processes:** A private "Assistant" created just for your script. This assistant keeps track of what you are doing so you don't interfere with other users on the network.

---

## 3. Warning: Node IDs are "Black Boxes"

A Node ID might look like a simple piece of text, but **never try to guess what it means**. 
- **The Rule:** Always ask the "Parent" node for the list of its children. Don't try to build a Node ID manually, or your script will break when you update Flame!

---

## 4. Key Takeaway for Beginners

The Gateway is your **"Window"** to the outside world. It turns raw files on a hard drive into professional Flame clips that your scripts can read and process. Always use the `wiretap_get_children` command to explore this hierarchy safely.
