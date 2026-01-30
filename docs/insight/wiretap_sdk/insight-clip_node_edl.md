# Insight: Clip Node Metadata (EDL)

This document explains the **EDL (Edit Decision List)** metadata stream inside a Flame clip. This is how Flame stores the "Edit Instructions" for a timeline.

**Target Audience:** Novice technical artists interested in conforming and editorial workflows.

---

## 1. What is a Wiretap EDL?

In the old days of film editing, an EDL was a simple text file that told a machine: *"Take 5 seconds from Tape A and join it to 10 seconds from Tape B."*

Wiretap uses a modern version of this called the **CMX 3600** format, but it adds special "Autodesk Tags" (starting with **`DLEDL:`**) to store extra info that normal EDLs can't handle.

---

## 2. Reading the "Map"

When you look at a Wiretap EDL, you will see lines like these:

- **`FCM: NON-DROP FRAME`**: Tells you if the clock skips numbers to stay accurate.
- **`DLEDL: SOURCEID`**: A unique ID for the original clip. This is much more reliable than just using a name like "v1."
- **`DLEDL: EDIT:0 FRAME`**: A specific hex code (like `0x2581...`) that identifies every single image in the edit.
- **`DLEDL: REEL`**: The full name of the tape or folder where the media lives.

---

## 3. Transitions and Virtual Sources

The EDL even handles complex things:
- **Dissolves:** These are marked with a `D` followed by the number of frames (e.g., `D 004`).
- **Virtual Tapes:** If a clip was generated inside Flame (like a solid Green color or SMPTE bars), the EDL gives it a "Virtual" tape name like `GREEN` or `COLOUR`.

---

## 4. Why is this useful?

By reading the EDL stream, your script can perfectly reconstruct a timeline in another application or database. You can see exactly which frames were used from which files without ever having to open the project in Flame.

---

## 5. Key Takeaway for Beginners

The EDL is the **"Recipe"** for your timeline. While the media files are the ingredients, the EDL tells Flame exactly how to "Cook" them—which parts to cut, where to overlap them, and which frame IDs to pull from the server.
