# Constant: execute_command

**Module**: `flame`

A Flame constant identified by the name `execute_command`. The exact meaning and runtime value are determined at execution time.

---

**Type:** `unknown`

**Example value:**

```python
import flame
print(flame.execute_command)  # -> <not available>
```

**Example usage:**

```python
# Example: pass to an execution API to invoke a named command
# system.execute(flame.execute_command, 'someCommand')
```

**See also:**

- `docs/api/constants/` index

**Notes:**
- Values are collected at runtime and may vary between Flame versions or environments.
- Run `scripts/generate_constant_docs.py --apply` to populate actual runtime values.
