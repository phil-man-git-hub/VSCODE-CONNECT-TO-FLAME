# Insight: Roles of the Wiretap Server and Client

This document explains how the "Brain" (Client) and the "Library" (Server) work together in the Wiretap system.

**Target Audience:** Novice programmers interested in software architecture.

---

## 1. The Division of Labor

Wiretap uses a "Client-Server" model. This means the work is split into two distinct roles to keep everything running fast.

### A. The Wiretap Server (The Librarian)
The server's only job is to **expose data**. It sits on the machine where the media is stored and waits for questions.
- It doesn't do heavy work like rendering or converting files.
- It provides a "Uniform View" of the data so the client doesn't need to know if it's talking to a database or a hard drive.
- *Goal:* Stay responsive and lightweight.

### B. The Wiretap Client (The Artist/Researcher)
The client is the program you write (like a Python script). It does the **heavy lifting**.
- If a file needs to be converted from one format to another, the client does it.
- If a frame needs to be rendered, the client does it.
- *Goal:* Process the data without slowing down the server.

---

## 2. Why this matters

By making the Client do all the work, Autodesk ensures that the **Flame Workstation** (the server) never slows down just because a background script is asking for information. The artist stays happy, and the pipeline stays fast.

---

## 3. Key Takeaway for Beginners

In Wiretap, the **Server** is the "Source of Truth" and the **Client** is the "Engine of Action." When you write a script, remember that you are the Client—you are responsible for downloading the data and doing something useful with it!
