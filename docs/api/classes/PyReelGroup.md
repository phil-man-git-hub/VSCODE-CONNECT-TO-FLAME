
# Class: PyReelGroup

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyFlameObject
* **Contains:** PyReel

## Functional Role & Context
* **Functional Role:** Represents a Reel Group, providing access to reels and group management operations.
* **Context:** Used for organizing, creating, and managing reels in the Flame environment.

## Description
The PyReelGroup class provides programmatic access to reel groups, supporting automation of reel management and organization in libraries and folders.


Object representing a Reel Group.

## API Insight
### Autodesk Flame API Insight (2026)

A `PyReelGroup` is the version container for a single asset — it holds multiple `PyReel` objects (versions). Use it to create new versions, list existing ones, and perform group-level operations.

**Key methods:** `create_reel(name)`, `save()`, `get_children()` (lists reels), and inherited archive methods like `delete()` and `move()`.

**Example:**

```python
# Create a reel group and add versions
shot_group = my_folder.create_reel_group('SH_010_050')
v001 = shot_group.create_reel('V001')
v002 = shot_group.create_reel('V002')
print([r.name for r in shot_group.reels])
```

## Attributes
| Attribute   | Type   | Description |
|-------------|--------|-------------|
| name        | str    | The name of an object in the Media Panel, resolving tokens if any are present. |
| uid         | str    | The unique identifier of an object in the Media Panel. |
| token_name  | str    | The tokenized name of an object in the Media Panel. |
| expanded    | bool   | The expanded state of an object in the Media Panel. True or False. |
| colour      | tuple  | The colour of an object in the Media Panel. |

## Methods
### Properties
- `children(...)` — None( (flame.PyReelGroup)arg1) -> list 
None( (flame.PyReelGroup)arg1) -> list

- `reels(...)` — None( (flame.PyReelGroup)arg1) -> list 
None( (flame.PyReelGroup)arg1) -> list


### Built-in methods
- `clear(...)` — clear( (PyReelGroup)arg1 [, (bool)confirm=True]) -> bool : 
clear( (PyReelGroup)arg1 [, (bool)confirm=True]) -> bool :
    Clear the Reel Group content.

- `create_reel(...)` — create_reel( (PyReelGroup)arg1, (str)name [, (bool)sequence=False]) -> object : 
create_reel( (PyReelGroup)arg1, (str)name [, (bool)sequence=False]) -> object :
    Create a new Reel inside a Reel Group.

- `save(...)` — save( (PyReelGroup)arg1) -> bool : 
save( (PyReelGroup)arg1) -> bool :
    Save the Reel Group to the defined save destination.


