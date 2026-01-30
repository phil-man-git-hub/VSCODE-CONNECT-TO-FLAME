# Insight: Custom Data Containers (<dict>)

This document explains the `<dict>` tag (short for "Dictionary"). It is a flexible container that lets you store almost any kind of custom information inside an Open Clip.

**Target Audience:** Novice programmers learning about "Key-Value Pairs."

---

## 1. What is a Dictionary?

In programming, a **Dictionary** is like a real-world dictionary: you have a **Key** (the word) and a **Value** (the definition).

In an Open Clip, you might want to save info that Flame doesn't have a standard button for—like "Artist Name," "Lens Info," or "Colorist Notes."

---

## 2. How it works in XML

Inside a `<userData>` tag, you use a `<dict>` to list your custom keys:

```xml
<userData type="dict">
    <Artist type="string">John Doe</Artist>
    <Status type="string">Approved</Status>
    <RenderTime type="int32">120</RenderTime>
</userData>
```

---

## 3. Supported Data Types

The `<dict>` is very versatile. You can tell Flame exactly what *kind* of data you are storing using the `type` attribute:
- **`string`**: Text (names, notes).
- **`int` / `float`**: Numbers (versions, frame rates).
- **`bool`**: Yes/No switches.
- **`time`**: Timecodes.
- **`dict`**: You can even put a dictionary *inside* another dictionary! (This is called "Nesting").

---

## 4. Why is this useful?

- **Pipeline Tracking:** Your studio's render manager can write a unique ID into the `<dict>`. Later, Flame can read that ID to find the original 3D project.
- **Automation:** You can write a Python script that looks at the `userData` to decide how to process a clip.
- **Organization:** It keeps your custom notes bundled right inside the media file, so they never get lost.

---

## 5. Key Takeaway for Beginners

The `<dict>` tag is your **"Miscellaneous"** folder. If Flame doesn't have a specific tag for the data you want to save, just create your own key inside a dictionary. It's the best way to make the Open Clip work for your specific studio needs.
