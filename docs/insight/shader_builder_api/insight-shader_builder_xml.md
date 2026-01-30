# Insight: Designing Shader Interfaces (XML)

This document explains the sidecar **XML** file that accompanies Matchbox and Lightbox shaders. It is the "Blueprint" for the user interface (UI) you see inside Flame.

**Target Audience:** Novice programmers who want to make their shaders easy for others to use.

---

## 1. Why do I need an XML file?

When you write a shader (`.glsl`), Flame can guess some simple buttons for you. But if you want a professional UI with organized pages, custom names, dropdown menus, or color wheels, you need an **XML sidecar file**.

You generate this file by running:
`shader_builder -x my_shader.glsl`

---

## 2. Anatomy of the UI

The XML file is broken down into a hierarchy:

### A. `<ShaderNodePreset>` (The Root)
This is the main container. It holds the name of your effect and settings like whether it supports 3D or if it provides a Matte.

### B. `<Uniform>` (The Controls)
Every slider, checkbox, or color pot in Flame is a **Uniform**.
- **`DisplayName`**: What the user sees (e.g., "Glow Strength" instead of `adskUID_strength`).
- **`Min` / `Max` / `Default`**: Sets the safe range for the slider.
- **`Tooltip`**: The helpful text that appears when a user hovers over the control.

### C. `<Page>` and `<Col>` (The Layout)
These organize your controls so the UI isn't just one long list.
- **Pages**: Tabs at the bottom of the node.
- **Columns**: Vertical groups within a page.

---

## 3. Special Control Types

The XML allows you to change how a value is presented:
- **`PopUp`**: Turns a number into a dropdown list (e.g., 0 = "Linear", 1 = "Log").
- **`Colour`**: Adds a color picker instead of three separate R, G, B sliders.
- **`Curve`**: Provides a graph editor for complex changes over time.

---

## 4. Smart UI (Conditional logic)

You can make your UI "smart" using **UIConditions**.
For example, you can hide the "Blur Amount" slider unless the "Enable Blur" checkbox is checked. This keeps the interface clean and prevents users from changing settings that don't do anything.

---

## 5. Key Tip: The `adsk_` Prefix

If you name a variable in your GLSL starting with `adsk_` (like `adsk_time`), Flame will **hide** it from the UI. This is useful for internal math that the user shouldn't touch.

---

## 6. Key Takeaway for Beginners

The XML file is your way of communicating with the artist. A well-organized XML makes a complex shader feel like a simple, built-in tool. If you can't find a setting, look for the `shader_builder -x` command—it's the best way to start building your custom interface.
