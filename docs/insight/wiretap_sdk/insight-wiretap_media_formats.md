# Insight: Media and Metadata Formats

This document provides an overview of the different "Languages" Wiretap speaks when it moves images, sounds, and data across your network.

**Target Audience:** Novice programmers interested in technical specifications and data types.

---

## 1. Moving Raw Media

Wiretap is designed for high performance. When it sends video or audio to your script, it usually converts it into a "Raw" format that is easy for a computer to understand:

- **Raw Video (RGB):** Images are sent as a simple buffer of Red, Green, and Blue pixels. There are no complex headers or compression—just pure color data.
- **Raw Audio (DL):** Sound is sent in blocks of samples (similar to a WAVE file but simplified for the network).

---

## 2. Moving Metadata (Info)

Metadata is the "Instructions" for the media. Wiretap uses two main formats for this:

- **XML (The Modern Way):** Projects, Managers, and Servers use XML to store settings. It's easy for humans to read and for computers to search.
- **EDL (The Editorial Way):** Timelines use an augmented version of the CMX 3600 EDL format to store edit instructions and transitions.

---

## 3. Specialized Formats

- **Clip Format:** A specialized metadata stream that describes the technical DNA of a clip (Resolution, Bit Depth, etc.).
- **Source Data:** The original "Receipt" for an imported file, stored in MIO XML format.

---

## 4. Why is this useful?

By understanding these formats, you can decide how to best "Listen" to the Wiretap network. 
- If you want to build a **Dashboard**, you listen to the **XML** streams.
- If you want to build an **Auto-Editor**, you listen to the **EDL** streams.
- If you want to build a **Transcoder**, you listen to the **Raw RGB** streams.

---

## 5. Key Takeaway for Beginners

Wiretap is a **Translator**. It takes the complex, proprietary databases inside Flame and translates them into standard formats like **XML**, **EDL**, and **Raw RGB** so your own scripts can easily understand them.
