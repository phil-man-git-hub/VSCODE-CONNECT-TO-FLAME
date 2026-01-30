# Insight: Using Sample Programs

This document explains how to use the "Ready-Made" examples inside the SDK to learn the Wiretap language faster.

**Target Audience:** Novice programmers looking for code templates.

---

## 1. The SDK "Cheat Sheet"

The SDK comes with a folder called **`samples/`**. These are small, focused scripts written by Autodesk engineers. They are the best way to see the "Best Practices" for using the API.

---

## 2. Two Recommended First Samples

### A. `listAllServers`
This sample does exactly what it says: it scans your network and prints a list of every workstation.
- **What you'll learn:** How to initialize the API and how to use the "Multicast" discovery system.

### B. `listChildren`
This sample lets you "Drill Down" into a project. You give it a starting point (like a Project name), and it lists everything inside.
- **What you'll learn:** How to navigate the tree-like structure of a Flame workstation.

---

## 3. How to use them

Don't just run them! **Read them.** 
- Open the `.py` or `.C` files in a text editor. 
- Look for the `WireTapClientInit()` function (The "Start" button) and the `WireTapClientUninit()` function (The "Stop" button).
- You can literally "Cut and Paste" these blocks of code into your own project.

---

## 4. Key Takeaway for Beginners

The sample programs are your **"Building Blocks."** You don't need to invent everything from scratch. If you want to build a tool that renames clips, find the sample that lists clips, copy that code, and then add your renaming logic on top of it.
