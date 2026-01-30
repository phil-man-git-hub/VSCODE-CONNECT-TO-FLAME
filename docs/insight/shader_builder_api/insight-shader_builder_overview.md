# Insight: Shader Builder Overview (High-Level)

This document provides a birds-eye view of the **Shader Builder** workflow. It is the master process for turning raw code into a professional tool for Autodesk Flame.

**Target Audience:** Novice programmers and technical artists.

---

## 1. The Workflow in 5 Steps

Creating a custom tool follows a specific sequence:

1.  **Write:** Create your graphics code in **GLSL** (The math of the effect).
2.  **Generate:** Use the `shader_builder` tool to create an **XML** file (The design of the buttons).
3.  **Refine:** Edit the XML to add better names, tooltips, and organized pages for your sliders.
4.  **Preset:** Open your shader in Flame, make a "Cool Look," and save it as a **Preset**.
5.  **Package:** Use `shader_builder` again to encrypt your code into a single **.mx** (Matchbox) or **.lx** (Lightbox) file.

---

## 2. Matchbox vs. Lightbox

| Feature | **Matchbox** | **Lightbox** |
| --- | --- | --- |
| **Dimension** | 2D (Flat Images) | 3D (Inside Action) |
| **Main Function** | `main()` | `adskUID_lightbox()` |
| **Location** | Batch, Timeline, Action | Attached to a Light in Action |
| **Best For** | Blurs, CC, Distortions | Relighting, Materials, 3D Glows |

---

## 3. The Power of `shader_builder`

`shader_builder` is a command-line utility. You use it in your terminal to:
- **Check for Errors:** It tries to "compile" your code. If you forgot a semicolon, it will tell you exactly where.
- **Auto-UI:** It looks at your variables and automatically builds a "Best Guess" user interface.
- **IP Protection:** It encrypts your code so other people can use your tool without seeing your secret formulas.

---

## 4. Why build your own shaders?

- **Unique Identity:** Make your studio's work stand out with looks that no one else has.
- **Speed:** Custom nodes can combine 10 standard nodes into one single, fast button.
- **Community:** You can join sites like [Logik Matchbook](https://logik-matchbook.org/) to download shaders from other professional artists around the world.

---

## 5. Key Takeaway for Beginners

The Shader Builder API is the **"Secret Sauce"** of Autodesk Flame. It allows you to transform the software from a standard editing tool into a specialized, high-performance visual effects engine tailored exactly to your needs.
