# Insight: Organizing Channels (<track>)

This document explains the `<track>` tag. It is used to separate different streams of data—like Video and Audio—inside a single Open Clip.

**Target Audience:** Novice programmers interested in multi-channel media.

---

## 1. What is a Track?

In Flame, a clip isn't just a movie; it's a collection of channels. 
The `<track>` tag allows you to define these channels individually. Common examples include:
- A **Video** track.
- An **Audio** track (you can have many of these).
- A **Matte** (Alpha) track.
- A **Layer** from a Photoshop or OpenEXR file.

---

## 2. Key Attributes of a Track

- **`uid` (Unique ID)**: Every track must have a name that makes it unique (e.g., "t0", "audio_left", "Beauty_Pass").
- **`<trackType>`**: Usually `video` or `audio`.
- **`<feeds>`**: This is where the actual media links live for this specific track.

---

## 3. Advanced Overrides

Normally, a track is as long as the movie file it points to. But you can use the `<track>` tag to **force** a specific timing:

- **`<startTimecode>`**: You can tell Track 1 to start at 01:00:00:00 even if the file itself starts at zero.
- **`<duration>`**: You can make a track appear longer or shorter than the physical media. If you make it longer, Flame will automatically show a "No Media" slate for the extra time.

---

## 4. Why use multiple tracks?

Imagine a 3D artist renders a scene. They give you one OpenEXR file that contains the "Beauty" pass, a "Shadow" pass, and a "Reflection" pass. 
By using three `<track>` tags in your Open Clip, Flame will see these as three separate, perfectly synced layers that you can edit independently!

---

## 5. Key Takeaway for Beginners

The `<track>` tag is like a **"Channel Strip"** on a mixer. It doesn't hold the media itself (that's the job of the `feed`), but it organizes the media into a logical stream that Flame can play back and edit.
