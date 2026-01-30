# Insight: Customizing Project Conversion in Flame

This document explains the `conversion_description.py` example script. It is a simple but powerful example of using **Hooks** to automate tasks when upgrading projects in Autodesk Flame.

**Target Audience:** Novice Python programmers interested in project management automation.

---

## 1. What is the Goal?

When you upgrade Autodesk Flame to a new major version (e.g., from 2025 to 2026), your existing projects often need to be "converted" to work with the new software.

Normally, this just happens. But what if you want to leave a "paper trail" or tag these projects so you know they have been changed?

**This script automates that tagging.**
- It automatically adds " (Converted)" to the end of the project's name.
- It changes the project's description to say exactly *when* the conversion happened.

---

## 2. Key Concepts

### A. The "Hook"
The core of this script is a special function name: `project_init_conversion`.
Flame looks for this specific function name. If it finds it in a loaded script, it runs it right before the conversion process starts.

### B. The `info` Dictionary
When Flame runs this function, it passes a variable called `info` to it.
Think of `info` as a container (a Python dictionary) that holds the project's ID card:
- `info["project_name"]`: The name of the project.
- `info["project_description"]`: The description text you see in the startup screen.

By changing the data inside this container, you change what Flame writes to the database.

---

## 3. Code Breakdown

Let's look at the code line by line:

```python
import datetime

def project_init_conversion(info):
    # 1. Modify the Name
    info["project_name"] = info["project_name"] + " (Converted)"

    # 2. Modify the Description
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info["project_description"] = "Converted on {0}".format(timestamp)
```

1.  **`import datetime`**: This imports a standard Python tool for working with dates and times.
2.  **`info["project_name"] = ...`**: It takes the current name (e.g., "MyCommercial") and adds text to it. The new name becomes "MyCommercial (Converted)".
3.  **`info["project_description"] = ...`**:
    - `datetime.datetime.now()` gets the current moment.
    - `.strftime(...)` formats it into a readable string like "2026-01-29 14:30:00".
    - It overwrites the old description with this new timestamp.

---

## 4. Why is this useful?

This is a perfect example of **Workflow Safety**.
- **Organization:** You can instantly tell which projects have been migrated just by looking at the list.
- **Audit Trail:** You know exactly when the migration happened.
- **Automation:** You don't have to remember to type this in manually for every single project.

## 5. Next Steps for You

Try customizing it!
- **Challenge:** Instead of overwriting the description, can you *append* the date to the existing description so you don't lose the original text?
- **Hint:**
  ```python
  # Try this instead:
  info["project_description"] = info["project_description"] + " | Converted on: " + timestamp
  ```
