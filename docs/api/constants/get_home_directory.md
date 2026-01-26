# Constant: get_home_directory

**Module**: `flame`

A Flame constant identified by the name `get_home_directory`. The exact meaning and runtime value are determined at execution time.

---

**Type:** `unknown`

**Example value:**

```python
import flame
print(flame.get_home_directory)  # -> <not available>
```

**Example usage:**

```python
# Example: use to request the user's home directory path from Flame
# home = system.get_path(flame.get_home_directory)
```

**See also:**

- `docs/api/constants/` index

**Notes:**
- Values are collected at runtime and may vary between Flame versions or environments.
- Run `scripts/generate_constant_docs.py --apply` to populate actual runtime values.
