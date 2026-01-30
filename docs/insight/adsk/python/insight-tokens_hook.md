# Insight: Creating Custom Naming Tokens

This document explains the `tokens_hook.py` file. It shows how to add your own "Magic Words" (Tokens) to Flame's naming and export windows.

**Target Audience:** Novice Python programmers interested in dynamic naming and string manipulation.

---

## 1. What are Tokens?

You've probably seen tokens in Flame like `<shot_name>` or `{width}`. When you use them, Flame automatically replaces the token with the real name or resolution of the clip.

**The Goal:** Add your own custom tokens, like `<artist_name>` or `<job_number>`, so you don't have to type them manually in every export window.

---

## 2. Two Steps to Custom Tokens

Adding a token is a two-part process:

### Step 1: Listing the Token (`get_hook_token_list`)
You first have to tell Flame that your token exists so it shows up in the "Add Token" dropdown menu.
- **Contexts:** You can add tokens for **Browsing** (MediaHub), **Clips** (Export), or **Segments** (Timeline).

### Step 2: Resolving the Token (`resolve_hook_token`)
This is the "Search and Replace" part. When Flame sees your token, it runs this function to find out what the real value should be.
```python
def resolve_hook_token(context, context_info, token_name, hint):
    if token_name == "<my_custom_token>":
        return "Real_Value_123"
```

---

## 3. Advanced Trick: The "Cache"

If you have a token that is hard to calculate (like asking a website for a job number), you don't want Flame to do that 1,000 times for 1,000 clips.

The script shows an example of a **TTL Cache** (Time-To-Live). It calculates the value once and then "remembers" it for 5 seconds. This keeps Flame feeling fast and responsive.

---

## 4. Why is this useful?

- **Dynamic Exporting:** You can create an export path that automatically includes the current artist's name and the date without ever typing it.
- **Project Context:** Pull information from external files or databases and inject it directly into Flame's file naming.
- **Consistency:** Ensures that everyone in the studio uses the exact same naming format for their renders.

---

## 5. Key Takeaway for Beginners

Tokens are like **Variables** for your filenames. By defining them in `tokens_hook.py`, you are creating a shortcut that turns complex, dynamic data into simple words that any Flame artist can use.
