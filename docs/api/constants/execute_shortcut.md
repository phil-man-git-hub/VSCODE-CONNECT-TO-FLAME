# Constant: execute_shortcut

**Module**: `flame`

A Flame constant identified by the name `execute_shortcut`. The exact meaning and runtime value are determined at execution time.

---

**Type:** `unknown`

**Example value:**

```python
import flame
print(flame.execute_shortcut)  # -> <not available>
```

**Example usage:**

```python
# Example: use to trigger a UI shortcut via script
# ui.trigger_shortcut(flame.execute_shortcut)
```

**See also:**

- `docs/api/constants/` index

**Notes:**
- Values are collected at runtime and may vary between Flame versions or environments.
- Run `scripts/generate_constant_docs.py --apply` to populate actual runtime values.
