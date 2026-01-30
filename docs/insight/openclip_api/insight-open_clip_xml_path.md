# Insight: Linking to Files (<path>)

This document explains the `<path>` tag. It is the lowest level of an Open Clip and tells Flame exactly where to find the physical media on your computer or server.

**Target Audience:** Novice programmers interested in file systems and patterns.

---

## 1. What is a Path?

A path is just an address. In an Open Clip, it can be two things:
1.  **A Single File:** Like a QuickTime movie (`video.mov`).
2.  **A Pattern:** Like a sequence of images (`shot_[001-100].dpx`).

---

## 2. Encoding Types

The `encoding` attribute tells Flame how to read the text inside the tag:
- **`encoding="file"`**: Take the text literally. Don't look for brackets or numbers.
- **`encoding="pattern"`**: Look for special characters like `[]` or `{frame}` to find a range of files.

---

## 3. Absolute vs. Relative Paths

- **Absolute:** The full address from the root of the computer (e.g., `/Volumes/Media/Shot01.mov`).
- **Relative:** The address starting from where the `.clip` file is saved (e.g., `Media/Shot01.mov`).
  - *Tip:* Relative paths are better because you can move the entire project folder to a new drive without breaking the links!

---

## 4. Range Patterns

Open Clip supports a shorthand for image sequences:
- `shot_[0001-0010].exr` will automatically find frames 1 through 10.
- `shot_{frame}.exr` will find *every* frame in that folder that matches the name, no matter what the numbers are.

---

## 5. Key Takeaway for Beginners

The `<path>` tag is the **"Street Address"** for your media. Whether you are pointing to one big movie file or 10,000 individual images, the `<path>` tag is where you give Flame the specific coordinates to find those bits and bytes.
