
# Class: PyMediaHubProjectsFolder

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Represents a folder entry in the MediaHub Projects tab.

## Description
Provides access to folder entries in the MediaHub Projects tab, including UID and file path.

---

## API Insight
### Autodesk Flame API Insight (2026)

The **`PyMediaHubProjectsFolder`** class represents a **folder** when browsing the **Projects tab** within the MediaHub interface. This object is used to interact with Flame's internal project and library structure, unlike the `PyMediaHubFilesFolder` which deals with the external file system.

It acts as a placeholder for a container object (like a reel group, library, or actual folder) within a Flame project hierarchy visible in the MediaHub's Projects view.

-----

#### 1. Definition and Hierarchy

| Property | Value | Description |
| :--- | :--- | :--- |
| **Class Name** | `PyMediaHubProjectsFolder` | Represents a **folder** displayed in the MediaHub **Projects tab**. |
| **Parent Class** | **`PyArchiveEntry`** | Inherits general archive and Wiretap management methods. |
| **Ancestor Class** | **`PyFlameObject`** | Inherits base object properties (`attributes`, `parent`). |
| **Primary Role** | **Internal Project Navigation** | Provides identification and location within the Flame project/library structure. |

-----

#### 2. Unique Attributes (Properties)

This class provides two key read-only properties for identifying the folder within the Flame environment:

| Attribute | Type | Access | Description |
| :--- | :--- | :--- | :--- |
| **`path`** | `str` | Read-only | Returns the **path** of the folder, typically the hierarchical name within the project structure (e.g., `Desktop/My_Project_Folder`). |
| **`uid`** | `str` | Read-only | Returns the **Unique ID** of the folder, a persistent identifier for the object within the project's database. |

-----

#### 3. Inherited Methods (From `PyArchiveEntry`)

Since `PyMediaHubProjectsFolder` derives from `PyArchiveEntry`, it inherits standard methods for managing library elements:

| Method | Arguments | Description |
| :--- | :--- | :--- |
| **`clear_colour()`** | None | Clears any custom **color tag** set on the object in the Media Panel. |
| **`commit()`** | None | Attempts to **commit** the object or its closest container to disk (used for ensuring metadata changes are saved). |
| **`get_wiretap_node_id()`** | None | Returns the **Wiretap Node ID** of the Flame object. Only returns a value if the object exists in the Media Panel. |
| **`get_wiretap_storage_id()`**| None | Returns the Wiretap server's **storage ID** for the Flame object. Only returns a value if the object exists in the Media Panel. |

-----

#### 4. Usage Context

This object is primarily used to browse or retrieve items already present in other Flame projects or libraries for potential copying or linking:

```python
import flame

# Access the Projects Tab (which implicitly starts at the root, showing all projects)
projects_tab = flame.media_hub.projects_tab

# List the top-level entries (other projects and libraries)
entries = flame.media_hub.list_entries(projects_tab.get_path())

# Search for a specific external project folder
external_project_folder = next((e for e in entries if isinstance(e, flame.PyMediaHubProjectsFolder) and 'Client_Project_A' in e.path), None)
if external_project_folder:
    print('Found external project folder:', external_project_folder.path)
```


## Methods
### Properties
- `uid(...)` — None( (flame.PyMediaHubProjectsFolder)arg1) -> str 
None( (flame.PyMediaHubProjectsFolder)arg1) -> str

- `path(...)` — None( (flame.PyMediaHubProjectsFolder)arg1) -> str 
None( (flame.PyMediaHubProjectsFolder)arg1) -> str


