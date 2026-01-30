# Insight: Open Clip XML Reference

This document explains the technical structure of an **Open Clip** XML file. It is the "Dictionary" for how Flame reads the instructions inside a `.clip` file.

**Target Audience:** Novice programmers interested in XML and data structure.

---

## 1. What is inside an Open Clip?

An Open Clip file is basically an XML list of directions. It tells Flame:
- **Where** the files are (File paths).
- **When** they start and end (Timecodes).
- **How** they are organized (Tracks and Versions).

**Important Note:** An Open Clip is **NOT** a timeline like an EDL or AAF. It doesn't contain "edits" or "effects." It only describes the media itself.

---

## 2. Key Components (The XML Tags)

When you open a `.clip` file in a text editor, you will see several standard tags:

- **`<clip>`**: The main container.
- **`<tracks>`**: Groups together all the different channels (Video, Audio).
- **`<versions>`**: Lists the different revisions of the media.
- **`<feeds>`**: The specific media streams for a version.
- **`<spans>`**: The actual links to files on your hard drive.

---

## 3. Version History

Open Clip has evolved over the years. The most current version is **Version 7**. 
- Newer versions support things like **Nested Dictionaries** (for complex metadata) and **Resolved Color Spaces** (so Flame knows exactly what color management to apply).

---

## 4. Learning by Example

The best way to understand the XML is to look at existing files. Flame installs several examples on your system:
`/opt/Autodesk/openclip_examples`

Try opening these in a text editor like VS Code to see how the tags fit together.

---

## 5. Key Takeaway for Beginners

Think of the Open Clip Reference as the **"Syntax Guide"** for Flame's media language. If you want to write a script that automatically generates these files, you need to follow these rules exactly so Flame can read your instructions correctly.
