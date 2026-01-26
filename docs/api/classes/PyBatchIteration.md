
# Class: PyBatchIteration

**Module**: `flame`

## Inheritance & Hierarchy
* **Standalone class** (not derived from PyFlameObject or PyArchiveEntry)
* **Functional Role:** Represents an iterable saved state or iteration of a Batch setup.


## Description
Represents a Batch Iteration, a saved state of a Batch Group that can be opened as a new Batch Group.

---

## Attributes
| Attribute   | Type   | Description |
|-------------|--------|-------------|
| name        | str    | The name of an object in the Media Panel, resolving tokens if any are present. |
| uid         | str    | The unique identifier of an object in the Media Panel. |
| token_name  | str    | The tokenized name of an object in the Media Panel. |
| expanded    | bool   | The expanded state of an object in the Media Panel. Values: True/False |
| colour      | tuple  | The colour of an object in the Media Panel. |

---


## Methods
### Properties
- `iteration_number(...)` — None( (flame.PyBatchIteration)arg1) -> int 
None( (flame.PyBatchIteration)arg1) -> int


### Built-in methods
- `open_as_batch_group(...)` — open_as_batch_group( (PyBatchIteration)arg1 [, (bool)confirm=True]) -> bool : 
open_as_batch_group( (PyBatchIteration)arg1 [, (bool)confirm=True]) -> bool :
    Open a Batch Iteration as a new Batch Group, adding it to PyDesktop.batch_groups. Can only be called from a Library.

## API Insight

- A Batch Iteration is a saved state of a Batch Group and exposes an `open_as_batch_group(confirm=True)` method to restore it into PyDesktop.batch_groups.
- Attributes such as `name`, `uid`, and `iteration_number` help locate and identify the iteration programmatically.

**Example:**

```python
# Open the iteration as a Batch Group without confirmation
iteration.open_as_batch_group(confirm=False)
```

