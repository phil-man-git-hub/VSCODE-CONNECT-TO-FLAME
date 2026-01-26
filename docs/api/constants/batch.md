# Constant: batch

**Module**: `flame`

A Flame constant identified by the name `batch`. The exact meaning and runtime value are determined at execution time.

---

**Type:** `unknown`

**Example value:**

```python
import flame
print(flame.batch)  # -> <not available>
```

**Example usage:**

```python
# Example: use the constant where Flame APIs expect this identifier
# some_api.call(flame.batch)
```

**See also:**

- `docs/api/constants/` index

**Notes:**
- Values are collected at runtime and may vary between Flame versions or environments.
- Run `scripts/generate_constant_docs.py --apply` to populate actual runtime values.
