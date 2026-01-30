# Insight: Scoping Tools to Specific Objects

This document explains the `object_scoping.py` example script. It shows how to make your Python tools "smart" so they only appear when they are actually useful.

**Target Audience:** Novice Python programmers who want to clean up their Flame menus.

---

## 1. What is Scoping?

If you write a script that "Deletes All Render Nodes," you don't want that script to show up when you right-click on a **Clip** or an **Audio Track**.

**Scoping** is the process of checking what the user has selected *before* showing the menu.

## 2. Three Common Scoping Patterns

The script shows three ways to filter your selection:

### A. Background Scoping (Nothing Selected)
Use this for tools that create new things from scratch, like "Import Media" or "Create New Reel."
```python
def scope_background(selection):
    return len(selection) == 0 # True only if the background was clicked
```

### B. Object Type Scoping (Is it a Node?)
Use this if your script only works on specific types of Flame objects.
```python
def scope_object(selection):
    for item in selection:
        if isinstance(item, flame.PyNode): # Is this a Batch Node?
            return True
    return False
```

### C. Specific Node Scoping (Is it a 'Comp' Node?)
This is the most precise. It checks the specific *kind* of node.
```python
def scope_node(selection):
    for item in selection:
        if isinstance(item, flame.PyNode) and item.type == "Comp":
            return True
    return False
```

---

## 3. How to use it in your Menu

Once you've written your scoping function, you simply plug it into your menu definition using the `isVisible` or `isEnabled` key:

```python
{
    "name": "My Smart Tool",
    "isVisible": scope_node, # Flame runs this function automatically!
    "execute": my_main_function
}
```

## 4. Why is this useful?

- **Prevent Errors:** Users can't run a "Batch" script on a "Timeline" segment by mistake.
- **Cleaner UI:** Your right-click menu stays short and relevant to what you are doing.
- **Professionalism:** This is how built-in Flame tools work.

---

## 5. Key Takeaway for Beginners

Think of scoping as an **"If Statement"** for your menu. Before you write the logic for what your tool *does*, first decide exactly *where* it belongs!
