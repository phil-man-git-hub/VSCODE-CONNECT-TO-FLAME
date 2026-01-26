
# Class: PyMediaHubFilesTabOptions

**Module**: `flame`

## Functional Role & Context
* **Functional Role:** Represents the options/settings for the MediaHub Files tab.

## Description
Provides access to the options and settings for the MediaHub Files tab, including import, cache, and color management options.



## Methods
- `multi_channel_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `sequence_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `cache_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `proxies_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `cache_and_proxies_all_versions(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool
- `resize_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `resize_filter(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `resolution(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `width(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `height(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `scaling_presets_value(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `frame_ratio(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `bit_depth(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
- `scan_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str
- `pixel_ratio(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> object 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> object
## API Insight
### Autodesk Flame API Insight (2026)

The **`PyMediaHubFilesTabOptions`** class is a crucial utility object in the Autodesk Flame Python API (2026). It represents and provides programmatic access to the entire set of **import options** found in the MediaHub's Files tab. By manipulating the attributes of this object, a script can define exactly how media files are interpreted and imported into the project environment, covering everything from frame rate and resolution to bit depth and color space.

This object is accessed through the `options` attribute of the `PyMediaHubFilesTab` class (e.g., `flame.media_hub.files_tab.options`).

-----

#### 1. Definition and Hierarchy

| Property | Value | Description |
| :--- | :--- | :--- |
| **Class Name** | `PyMediaHubFilesTabOptions` | Represents the **MediaHub Files tab import settings**. |
| **Parent Class** | None explicit (Utility Class) | A settings container object. |
| **Access** | **Via `PyMediaHubFilesTab`** | Accessed as a data descriptor attribute named `options`. |
| **Primary Role** | **Configuration** | Defines all technical parameters for media clips upon import (e.g., color, resolution, timing). |

-----

#### 2. Attributes (Import Configuration Properties)

These are data descriptors that allow you to get or set the various import options. The values must correspond to the options available in the Flame UI's MediaHub.

| Attribute | Type | Read/Write | Description & Possible Values |
| :--- | :--- | :--- | :--- |
| **`bit_depth`** | `str` | Read/Write | Sets the import **bit depth**. Possible values include: `"8"`, `"10"`, `"12"`, `"16"`, `"32"`, and `"From Source"`. |
| **`cache_and_proxies_all_versions`** | `bool` | Read/Write | If `True`, cache and proxies are generated for **all versions** upon import, instead of just the current version. |
| **`cache_mode`** | `str` | Read/Write | Sets the **caching mode** for media on import (e.g., "Always Cache", "Never Cache"). |
| **`frame_ratio`** | `float` | Read/Write | Sets the **frame ratio** value for import, but only when the `resolution` mode is set to **Resolution List**. |
| **`height`** | `int` | Read/Write | Sets the clip **height** for import. Returns `None` when `resolution` is set to `"Same as Source"`, `"Scaling Presets"`, or `"Adaptive"` (if based on width). |
| **`multi_channel_mode`**| `str` | Read/Write | Sets the **Multi-Channel Mode** to use upon import. |
| **`pixel_ratio`** | `float` | Read/Write | Sets the **pixel ratio** value for import. Returns `None` when `resolution` is set to `"Same As Source"`. |
| **`proxies_mode`** | `str` | Read/Write | Controls if and how **proxies** are generated on import. |
| **`resize_filter`** | `str` | Read/Write | Sets the **resizing filter** to use. Possible values include: `"Lanczos"`, `"Shannon"`, `"Gaussian"`, `"Quadratic"`, `"Bicubic"`, `"Mitchell"`, `"Triangle"`, and `"Impulse"`. |
| **`resize_mode`** | `str` | Read/Write | Sets the **resizing mode**. Possible values include: `"Letterbox"`, `"Crop Edges"`, `"Fill"`, and `"Centre"`. |
| **`resolution`** | `str` | Read/Write | Sets the overall resolution policy. Possible values include: `"Custom Resolution"`, `"Project Res"`, `"Adaptive"`, `"Scaling Presets"`, `"Same as Source"`, or a specific resolution string like `"HD 720 16:9 (1280 x 720)"`. |
| **`scaling_presets_value`**| `str` | Read/Write | Sets the **scaling preset value**, but only when the `resolution` selector is set to `"Scaling Presets"`. |
| **`scan_mode`** | `str` | Read/Write | Sets the **scan mode** (interlaced or progressive). Possible values include: `"P"` (Progressive), `"F1"`, `"F2"` (Field 1 or 2), and `"From Source"`. |
| **`sequence_mode`** | `bool` | Read/Write | If `True`, forces the use of **sequence mode** to import a range of files (e.g., `clip.0001.exr` to `clip.0100.exr`). |
| **`width`** | `int` | Read/Write | Sets the clip **width** for import. Returns `None` when `resolution` is set to `"Same as Source"`, `"Scaling Presets"`, or `"Adaptive"` (if based on height). |

-----

#### 3. Key Methods

| Method | Arguments | Description |
| :--- | :--- | :--- |
| **`set_tagged_colour_space(colour_space)`** | `colour_space` (`str`) | Sets the **tagged color space** that the imported media is assumed to be in, overriding any metadata in the file itself. |

-----

#### 4. Usage Example

To ensure an import is processed correctly, you first configure the options object and then call the `import_media` method on the parent `PyMediaHub` object:

```python
import flame

# 1. Get the options object
options = flame.media_hub.files_tab.options
# 2. Configure options
options.resolution = 'Project Res'
options.bit_depth = 'From Source'
# 3. Use MediaHub to import files after configuration
files = ['/mnt/assets/shot01_v01.exr']
flame.media_hub.import_media(files, flame.project.reels[0])
```
- `colour_mgmt_mode(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str

- `colour_mgmt_view(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str

- `tagged_colour_space(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str

- `colour_mgmt_display(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str

- `colour_mgmt_working_space(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> str 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> str

- `colour_mgmt_invert(...)` — None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool 
None( (flame.PyMediaHubFilesTabOptions)arg1) -> bool


### Built-in methods
- `import_transform(...)` — import_transform( (PyMediaHubFilesTabOptions)arg1, (str)file_path) -> None : 
import_transform( (PyMediaHubFilesTabOptions)arg1, (str)file_path) -> None :
    Import a transform from a file.

- `set_tagged_colour_space(...)` — set_tagged_colour_space( (PyMediaHubFilesTabOptions)arg1, (str)colour_space) -> None : 
set_tagged_colour_space( (PyMediaHubFilesTabOptions)arg1, (str)colour_space) -> None :
    Set the tagged colour space to use upon import.


