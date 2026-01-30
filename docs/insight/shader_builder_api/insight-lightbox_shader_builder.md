# Insight: Creating Lightbox Shaders

This document explains the **Lightbox** framework in Autodesk Flame. It shows how you can write your own 3D lighting effects using GLSL (OpenGL Shading Language).

**Target Audience:** Novice programmers and technical artists interested in 3D compositing and GLSL.

---

## 1. What is a Lightbox?

A **Lightbox** is a custom shader that lives inside **Action** (Flame's 3D engine). Think of it as a "Smart Filter" for a light. 

Usually, a light just makes things brighter. A Lightbox can make a light do *anything*—like inverting colors, adding texture, or changing the way a surface reacts to distance.

---

## 2. The Basic Structure

A Lightbox shader is a small piece of code written in GLSL. It always has a specific function:

```glsl
vec4 adskUID_lightbox(vec4 source)
{
    // 'source' is the pixel color before this light hits it.
    // Your code goes here...
    return source;
}
```

- **`adskUID_`**: This prefix is mandatory. It stands for "Unique ID" and prevents your shader from clashing with others when multiple Lightboxes are loaded.
- **`source`**: This represents the color and transparency (RGBA) of the object being lit.

---

## 3. Writing and Testing

1.  **Code:** Write your shader in a text editor and save it as `.glsl`.
2.  **Validate:** Use the `shader_builder` utility in your terminal:
    `shader_builder -l -x my_shader.glsl`
    - `-l` tells it this is a **Lightbox**.
    - `-x` tells it to generate an **XML** file (this creates the buttons and sliders in Flame).
3.  **Fix:** If there are errors (like a missing `;`), `shader_builder` will tell you exactly which line is broken.

---

## 4. Key Concepts to Remember

- **Pre vs. Post:** In Flame, a Lightbox can run *before* the light hits the object (to modify the surface) or *after* the light (to modify the final lit result).
- **The Alpha Rule:** Always return a valid Alpha (`source.a`). If you set Alpha to 0, the object will disappear!
- **Namespacing:** You must use the `adskUID_` prefix for every variable you create (like `adskUID_gain`). If you don't, you can only load one copy of your shader at a time.

---

## 5. Why use Lightbox instead of Matchbox?

- **Matchbox** is for 2D image processing (like blurs or color corrections).
- **Lightbox** is for 3D interactions. It has access to things like the position of the light, the direction of the surface (normals), and the 3D depth of the scene.

---

## 6. Key Takeaway for Beginners

Lightbox allows you to "hijack" Flame's 3D lighting pipeline. Whether you want to make a light that only affects blue objects or a light that adds a custom glow pattern, the `adskUID_lightbox` function is where you build that logic.
