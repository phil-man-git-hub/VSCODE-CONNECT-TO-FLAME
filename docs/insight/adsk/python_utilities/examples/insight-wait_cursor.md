# Insight: Managing the Wait Cursor

This document explains the `wait_cursor.py` example script. It shows how to control that spinning "loading" icon so your users don't get frustrated when using your tools.

**Target Audience:** Novice Python programmers interested in User Experience (UX).

---

## 1. What is the Wait Cursor?

In Flame, when a script is running, the mouse cursor usually turns into a "Wait" icon (a spinning circle or watch). This tells the user: *"The computer is busy, please don't click anything."*

## 2. When to Hide It

Sometimes, you *want* the user to click something while your script is running!
- **Example:** You pop up a window asking the user to "Select a Folder."
- **The Problem:** If the cursor is stuck in "Wait" mode, the user can't interact with your pop-up window properly.

## 3. How to Control It

In your menu definition, you can use the `waitCursor` key:

### A. For Long Tasks (`waitCursor: True`)
If your script is doing a lot of math or moving files, keep the wait cursor on.
```python
{
    "name": "Process 1000 Clips",
    "execute": my_long_function,
    "waitCursor": True # This is the default
}
```

### B. For Interactive Tasks (`waitCursor: False`)
If your script shows a window or asks a question, turn the wait cursor off so the mouse works normally.
```python
{
    "name": "Show My Custom Window",
    "execute": show_window_function,
    "waitCursor": False # Gives control back to the user
}
```

---

## 4. Why is this useful?

- **Reduced Frustration:** There is nothing worse than a pop-up window you can't click because your mouse is "stuck" in a loading state.
- **Clarity:** It tells the user exactly when it's safe to interact with Flame and when they should wait.

---

## 5. Key Takeaway for Beginners

If your script opens a window (using `PySide6` or `flame.messages.show_in_dialog`), you should almost always set `"waitCursor": False`. If your script runs in the background with no windows, keep it `True`.
