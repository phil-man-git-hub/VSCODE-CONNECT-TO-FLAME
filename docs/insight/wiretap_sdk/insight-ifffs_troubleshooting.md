# Insight: IFFFS Troubleshooting (Unlinked Media)

This document explains a common "Gotcha" when using Wiretap to build timelines in Flame: why media sometimes appears "Unlinked" (Offline).

**Target Audience:** Novice technical artists building automated conforming tools.

---

## 1. The "Online" Mystery

You write a perfect script to build a timeline via Wiretap, but when you open Flame, the clips are all "Checkerboard" (No Media). Why?

Flame is very strict about where it looks for files. When you create a timeline through the IFFFS Wiretap server, Flame uses two rules to find the media:

### Rule A: The Same Reel
Flame expects the source clips to be in the **Same Reel** as the timeline you are building. If you put the sources in "Reel 1" but build the timeline in "Reel 2," Flame might not look in the right place to link them.

### Rule B: Tape Name Match
Flame identifies clips by their **Tape Name**. 
- If your media file says its tape name is `SHOT_01`, but your script tells the timeline to look for `Shot_01` (lowercase), they won't match! 
- *Tip:* Always double-check your metadata for typos or case-sensitivity issues.

---

## 2. Why use IFFFS for Timelines?

Even with these rules, using IFFFS is the fastest way to build complex edits from the outside. Once you ensure your tape names are consistent and your organizational structure is clean, conforms happen instantly across the network.

---

## 3. Key Takeaway for Beginners

If your media is offline after a Wiretap conform, check your **Organization** first. Make sure your source clips and your new timeline are "Neighbors" in the same reel, and that their **Tape Names** match exactly, character for character.
