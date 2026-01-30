# Insight: Wiretap Terminology

This document explains the basic words and concepts you need to know to work with the **Wiretap SDK**.

**Target Audience:** Novice programmers learning the "Language" of Flame networking.

---

## 1. Servers and Clients

- **Wiretap Server:** A program running on a machine that "exposes" a database to the network. It's like a librarian who knows where all the books are.
  - **IFFFS:** Exposes Flame's clip library.
  - **Gateway:** Exposes regular files on your hard drive.
  - **Backburner:** Exposes render jobs and status.
- **Wiretap Client:** A program (like your Python script) that asks the server for information. It's like the person asking the librarian for a book.

---

## 2. Nodes and Node IDs

- **Node:** A single "Item" in the Wiretap tree. A project is a node, a library is a node, and a clip is a node.
- **Node ID:** A unique string of text that identifies exactly which node you are talking about (e.g., `clip:123456`).

---

## 3. Frames and Formats

- **Frame:** A single image or a small piece of audio. When you ask Wiretap for a frame, it gives you a "Buffer" (a chunk of raw data).
- **Frame Format:** The "Translation Guide" for the data. It tells the computer if the frame is an `RGB` image, a `YUV` image, or an `AIFF` audio clip.

---

## 4. Metadata

Metadata is "Data about Data." In Wiretap, it is usually a text file (XML or EDL) that describes a clip. It tells you things like the timecode, the name of the clip, and what effects are applied to it.

---

## 5. Key Takeaway for Beginners

To use Wiretap, you just need to know the **Node ID** of what you want and the **Server** where it lives. Once you have those two things, you can ask for the **Metadata** (to see what it is) or the **Frames** (to see the actual video).
