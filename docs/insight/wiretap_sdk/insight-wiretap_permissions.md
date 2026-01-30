# Insight: Users, Groups, and Permissions

This document explains how Wiretap decides if your script is "Allowed" to touch a file or project.

**Target Audience:** Novice system administrators and security-conscious programmers.

---

## 1. The ID Rule (POSIX)

Wiretap works across a network of computers. To keep permissions simple, it assumes that every computer in the studio uses the same **User IDs**.
- If your ID is `501` on your laptop, the server expects you to be ID `501` there too.
- As long as these IDs match, the server will "Honor" your credentials and let you edit your projects.

---

## 2. Fallback: The "Anonymous" User

If your script connects from a computer that the server doesn't recognize, it won't just block you. It will treat you as an **Anonymous User**.
- **IFFFS Server:** Falls back to a user named `IFFFS_user`.
- **Gateway Server:** Falls back to a user named `wtguser`.
- *Note:* These anonymous users usually have very limited power (e.g., they can see files but not delete them).

---

## 3. The "Root" Restriction

By default, the "Superuser" (Root) is **Blocked** from accessing Wiretap over the network.
- **Why?** This is a safety feature to prevent someone from accidentally deleting every project in the studio with one command.

---

## 4. Why is this useful?

This system allows you to build a secure pipeline where artists can only see and edit their own work, while managers can see everything—just like in a normal computer file system.

---

## 5. Key Takeaway for Beginners

Wiretap permissions are based on **Identity**. If your script can't access a project, it's usually because the server doesn't recognize your User ID. Always check the `[Authentication]` section of the server's config file if you are having permission issues.
