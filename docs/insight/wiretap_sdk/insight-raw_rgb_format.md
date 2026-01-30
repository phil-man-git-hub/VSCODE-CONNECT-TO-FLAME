# Insight: Raw RGB Video Format

This document explains the technical "Architecture" of an image frame when it moves through Wiretap.

**Target Audience:** Novice programmers interested in low-level image data and memory management.

---

## 1. Pure Pixel Data

When you ask Wiretap for a frame, it doesn't give you a file (like a .jpg). It gives you a **Buffer**—a giant chunk of memory filled with raw color numbers.

- **Orientation:** Flame reads images from **Bottom to Top**. 
- **Components:** Every pixel has 3 parts: **Red, Green, and Blue**.

---

## 2. Bit Size (Depth)

The "Bit Size" tells you how much detail is in every color. Wiretap supports several levels:
- **8-bit:** Standard quality (256 levels of color).
- **10-bit:** Professional quality (1,024 levels).
- **32-bit float:** High-end visual effects (Used for complex lighting and HDR).

---

## 3. The "Padding" Trick

Computers like to read data in neat blocks of 32 bits. If your image width isn't a "Perfect" number, Wiretap adds invisible **Filler Bits** (Padding) to the end of every line.
- **Why?** It makes the computer's CPU work much faster because it doesn't have to "Guess" where the next line starts.

---

## 4. Calculating Memory

If you want to know how much RAM you need to hold a frame, use this formula:
**`Width` x `Height` x `Bytes per Pixel` = `Total Memory`**

- *Example:* A 1080p 8-bit frame is about **6 MB**. 
- *Example:* A 4K 32-bit float frame can be over **100 MB**!

---

## 5. Key Takeaway for Beginners

Raw RGB is like a **"Map of Numbers."** There are no shortcuts or compression. To use it in your script, you need to know exactly how many bits each color uses and how many "Filler" bits are at the end of each line so you don't accidentally shift the image sideways!
