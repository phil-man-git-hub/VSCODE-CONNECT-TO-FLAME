# Insight: Version Metadata (<version>)

This document explains the `<version>` tag. It is used to store information about a specific iteration of your work—like "V1" or "Final_Master."

**Target Audience:** Novice programmers interested in creative workflow metadata.

---

## 1. What is a Version?

In filmmaking, we never get it right the first time. We render "Version 1", then "Version 2," and so on. The `<version>` tag allows you to add specific **Notes** to those iterations.

---

## 2. Key Information inside a Version

- **`uid`**: The unique link (like "v1") that connects this metadata to the actual media in the tracks.
- **`<name>`**: A friendly name for the version (e.g., "Roto Version").
- **`<comment>`**: A place for instructions (e.g., "Added more blur to the edges").
- **`<creationDate>`**: When this version was rendered.

---

## 3. Why is this useful?

- **Communication:** An artist can see exactly why a new version was created by looking at the comments inside the Open Clip.
- **Audit Trail:** You can keep track of who worked on a shot and when it was finished.
- **Pipeline Logic:** You can use the `creationDate` to automatically show the most recent render to the artist.

---

## 4. Key Takeaway for Beginners

The `<version>` tag is the **"Artist's Notebook"** for a clip. While other tags focus on technical things like file paths and frame rates, the `<version>` tag is where you store the human history of the shot.
