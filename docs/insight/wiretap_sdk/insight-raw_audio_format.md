# Insight: Raw Audio Format (DL)

This document explains how sound is "Encoded" when it travels through the Wiretap network.

**Target Audience:** Novice programmers interested in audio engineering and data types.

---

## 1. What is Raw Audio?

Raw audio is just a long list of numbers representing sound waves. Wiretap calls this the **`dlaudio`** format.

---

## 2. Key Formats

The API supports three main types of numbers for sound:
- **`int16`**: CD Quality.
- **`int24`**: Studio Quality.
- **`float`**: High-end processing (Used for internal mixing).

---

## 3. Endianness (The "Big vs Little" rule)

Computers read numbers in different directions.
- **Big-endian:** Reads the most important digit first.
- **Little-endian (`_le`):** Reads the smallest digit first.
Wiretap supports both, and your script must check which one the server is using so the sound doesn't come out as static!

---

## 4. Multi-Channel Audio

If a clip has multiple tracks (like Stereo Left and Right), Wiretap **Interlaces** them. 
- Instead of all the Left samples followed by all the Right samples, it sends them in pairs: `L, R, L, R, L, R`. 
- This ensures that the left and right speakers stay perfectly in sync.

---

## 5. Key Takeaway for Beginners

To read audio in Wiretap, you first ask for the **`formatTag`**. This tells you if the samples are Integers or Floats, and if they are Big- or Little-Endian. Once you know that, you just "De-interlace" the stream to separate the different speakers.
