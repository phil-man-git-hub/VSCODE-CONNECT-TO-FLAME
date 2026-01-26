# Class: PyMediaPanel

**Module**: `flame`

This class represents the media panel.

## Methods
### `selected_entries(...)`

None( (flame.PyMediaPanel)arg1) -> object

### `visible(...)`

None( (flame.PyMediaPanel)arg1) -> bool

### `full_height(...)`

None( (flame.PyMediaPanel)arg1) -> bool

### `full_width(...)`

None( (flame.PyMediaPanel)arg1) -> bool

### `dual(...)`

None( (flame.PyMediaPanel)arg1) -> bool

### `move(...)`

move( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object :
    Move a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.
    Return a list of the moved PyObjects.
    Keyword arguments:
    source_entries -- The PyObject or list of PyObjects to move.
    destination -- The PyObject that acts as destination.
    duplicate_action -- Action to take when finding an object with the same name (add or replace).
    

### `copy(...)`

copy( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object :
    Copy a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.Return a list of the copied PyObjects.Keyword arguments:
    source_entries -- The PyObject or list of PyObjects to copy.
    destination -- The PyObject that acts as destination.
    duplicate_action -- Action to take when finding an object with the same name (add or replace).
    

