# Insight: Supported OS and Platforms

This document explains which computers can run the Wiretap SDK.

**Target Audience:** Novice developers planning their studio infrastructure.

---

## 1. Professional Foundations

Wiretap is designed for high-end film and TV workstations. Because of this, it is only built for the two most common professional operating systems:

- **Linux (x86-64):** The industry standard for large render farms and high-end workstations.
- **macOS (Intel & Apple Silicon):** The standard for creative editing and design. Wiretap supports both the older Intel chips and the new **M1/M2/M3 (arm64)** chips.

---

## 2. Why no Windows?

Autodesk Flame's main core runs on Linux and macOS. Since the Wiretap SDK is used to "Reach Inside" Flame, it stays on the same platforms to ensure the best possible performance and security.

---

## 3. Key Takeaway for Beginners

You can write your Wiretap tools on a **Mac** and they will work perfectly when talking to a **Linux** server. This "Cross-Platform" support allows you to build a studio where different types of computers can all work together on the same projects.
