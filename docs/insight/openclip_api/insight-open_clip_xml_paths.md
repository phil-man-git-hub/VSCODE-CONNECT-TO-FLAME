# Insight: Multiple Views (<paths>)

This document explains the `<paths>` tag (with an 's'). It is a special container used when you have multiple "Views" of the exact same moment in time—the most common example being **Stereo 3D**.

**Target Audience:** Novice programmers interested in 3D and stereoscopic media.

---

## 1. What is the `<paths>` tag?

Sometimes, one path isn't enough to describe a single moment of video. In a 3D movie, you need a path for the **Left Eye** and a different path for the **Right Eye**. 

The `<paths>` tag groups these two links together so Flame knows they are two halves of the same stereoscopic image.

---

## 2. Using `subFeedId`

Inside the `<paths>` tag, you list multiple `<path>` tags. You use the **`subFeedId`** attribute to label them:

```xml
<paths>
    <path subFeedId="Left" encoding="file">Media/shot_L.mov</path>
    <path subFeedId="Right" encoding="file">Media/shot_R.mov</path>
</paths>
```

---

## 3. Why is this different from Tracks?

- **Tracks** are for *different things* (like Video vs. Audio). They can have different lengths and frame rates.
- **Paths** (inside a Feed) are for *different views of the same thing*. The Left and Right eyes **must** have the exact same duration and frame rate to work together.

---

## 4. Why is this useful?

It simplifies the artist's life. Instead of having two separate clips (one for each eye), the artist just sees one "Stereo Clip." Flame handles the complexity of reading both files in the background and keeping them perfectly in sync.

---

## 5. Key Takeaway for Beginners

The `<paths>` tag is the **"Stereo Pair"** container. Use it whenever you have media that needs to be "Joined at the Hip"—different files that represent different angles or views of the exact same sequence of frames.
