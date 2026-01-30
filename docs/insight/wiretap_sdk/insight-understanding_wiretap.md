# Insight: Understanding Wiretap

This document explains the **Wiretap** framework in Autodesk Flame. It is the "Communication Layer" that allows different software and servers to talk to each other and share media.

**Target Audience:** Novice programmers and technical artists interested in network storage and interoperability.

---

## 1. What is Wiretap?

Wiretap is a high-performance system used to move media (video/audio) and metadata (info about clips) across a network. 

Think of it as a **"Universal Language"** for the Flame ecosystem. Whether you are using a Python script, a web browser, or another Flame workstation, Wiretap allows you to "reach into" a database and grab exactly what you need without manually copying files.

---

## 2. The Core Pillars

Wiretap is built on three main sections:

- **Wiretap Terminology:** The basic words you need to know (Servers, Clients, Nodes).
- **Server/Client Roles:** How the different parts of the system interact.
- **Self-Discovery:** How Wiretap "finds" other machines on your network automatically.

---

## 3. Why is this useful?

Without Wiretap, you would have to manually find clips on a hard drive, remember which folder they are in, and hope you don't break the database. 

**With Wiretap:**
- You can write a script that says: *"Find me the 'Final Render' in the 'Summer Commercial' project."*
- Wiretap finds it instantly, no matter which server it is stored on.
- You can stream that media directly into your script for processing.

---

## 4. Key Takeaway for Beginners

Wiretap turns your studio from a collection of "Hard Drives and Folders" into a **Unified Database**. It is the technology that makes collaborative workflows possible in a professional post-production environment.
