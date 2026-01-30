# Insight: The Channel Manager (<tracks>)

This document explains the `<tracks>` tag (with an 's'). It is the part of the Open Clip that organizes all the different "Layers" or "Channels" of your media.

**Target Audience:** Novice programmers interested in multi-layer media organization.

---

## 1. What is the `<tracks>` tag?

Think of `<tracks>` as the **Backbone** of the clip. It is a container that holds all the individual `<track>` tags (the specific video, audio, or metadata channels).

---

## 2. Global Track Management

While each individual track has its own settings, the `<tracks>` tag allows you to see the "Big Picture" of what the clip is made of.
- Does it have 1 video and 2 audio channels?
- Does it have 50 layers from a complex 3D render?
All of those will be listed neatly inside this one tag.

---

## 3. Why is this useful?

It allows for **Multi-Channel Workflows**. 
By grouping everything inside `<tracks>`, you ensure that Flame sees all the components of a shot together. For example, if you have a "Beauty" layer, a "Depth" layer, and an "Ambient Occlusion" layer, they all live inside the `<tracks>` container, perfectly synced and ready for compositing.

---

## 4. Key Takeaway for Beginners

The `<tracks>` tag is the **"Master List"** of every channel in your clip. It provides the high-level structure that allows Flame to understand that several different media streams are actually parts of the same single object.
