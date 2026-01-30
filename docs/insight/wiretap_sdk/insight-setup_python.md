# Insight: Setting up for Python Developers

This document explains the easiest way to start writing scripts for Flame using the Python language.

**Target Audience:** Novice programmers interested in rapid automation.

---

## 1. The Easiest Way: Use Flame's Python

You don't need to install Python yourself! Every Flame workstation already has a professional Python environment installed.
- **Location:** `/opt/Autodesk/python/<version>/bin/python`
- **Why use it?** It already has the Wiretap libraries pre-installed and ready to go. You can just start writing code!

---

## 2. Using External Python

If you want to use your own version of Python (like Python 3.11), you can do that too. 
- You just need to "Link" the Wiretap library by copying the `libwiretapPythonClientAPI.so` file from the SDK into your Python's `site-packages` folder.

---

## 3. How to get Help (The Python Way)

The SDK doesn't include a separate manual for Python. Instead, you can ask Python to "Explain" itself:

1.  Open Python in your terminal.
2.  Import the library: `import libwiretapPythonClientAPI as wiretap`
3.  Ask for a list of classes: `dir(wiretap)`
4.  Ask for instructions on a specific tool: `help(wiretap.WireTapNodeHandle)`

---

## 4. Key Takeaway for Beginners

Python is the **"Speed Demon"** of development. You don't have to compile your code, and you can get immediate answers using the `help()` command. If you want to build a tool quickly, always start with Python!
