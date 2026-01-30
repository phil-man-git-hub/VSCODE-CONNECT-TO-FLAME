# Insight: Listing Backburner Servers

This document explains how to get a list of every computer (Render Node) currently registered with your Backburner farm.

**Target Audience:** Novice technical artists and IT support.

---

## 1. Where do the workers live?

In the Backburner node hierarchy, all computers are listed in a branch called **`/servers`**. 

---

## 2. Using the Command Line

To see every computer on your farm, use the `wiretap_get_children` tool:

`wiretap_get_children -h localhost:Backburner -n /servers`

- **`-h`**: The machine running the Backburner Manager.
- **`-n`**: The folder containing the computer list (`/servers`).

---

## 3. What you get back

The command will return a list of **Hostnames** (e.g., `RenderNode01`, `ArtistWorkstation`, `BladeServer`). You can then use these hostnames to check the health of each machine individually.

---

## 4. Why is this useful?

- **Network Audit:** Quickly see if any computers have gone missing from the farm.
- **Dynamic Targeting:** You can write a script that finds every idle machine and assigns them a high-priority task.
- **Troubleshooting:** Confirm that a new computer has successfully "Joined" the farm after installation.

---

## 5. Key Takeaway for Beginners

The `/servers` node is the **"Staff Roster"** of your studio. It tells you exactly who is available to work. By querying this list, you can keep your studio's rendering resources organized and accounted for.
