# Insight: Server Group Metadata

This document explains how to organize your computers into teams (Groups) and how to manage those groups using Wiretap.

**Target Audience:** Novice system administrators and pipeline developers.

---

## 1. What is a Server Group?

A **Server Group** is a collection of computers that you can target as a single unit. Instead of sending a job to one specific machine, you send it to "The Team."

- *Example:* You might create a group called "GPU_FARM" for jobs that need high-end graphics cards.

---

## 2. Reading the Group Info

Every group has an `info` stream that tells you:
- **`name`**: The name of the team (e.g., "Daily_Render_Nodes").
- **`servers`**: A list of every computer currently in that team.
- **`editable`**: Tells you if you have permission to change who is in the team.

---

## 3. Why is this useful?

- **Prioritization:** You can reserve your fastest machines for "Rush" jobs by putting them in a special group.
- **Organization:** You can separate machines by OS (e.g., "Linux_Nodes" vs. "Windows_Nodes").
- **Automation:** Your pipeline script can look at a job's requirements and automatically pick the best Server Group to handle it.

---

## 4. Key Takeaway for Beginners

Server Groups are the **"Teams"** of your render farm. By grouping your computers, you make it much easier to manage a large studio. Instead of managing 100 individual computers, you just manage 5 specialized groups.
