# Insight: Supported Ingest Formats

This document explains the two main ways video is stored on your hard drive and how the Wiretap Gateway understands them.

**Target Audience:** Novice programmers and technical artists.

---

## 1. Image Sequences (The "Stack of Photos")

An image sequence is a folder full of files, where each file is exactly one frame of video.
- **Common Formats:** DPX, OpenEXR, TIFF, Cineon.
- **Easy to Identify:** You can usually tell what's inside just by looking at the file extension (e.g., `.exr`).

---

## 2. Container Formats (The "Box of Chocolate")

A container (or "Wrapper") is one single file that holds many different things inside it (Video, Audio, Metadata).
- **Common Formats:** QuickTime (`.mov`), MXF, RED (`.r3d`).
- **The Catch:** You can't tell what's inside just by the extension. A `.mov` file could be a low-res preview or a high-res master.

---

## 3. How the Gateway Helps

The Wiretap Gateway is built to handle both.
- It automatically "Groups" a stack of 10,000 DPX files into a single Clip node.
- It "Unwraps" container files like ProRes or RED files so you can stream the video frames inside them across the network.

---

## 4. Key Takeaway for Beginners

The Gateway is your **"Universal Decoder."** It doesn't matter if your footage is a giant list of EXR images or a single compressed QuickTime file—the Gateway translates them all into the same "Language" so your Wiretap scripts can read them the same way.
