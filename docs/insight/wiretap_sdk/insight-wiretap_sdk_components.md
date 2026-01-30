# Insight: Components of the SDK

This document explains what you get inside the **Wiretap SDK** package and where to find the tools you need to start programming.

**Target Audience:** Novice developers interested in software installation and file structure.

---

## 1. What's in the Box?

The SDK is organized into five main folders:

- **`api/`**: The "Instruction Manual" for the compiler. It contains the C++ header files (`.h`) that your code needs to "include."
- **`doc/`**: The technical reference guide (HTML). This is where you look up specific function names and parameters.
- **`lib/`**: The "Engines." These are the actual libraries (`.a` or `.so`) that do the work of connecting to the servers.
- **`samples/`**: The "Cheat Sheets." This folder contains example programs written by Autodesk engineers. 
- **`tools/`**: The "Power Tools." These are pre-made command-line programs like `wiretap_ping` or `wiretap_get_metadata` that you can use for testing.

---

## 2. A Warning about Tools

Autodesk includes the **`tools/`** folder for testing and troubleshooting. 
- **The Rule:** Don't build your studio's mission-critical automation around these tools! 
- **Why?** Autodesk might change how the tools work in the future. If you want to build something permanent, you should write your own script using the **Python** or **C++** API directly.

---

## 3. Key Takeaway for Beginners

The SDK folder is your **"Laboratory."** Start by looking at the **`samples/`** to see how professionals write Wiretap code, and use the **`tools/`** to double-check that your network is working before you start writing your own complex scripts.
