# Insight: Using Command Line Tools

This document explains how to use the pre-built programs included in the SDK to test your network and "See" inside Flame without writing any code.

**Target Audience:** Novice developers and technical artists.

---

## 1. Where are the tools?

Autodesk keeps the current version of the tools in a standard location on your computer:
`/opt/Autodesk/wiretap/tools/current/`

---

## 2. Three Essential Tools

### A. `wiretap_ping`
The "Hello, World" of Wiretap. It checks if a machine is alive and speaking the Wiretap language.
- **Command:** `wiretap_ping -h <machine_name>`

### B. `wiretap_server_dump`
The "Radar." it scans your entire network and shows you every Flame workstation, Gateway, and Backburner Manager.
- **Command:** `wiretap_server_dump`

### C. `wiretap_print_tree`
The "X-Ray." It prints out the entire organizational structure of a workstation, showing every Project, Library, and Clip.
- **Command:** `wiretap_print_tree -h <machine_name> -d 2` (The `-d 2` tells it to only go two levels deep).

---

## 3. How to get help

Every tool has a manual built right in. Just type the command followed by `--help`:
`wiretap_ping --help`

---

## 4. Why use these tools?

Before you start writing a complex script to delete old projects, use `wiretap_print_tree` to make sure you can "See" those projects first. It’s the best way to verify that your network and permissions are set up correctly.

---

## 5. Key Takeaway for Beginners

The command-line tools are your **"Sanity Check."** If you can't see a workstation with `wiretap_server_dump`, your script won't be able to see it either. Always use these tools to confirm your network is working before you spend time writing custom code.
