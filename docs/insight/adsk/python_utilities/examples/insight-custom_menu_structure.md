# Insight: Designing Complex Menus in Flame

This document explains the `custom_menu_structure.py` example script. It shows how to organize your Python scripts into clean, professional submenus within the Flame interface.

**Target Audience:** Novice Python programmers who want to improve the "Look and Feel" of their tools.

---

## 1. Organizing Your Tools

When you start writing many scripts, putting them all in one long list makes the Flame UI messy. Professional tools use **Submenus**, **Ordering**, and **Separators**.

## 2. The "Modern" Way (Flame 2023.2+)

In newer versions of Flame, the API gives you precise control over the menu layout using three key attributes:

### A. `hierarchy`
This tells Flame where to put your menu item.
- `hierarchy: []` means "put this in the main right-click menu."
- `hierarchy: ["Example / Add Nodes"]` means "put this inside the 'Add Nodes' folder."

### B. `order`
Normally, Flame lists things alphabetically. `order` lets you force a specific sequence.
- An item with `order: 1` will always appear above `order: 2`.

### C. `separator`
Use `"separator": "below"` to draw a thin line in the menu. This is great for grouping related tools together (e.g., separating "Import" tools from "Export" tools).

---

## 3. Code Example Breakdown

The script creates a main category called **"Example / Add Nodes"**. Inside that, it creates two sub-folders:

1.  **Tools:** Contains "Add Resize" and "Add Mono".
2.  **Outputs:** Contains "Add Render" and "Add Write File".

```python
{
    "name": "Tools",
    "hierarchy": ["Example / Add Nodes"], # Put inside the main folder
    "order": 1,                           # Show this folder first
    "separator": "below",                 # Put a line under this folder
    "actions": [...]                      # The actual buttons
}
```

## 4. Supporting Older Versions

The script also shows how to use `maximumVersion`.
- If a user is on an old version of Flame that doesn't support submenus, the script provides a "flat list" instead.
- **Why?** This ensures your script doesn't crash if a colleague is using an older version of the software.

---

## 5. Key Takeaway for Beginners

Good code isn't just about what it *does*; it's about how easy it is for a human to *use*. Taking five minutes to organize your menus makes your tools feel like a built-in part of Flame!
