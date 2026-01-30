# Insight: Traversing and Modifying Nodes

This document explains how to "Walk" through Flame's database and change things using the Wiretap SDK.

**Target Audience:** Novice programmers learning about object manipulation and navigation.

---

## 1. The Node Handle (`WireTapNodeHandle`)

In Wiretap, you don't "touch" a clip directly. Instead, you use a **Handle**. 
- Think of a Handle like a **Remote Control**. You point it at a node (like a clip or project) and press buttons to "Rename," "Delete," or "Copy" it.

**Important Rule:** Handles are not "Live." If an artist in Flame renames a clip while your script is running, your handle won't know unless you specifically ask it to refresh.

---

## 2. Navigating the Tree

To find a specific clip, you use these basic commands:
- **`wiretap_get_root_node`**: Start at the very top (The Trunk).
- **`wiretap_get_children`**: See everything "inside" the current node.
- **`wiretap_get_parent_node`**: Move back up one level.

---

## 3. Creating and Deleting

- **`createNode`**: Use this to build new Projects or Libraries.
- **`createClipNode`**: A special command just for making clips.
- **`destroyNode`**: The "Delete" button. Be careful—this is permanent!

---

## 4. Metadata: Reading the "Tag"

Every node has a **Metadata Stream**. This is usually an XML file that describes the node.
- **`getMetaData`**: Read the info (e.g., "What is the frame rate of this clip?").
- **`setMetaData`**: Write new info (e.g., "Change the description of this project").

---

## 5. Key Takeaway for Beginners

Think of traversing like using **Finder** or **Windows Explorer**, but with code. You "Open folders" (Nodes) and "Read files" (Metadata) until you find exactly what you are looking for. Once you have the right **Node ID**, you can use your Handle to modify it.
