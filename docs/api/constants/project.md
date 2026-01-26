# Constant: project

**Module**: `flame`

A Flame constant identified by the name `project`. The exact meaning and runtime value are determined at execution time.

---

**Type:** `unknown`

**Example value:**

```python
import flame
print(flame.project)  # -> <not available>
```

**Example usage:**

```python
# Example: use to identify project-scoped operations
# project_api.call(flame.project, 'Open')
```

**See also:**

- `docs/api/constants/` index

**Notes:**
- Values are collected at runtime and may vary between Flame versions or environments.
- Run `scripts/generate_constant_docs.py --apply` to populate actual runtime values.
