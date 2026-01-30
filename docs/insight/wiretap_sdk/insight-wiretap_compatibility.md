# Insight: Version Compatibility

This document explains how different versions of Flame and the Wiretap API work together without breaking your studio's pipeline.

**Target Audience:** Novice developers concerned about software updates.

---

## 1. Do I need to re-write my code?

The best thing about the Wiretap API is that it is **Backward-Compatible**. 
- If you write a tool for Flame 2025, it will still work perfectly with Flame 2026.
- You only need to update your script if you want to use a **New Feature** that was just added.

---

## 2. Server vs. Client Versions

When your script (The Client) connects to a Flame workstation (The Server), they perform a "Handshake":

- **Backburner:** Always uses the newest version available on the machine.
- **IFFFS / Gateway:** They try to **Match** the version of your script. If your script says "I am Version 2025," the server will try to act like a 2025 server to make sure your code understands the response.

---

## 3. Forcing a Version

If you are working on a very old project, you can tell your script to "Pretend" to be an older version of Flame using this command:
`WireTapClientSetVersion(year, minor, patch)`

---

## 4. Why is this useful?

It allows you to build **Long-Term Tools**. You can write a single pipeline script that manages projects from five years ago and projects starting today, and Wiretap handles the translation between versions automatically.

---

## 5. Key Takeaway for Beginners

Don't be afraid of Flame updates! Your Wiretap scripts are built on a very stable foundation. As long as you aren't using "Experimental" features, your code will continue to work year after year as the software evolves.
