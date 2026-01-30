# Insight: Precision Frame Rates (<rate>)

This document explains the `<rate>` tag. It is used to tell Flame exactly how many frames (images) should play every second.

**Target Audience:** Novice programmers interested in video timing and math.

---

## 1. Why Not Just Use Decimals?

In the movie world, frame rates are often messy. For example, "23.98 fps" is actually **23.976023976...** infinitely. If a computer uses a simple decimal, it will eventually lose sync over a long movie.

---

## 2. The Rational Solution (Numerator & Denominator)

To keep things 100% precise, Open Clip uses **Fractions**. 

```xml
<rate type="rate">
    <numerator>24000</numerator>
    <denominator>1001</denominator>
</rate>
```

- **Numerator:** The top number.
- **Denominator:** The bottom number.
- **Result:** `24000 / 1001` equals exactly **23.976...** without any rounding errors.

---

## 3. Simplified Decimal Format

If you aren't worried about extreme precision (like for a short 5-second clip), you can still use a simple number:

```xml
<rate type="rate">24</rate> <!-- Exactly 24 frames per second -->
```

---

## 4. Why is this useful?

Precision frame rates ensure that your audio and video stay perfectly in sync, even if the movie is 3 hours long. By using the `<numerator>` and `<denominator>`, you are giving Flame the most accurate "Clock" possible.

---

## 5. Key Takeaway for Beginners

The `<rate>` tag is the **"Metronome"** of your clip. Using the fraction format (`24000/1001`) is the professional way to handle frame rates, ensuring that every single frame plays at exactly the right micro-second.
