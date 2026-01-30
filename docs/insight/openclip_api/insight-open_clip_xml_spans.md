# Insight: Joining Segments (<spans>)

This document explains the `<spans>` tag (with an 's'). It is a simple list that holds all the individual links (spans) for a media stream.

**Target Audience:** Novice programmers learning about sequential data.

---

## 1. What is the `<spans>` tag?

Think of `<spans>` as a **Playlist**. It defines the order in which individual files should be played to make up one version of a track.

---

## 2. Order Matters

The order in which you list the `<span>` tags inside the `<spans>` container is exactly how Flame will play them.
1.  First `<span>` = The beginning of the clip.
2.  Second `<span>` = Joined immediately after the first.
3.  ...and so on.

---

## 3. Why is this useful?

It allows for **"Virtual Assembly."** 
You can join dozens of files together without moving them or renaming them. As long as they are listed in the `<spans>` tag, Flame handles the transition between the files invisibly in the background. This is common for "Spanned" camera recordings where one long take is saved as multiple smaller files.

---

## 4. Key Takeaway for Beginners

The `<spans>` tag is the **"Sequential List"** of your media. It takes individual building blocks (spans) and glues them together into a single, seamless stream of frames for Flame to play.
