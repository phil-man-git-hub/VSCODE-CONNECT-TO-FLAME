# Insight: Project Metadata (XML)

This document explains the XML structure Flame uses to store project settings like resolution, frame rate, and color management.

**Target Audience:** Novice programmers interested in technical specifications and configuration.

---

## 1. What is Project Metadata?

When you create a new project in Flame, you set certain "Rules"—for example, "This project is 1920x1080 at 24fps." Wiretap stores these rules in an XML stream.

---

## 2. Key Settings (The XML Tags)

When you look at a project's metadata, you will see these important tags:

- **`<FrameWidth>` / `<FrameHeight>`**: The "Size" of your video.
- **`<FrameRate>`**: How fast it plays (e.g., `24 fps` or `29.97 fps NDF`).
- **`<AspectRatio>`**: The shape of the screen (e.g., `1.77778` for 16:9).
- **`<ProxyQuality>`**: How Flame generates low-res "Proxy" versions of your media.
- **`<OCIOConfigFile>`**: The path to your color management "Rulebook."

---

## 3. Editable vs. Fixed

- **Creation Only:** Some settings, like where the media is stored (`<MediaDir>`), can ONLY be set when the project is first created.
- **Always Editable:** You can change things like the `<Description>` or `<FrameDepth>` (8-bit vs 10-bit) any time you want using the `setMetaData` command.

---

## 4. Why is this useful?

By reading this XML, a pipeline script can automatically check if a project is set up correctly according to studio standards. If a project is set to "8-bit" when it should be "16-bit fp," the script can flag it or even fix it automatically.

---

## 5. Key Takeaway for Beginners

Project XML is the **"Birth Certificate"** of a Flame project. It lists every important detail about how video should be handled. If you want to automate project creation, you must master these XML tags!
