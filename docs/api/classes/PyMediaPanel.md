# Class: PyMediaPanel

**Module**: `flame`

**Inherits from**: instance, object

## Description
This class represents the media panel.


## Properties
| Name | Description |
| --- | --- |
| `dual` | The dual view status of the media panel. |
| `full_height` | The full height status of the media panel. |
| `full_width` | The full width status of the media panel. |
| `selected_entries` | A list of PyObject currently selected. |
| `visible` | The visible status of the media panel. |


## Methods
### `copy`
```python
copy
```


copy( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object :

    Copy a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.Return a list of the copied PyObjects.Keyword arguments:

    source_entries -- The PyObject or list of PyObjects to copy.

    destination -- The PyObject that acts as destination.

    duplicate_action -- Action to take when finding an object with the same name (add or replace).

    

---

### `move`
```python
move
```


move( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object :

    Move a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.

    Return a list of the moved PyObjects.

    Keyword arguments:

    source_entries -- The PyObject or list of PyObjects to move.

    destination -- The PyObject that acts as destination.

    duplicate_action -- Action to take when finding an object with the same name (add or replace).

    

---
