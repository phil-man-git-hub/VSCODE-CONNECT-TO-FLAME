
# Class: PyMediaPanel

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Represents the overall Media Panel UI container, providing access to selected entries and panel state.

## Description
Provides access to the Media Panel UI, including selection, visibility, and move/copy operations.


## API Insight
### Autodesk Flame API Insight (2026)

The **`PyMediaPanel`** class provides programmatic access to the Media Panel area of the Flame interface, which is the primary location for managing archived, shared, and versioned media objects within the project. It is typically accessed as a singleton object.

---

#### 1. Definition and Hierarchy

| Property | Value | Description |
| :--- | :--- | :--- |
| **Class Name** | `PyMediaPanel` | This class represents the **media panel** in the Flame UI. |
| **Parent Class** | None explicit (Utility Class) | It is not explicitly derived from `PyFlameObject`, suggesting it is a top-level utility object for UI control, like `PyMediaHub` or `PyMessages`. |
| **Primary Role** | **UI Interface Object** | Serves as an interface for managing the visibility, state, and interaction with the Media Panel and its contained media. |
| **Access** | **Singleton** | The object is accessed through the `flame` module (e.g., `flame.media_panel`). |

---

#### 2. Attributes and Methods (API Members)

Based on the official Autodesk Flame 2026 API documentation structure, the `PyMediaPanel` class does not publicly expose a dedicated list of unique attributes or methods directly on the class itself in the manner that data objects like `PyBatch` or `PyClip` do.

It appears to serve primarily as a **root utility container** whose functionality is often channeled through related objects or global functions.

| Member Type | Member Name | Availability | Description |
| :--- | :--- | :--- | :--- |
| **Methods** | `__init__`, `__reduce__` | Static (Internal) | Standard Python class setup methods, which cannot be instantiated or called directly. |
| **Attributes** | None Explicit | N/A | No unique, publicly documented attributes (like `selected_item` or `current_tab`) are listed directly under the `PyMediaPanel` definition. |

**Note on Functionality:**
While the `PyMediaPanel` object exists, its core tasks—such as importing media, managing file paths, and changing media views—are generally handled by the related `PyMediaHub` class and its components (e.g., `PyMediaHubFilesTab`).

For most scripting purposes, you will interact with the following related objects:

* **`flame.media_hub`**: For controlling imports, browsing file paths, and setting import options.
* **`PyArchiveEntry` subclasses** (like `PyClip`, `PyFolder`, `PyProject`): These are the actual objects *within* the Media Panel that you manipulate.

**Example:**

```python
# Move selected entries into a destination folder
selected = flame.media_panel.selected_entries
destination = flame.desktop.get_item('RENDERS')
if selected and destination:
    flame.media_panel.move(selected, destination)
```

## Methods
### Properties
- `selected_entries(...)` — None( (flame.PyMediaPanel)arg1) -> object 
None( (flame.PyMediaPanel)arg1) -> object

- `visible(...)` — None( (flame.PyMediaPanel)arg1) -> bool 
None( (flame.PyMediaPanel)arg1) -> bool

- `full_height(...)` — None( (flame.PyMediaPanel)arg1) -> bool 
None( (flame.PyMediaPanel)arg1) -> bool

- `full_width(...)` — None( (flame.PyMediaPanel)arg1) -> bool 
None( (flame.PyMediaPanel)arg1) -> bool

- `dual(...)` — None( (flame.PyMediaPanel)arg1) -> bool 
None( (flame.PyMediaPanel)arg1) -> bool


### Built-in methods
- `move(...)` — move( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object : 
move( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object :
    Move a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.
    Return a list of the moved PyObjects.
    Keyword arguments:
    source_entries -- The PyObject or list of PyObjects to move.
    destination -- The PyObject that acts as destination.
    duplicate_action -- Action to take when finding an object with the same name (add or replace).

- `copy(...)` — copy( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object : 
copy( (PyMediaPanel)arg1, (object)source_entries, (object)destination [, (str)duplicate_action='add']) -> object :
    Copy a PyObject or a list of PyObjects from the Media Panel to a destination inside the Media Panel.Return a list of the copied PyObjects.Keyword arguments:
    source_entries -- The PyObject or list of PyObjects to copy.
    destination -- The PyObject that acts as destination.
    duplicate_action -- Action to take when finding an object with the same name (add or replace).


