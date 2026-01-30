# Insight: Wiretap Error Handling & Threading

This document explains how to handle failures and how to use multiple threads safely when writing Wiretap scripts.

**Target Audience:** Novice programmers interested in robust code and performance.

---

## 1. Handling Errors (The `lastError` pattern)

In Wiretap, functions don't usually "Throw Errors" that crash your script. Instead, they return a simple **True** (Success) or **False** (Failure).

If a function returns `False`, you must immediately ask for the "Librarian's Note" to see what went wrong:
- **Command:** `handle.lastError()`
- **Rule:** Read the error message **immediately**. The next time you call *any* function, the old error message is erased!

---

## 2. Is it Thread-Safe?

Thread-safety means "Can two parts of my script talk to the same object at the same time?" 
- **The Answer:** Mostly **No**.
- **The Rule:** Each thread in your script should have its own "Remote Control" (Handle). You should never share a single `WireTapNodeHandle` between two threads, or they will get confused and crash.

---

## 3. Improving Performance

If you want to move media faster, you might think "I'll use 10 threads!" 
- **The Reality:** This usually doesn't help. Because all threads are trying to squeeze through the same network "Pipe," they just end up waiting for each other.
- **The Best Way:** Process frames one after another (Sequentially). The Wiretap server is smart—it "Reads Ahead" and prepares the next frame for you before you even ask for it.

---

## 4. Why did my script crash on exit?

Wiretap uses background threads to keep the connection alive. 
- **The Fix:** You must always call `WireTapClientUninit()` before your script finishes. This tells Wiretap to "Park the car and turn off the engine" safely.

---

## 5. Key Takeaway for Beginners

Wiretap is a "Polite" API. It won't crash your script if something goes wrong; it will just say "False." It's your job as the programmer to check that value and read the `lastError()` message to explain the problem to the user.
