# Insight: Precise Fractions (<rational>)

This document explains the `<rational>` tag. It is very similar to the `<rate>` tag, but it's used for general math instead of just frame rates.

**Target Audience:** Novice programmers learning about data precision.

---

## 1. What is a Rational number?

In mathematics, a **Rational** number is any number that can be written as a fraction (one number divided by another). 

In an Open Clip, we use this for things like **Aspect Ratio** (the shape of the screen).

---

## 2. Using the Fraction Format

Instead of saying "The screen is 1.777 wide," we use the exact fraction for 16:9:

```xml
<rational type="rational">
    <numerator>16</numerator>
    <denominator>9</denominator>
</rational>
```

---

## 3. Why is this useful?

Just like frame rates, using fractions prevents "Rounding Errors." 
If a computer rounds `1.777777` to `1.78`, your image might look slightly stretched or squashed. By giving Flame the exact numbers (`16` and `9`), the math stays perfect.

---

## 4. Key Takeaway for Beginners

The `<rational>` tag is used whenever you need to be **100% accurate** about a ratio or fraction. Use it for aspect ratios or any other setting where a simple decimal isn't precise enough for professional filmmaking.
