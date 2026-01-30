# Insight: The Master Version List (<versions>)

This document explains the `<versions>` tag. It is the "Master Registry" that tells Flame exactly which versions exist for the entire clip.

**Target Audience:** Novice programmers interested in high-level media organization.

---

## 1. The Global List

While each **Track** has a list of feeds, the **Clip** needs one central list that summarizes every version available across the whole project. That is the `<versions>` tag.

It usually looks like this:
```xml
<versions currentVersion="v2">
    <version uid="v1"/>
    <version uid="v2"/>
    <version uid="v3"/>
</versions>
```

---

## 2. How it Connects Everything

The `uid` inside a `<version>` tag acts as a **Link**. 
When you switch the clip to "v2" in Flame, the software looks at this list and then goes to every track and says: *"Find me the feed that also has the ID 'v2'."*

---

## 3. Why is this useful?

- **Consistency:** It ensures that "Version 2" means the same thing for the Video track as it does for the Audio track.
- **Easy UI:** Flame uses this list to build the dropdown menu that the artist uses to pick a version.
- **Safety:** It prevents Flame from trying to load a version that doesn't actually exist.

---

## 4. Key Takeaway for Beginners

The `<versions>` tag is the **"Global Table of Contents"** for your clip. It doesn't contain links to files; it just defines the "Names" of the versions so that the Tracks can stay in sync when an artist switches between them.
