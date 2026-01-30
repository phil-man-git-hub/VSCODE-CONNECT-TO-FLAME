# Insight: Listing Backburner Jobs

This document explains how to get a simple list of everything currently happening on your render farm.

**Target Audience:** Novice programmers interested in simple network queries.

---

## 1. Where do the jobs live?

In the Backburner node hierarchy, all jobs are stored in a branch called **`/jobs`**. 

To see what's happening, you don't need to look at every machine; you just ask the **Manager** to show you the contents of that folder.

---

## 2. Using the Command Line

The easiest way to see the list is using the `wiretap_get_children` tool in your terminal:

`wiretap_get_children -h localhost:Backburner -n /jobs`

- **`-h`**: The machine running the Backburner Manager.
- **`-n`**: The folder you want to look at (`/jobs`).

---

## 3. What you get back

The command will return a list of **Node IDs**. Each ID represents one job. You can then use those IDs to ask for more specific info (like the name or status) using the metadata commands.

---

## 4. Why is this useful?

Listing jobs is the first step for any automated tool. 
- You might write a script that counts how many jobs are currently "Waiting."
- You could create a tool that automatically deletes all "Completed" jobs every Friday.

---

## 5. Key Takeaway for Beginners

Listing is the **"Discovery"** phase. Before you can monitor or control a job, you first have to find its ID. The `/jobs` folder is the central catalog where every task in the studio is recorded.
