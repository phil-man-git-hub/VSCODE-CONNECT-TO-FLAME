# Constant: find_by_name

**Module**: `flame`

A Flame constant identified by the name `find_by_name`. The exact meaning and runtime value are determined at execution time.

---

**Type:** `unknown`

**Example value:**

```python
import flame
print(flame.find_by_name)  # -> <not available>
```

**Example usage:**

```python
# Example: pass to a search function to specify a find-by-name search mode
# results = search.find(flame.find_by_name, 'pattern')
```

**See also:**

- `docs/api/constants/` index

**Notes:**
- Values are collected at runtime and may vary between Flame versions or environments.
- Run `scripts/generate_constant_docs.py --apply` to populate actual runtime values.
