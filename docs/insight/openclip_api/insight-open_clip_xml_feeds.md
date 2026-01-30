# Insight: Managing Version Lists (<feeds>)

This document explains the `<feeds>` tag (note the 's' at the end!). It is a simple container that holds all the different versions available for a single track.

**Target Audience:** Novice programmers learning about XML lists.

---

## 1. What is the `<feeds>` tag?

Think of `<feeds>` as a **Folder**. Inside this folder, you put all the individual `<feed>` tags (the specific versions) for a track.

---

## 2. The "Active" Version

The most important job of the `<feeds>` tag is to tell Flame which version to show first. It does this using the **`currentVersion`** attribute.

```xml
<feeds currentVersion="v2">
    <feed vuid="v1" ... />
    <feed vuid="v2" ... /> <!-- This one is active! -->
</feeds>
```

- If you don't specify a `currentVersion`, Flame will usually just pick the last one in the list.

---

## 3. Why is this useful?

It allows for **Instant Switching**. 
Because all the versions are listed inside the `<feeds>` container, an artist in Flame can just click a button to swap between "v1" and "v2" instantly. The `<feeds>` tag keeps those options organized and ready to go.

---

## 4. Key Takeaway for Beginners

The `<feeds>` tag is the **Manager** of a track's history. It doesn't hold any media itself; it just keeps a list of every version that has been rendered for that track and marks which one is the "Current Master."
