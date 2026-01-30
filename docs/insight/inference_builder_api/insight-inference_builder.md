# Insight: The Inference Builder API (AI Model Packaging)

This document explains the **Inference Builder**, a specialized tool in Autodesk Flame that allows you to bring your own **Artificial Intelligence (AI)** models into your creative workflow.

**Target Audience:** Novice Python programmers and technical artists interested in Machine Learning (ML).

---

## 1. What is the Inference Builder?

Autodesk Flame can run custom AI models (like tools that remove backgrounds, upscale low-res video, or clean up digital noise). These models are usually saved in a standard format called **ONNX**.

However, Flame needs a bit more information to use these models correctly—like knowing which socket is "Video" and which is "Alpha." The **Inference Builder** is the tool that packages an AI model into a single, encrypted file called an **.inf** file (similar to how Matchbox uses `.mx` files).

---

## 2. The Three-Part Package

To create a professional AI tool for Flame, you need three files with the same name:
1.  **`MyModel.onnx`**: The actual "Brain" (the trained AI model).
2.  **`MyModel.json`**: The "Instruction Manual" (the sidecar file that explains how to use the brain).
3.  **`MyModel.png`**: The "Cover Art" (a 128x94 thumbnail for the Flame file browser).

---

## 3. The "Instruction Manual" (JSON File)

The `.json` file is where you do most of your work. It tells Flame how to connect its inputs to the AI model's inputs.

### Key Settings to Know:
- **`ScalingFactor`**: If your AI model makes a 1080p image into a 4K image, you set this to `2.0`. This tells Flame to prepare a larger canvas for the result.
- **`Channels`**: AI models are very picky. One model might want "Red, Green, Blue," while another wants "Blue, Green, Red." You use the `Channels` setting (like `"RGB"` or `"BGR"`) to translate between them.
- **`Padding`**: Some AI models can only work on images that are multiples of 8 or 16 pixels. If you set `Padding: 8`, Flame will automatically add invisible pixels to the edges to make the AI happy, then trim them off when it's done.

---

## 4. The Workflow

1.  **Generate:** Run the `inference_builder -j` command to create a "starting" JSON file based on your model.
2.  **Edit:** Open the JSON in a text editor and fill in the descriptions and channel types.
3.  **Test:** Load your `.onnx` and `.json` files into an **Inference Node** in Batch.
4.  **Package:** Once it's working perfectly, run `inference_builder -p` to turn everything into a single, encrypted `.inf` file.

---

## 5. Why is this useful?

- **Custom Tools:** You can download open-source AI models from the internet (like those on HuggingFace) and turn them into native Flame tools.
- **IP Protection:** Packaging into an `.inf` file encrypts your model, so you can share your tool with other studios without them seeing your secret AI "Brain" code.
- **User Friendly:** It turns a complex technical process into a simple "Node" that any Flame artist can use without knowing anything about AI.

---

## 6. Key Takeaway for Beginners

Think of the Inference Builder as a **"Gift Wrapper."** You take a raw AI model (the gift), write a card explaining how to use it (the JSON), add a nice picture (the thumbnail), and wrap it all into a professional package (the `.inf` file) that works perfectly inside Flame.
