# Insight: Managing Containers

This document explains how to use "Folders" (Containers) to keep your Flame projects organized using the API.

**Target Audience:** Novice programmers interested in project management and organization.

---

## 1. What are Containers?

In Flame, you don't just dump all your clips in one big pile. You organize them using specialized containers:

- **`WORKSPACE`**: A private area for an artist.
- **`DESKTOP`**: The "Current Work" area.
- **`LIBRARY`**: A permanent folder for storing clips.
- **`REEL`**: A smaller group inside a library.
- **`BATCH`**: A special container for complex compositing trees.

---

## 2. Navigating and Creating

Building a studio standard is easy with the API. You can write a script that says:
1.  **`createNode`**: Build a new Library called "Renders_V01."
2.  **`wiretap_print_tree`**: Check to make sure it was built in the right place.
3.  **`can_create_node`**: Ask if it is legal to put a Reel inside this Folder (The API will tell you "Yes" or "No").

---

## 3. The "Exclusive Access" Rule

To keep data safe, Wiretap needs **Exclusive Access** to change a container.
- If an artist has a Library open in Flame and is currently editing it, your script will fail if it tries to rename that Library.
- *Tip:* Always check if the node is "In Use" before trying to change its structure.

---

## 4. Why use Containers?

Standardization is key to a professional studio. By using the API to manage containers, you can ensure that every artist in the building has the exact same "Daily" and "Archive" folders, making it much easier for people to share work.

---

## 5. Key Takeaway for Beginners

Containers are the **"Infrastructure"** of your project. They don't hold video data directly; they hold the organization that makes the video data easy to find. Use `createNode` to build your studio's standardized roadmap!
