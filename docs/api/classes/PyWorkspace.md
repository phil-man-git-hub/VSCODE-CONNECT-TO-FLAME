# Class: PyWorkspace

**Module**: `flame`

**Inherits from**: [PyArchiveEntry](PyArchiveEntry.md), [PyFlameObject](PyFlameObject.md), instance, object

## Description
Object representing a Workspace.


## Properties
| Name | Description |
| --- | --- |
| `attributes` | The attributes of a python object. |
| `desktop` | Return the current Desktop. |
| `libraries` | Return the Workspace Libraries. |
| `parent` | The parent object of this object. |


## Methods
### `clear_colour`
```python
clear_colour
```


clear_colour( (PyArchiveEntry)arg1) -> None :

    Clear the colour of an object in the Media Panel.

---

### `commit`
```python
commit
```


commit( (PyArchiveEntry)arg1) -> None :

    Commit to disk the Media Panel object or its closest container possible.

---

### `create_library`
```python
create_library
```


create_library( (PyWorkspace)arg1, (str)name) -> object :

    Create a new Library in a Workspace.

---

### `get_wiretap_node_id`
```python
get_wiretap_node_id
```


get_wiretap_node_id( (PyArchiveEntry)arg1) -> str :

    Return the Wiretap Node ID of the Flame object, but only if the object is in the Media Panel.

---

### `get_wiretap_storage_id`
```python
get_wiretap_storage_id
```


get_wiretap_storage_id( (PyArchiveEntry)arg1) -> str :

    Return the Wiretap server's storage ID for the Flame object, but only if the object is in the Media Panel.

---

### `replace_desktop`
```python
replace_desktop
```


replace_desktop( (PyWorkspace)arg1, (PyDesktop)desktop) -> bool :

    Replace the Workspace active Desktop with another one.

---

### `set_desktop_reels`
```python
set_desktop_reels
```


set_desktop_reels( (PyWorkspace)arg1 [, (object)group=None]) -> bool :

    Set the Desktop Reels view mode.

---

### `set_freeform`
```python
set_freeform
```


set_freeform( (PyWorkspace)arg1 [, (object)reel=None]) -> bool :

    Set the Freeform view mode.

---
