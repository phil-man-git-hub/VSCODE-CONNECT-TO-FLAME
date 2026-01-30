# Insight: Setting up for C++ Developers

This document explains the technical "Ingredients" you need to build a high-performance Wiretap program in C++.

**Target Audience:** Novice developers interested in low-level systems programming.

---

## 1. The Ingredients (Headers and Libraries)

To bake a C++ program, you need two things from the SDK:
1.  **Headers (`.h` files):** These are in the `api/` folder. They tell your code which functions are available.
2.  **Libraries (`.a` or `.dylib` files):** These are in the `lib/` folder. They are the "Engine" that does the work.

---

## 2. Compiling your Code

Compiling is the process of turning your human-readable code into a program the computer can run.

### On Linux (Using GCC):
You must link your code against the Wiretap library and standard network tools:
`g++ my_code.C -o my_app -I ../api ../lib/libwiretapClientAPI.a -lpthread`

### On macOS (Using Clang):
It's very similar, but you also need to include Apple's "Carbon" and "SystemConfiguration" frameworks so Wiretap can talk to the Mac's network settings.

---

## 3. Why use C++?

C++ is the fastest way to talk to Flame. If your tool needs to move thousands of 4K frames every minute, C++ will give you much better performance than Python.

---

## 4. Key Takeaway for Beginners

C++ development is like **"Custom Engine Building."** It's more complex than Python, and you have to manually "Wire up" the headers and libraries during compilation. But once it's built, you have the most powerful and efficient tool possible for managing your Flame studio.
