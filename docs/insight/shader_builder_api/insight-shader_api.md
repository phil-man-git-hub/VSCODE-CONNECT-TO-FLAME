# Insight: The Shader API (Helper Functions)

This document explains the built-in **Shader API**. These are special "shortcuts" (functions) that Autodesk provides to help you write complex shaders without doing all the hard math yourself.

**Target Audience:** Novice programmers learning GLSL syntax.

---

## 1. What is the Shader API?

When you write a shader for Flame, you don't have to calculate things like "How bright is this light?" or "Convert this color to Grayscale" from scratch. Flame has a library of pre-written functions you can "call" in your code.

---

## 2. Lighting & 3D Helpers (Lightbox)

These are for interacting with the 3D scene in Action:
- **`adsk_getLightPosition()`**: Tells you exactly where the light is in 3D space.
- **`adsk_getNormal()`**: Tells you which way the surface of an object is facing.
- **`adsk_getLightColour()`**: Tells you the color and brightness of the light.
- **`adsk_getVertexPosition()`**: Tells you the 3D coordinate of the pixel you are currently coloring.

## 3. Color Space Helpers (Matchbox & Lightbox)

Moving between different color "languages" is easy with these functions:
- **`adsk_rgb2hsv()`**: Converts standard Red/Green/Blue into Hue/Saturation/Value (great for making "Hue Shift" tools).
- **`adsk_scene2log()`**: Converts linear light into "Log" (Cineon) space.
- **`adsk_getLuminance()`**: Quickly turns a color image into a perfect black-and-white (grayscale) image.

## 4. Blending Helpers

Instead of writing complex math for "Overlay" or "Screen" modes, you can just use:
- **`adsk_getBlendedValue(blendType, foreground, background)`**
By changing the `blendType` number (e.g., 0 for Add, 2 for Multiply), you can replicate any Photoshop-style blending mode.

## 5. Built-in Variables (Uniforms)

Flame also automatically gives you these "Magic Variables":
- **`adsk_time`**: The current frame number (useful for making things animate or flicker).
- **`adsk_result_w` / `h`**: The width and height of your image.

---

## 6. Key Takeaway for Beginners

The Shader API is like a **"Toolbox."** Before you try to write a complex mathematical formula, check the API documentation first. There is a high chance that Autodesk has already written a one-line function that does exactly what you need!
