# Understanding AI Modalities

"Modality" refers to the *type* of data the AI can understand or create. Early AI was mostly "Single-Modal" (just text). Modern AI is "Multi-Modal."

---

## 1. Text (The Foundation)
The most common modality. AI "sees" text as **Tokens** (chunks of characters) rather than whole words.

## 2. Vision (Image & Video)
*   **Image Understanding:** Identifying objects, reading text in photos (OCR), or describing the "vibe" of a picture.
*   **Video Understanding:** Seeing how things change over time. This is critical for tools interacting with the Autodesk Flame UI.

## 3. Audio (Sound & Speech)
*   **STT (Speech-to-Text):** Also known as Transcription. Turning a spoken meeting into a text summary.
*   **TTS (Text-to-Speech):** Turning a script into a natural-sounding voice.
*   **Audio-to-Audio:** Some new models can "listen" to a voice and respond with a voice *without* turning it into text in the middle, preserving the emotion and tone.

## 4. Multimodal Interplay
**The Real Power**

The most advanced AIs can "connect" these senses. 
*   **Example:** You can show an AI a video of a software crash and *say* out loud, "Why did that happen?" The AI processes the video (Vision) and your voice (Audio) together to give you a text answer.

## 5. OCR (Optical Character Recognition)
**Reading the Unreadable**

*   **What it is:** The specific skill of looking at an image (like a scan of a receipt or a screenshot of a menu) and pulling out the text characters.
*   **In this Repo:** We might use OCR to "read" values from the Flame UI that aren't available through the standard API.
