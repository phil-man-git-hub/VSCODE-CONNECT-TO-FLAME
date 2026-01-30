# Insight: Managing Version Compatibility

This document explains the `version_scoping_hooks.py` example script. It shows how to ensure your Python tools only appear in versions of Flame where they actually work.

**Target Audience:** Novice Python programmers sharing scripts with a team.

---

## 1. The Version Headache

Sometimes, Autodesk adds a new feature to Flame 2026 that didn't exist in 2024. If you write a script using that new feature and give it to a friend using the older version, the script might crash or cause errors.

**The Solution:** Version Scoping. You can tell Flame: *"Only show this menu item if the software version is between X and Y."*

## 2. Two Ways to Set Limits

The script shows two different places where you can set version limits:

### A. Inside the Menu Dictionary (`minimumVersion`)
This is the most common way. You add it directly to the button definition.
```python
{
    "name": "Super New Tool",
    "execute": my_function,
    "minimumVersion": "2026.1" # Only shows up in 2026.1 or newer
}
```

### B. On the Function Itself (`minimum_version`)
This is a more "global" way to block an entire set of tools. You set it after the function is defined:
```python
def get_batch_custom_ui_actions():
    ...

get_batch_custom_ui_actions.minimum_version = "2023.0"
```

## 3. How Version Numbers Work

Flame version numbers follow a specific pattern: `Year.Minor.Patch`
- **`2026`**: Works for any version of 2026.
- **`2026.1`**: Only works for 2026 Update 1 or newer.
- **`2026.1.2`**: Only works for a very specific bug-fix release.

---

## 4. Why is this useful?

- **Prevent Crashes:** You don't have to worry about old versions of Flame trying to run code they don't understand.
- **Easy Maintenance:** You can keep one "Super Script" that has different buttons for different versions of the software.
- **Professionalism:** Your tools feel reliable and well-tested across the whole studio.

---

## 5. Key Takeaway for Beginners

Think of Version Scoping as a **"System Requirement"** for your script. By setting these limits, you are protecting your users from seeing tools that won't work on their specific version of Flame.
