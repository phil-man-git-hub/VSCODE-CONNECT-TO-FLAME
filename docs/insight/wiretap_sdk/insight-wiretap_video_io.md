# Insight: Reading and Writing Video Media

This document explains the two ways you can pull images (frames) out of Flame using the Wiretap API.

**Target Audience:** Novice programmers interested in image processing and performance.

---

## 1. Two Ways to Get Frames

When you want to look at a frame of video from a server, you have two choices:

### Option A: Read through the Server (The "Easy" Way)
You ask the Wiretap Server to give you the frame.
- **How it works:** The server reads the file from the hard drive, converts it into raw **RGB** pixels, and sends it to your script.
- **Pros:** Very simple. Your script doesn't need to know if the file is a DPX, JPEG, or ProRes. The server does all the "Translation" for you.
- **Cons:** It puts a heavy load on the server's CPU.

### Option B: Read from Storage (The "Fast" Way)
You ask the server for the "Address" of the file, then your script reads the file directly from the hard drive.
- **How it works:** Wiretap gives you a path like `/Volumes/Media/shot.001.dpx`. Your script opens that file.
- **Pros:** Much faster! It doesn't use the server's CPU, and there's no extra "Network Hop."
- **Cons:** More complex. Your script must know how to "Speak the Language" of the file (e.g., you need a library to read DPX or EXR files).

---

## 2. Choosing the Right Handle

- **`WireTapNodeHandle`**: Use this if you have a Clip ID and an index (e.g., "Give me Frame 10 of Clip A"). This is the standard way.
- **`WireTapServerHandle`**: Use this only if you have a "Frame ID" but don't know which clip it belongs to. This is rare and mostly for advanced timeline tools.

---

## 3. Key Takeaway for Beginners

Start with **Option A** (Reading through the server). It's the most "Programmer-Friendly" because you get raw pixels that are ready to use. Only switch to **Option B** if you are moving millions of frames and need to save time and server power.
