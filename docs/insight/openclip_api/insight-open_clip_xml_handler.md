# Insight: The Media Interpreter (<handler>)

This document explains the `<handler>` tag. It is the part of the Open Clip that acts as a "Driver" or "Interpreter" for the media files.

**Target Audience:** Novice programmers interested in how software reads files.

---

## 1. What is a Handler?

When Flame looks at a file (like a DPX sequence), it needs to know how to read the metadata inside it—like the frame rate or the timecode. The `<handler>` tag tells Flame which "Logic Engine" to use.

Common handlers include:
- **MIO Clip**: The standard engine for reading modern media files.

---

## 2. Dynamic Discovery (ScanPattern)

One of the most powerful things a handler can do is **Scan**. 
Instead of you listing every single file path in the XML, you can give the handler a "Search Pattern" using the `<ScanPattern>` option.

```xml
<ScanPattern>Media/Shot_v{version}.{frame}.exr</ScanPattern>
```

- **How it works:** Flame will look at the `Media` folder. If it finds `Shot_v01.001.exr` and `Shot_v02.001.exr`, it will **automatically** create Version 1 and Version 2 for you.
- **Why use it?** It makes your Open Clips "Self-Updating." As soon as a 3D artist renders a new version, Flame sees it instantly.

---

## 3. Handler Options

Inside the handler, you can also set "Rules" for how to interpret the media:
- **`RateMode`**: Should Flame trust the "Header" of the file for the frame rate, or should you force a specific number?
- **`AlignToZero`**: Should the first frame of the file always be treated as "Frame 0"?

---

## 4. Why is this useful?

The handler removes the manual labor of building complex clips. By setting up a good Scan Pattern, you can create a single `.clip` file that acts as a window into a messy folder of renders, organizing them into a neat, versioned interface for the artist.

---

## 5. Key Takeaway for Beginners

Think of the `<handler>` as the **"Smart Assistant."** You give it a general rule (the Scan Pattern), and it does the tedious work of finding files and identifying versions so you don't have to write thousands of lines of XML.
