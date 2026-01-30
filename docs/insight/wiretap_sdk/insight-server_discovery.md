# Insight: Discovering Wiretap Servers

This document explains the "Three IDs" Wiretap uses to find and remember machines on your network.

**Target Audience:** Novice technical artists interested in network persistence.

---

## 1. The Server ID (The "Nickname")

The Server ID is what you use to connect for the first time.
- **Formula:** `Hostname : ServerType` (e.g., `Workstation01:IFFFS`).
- **Flexible:** You can use the computer's name OR its IP address (e.g., `192.168.1.50:IFFFS`).

---

## 2. The Host UUID (The "Social Security Number")

A computer's name might change (e.g., if it moves to a different office), but its **Host UUID** never changes.
- **Why use it?** If you have a script that needs to find the *exact same* computer every day, use the UUID. It identifies the hardware, not the network name.

---

## 3. The Storage ID (The "Briefcase ID")

A Storage ID identifies the **Hard Drive Array** connected to a server.
- **Persistence:** If a studio moves a hard drive from "Computer A" to "Computer B," the Storage ID stays the same. 
- **The Rule:** Professional tools always remember the **Storage ID**. That way, if the network changes, the script can just scan the network and say: *"Who is holding the briefcase with ID #1234?"* and find the data instantly.

---

## 4. Key Takeaway for Beginners

To connect to a server today, use the **Server ID**. To make your script work tomorrow (even if the computer is renamed), ask the server for its **Storage ID** and save that ID in your database.
