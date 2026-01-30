# Insight: Creating Shader Presets

This document explains how to create **Presets** for your Matchbox or Lightbox shaders. Presets allow you to save specific settings (like a "Sepia" look or a "Heavy Blur" look) so users don't have to start from scratch.

**Target Audience:** Novice programmers and tool creators.

---

## 1. What is a Preset?

A preset is a small XML file that tells Flame: *"When this shader loads, set the 'Gain' to 0.5 and the 'Color' to Blue."*

In the Flame UI, these appear in the "Presets" dropdown menu at the top of the node settings.

---

## 2. The "Print to Shell" Workflow

You don't have to write preset code by hand. Flame can write it for you!

1.  **Adjust Settings:** Load your shader in Flame and move the sliders until you have a "look" you like.
2.  **Print XML:** Go to the **Node Prefs** menu and click the **UI XML Shell Printout** button.
3.  **Find the Code:** Look at the terminal/shell window where you launched Flame. You will see a block of XML code starting with `<Presets>`.
4.  **Save:** Copy that code into a new text file.

---

## 3. Saving the File

To make the preset work, you must name the file correctly:
- **Rule:** `<shader_name>.preset.xml`
- **Example:** If your shader is `MyGlow.glsl`, your preset file must be `MyGlow.preset.xml`.

Place this file in the same folder as your `.glsl` and `.xml` files.

---

## 4. Organizing Multiple Presets

You can have many looks inside one file. Just add more `<Preset>` blocks:

```xml
<Presets>
   <Preset Name="Warm Glow">
      ... settings for warm glow ...
   </Preset>
   <Preset Name="Cool Blue">
      ... settings for cool blue ...
   </Preset>
</Presets>
```

---

## 5. Why use Presets?

- **Efficiency:** Give artists a head start by providing common settings.
- **Guidance:** Show what your shader is capable of by creating a few extreme "demo" looks.
- **Sharing:** Artists can send you their shell printouts to include in your next update!

---

## 6. Key Takeaway for Beginners

Presets are the **"Finishing Touch"** for a custom tool. By spending 5 minutes "printing" a few cool looks to the shell, you make your shader much more useful and professional for the final artist.
