# Insight: Reading Audio Media

This document explains how Wiretap handles audio data and how it differs from video data.

**Target Audience:** Novice programmers interested in audio processing and network efficiency.

---

## 1. Small Data, Big Network

Audio data is tiny compared to video. 
- **Video:** 1 second of video can be 30MB or more.
- **Audio:** 1 second of audio is only about 172KB.

If you asked Wiretap for every single audio sample one-by-one, the network would get "Clogged" with thousands of tiny requests. 

---

## 2. The "Block" Solution

To keep things fast, Wiretap doesn't send audio sample-by-sample. Instead, it groups samples together into **Blocks** (called "Frames" in the API).

- When you ask for an "Audio Frame," you are actually getting a chunk of sound—usually enough to match exactly one frame of video.
- The size of these blocks is determined by the **`WireTapClipFormat`**. It tells your script: *"This block has 2,000 samples of 16-bit audio."*

---

## 3. Why is this useful?

This ensures that audio and video stay perfectly in sync. Because one "Frame" of audio matches one "Frame" of video, your script can process them together without having to do complex math to align the timing.

---

## 4. Key Takeaway for Beginners

In Wiretap, **Audio is treated like Video**. You ask for a "Frame" of audio just like you would for a picture. The API handles the grouping of tiny samples into efficient blocks so your network stays fast and your sound stays in sync.
