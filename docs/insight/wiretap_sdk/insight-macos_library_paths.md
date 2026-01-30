# Insight: Build Issues on macOS

This document explains a specific technical hurdle you might face when writing Wiretap tools on a Mac: managing dynamic library paths.

**Target Audience:** Novice developers using macOS for studio automation.

---

## 1. The macOS "Hardcoded Path" Rule

On most computers (Linux/Windows), when you write a program, it looks for its "Engine" files (Libraries) in a standard list of folders. 

On **macOS**, libraries (`.dylib` files) often have their exact "Home Address" baked right into them. By default, the Wiretap library expects to live in `/Library/Frameworks`.

---

## 2. The Problem

If you install the Wiretap SDK in a different folder (like your desktop or a custom project folder), your program will crash because it's still looking for the library in the "Standard" location.

---

## 3. Two Ways to Fix It

### A. The "Shortcut" (Environment Variable)
You can tell your computer to look in a different place just for this session by setting the `DYLD_LIBRARY_PATH`. This is like giving the computer a temporary set of directions.

### B. The "Surgery" (`install_name_tool`)
You can use a built-in Mac tool to "Rewrite" the library's address permanently. 
- **Command:** `install_name_tool -id /New/Path/libwiretap.dylib`
- **Verification:** You can use the `otool -L` command to confirm the change. It's like checking the ID card of the library to make sure it has the new address.

---

## 4. Key Takeaway for Beginners

If your Mac script won't run and says "Library not found," it's probably because of this hardcoded path rule. Before you give up, try using `install_name_tool` to tell the library exactly where it is currently living on your hard drive.
