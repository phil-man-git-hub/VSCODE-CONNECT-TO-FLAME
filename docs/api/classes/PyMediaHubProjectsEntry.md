
# Class: PyMediaHubProjectsEntry

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Represents a clip entry in the MediaHub Projects tab.

## Description
Provides access to clip entries in the MediaHub Projects tab, including UID and file path.

---

## API Insight
### Autodesk Flame API Insight (2026)

The **`PyMediaHubProjectsEntry`** class represents an existing **clip, sequence, or other media item** as it is displayed when browsing the **Projects tab** within the MediaHub. This object allows Python scripts to identify and interact with media that is already part of a Flame project, library, or archive for operations like copying, linking, or consolidating.

-----

#### 1. Definition and Hierarchy

| Property | Value | Description |
| :--- | :--- | :--- |
| **Class Name** | `PyMediaHubProjectsEntry` | Represents a **clip or media object** displayed in the MediaHub **Projects tab**. |
| **Parent Class** | **`PyArchiveEntry`** | Inherits general methods for archive management and Wiretap identification. |
| **Ancestor Class** | **`PyFlameObject`** | Inherits base object properties (`attributes`, `parent`). |
| **Primary Role** | **Project Media Identification** | Provides persistent and hierarchical identification of media items *within* the Flame ecosystem. |

-----

#### 2. Unique Attributes (Properties)

This class provides two key read-only properties crucial for identifying the clip within the Flame environment:

| Attribute | Type | Access | Description |
| :--- | :--- | :--- | :--- |
| **`path`** | `str` | Read-only | Returns the **hierarchical path** of the clip, representing its location within the Flame project structure (e.g., `Desktop/Shots/V010_Comp_Reel/Shot_A010`). |
| **`uid`** | `str` | Read-only | Returns the **Unique ID** (UID) of the clip, a persistent, database-level identifier for the media object. |

-----

#### 3. Inherited Methods (From `PyArchiveEntry`)

Since `PyMediaHubProjectsEntry` derives from `PyArchiveEntry`, it includes standard methods for managing library elements:

| Method | Arguments | Description |
| :--- | :--- | :--- |
| **`clear_colour()`** | None | Clears any custom **color tag** set on the object in the Media Panel. |
| **`commit()`** | None | Attempts to **commit** the object or its closest container to disk, ensuring metadata changes are saved. |
| **`get_wiretap_node_id()`** | None | Returns the **Wiretap Node ID** of the Flame object. |
| **`get_wiretap_storage_id()`**| None | Returns the Wiretap server's **storage ID** for the Flame object. |

-----

#### 4. Usage Context

This object is used when a script needs to browse and select existing clips from other projects or archived media for actions like importing, linking, or batch copying into the currently open project.

```python
import flame

# Example: Selecting a clip from an external project via the MediaHub Projects tab

# 1. Set the MediaHub Projects tab path to the location of the clip
clip_path = 'External_Project/Reels/Comp_Finals/shot_100_v01'
flame.media_hub.projects_tab.set_path(clip_path)

# 2. List the entries at that path
entries = flame.media_hub.list_entries(clip_path)

# 3. Find a clip entry by UID or path
clip_entry = next((e for e in entries if isinstance(e, flame.PyMediaHubProjectsEntry) and 'shot_100' in e.path), None)
if clip_entry:
    print('Found clip:', clip_entry.uid)
```


## Methods
### Properties
- `uid(...)` — None( (flame.PyMediaHubProjectsEntry)arg1) -> str 
None( (flame.PyMediaHubProjectsEntry)arg1) -> str

- `path(...)` — None( (flame.PyMediaHubProjectsEntry)arg1) -> str 
None( (flame.PyMediaHubProjectsEntry)arg1) -> str


