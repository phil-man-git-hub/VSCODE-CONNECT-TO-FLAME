# Insight: Getting Started with Wiretap

This document explains the first steps to using the **Wiretap SDK** and the three different ways you can interact with it.

**Target Audience:** Novice programmers and technical artists looking for the best "Entry Point."

---

## 1. Prerequisites

Before you can write code, you need to download and install the **Wiretap Client SDK** from Autodesk. This puts the necessary "Tools" and "Libraries" on your computer so your scripts can talk to Flame.

---

## 2. Three Ways to Play

Autodesk provides three ways to use the API, depending on your skill level and needs:

### A. Command Line Tools (For Everyone)
These are pre-written programs you can run in your terminal. They allow you to "See" the API in action without writing a single line of code.
- *Best for:* Quick tests, finding Node IDs, and seeing if your network is connected.

### B. Python Modules (For Rapid Scripting)
Python is the most common way to use Wiretap. You don't have to compile your code, and you can see results instantly.
- *Best for:* Automation, studio pipelines, and small utility tools.

### C. C++ Classes (For Developers)
This is for high-performance, professional application building. It is more complex but offers the most speed and control.
- *Best for:* Building standalone apps that need to move massive amounts of video data very quickly.

---

## 3. Key Takeaway for Beginners

Start with the **Command Line Tools**! 
Run a command like `wiretap_get_node_info` just to see how the computer responds. Once you understand how the system "looks," moving to **Python** will be much easier because you'll already know what data to expect.
