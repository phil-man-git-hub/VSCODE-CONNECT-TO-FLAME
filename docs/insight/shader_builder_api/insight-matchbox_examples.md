# Insight: Matchbox Shader Examples

This document provides a summary of the official Matchbox examples provided by Autodesk. These files demonstrate the wide variety of technical tricks you can use in your own shaders.

**Location in Flame:** `/opt/Autodesk/presets/<version>/matchbox/shaders/EXAMPLES/`

---

## 1. UI and Interaction Examples

- **`Curves.glsl`**: Shows how to add a graph editor to your node. This is perfect for custom color grading or complex easing.
- **`ColourWheel.glsl`**: Shows how to use the standard "Lift/Gamma/Gain" style wheels in your UI.
- **`ConditionalUI.glsl`**: Shows how to make a button appear or disappear based on another setting (e.g., hiding a "Size" slider when "Auto-Scale" is checked).

## 2. Technical Feature Examples

- **`Accumulate.glsl`**: Shows how to "remember" the previous frame. This is essential for trails, echoes, or temporal noise reduction.
- **`TemporalSampling.glsl`**: Shows how to look at the frames immediately before and after the current one.
- **`Mipmaps.glsl`**: Shows how to use Flame's built-in "low-res" versions of an image to create very fast, high-quality blurs.

## 3. Real-World Tool Examples

- **`TransitionShader.glsl`**: A template for building your own timeline transitions (like wipes, dissolves, or glitched cuts).
- **`DecodeZDepthHQ.glsl`**: An advanced example that shows how to take technical data from Action (depth information) and use it to build a 3D-aware 2D effect (like Depth of Field).
- **`ImagePosition/Rotation/Scaling`**: These show the core math for basic image transforms. If you've ever wondered how a computer "moves" an image, look at these files.

---

## 4. How to use these Examples

The EXAMPLES folder is a **"Library of Parts."** 
- Need a blur? Check `PyramidBlur`.
- Need a dropdown list? Check `BuildList`.
- Need to blend two images? Check `Blending`.

**Pro Tip:** Don't try to memorize the code. Just remember that these examples exist, and copy-paste the sections you need into your own project!

---

## 5. Key Takeaway for Beginners

The strength of Matchbox is its **versatility**. These examples prove that you can build everything from a simple color filter to a complex 3D-aware compositing tool. If you can't figure out how to do something in GLSL, there is probably an example in this folder that shows you the way.
