# Insight: FAQs and Troubleshooting

This document provides a summary of the most common questions and hurdles people face when starting with the Wiretap SDK.

**Target Audience:** Novice developers looking for quick solutions to common problems.

---

## 1. Where do I start?

If you are stuck, the first thing to check is the **General API** issues. This covers things like how Wiretap handles errors and how to use threads safely.

---

## 2. Common Troubleshooting Areas

The documentation is split into several "Problem Zones":

- **IFFFS Issues:** Problems with Flame's internal database (like unlinked clips).
- **Network Issues:** Why can't I see all the servers on my network? (Check your router's "Multicast" settings!).
- **Media Issues:** Problems reading or writing specific video or audio formats.
- **Mac Issues:** Specific hurdles for macOS users, like library paths.
- **Permissions:** Why is the "Root" user blocked from accessing media over the network?

---

## 3. Key Pro-Tip: Multicast Ping

If your script can't find any servers, try this command in your terminal:
`ping 224.0.0.1`
- If every machine on your network responds, your network is healthy.
- If no one responds, your router is blocking Wiretap's "Auto-Discovery" messages.

---

## 4. Key Takeaway for Beginners

Troubleshooting is a process of **Elimination**. 
1.  Check the network first (Ping).
2.  Check the server next (Is it running?).
3.  Check your script last (Are you handling the `lastError` correctly?).
Most problems are solved by simply following these three steps in order.
