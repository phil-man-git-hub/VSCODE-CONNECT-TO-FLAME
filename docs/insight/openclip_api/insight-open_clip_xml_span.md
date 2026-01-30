# Insight: The File Link (<span>)

This document explains the `<span>` tag. It is the part of the Open Clip that describes a single continuous piece of media.

**Target Audience:** Novice programmers interested in how software links to files.

---

## 1. What is a Span?

In the real world, a "Span" is a distance between two points. In an Open Clip, a `<span>` is a continuous segment of time that points to a specific physical location on your hard drive.

A `<feed>` is made up of one or more spans.

---

## 2. Key Information inside a Span

- **`<path>`**: The address of the file (e.g., `Media/video.mov`).
- **`<duration>`**: How many frames this specific file lasts.
- **`<trackIndex>`**: If you are pointing to a file with many tracks (like a multi-channel OpenEXR), this tells Flame which specific channel to look at (e.g., Index 0 for Red, Index 1 for Green).

---

## 3. Why use multiple spans?

Imagine you have a long movie that was recorded by a camera that split the file into 4GB chunks (`part1.mov`, `video2.mov`, `final.mov`). 
Instead of joining them in an editing program, you can just list three `<span>` tags inside your Open Clip. Flame will play them back-to-back as if they were one single, perfect file!

---

## 4. Creating Gaps

If you have a `<span>` with a duration but **no path**, Flame treats it as a **Gap**. It will just show black for that amount of time. This is a great way to "Pad" a clip if you know more media is coming later.

---

## 5. Key Takeaway for Beginners

The `<span>` tag is the **"Building Block"** of your media stream. By stacking multiple spans together, you can bridge multiple files into one continuous clip without ever needing to render a new file.
