# Insight: The Root Container (<clip>)

This document explains the `<clip>` tag, which is the "Main Envelope" of an Open Clip XML file. Everything else in the file lives inside this tag.

**Target Audience:** Novice programmers learning XML structure.

---

## 1. What is the `<clip>` tag?

The `<clip>` tag is the **Root Element**. This means it is the first tag you open and the last tag you close. It defines the basic identity of the clip.

```xml
<clip type="clip" version="7">
    ... everything else ...
</clip>
```

---

## 2. Key Information inside `<clip>`

Inside the clip tag, you can define "Global" settings that apply to the whole object:

- **`<name>`**: What the clip is called in Flame.
- **`<tracks>`**: The list of all video and audio channels.
- **`<versions>`**: The list of all available versions (V1, V2, etc.).
- **`<startTimecode>`**: Where the clip starts on a clock (e.g., 01:00:00:00).
- **`<duration>`**: How long the clip is.
- **`<userData>`**: A secret compartment where you can store your own custom notes or tracking IDs.

---

## 3. Why is it useful?

The `<clip>` tag acts as a **"Summary."** 
If you don't define a specific duration or start time, Flame is smart. It looks inside the clip at all the media and **infers** the information automatically. This means your XML can be very short if you just want to point to one file, or very detailed if you need to override specific settings.

---

## 4. Key Takeaway for Beginners

Think of the `<clip>` tag as the **"Header"** of a document. It sets the version of the "Open Clip Language" you are using (currently Version 7) and provides the overall context for Flame to understand the media streams hidden inside.
