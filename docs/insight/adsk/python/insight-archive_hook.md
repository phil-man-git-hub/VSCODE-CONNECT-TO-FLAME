# Insight: Monitoring Archive Operations

This document explains the `archive_hook.py` file. It shows how Flame can notify your Python scripts about the status of backups and restores.

**Target Audience:** Novice Python programmers interested in data safety and system monitoring.

---

## 1. What is an Archive Hook?

In Flame, "Archiving" is the process of backing up your project to a server or a tape. Because archives can take a long time, you might not want to sit and watch the progress bar.

**The Solution:** Archive Hooks. These are "Event Listeners" that run automatically when an archive starts, finishes, or hits a milestone.

---

## 2. Key Events (Hooks)

The script defines several empty placeholders (functions) that Flame will fill with data:

### A. `archive_completed`
Flame runs this as soon as a backup is 100% finished.
- **Use case:** Send an email to the producer saying: *"The backup for 'Project_X' is done!"*

### B. `archive_restored`
Runs when you successfully bring a project back from an archive.
- **Use case:** Log that a project was reopened for auditing purposes.

### C. `archive_segment_completed`
Archives are often broken into smaller "segments" (files). This hook runs every time one of those small files is finished.
- **Why?** It tells you the `status`. If it's not zero, something went wrong! You can catch errors early instead of waiting for the very end.

### D. `archive_selection_updated`
Runs when you select clips to be archived. It gives you technical data like `num_frames` and `data_size` (in MB).
- **Use case:** Warn the artist if they are trying to archive more data than is available on the backup drive.

---

## 3. Why is this useful?

- **Automation:** You can trigger external scripts (like database updates) based on archive success.
- **Error Handling:** You get immediate, detailed feedback if a backup fails.
- **Reporting:** You can build a history of how much data your studio is archiving every day.

---

## 4. Key Takeaway for Beginners

Hooks are like **"Automatic Notifications"** for your code. Instead of your script constantly asking Flame *"Are you done yet?"*, Flame simply "calls" your script's function when the event happens and hands over all the relevant information (like the archive name and path).
