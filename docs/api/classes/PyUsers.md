
# Class: PyUsers

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contains:** PyUser

## Functional Role & Context
* **Functional Role:** Represents the user manager, providing access to user management and current user selection.
* **Context:** Used for automating user management, selection, and customization in Flame.

## Description
The PyUsers class provides programmatic access to user management, supporting automation of user selection and management in the Flame environment.

---

Object representing the User manager.

## API Insight
### Autodesk Flame API Insight (2026)

`PyUsers` is the system user manager accessible via `flame.users`. It exposes `current_user` and a `users` list and provides a `get_user(name)` helper to fetch a `PyUser` object.

**Common usage:** check the current user, list all users, and obtain user-specific desktops and settings.

**Example:**

```python
users_mgr = flame.users
print('Current user:', users_mgr.current_user.name)
for u in users_mgr.users:
    print(f"User: {u.name} ({u.user_id})")
# Fetch a specific user
admin = users_mgr.get_user('admin')
``` 

## Methods
### Properties
- `current_user(...)` — None( (flame.PyUsers)arg1) -> object 
None( (flame.PyUsers)arg1) -> object


