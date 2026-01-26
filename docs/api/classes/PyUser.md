
# Class: PyUser

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contained By:** PyUsers

## Functional Role & Context
* **Functional Role:** Represents a user, providing access to user properties and profile management.
* **Context:** Used for automating user management, profile access, and customization in Flame.

## Description
The PyUser class provides programmatic access to user properties and profile management, supporting automation of user customization and management in the Flame environment.

---

Object representing a User.

## API Insight
### Autodesk Flame API Insight (2026)

`PyUser` represents a single Flame user profile. It exposes identifying properties and the user's workspace (`desktop`). This object is typically accessed from `flame.users.current_user` or via `flame.users.get_user(name)`.

**Attributes:** `desktop` (PyDesktop), `id` (int), `name` (str), `user_id` (int).

**Example:**

```python
# Get the current user and their desktop
current = flame.users.current_user
print(f"Logged-in user: {current.name} (ID: {current.id})")
print('Desktop contains:', [c.attributes.name for c in current.desktop.children])
```

## Methods
### Properties
- `name(...)` — None( (flame.PyUser)arg1) -> str 
None( (flame.PyUser)arg1) -> str

- `nickname(...)` — None( (flame.PyUser)arg1) -> str 
None( (flame.PyUser)arg1) -> str

- `shortcuts_profile(...)` — None( (flame.PyUser)arg1) -> str 
None( (flame.PyUser)arg1) -> str


