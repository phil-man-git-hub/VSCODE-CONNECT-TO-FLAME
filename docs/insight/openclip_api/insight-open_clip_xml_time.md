# Insight: Measuring Time (<time>)

This document explains the `<time>` tag. It is how Flame calculates where a clip sits on a timeline and how long it lasts.

**Target Audience:** Novice programmers interested in timecodes and duration.

---

## 1. How is Time measured in Flame?

In digital video, time isn't just "minutes and seconds." It's a combination of two things:
1.  **A Count:** How many frames (samples) are there?
2.  **A Speed:** How fast do those frames play?

---

## 2. The Anatomy of the `<time>` tag

The `<time>` tag combines these two parts:

- **`<nbTicks>`**: The number of "Ticks" or Frames. (e.g., 240 frames).
- **`<rate>`**: The speed (e.g., 24 frames per second).
- **`<dropMode>`**: For certain broadcast standards (like NTSC), you might need "Drop Frame" (`DF`) or "Non-Drop Frame" (`NDF`) mode to keep the clock accurate.

---

## 3. Calculating Seconds

To find out how many seconds a clip is, Flame does a simple math problem:
**`nbTicks` divided by `rate` = `seconds`**

*Example:* `48 frames` / `24 fps` = `2 seconds`.

---

## 4. Why is this useful?

- **Flexibility:** You can define time in frames, or you can get extremely precise using fractional rates (like `24000/1001`).
- **Communication:** It allows the Open Clip to speak the "Language of Timecode," which is essential for editors who need to know exactly which hour, minute, and second a shot belongs to.

---

## 5. Key Takeaway for Beginners

Time in an Open Clip is a **Calculation**. The `<time>` tag gives Flame the two ingredients it needs (Count and Speed) to correctly place your media on the timeline.
