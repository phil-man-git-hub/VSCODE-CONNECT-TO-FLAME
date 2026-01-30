# Insight: Programming Typical Workflows

This document provides an overview of the "Job Roles" the Wiretap SDK can perform in your studio.

**Target Audience:** Novice programmers and pipeline technical directors.

---

## 1. What can you automate?

The Wiretap SDK isn't just for reading data; it's for **Taking Action**. The typical workflows are divided into three main categories:

### A. Managing Projects
Automatically create new projects, set their resolution and frame rate, and prepare the workspace for the artist.

### B. Managing Containers
Organize your project by creating Libraries, Folders, and Reels. You can build a script that sets up a standardized folder structure for every new job.

### C. Managing Clips
The most common task. Use the API to:
- Soft-import media from a server.
- Rename or delete old versions.
- Build timelines automatically from an EDL.

---

## 2. Choosing your Server

The workflow you choose depends on which "Librarian" you talk to:
- Talk to **IFFFS** to manage Flame's internal database.
- Talk to **Gateway** to browse and ingest files from your hard drives.
- Talk to **Backburner** to handle the rendering of your work.

---

## 3. Key Takeaway for Beginners

Think of typical workflows as **"Tool Templates."** Whether you want to build a "Project Creator" or a "Media Browser," the SDK documentation provides the logical steps and sample code to get you started.
