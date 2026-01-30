# Insight: Creating Custom Right-Click Menus

This document explains the `custom_actions_hook.py` file. It is the "Master List" of where and how you can add your own buttons to the Flame interface.

**Target Audience:** Novice Python programmers who want to customize the Flame UI.

---

## 1. What are Custom Actions?

In Flame, almost every area (the Media Panel, the Timeline, the Batch Schematic) has a right-click menu. A **Custom Action** is your way of adding a new button to those menus that runs your own Python code.

---

## 2. Where can you add Menus?

The script lists many functions, each corresponding to a different "Home" in Flame:

- **`get_media_panel_custom_ui_actions`**: Right-clicking on clips or folders in the browser.
- **`get_main_menu_custom_ui_actions`**: The top Flame menu.
- **`get_timeline_custom_ui_actions`**: Right-clicking on segments in the timeline.
- **`get_batch_custom_ui_actions`**: Right-clicking in the Batch schematic.
- **`get_mediahub_files_custom_ui_actions`**: Right-clicking on files you are about to import.

---

## 3. How to Define an Action

Each action is a **Dictionary** (a list of settings). Here are the most important settings:

- **`name`**: The text that appears in the menu.
- **`execute`**: The name of the Python function to run when the user clicks the button.
- **`isVisible`**: A "Gatekeeper." If this is False, the button stays hidden. 
  - *Tip:* Use this to only show "Timeline" tools when the user is actually on the Timeline.
- **`isEnabled`**: Similar to `isVisible`, but it makes the button greyed-out (disabled) instead of hiding it.

---

## 4. Organizing with Groups

You don't just add single buttons; you add **Groups**. 
- A Group is like a folder in the menu. 
- This keeps your tools organized (e.g., all your "Export" tools inside one "My Studio / Exports" group).

---

## 5. Key Takeaway for Beginners

Think of `custom_actions_hook.py` as the **"Registry"** of your tools. It doesn't usually contain the logic of *what* the tool does; it just tells Flame *where* to put the button and *which* script to wake up when that button is pressed.
