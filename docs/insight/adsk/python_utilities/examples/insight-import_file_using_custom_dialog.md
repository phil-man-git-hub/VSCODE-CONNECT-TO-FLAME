# Insight: Custom File Browsers in Flame

This document explains the `import_file_using_custom_dialog.py` example script. It shows two different ways to let a user pick files from their computer using Python.

**Target Audience:** Novice Python programmers interested in User Interface (UI) design.

---

## 1. Why Not Just Hardcode Paths?

If you write a script that always imports `C:\Media\shot.mov`, it only works once. To make a tool useful, you need to let the user **browse** and **select** the files they want.

## 2. Two Different Approaches

This script shows two ways to do this:

### A. The "Standard Computer" Way (Qt / PySide6)
This uses **PySide6**, which is the industry-standard way to make windows and buttons in Python.
- **Pros:** It looks like a normal Windows or Mac folder window. It's familiar to everyone.
- **How it works:**
  ```python
  from PySide6 import QtWidgets
  dlg = QtWidgets.QFileDialog() # Create a window
  if dlg.exec(): # Show the window and wait for the user to click OK
      files = dlg.selectedFiles() # Get the list of chosen files
  ```

### B. The "Flame Native" Way (`flame.browser`)
Flame has its own built-in file browser.
- **Pros:** It looks exactly like Flame. It understands Flame-specific things like "Clips" and "Frame Sequences."
- **How it works:**
  ```python
  import flame
  flame.browser.show(title="Select Clips", multi_selection=True)
  # The user's choice is saved in flame.browser.selection
  flame.batch.import_clips(flame.browser.selection, ...)
  ```

---

## 3. Scoping: Making the Menu Context-Aware

The script uses a clever trick to make sure the "Import" buttons only appear when you right-click on the **background** of the Batch schematic:

```python
def scope_background(selection):
    return len(selection) == 0 # Only True if NOTHING is selected
```

If you right-click on a clip node, this menu won't show up. This prevents clutter and ensures you don't try to "import into a clip."

---

## 4. Key Takeaway for Beginners

- Use `PySide6` if you want a standard OS feeling or need special filters (like "only show .jpg").
- Use `flame.browser` if you want your tool to feel like a native part of the Flame experience.
- Both ways ultimately give you a **Path** (a string of text like `/Users/pman/Desktop/video.mov`) which you then pass to Flame's `import_clip()` command.
