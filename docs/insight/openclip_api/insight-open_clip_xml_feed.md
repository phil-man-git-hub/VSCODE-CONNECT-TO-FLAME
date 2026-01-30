# Insight: The Media Stream (<feed>)

This document explains the `<feed>` tag. It is the part of the Open Clip that points to a specific stream of media for a specific version.

**Target Audience:** Novice programmers interested in versioning and media streams.

---

## 1. What is a Feed?

If a **Track** is like a channel on a TV, a **Feed** is the actual show playing on that channel right now. 

Specifically, a `<feed>` represents **one version** of a track. If you have "Version 1" and "Version 2" of a shot, each one will have its own `<feed>` tag inside the track.

---

## 2. Connecting Feeds to Versions

The most important part of a feed is the **`vuid`** (Version Unique ID).
- All feeds that belong to "Version 1" (across all your video and audio tracks) must share the same `vuid` (e.g., `vuid="v1"`).
- This is how Flame knows that when you switch the clip to "Version 2," it should switch the Video Feed AND the Audio Feed at the same time.

---

## 3. Key Information inside a Feed

- **`uid`**: A unique name for this specific stream.
- **`<spans>`**: This is where the actual links to the files on your hard drive are stored.
- **`<sampleRate>`**: The frame rate of the media (e.g., 24 or 30).
- **`<startOffset>`**: A way to slide the media forward or backward in time without changing the original file.

---

## 4. Why is this useful?

Feeds allow you to have **Heterogeneous Media**. 
- Version 1 could be a low-res Proxy (`.mov`).
- Version 2 could be a high-res master (`.exr`).
Because they are in separate `<feed>` tags, Flame can manage them both inside the same clip perfectly.

---

## 5. Key Takeaway for Beginners

The `<feed>` tag is the bridge between the high-level organization (Tracks and Versions) and the low-level files (Spans). It tells Flame: *"For Version X of this track, use these specific files."*
