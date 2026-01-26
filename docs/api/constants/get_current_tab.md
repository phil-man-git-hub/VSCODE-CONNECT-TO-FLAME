# Constant: get_current_tab

**Module**: `flame`

A Flame constant identified by the name `get_current_tab`. The exact meaning and runtime value are determined at execution time.

---

**Type:** `unknown`

**Example value:**

```python
import flame
print(flame.get_current_tab)  # -> <not available>
```

**Example usage:**

```python
# Example: read current UI tab / pass to a tab-management API
# current = ui.get_tab(flame.get_current_tab)
```

**See also:**

- `docs/api/constants/` index

**Notes:**
- Values are collected at runtime and may vary between Flame versions or environments.
- Run `scripts/generate_constant_docs.py --apply` to populate actual runtime values.
