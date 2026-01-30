# Insight: Creating Matchbox Shaders

This document explains the **Matchbox** framework in Autodesk Flame. It is the most common way to build custom 2D image effects (like blurs, color corrections, or distortions) using GLSL.

**Target Audience:** Novice programmers and technical artists interested in image processing and 2D compositing.

---

## 1. What is a Matchbox?

A **Matchbox** is a standalone image processor. Unlike a Lightbox (which lives inside 3D space), a Matchbox takes an input image, does some math to every pixel, and spits out a new result. 

You can use Matchboxes in:
- **Batch**: As a node in your compositing tree.
- **Timeline**: As a transition between two clips.
- **Action**: As a post-processing filter.

---

## 2. The Basic Structure

A Matchbox shader is a GLSL file. Unlike Lightbox, it uses the standard `main()` function:

```glsl
uniform float adsk_result_w, adsk_result_h;
uniform sampler2D input1;

void main()
{
   // 1. Get the current pixel's coordinate
   vec2 coords = gl_FragCoord.xy / vec2(adsk_result_w, adsk_result_h);
   
   // 2. Read the color from the input
   vec4 color = texture2D(input1, coords);
   
   // 3. Output the final color
   gl_FragColor = color;
}
```

- **`adsk_result_w/h`**: These are built-in variables that Flame fills with the width and height of your output.
- **`input1`**: This represents the first image socket on the node.

---

## 3. Key Features

### A. Multiple Inputs
A Matchbox can have up to 6 input sockets. You can define what these sockets are for (Front, Back, Matte) in your XML file so they are color-coded correctly in Batch.

### B. Multi-pass Rendering
If your effect is complex (like a heavy blur), you can split it into multiple "Passes." You write several GLSL files (e.g., `Blur.1.glsl`, `Blur.2.glsl`), and Flame runs them in sequence.

### C. Selective FX
This is a specialized Matchbox that can interact with Flame's "Selective" node. It allows you to isolate a specific area (like a person's face) and apply the effect only there, with a perfect soft edge.

---

## 4. Writing and Testing

1.  **Code:** Write your GLSL and save it.
2.  **Validate:** Run `shader_builder -m -x my_shader.glsl`.
    - `-m` tells it this is a **Matchbox**.
3.  **Package:** Use `shader_builder -m -p my_shader.glsl` to create an encrypted `.mx` file for sharing.

---

## 5. Why use Matchbox?

- **Custom Filters:** Build a specific look that doesn't exist in Flame's standard library.
- **Performance:** GLSL runs on the GPU, making it extremely fast for complex math.
- **Universal:** Once you build a Matchbox, you can use it anywhere in the Flame family (Flame, Flare, Flame Assist).

---

## 6. Key Takeaway for Beginners

Matchbox is your **"Custom Node Factory."** If you can imagine a mathematical formula for how a pixel should change based on its color or position, you can turn that into a Matchbox tool.
