
# Class: PyMediaHubFilesTab

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Represents the MediaHub Files tab, providing access to file browsing and import options.

## Description
Provides access to the MediaHub Files tab UI, including options and file/folder navigation.

---

## API Insight
### Autodesk Flame API Insight (2026)

The **`PyMediaHubFilesTab`** class represents the "Files" tab within the Autodesk Flame MediaHub interface. It inherits basic path management capabilities from its parent class, `PyMediaHubTab`, but its unique role is to act as the gateway to the highly detailed **import options** that govern how external media is ingested into the Flame project.

This object is accessed directly via the `PyMediaHub` instance, typically as `flame.media_hub.files_tab`.

-----

#### 1. Definition and Hierarchy

| Property | Value | Description |
| :--- | :--- | :--- |
| **Class Name** | `PyMediaHubFilesTab` | This class represents the **MediaHub Files tab**. |
| **Parent Class** | **`PyMediaHubTab`** | Inherits methods for navigating file paths (`get_path`, `set_path`). |
| **Primary Role** | **Bridging Path & Options** | Connects the browsed file system location (from parent class methods) to the import configuration (via its unique `options` attribute). |
| **Access** | **Via `PyMediaHub`** | E.g., `flame.media_hub.files_tab`. |

-----

#### 2. Unique Attributes (Properties)

The `PyMediaHubFilesTab` object has one crucial, unique attribute that links it to the import settings panel:

| Attribute | Type | Access | Description |
| :--- | :--- | :--- | :--- |
| **`options`** | **`PyMediaHubFilesTabOptions`** | Read-only | Provides access to all the granular import settings (resolution, frame rate, bit depth, color space, etc.) required before media can be imported into a project. |

-----

#### 3. Inherited Methods (Path Management)

As a child of `PyMediaHubTab`, it inherits the methods necessary for navigating the external file system:

| Method | Arguments | Return Type | Description |
| :--- | :--- | :--- | :--- |
| **`get_path()`** | None | `str` | Returns the **current file system path** displayed in the Files tab. |
| **`set_path(path, allow_partial_success=False)`**| `path` (`str`), `allow_partial_success` (`bool`, optional) | `bool` | **Navigates the Files tab** to the specified absolute path. If `allow_partial_success` is `True`, it navigates to the deepest valid folder if the full path fails. |

-----

#### 4. Usage Context

To perform a complete media import via the Python API, you must interact with both the `PyMediaHubFilesTab` (to access its `options`) and the top-level `PyMediaHub` object (to execute the actual import):

```python
import flame

# Access the Files Tab object
files_tab = flame.media_hub.files_tab

# 1. Set the working directory for the MediaHub (Inherited method)
files_tab.set_path('/mnt/server/assets/renders/v001')

# 2. Configure the Import Options (Unique Attribute access)
import_options = files_tab.options
import_options.resolution = 'Project Res'
import_options.set_tagged_colour_space('Rec.709')

# 3. Execute the import (Method on PyMediaHub)
files_to_import = ['/mnt/server/assets/renders/v001/shot01_v001.exr']
flame.media_hub.import_media(files_to_import, flame.project.reels[0])
```


## Methods
### Properties
- `options(...)` — None( (flame.PyMediaHubFilesTab)arg1) -> flame.PyMediaHubFilesTabOptions 
None( (flame.PyMediaHubFilesTab)arg1) -> flame.PyMediaHubFilesTabOptions


