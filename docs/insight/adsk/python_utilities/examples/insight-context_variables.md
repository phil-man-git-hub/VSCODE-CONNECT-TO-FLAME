# Insight: Automating OCIO Context Variables in Flame

This document explains the `context_variables.py` example script. It is designed to help you understand how to automate **OpenColorIO (OCIO) Context Variables** using the Autodesk Flame Python API.

**Target Audience:** Novice Python programmers getting started with Flame automation.

---

## 1. What is the Goal?

In modern color pipelines, we often use **OCIO** (OpenColorIO) to manage color spaces. A powerful feature of OCIO is **Context Variables**.

Imagine you have a specific Color Correction file (`.cc` or `.lut`) for *every single shot* in your movie. Instead of manually loading `shot_010.cc` for Shot 010 and `shot_020.cc` for Shot 020, you can tell Flame:

> "Look for a file named `${SHOT}.cc`."

Then, you just need to tell Flame what `${SHOT}` equals for each clip.

**This script automates that second part.** It takes the **Shot Name** of your clip (e.g., "sh010") and automatically plugs it into the `SHOT` Context Variable in the Color Management settings.

---

## 2. Key Functions Breakdown

The script provides two main ways to do this: one for the **Timeline** and one for **Batch**.

### A. Timeline Workflow: `add_cmfx_with_shot_based_cc`

This function adds a **Source Colour Management** Timeline FX to your segments.

1.  **Selection Handling:**
    First, it looks at what you selected.
    -   If you selected **Segments**, it uses them directly.
    -   If you selected **Sequences**, it finds all the segments inside them.

2.  **Safety Check:**
    It checks if you already have a Color Management effect.
    -   If yes, it pops up a dialog box asking: *"Do you want to overwrite the existing effect?"*
    -   This is great practice! It prevents your script from accidentally destroying previous work.

3.  **The "Magic" Loop:**
    It goes through each segment one by one:
    ```python
    # 1. Get the Shot Name
    shot_name = segment.shot_name.get_value()

    # 2. Create the Effect
    clmgt = segment.create_effect("Source Colour Mgmt")

    # 3. Configure the Effect
    clmgt.mode = "View Transform"
    clmgt.view = "Shot Based CC" # This view expects a variable!

    # 4. Set the Variable
    clmgt.set_context_variable("SHOT", shot_name)
    ```
    **Result:** The effect is created, and the `${SHOT}` variable is now equal to "sh010" (or whatever your shot is named).

### B. Batch Workflow: `add_cmnode_with_shot_based_cc`

This function works in the **Batch** schematic (Flame's node-based compositor).

1.  **Selection Handling:**
    It looks for **Clip Nodes** in your selection or inside selected Batch Groups.

2.  **Node Creation:**
    For every clip:
    -   It creates a new **Colour Mgmt** node.
    -   It connects it to the Clip node automatically.
    -   *Tip:* `batch.connect_nodes(clip_node, "Default", clmgt, "Default")` is how you wire things together with code.

3.  **Setting the Variable:**
    Just like the timeline version, it takes the `shot_name` from the clip and feeds it into `clmgt.set_context_variable("SHOT", shot_name)`.

---

## 3. How does it appear in Flame?

The functions at the bottom (`get_timeline_custom_ui_actions`, etc.) tell Flame where to put this script in the menu.

-   **Context:** You will see a new menu item **"Examples / Context Variables"** when you right-click on the Timeline, in Batch, or in the Media Panel.
-   **Visibility:** The `isVisible` filters ensure you only see the "Batch" command when you are actually in Batch, and the "Timeline" command when you are on the Timeline. This keeps the menus clean.

## 4. Why is this useful?

Without this script, you would have to:
1.  Add a Color Mgmt node.
2.  Open it.
3.  Type the shot name into the Context Variable tab.
4.  Repeat 100 times for 100 shots.

**With this script, you click one button, and it's done for all 100 shots instantly.**

## 5. Next Steps for You

Try modifying the script!
-   **Challenge:** Can you change it to use a different variable name, like `SEQUENCE` instead of `SHOT`?
-   **Hint:** Look for the line `clmgt.set_context_variable("SHOT", shot_name)` and change `"SHOT"` to `"SEQUENCE"`.
