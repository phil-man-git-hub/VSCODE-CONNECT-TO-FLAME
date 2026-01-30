# Insight: Wiretap Self-Discovery

This document explains how Wiretap finds other machines on your network automatically, almost like a "Bluetooth pairing" for video servers.

**Target Audience:** Novice technical artists interested in network configuration.

---

## 1. How does it find a machine?

When you run a Wiretap command, you need to tell it which machine to talk to. You have three ways to do this:

### A. The "Direct" Way (IP Address)
- **Format:** `192.168.1.50:5555`
- **Pros:** The fastest and most reliable. Bypasses all searching.
- **Cons:** Not flexible (if the machine's IP changes, your script breaks).

### B. The "Name" Way (DNS)
- **Format:** `FlameWorkstation01:5555`
- **Pros:** Easier for humans to read.
- **Cons:** Can be slow if your network's "Name Server" (DNS) is acting up.

### C. The "Auto" Way (Multicast Discovery)
- **Format:** `IFFFS` or `Gateway` or `Backburner`
- **Pros:** Extremely flexible. You don't need to know the IP or port. 
- **How it works:** Your script shouts: *"Is there an IFFFS server here?"* and the first workstation to respond sends back its full details.

---

## 2. When Auto-Discovery Fails

In complex setups (like cloud servers or different office floors), the "shouting" might not reach every machine. 
- **The Fix:** You can "hardcode" the network map in a file called `services.cfg`. This acts like a phone book that tells Wiretap exactly where everyone lives without having to shout for them.

---

## 3. Key Takeaway for Beginners

Self-discovery is great for small offices, but for professional studio pipelines, using a specific **IP Address** or a **Services Config** file is much safer. It ensures your scripts always connect to the right machine instantly every time.
