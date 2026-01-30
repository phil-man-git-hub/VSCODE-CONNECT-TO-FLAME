# Insight: Protecting Your Projects with Hooks

This document explains the `project_protection.py` example script. It shows how to create "Safety Locks" that prevent people from accidentally editing or deleting important Flame projects.

**Target Audience:** Novice Python programmers interested in system administration and data safety.

---

## 1. What is Project Protection?

In a busy studio, you might have a project named "Final_Master_Render". You don't want a junior artist or a tired editor to accidentally delete it or change its settings.

**The Solution:** A script that automatically blocks certain actions if the project name matches a "Restricted" list.

## 2. The "Abort" Mechanism

Flame has hooks that run *before* a project is edited, deleted, or converted:
- `project_pre_edition`
- `project_pre_delete`
- `project_pre_conversion`

These hooks are special because they allow you to **Cancel** the action before it happens.

## 3. How the Script Works

The script defines a list of "Danger" names:
```python
restricted_project_names = ["final", "final_final"]
```

Then, it creates a `check` function that looks at the current project:
```python
def check(info):
    # If the name is in our list, set 'abort' to True
    info["abort"] = info["project_name"] in restricted_project_names
    
    # Give the user a reason why it failed
    info["abort_message"] = "This project is flagged as restricted."
```

When `info["abort"]` is set to `True`, Flame stops whatever it was doing and pops up a message box with your `abort_message`.

---

## 4. Why is this useful?

- **Zero Accidents:** It's impossible to delete a "protected" project while this script is active.
- **Workflow Control:** You can ensure that only specific projects (like those following a naming convention) can be modified.
- **Peace of Mind:** You don't have to rely on "Common Sense" when you have a script enforcing the rules!

---

## 5. Key Takeaway for Beginners

Hooks with an `abort` option are like **Security Guards**. They stand at the door and check IDs before letting anyone change your important data. 
