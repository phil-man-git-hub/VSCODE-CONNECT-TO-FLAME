# Insight: Lightbox Shader Examples

This document provides a summary of the official Lightbox examples provided by Autodesk. These are the best place to start if you want to learn by "deconstructing" existing code.

**Location in Flame:** `/opt/Autodesk/presets/<version>/action/lightbox/EXAMPLES`

---

## 1. The Learning Path

### Level 1: The Basics
- **`LightboxBasics.glsl`**: The simplest possible Lightbox. It just multiplies the color by a "Gain" value. Use this to see the minimum code required to make a Lightbox work.

### Level 2: Replicating Flame
- **`SimpleLight.glsl`**: Shows you how to manually recreate the math of a standard "Point Light." It's a great lesson in 3D math and how Flame calculates brightness based on distance.

### Level 3: Interaction with 3D Space
- **`LightboxAPISimple.glsl`**: Shows how to ask Flame for information about the 3D scene, like the position of the light and the position of the pixels (vertices). This allows for "Decay" effects where the light gets weaker as it gets further away.

### Level 4: Advanced Material Science
- **`PhysicallyBasedIBL`** and **`GGXMaterial`**: These are complex shaders. They use "Physically Based Rendering" (PBR) to make surfaces look like real metal, plastic, or glass. They show how a Lightbox can completely change the "look" of an object's material.

---

## 2. Key Code Snippets to Look For

When you open these files, look for these specific API calls:

- **`adsk_getLightPosition()`**: Where is the light?
- **`adsk_getVertexPosition()`**: Where is the object?
- **`adsk_rgb2yuv()`**: A built-in helper to change color spaces quickly.

---

## 3. How to use these Examples

Don't try to write a complex shader from scratch. 
1. **Copy** an example that is close to what you want.
2. **Modify** one or two lines of code.
3. **Run** `shader_builder` to see if it still works.
4. **Load** it into Action to see the result.

---

## 4. Key Takeaway for Beginners

The EXAMPLES folder is your **"Cheat Sheet."** Most professional shaders are just variations of these basic patterns. If you want to build a tool that relights a scene, start with `SimpleLight` and build from there!
