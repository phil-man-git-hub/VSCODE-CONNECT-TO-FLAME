# Insight: Workflow, Samples and Tools

This document acts as a "Master Map" to help you find the right example code for common studio tasks.

**Target Audience:** Novice developers looking for a "Quick Start" guide.

---

## 1. Finding the Right Sample

If you have a task in mind, look at this list to see which file in the `samples/` folder you should study first:

- **"List every machine in the building"**: Study `listAllServers.py`.
- **"Explore a project tree"**: Study `listChildren.py`.
- **"Rename or Copy a clip"**: Study `duplicateNode.py`.
- **"Send a job to the render farm"**: Study `submitJob.C` (or the Python equivalent).

---

## 2. Comparing with Command Line Tools

If you aren't sure if your script is working correctly, you can compare its results with the professional tools Autodesk included in the SDK:

| Your Task | The Python Sample | The "Official" Tool |
| --- | --- | --- |
| Scanning Network | `listAllServers.py` | `wiretap_server_dump` |
| Browsing Nodes | `listChildren.py` | `wiretap_get_children` |
| Reading Metadata | `dir(wiretap)` | `wiretap_get_metadata` |

---

## 3. Why is this useful?

This map saves you from "Re-inventing the wheel." 
- **Step 1:** Run the "Official" tool to see what the data should look like.
- **Step 2:** Open the matching Python sample to see how the code was written.
- **Step 3:** Copy that code and change it to fit your studio's needs.

---

## 4. Key Takeaway for Beginners

The samples and tools are **"Interactive Documentation."** Instead of just reading about how to do something, you can run the sample and see it happen in real-time. This is the fastest way to master the Wiretap SDK!
