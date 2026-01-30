# Insight: Talking to the User (Console vs. Dialogs)

This document explains the `show_messages.py` example script. It shows how your Python script can "talk" back to the person using Flame, either quietly in the corner or with a pop-up window.

**Target Audience:** Novice Python programmers interested in User Experience (UX).

---

## 1. Two Ways to Communicate

When your script runs, it often needs to tell the user something. Flame provides two main channels for this:

### A. The Console / Message Bar (`show_in_console`)
This is the small text bar at the bottom of the Flame screen. Use this for non-critical info that doesn't need to stop the user's flow.
- **Example:** A countdown or a status update.
- **Code:**
  ```python
  flame.messages.show_in_console("Processing clip...", "info", duration=5)
  ```
- **Types:** You can use `"info"`, `"warning"`, or `"error"` to change the color/priority.

### B. The Dialog Box (`show_in_dialog`)
This is a "modal" pop-up. It stops everything and waits for the user to click a button. Use this for critical errors or when you need the user to make a choice.
- **Example:** Telling the user they forgot to select a clip.
- **Code:**
  ```python
  flame.messages.show_in_dialog(
      title="Error",
      message="Please select a clip first!",
      type="error",
      buttons=["OK"]
  )
  ```

---

## 2. Practical Examples in the Script

### The Countdown
The `countdown` function shows how you can update the console in real-time. It uses `time.sleep(1)` to wait one second between numbers.

### The Disk Space Checker
The `freespace` function uses a standard Python tool (`shutil`) to check your hard drive. 
- If you have plenty of space, it shows an **Info** message (usually green/white).
- If space is low, it shows a **Warning** message (usually yellow/orange).

### The Error Catcher
The `set_batch_duration` function tries to set the length of a Batch group. If it fails (because there's no clip), it uses a **Dialog Box** to explain exactly what went wrong.

---

## 3. Key Takeaway for Beginners

- Use the **Console** for "FYI" messages (Status updates, progress).
- Use **Dialogs** for "STOP" messages (Errors, confirmations, questions).

Always try to give the user helpful information. A script that fails silently is frustrating; a script that says "No Clip Found" is helpful!
