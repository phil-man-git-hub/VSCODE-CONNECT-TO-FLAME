# Insight: Clip Format Metadata

This document explains the technical "DNA" of a clip—its format, resolution, and original source metadata.

**Target Audience:** Novice programmers interested in technical metadata and file properties.

---

## 1. What is Clip Format?

Every video clip in Flame has a specific "Identity":
- "I am 1920x1080."
- "I am 10-bit color."
- "I play at 24 frames per second."

The **`WireTapClipFormat`** class is the tool you use to read these specific properties.

---

## 2. Accessing the Source Data

When you import a file (like an R3D or an OpenEXR) into Flame, Flame keeps a "Receipt" of where that file came from and all its original settings. This is called the **`SourceData`** stream.

- **The Format:** The `SourceData` is written in **MIO XML**, which is very similar to the "Open Clip" format.
- **The Command:** You use `getMetadata` with the `-s SourceData` flag to see it.

---

## 3. Why is this useful?

- **Verification:** You can write a script that checks every clip in a library to make sure they are all the same resolution.
- **Lineage:** You can look at the `SourceData` to find the exact file path on the server where the original media lives, even if someone renamed the clip in Flame.
- **Audio Info:** For audio clips, there is a matching class called **`WireTapAudioClipFormat`** that tells you things like the sample rate (e.g., 48kHz).

---

## 4. Key Takeaway for Beginners

Think of Clip Format as the **"Spec Sheet"** for your video. While the `info` metadata tells you the name and date, the `ClipFormat` tells you the technical details you need to process the images correctly.
