
# Class: PyArchiveEntry

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyFlameObject`
* **Functional Role:** Base class for any object displayed in the Media Panel (e.g., Project, Library, Folder, Reel, Clip, Sequence, etc.)

## Description
Represents the base class for all major organizational and media container objects in the Flame Media Panel.


## API Insight: Definition, Attributes, and Methods
The **PyArchiveEntry** class is foundational in the Autodesk Flame Python API, acting as the central base for all scriptable objects managed in the Flame database and shown in the Media Panel.

### Definition and Inheritance
| Property      | Value         | Description |
|-------------- |-------------- |-------------|
| Class Name    | PyArchiveEntry| Base class for archival elements. |
| Parent Class  | PyFlameObject | Inherits core API access methods. |
| Primary Role  | Media Panel Foundation | Defines the structural layer for all organizational containers and media assets. |

### Core Properties (Attributes)
| Attribute   | Type   | Access     | Description |
|------------ |--------|----------- |-------------|
| id          | str    | Read-only  | Unique database identifier for the archive entry. |
| name        | str    | Read/Write | Display name in the Media Panel. |
| colour      | tuple  | Read/Write | Colour assigned for labelling. |
| modified    | datetime | Read-only | Last modified timestamp. |
| archived    | bool   | Read/Write | Archive status. |
| online      | bool   | Read-only  | Media availability status. |

### Key Methods (Functionality)
| Method                | Returns         | Description |
|-----------------------|----------------|-------------|
| delete([confirm=True])| bool           | Deletes the archive entry, optionally with confirmation. |
| duplicate()           | PyArchiveEntry | Creates a copy of the archive entry. |
| move(destination)     | bool           | Moves the archive entry to a new container. |
| reveal_in_ui()        | bool           | Selects and displays the object in the UI. |
| get_children()        | list           | Retrieves immediate children of the entry. |

### Hierarchical Significance (Derived Classes)
Many powerful objects inherit from PyArchiveEntry, making them manageable by the methods above:
| Category           | Derived Classes (Examples) |
|--------------------|---------------------------|
| Project Structure  | PyProject, PyWorkspace, PyDesktop, PyLibrary |
| Organization       | PyFolder, PyReelGroup, PyReel |
| Media Assets       | PyClip, PySequence |

### Example
```python
# Example: Reveal an archive entry and duplicate it
entry = flame.project.desktop.get_children()[0]
entry.reveal_in_ui()
copy = entry.duplicate()
print('Duplicated:', copy.name)
```

## Methods
### Built-in methods
- `delete(...)` — delete( (PyArchiveEntry)arg1 [, (bool)confirm=True]) -> bool : 
delete( (PyArchiveEntry)arg1 [, (bool)confirm=True]) -> bool :
    Delete the archive entry. If `confirm` is True (default) a UI confirmation will be shown.

- `duplicate(...)` — duplicate( (PyArchiveEntry)arg1) -> object : 
duplicate( (PyArchiveEntry)arg1) -> object :
    Create and return a duplicate copy of the archive entry.

- `move(...)` — move( (PyArchiveEntry)arg1, (PyArchiveEntry)destination) -> bool : 
move( (PyArchiveEntry)arg1, (PyArchiveEntry)destination) -> bool :
    Move the archive entry to the specified destination container.

- `reveal_in_ui(...)` — reveal_in_ui( (PyArchiveEntry)arg1) -> bool : 
reveal_in_ui( (PyArchiveEntry)arg1) -> bool :
    Select and display this object in the Flame Media Panel UI.

- `get_children(...)` — get_children( (PyArchiveEntry)arg1) -> list : 
get_children( (PyArchiveEntry)arg1) -> list :
    Return a list of immediate children contained by this archive entry.

- `get_wiretap_storage_id(...)` — get_wiretap_storage_id( (PyArchiveEntry)arg1) -> str : 
get_wiretap_storage_id( (PyArchiveEntry)arg1) -> str :
    Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.

- `get_wiretap_node_id(...)` — get_wiretap_node_id( (PyArchiveEntry)arg1) -> str : 
get_wiretap_node_id( (PyArchiveEntry)arg1) -> str :
    Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.

- `commit(...)` — commit( (PyArchiveEntry)arg1) -> None : 
commit( (PyArchiveEntry)arg1) -> None :
    Commit to disk the Media Panel object or its closest container possible.

- `clear_colour(...)` — clear_colour( (PyArchiveEntry)arg1) -> None : 
clear_colour( (PyArchiveEntry)arg1) -> None :
    Clear the colour of an object in the Media Panel.


