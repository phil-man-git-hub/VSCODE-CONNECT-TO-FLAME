# Insight: Backburner Manager Metadata

This document explains the "Global Settings" for your render farm. These settings control the behavior of the entire Backburner system.

**Target Audience:** Novice technical artists and system administrators.

---

## 1. The Manager's Rulebook

The Backburner Manager has an `info` stream that acts as the "Rulebook" for all computers on the farm. By changing these tags, you change how every job is handled.

### Key Rules:
- **`retryCount`**: If a computer crashes during a render, how many times should the Manager try again? (Usually set to 3).
- **`maxConcurrentJobs`**: How many jobs are allowed to run at the exact same time across the whole farm?
- **`archiveDays`**: How long should a finished job sit in the "Recent" list before being moved to the "Old" archive?
- **`logLevel`**: How much detail should the Manager write to its diary? (Set to `debug` if you are trying to find a bug).

---

## 2. Security and Admins

The Manager also keeps a list of **`administrators`**. These are the only users allowed to cancel someone else's render or change the global rules.

- **`restrictRoot`**: A safety switch. If this is on, even the "Superuser" (Root) cannot send jobs from a remote computer.

---

## 3. Why is this useful?

By reading the Manager's metadata, your script can verify the health of the farm. 
- You can check if the **`mailServer`** is set up correctly so artists get their "Render Done" emails.
- You can automatically increase the **`retryCount`** if the network is having a bad day.

---

## 4. Key Takeaway for Beginners

The Manager Metadata is the **"Control Panel"** for the studio. It defines the "Policy" for how work gets done. Understanding these tags is the first step to managing a professional, reliable render farm.
