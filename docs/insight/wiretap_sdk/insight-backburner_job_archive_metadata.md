# Insight: Backburner Job Archive Metadata

This document explains how to quickly look at the history of everything your render farm has ever done.

**Target Audience:** Novice programmers interested in database history and reporting.

---

## 1. What is the Job Archive?

When a job is finished and old, Backburner moves it from the active `/jobs` folder to the **`/archive`** folder. This keeps the active list clean and fast.

---

## 2. The "Super Query"

Normally, if you want to know about 100 jobs, you have to ask 100 questions. That's slow!

Wiretap has a "Super Query" for the archive. When you ask for metadata on the `/archive` node, it gives you a **giant list** of every archived job all at once.

```xml
<info>
  <job id="101" name="Shot_01" user="John" ... />
  <job id="102" name="Shot_02" user="Jane" ... />
</info>
```

---

## 3. Why is this useful?

- **Auditing:** You can see exactly what was rendered three months ago.
- **Speed:** It is much faster for your script to download one big list than to ask for jobs one-by-one.
- **Cleanup:** You can look at the `endTime` of all archived jobs and decide which ones are old enough to be deleted forever.

---

## 4. Key Takeaway for Beginners

The `/archive` node is the **"History Book"** of your studio. By using the `info` stream on this node, you can get a summary of months of work in just a few seconds. It is the most efficient way to build long-term reports.
