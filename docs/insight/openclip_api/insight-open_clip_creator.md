# Insight: The Open Clip Creator

This document explains the **Open Clip Creator**, a tool used to build special XML files that Flame uses to manage complex media.

**Target Audience:** Novice technical artists and pipeline developers.

---

## 1. What is an Open Clip?

Think of an **Open Clip** (`.clip` file) as a "Smart Folder." 

Instead of Flame just looking at one movie file, an Open Clip tells Flame:
> "This clip actually has 3 different versions (V1, V2, V3), a separate Left/Right eye for 3D, and it's made up of 5,000 individual DPX images stored on a server."

It "wraps" all that complexity into one single file that Flame can load as a regular clip.

---

## 2. The Hierarchy (From Small to Large)

The Open Clip is built like a pyramid:
1.  **Span:** The lowest level. It's just a path to a piece of media on your hard drive.
2.  **Feed:** A collection of spans that make up one version of a track.
3.  **Track:** All the versions and information about a single channel (like "Video" or "Audio").
4.  **Clip:** The top level. It brings all the tracks together into one object.

---

## 3. Powerful Features: Patterns

The most useful part of Open Clips for programmers is **Patterns**. 
Instead of typing every single filename, you can use **Tokens** like:
- `{name}`: The name of the clip.
- `{version}`: The version number (e.g., v01, v02).
- `{frame}`: The frame number in a sequence.

**Why?** If you drop a new file named `Shot01_v02.mov` into a folder, an Open Clip using patterns will **automatically see it** as a new version inside Flame without you doing anything!

---

## 4. How to Create Them

You have three options:
1.  **In Flame:** Select clips in the MediaHub, right-click, and choose "Create Open Clip."
2.  **The App:** Use the standalone "Open Clip Creator" application.
3.  **Command Line:** Use the `openclip_creator` tool in your terminal to automate the process for thousands of shots at once.

---

## 5. Key Takeaway for Beginners

Open Clips are the **"Glue"** of a professional pipeline. They allow you to organize messy folders of renders and movie files into neat, versioned clips that Flame understands perfectly. If you find yourself manually importing "v02" every time a render finishes, you should probably be using an Open Clip!
