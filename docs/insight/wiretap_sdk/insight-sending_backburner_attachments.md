# Insight: Sending Job Attachments

This document explains how to send large files (like 3D scenes or color LUTs) along with your render job to the farm.

**Target Audience:** Novice programmers interested in data transfer and complex job submission.

---

## 1. Metadata vs. Streams

- **Metadata (`details`):** Use this for small text instructions (e.g., "Render Frame 1 to 10").
- **Streams (`pushStream`):** Use this for large or binary files (e.g., a 500MB project file or a complex texture).

---

## 2. The "Push" Workflow

If your render needs a specific file to work, you don't just tell Backburner where the file is on your computer. You **Upload** the file to the Backburner Manager.

1.  **Prepare:** Compress your file (e.g., zip it) to make the upload faster.
2.  **Push:** Use the `pushStream` command to send the file to the Manager.
3.  **Deploy:** When a worker computer (Server) starts your job, the Manager automatically hands it the attachment so it has everything it needs to render.

---

## 3. Why is this useful?

It ensures that the render farm doesn't need access to your personal computer's hard drive. By "Attaching" the files to the job, you are making the job **Self-Contained**. This is the only way to reliably render complex projects on a large, multi-machine farm.

---

## 4. Key Takeaway for Beginners

Attachments are the **"Backpack"** for your job. You fill the backpack with all the tools and maps the worker needs, then hand it to the Manager. No matter which machine in the studio does the work, they'll have the backpack ready to go.
