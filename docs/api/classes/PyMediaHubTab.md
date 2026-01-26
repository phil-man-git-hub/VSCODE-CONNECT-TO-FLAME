
# Class: PyMediaHubTab

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Base class for MediaHub tabs, providing navigation and path management.

## Description
Provides access to MediaHub tab UI, including path navigation and management.

---

## API Insight
### Autodesk Flame API Insight (2026)

The **`PyMediaHubTab`** class serves as the base class for all tab objects within the MediaHub interface. Its primary role is to provide common functionality for navigating the various locations (file system paths, project folders, etc.) browsed by a MediaHub tab.

#### Key Methods
| Method | Arguments | Return Type | Description |
| :--- | :--- | :--- | :--- |
| `get_path()` | None | `str` | Returns the current path being browsed by the tab. |
| `set_path(path, allow_partial_success=False)` | `str`, `bool` | `bool` | Set the tab's path. When `allow_partial_success=True`, the method will navigate to the deepest valid parent folder if the full path is invalid.

**Example:**

```python
# Navigate the Files tab and gracefully fall back to the nearest valid folder
files_tab = flame.media_hub.files_tab
if not files_tab.set_path('/mnt/nonexistent/deep/path'):
    files_tab.set_path('/mnt/nonexistent/deep', allow_partial_success=True)
print('Current MediaHub path:', files_tab.get_path())
```


## Methods
### Built-in methods
- `get_path(...)` — get_path( (PyMediaHubTab)arg1) -> str : 
get_path( (PyMediaHubTab)arg1) -> str :
    Return the MediaHub tab current path.

- `set_path(...)` — set_path( (PyMediaHubTab)arg1, (str)arg2 [, (bool)allow_partial_success=False]) -> bool : 
set_path( (PyMediaHubTab)arg1, (str)arg2 [, (bool)allow_partial_success=False]) -> bool :
    Set the MediaHub tab current path. If allow_partial_success is True, the path will be set to the last valid folder in the path.


