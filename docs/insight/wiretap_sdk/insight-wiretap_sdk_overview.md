# Insight: Wiretap SDK Overview

This document provides a birds-eye view of the **Wiretap SDK**. It is the master framework for automating Autodesk Flame.

**Target Audience:** Novice programmers and studio technical directors.

---

## 1. What is the SDK for?

The Wiretap SDK allows you to write your own standalone programs that can reach inside Flame's database from the outside. 

Normally, you have to open Flame to change a project or render a clip. With the SDK, you can do all of that from a simple script, even if Flame isn't running on your machine!

---

## 2. The Three Flavors of Servers

The SDK allows you to talk to three specialized servers:

1.  **IFFFS Server:** Handles projects and clips. Use this to automatically create new jobs or organize footage into libraries.
2.  **Gateway Server:** Handles "Ingest." Use this to stream raw video from hard drives (like R3D or ProRes files) directly into your pipeline.
3.  **Backburner Server:** Handles "Rendering." Use this to submit and monitor background render jobs on the farm.

---

## 3. Platform Support

Wiretap is **Cross-Platform**. You can write a script on a **Linux** machine that reaches across the network to modify a project on a **macOS** Flame workstation.

---

## 4. Why use the SDK?

- **Workflow Automation:** Eliminate repetitive tasks like creating folders and naming projects.
- **Custom Monitoring:** Build your own custom dashboards to see which projects are taking up the most disk space.
- **Pipeline Integration:** Bridge Flame with other studio software (like ShotGrid or a custom web portal).

---

## 5. Key Takeaway for Beginners

The Wiretap SDK is the **"Master Key"** to the Autodesk Flame ecosystem. It gives you the power to manage your media and renders using code, transforming Flame from a creative tool into a fully automated production engine.
