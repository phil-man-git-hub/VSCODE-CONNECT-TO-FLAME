# Insight: Basic Programming Issues

This document explains the fundamental "Rules of the Road" when writing code for Wiretap.

**Target Audience:** Novice programmers learning the API's syntax and behavior.

---

## 1. The "WireTap" Nameplate

Every class and function in the SDK starts with the word **`WireTap`**. 
- *Why?* This is called **Namespacing**. it ensures that if your code uses other libraries (like a standard math library), the names won't clash and cause confusion for the computer.

---

## 2. Strings and the `WireTapStr` Class

In C++, "Strings" (text) can be tricky. Wiretap uses its own simplified version of text called **`WireTapStr`**.
- **Important:** If you want to use Wiretap text in your own script, you usually have to "Copy" it into your own text variables first.

---

## 3. Error Handling (The Success Switch)

Every time you ask Wiretap to do something, it doesn't just "do it"—it tells you **True** (I did it!) or **False** (I couldn't do it).
- **Pro Tip:** Always wrap your Wiretap commands in an "If Statement."
```python
if handle.renameNode("NewName") == False:
    print(handle.lastError())
```

---

## 4. Multi-Threading (Can I do two things at once?)

Wiretap allows you to use different threads (running different parts of your script simultaneously), but there is a catch:
- **The Rule:** You can't share one "Remote Control" (Handle) between two threads. 
- **The Solution:** If you have two threads, give each one its own unique handle to the clip.

---

## 5. Key Takeaway for Beginners

The Wiretap API is built for **Stability**. It uses strict namespacing, custom text types, and a standard True/False success check to ensure that your studio's automation is reliable and doesn't crash when things get complicated.
