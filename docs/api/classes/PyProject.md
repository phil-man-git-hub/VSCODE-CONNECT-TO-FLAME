

# Class: PyProject

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyArchiveEntry (inherits from PyFlameObject)
* **Contains:** PyWorkspace, PyLibrary, PyDesktop

## Functional Role & Context
* **Functional Role:** Represents the entire active project in Flame, serving as the root organizational object for all media, sequences, and settings.
* **Context:** Used for project-level automation, management, and access to all major project components.

## Description
The PyProject class provides programmatic access to the Flame project, enabling automation of project-wide operations, workspace/library/desktop management, and access to project metadata and folders.


## Key Attributes
| Attribute                | Type   | Description                                      |
|--------------------------|--------|--------------------------------------------------|
| name                     | str    | The name of the project.                         |
| nickname                 | str    | The nickname of the project.                     |
| description              | str    | The description of the project.                  |
| project_name             | str    | The project name.                                |
| shotgrid_project_name    | str    | Name of the linked Flow Production Tracking project. |
| working_colour_space     | str    | The working colour space of the Project.         |
| action_colour_space      | str    | The colour space used to render in Action.       |
| workspaces_count         | int    | Number of workspaces in the project.             |
| current_workspace        | object | The current workspace object.                    |
| shared_libraries         | list   | List of shared libraries in the project.         |
| project_folder           | str    | Path to the project folder.                      |
| setups_folder            | str    | Path to the setups folder.                       |
| media_folder             | str    | Path to the media folder.                        |

## Attributes (Authoritative)
| Attribute                | Type   | Description                                      |
|--------------------------|--------|--------------------------------------------------|
| shotgrid_project_name    | str    | The name of the linked Flow Production Tracking project. |
| working_colour_space     | str    | The working colour space of the Project.         |
| action_colour_space      | str    | The colour space used to render in Action.       |



## Methods
### Properties
- `name(...)` — None( (flame.PyProject)arg1) -> str 
None( (flame.PyProject)arg1) -> str

- `nickname(...)` — None( (flame.PyProject)arg1) -> str 
None( (flame.PyProject)arg1) -> str

- `description(...)` — None( (flame.PyProject)arg1) -> str 
None( (flame.PyProject)arg1) -> str

- `project_name(...)` — None( (flame.PyProject)arg1) -> str 
None( (flame.PyProject)arg1) -> str

- `workspaces_count(...)` — None( (flame.PyProject)arg1) -> int 
None( (flame.PyProject)arg1) -> int

- `current_workspace(...)` — None( (flame.PyProject)arg1) -> object 
None( (flame.PyProject)arg1) -> object

- `shared_libraries(...)` — None( (flame.PyProject)arg1) -> list 
None( (flame.PyProject)arg1) -> list

- `project_folder(...)` — None( (flame.PyProject)arg1) -> str 
None( (flame.PyProject)arg1) -> str

- `setups_folder(...)` — None( (flame.PyProject)arg1) -> str 
None( (flame.PyProject)arg1) -> str

- `media_folder(...)` — None( (flame.PyProject)arg1) -> str 
None( (flame.PyProject)arg1) -> str


### Built-in methods
- `create_shared_library(...)` — create_shared_library( (PyProject)arg1, (str)name) -> object : 
create_shared_library( (PyProject)arg1, (str)name) -> object :
    Create a new Shared Library in the Project.

- `refresh_shared_libraries(...)` — refresh_shared_libraries( (PyProject)arg1) -> bool : 
refresh_shared_libraries( (PyProject)arg1) -> bool :
    Refresh the Shared Libraries list in the Media Panel.

- `reload_ocio_config(...)` — reload_ocio_config( (PyProject)arg1 [, (bool)reset_colour_policy=False]) -> bool : 
reload_ocio_config( (PyProject)arg1 [, (bool)reset_colour_policy=False]) -> bool :
    Reload the OCIO config file.
    Keyword argument:
    reset_colour_policy -- Delete the project's custom colour spaces, roles, and rules (false by default).

- `export_ocio_config(...)` — export_ocio_config( (PyProject)arg1, (str)config_name [, (str)destination_folder='' [, (bool)overwrite_existing=False [, (bool)export_as_locked=False [, (bool)generate_ocioz=False]]]]) -> bool : 
export_ocio_config( (PyProject)arg1, (str)config_name [, (str)destination_folder='' [, (bool)overwrite_existing=False [, (bool)export_as_locked=False [, (bool)generate_ocioz=False]]]]) -> bool :
    Export the OCIO config file.
    Keyword arguments:
    config_name -- Specifies the name that will be written inside the exported OCIO config and used as the parent folder name where the config will be exported. It should not contain the '.ocio' extension. Mandatory.
    destination_folder -- Specifies the absolute destination folder for the exported OCIO config. It will use the default colour management shared path if empty.
    overwrite_existing -- Specifies if the export should overwrite an existing OCIO config with the same name located in the same destination_folder.
    export_as_locked -- Specifies if the exported OCIO config should be locked (the 'LockedPolicy' parameter inside the settings.cfg sidecar file).
    generate_ocioz -- Specifies if an OCIOZ archive should be created alongside the exported OCIO config.

- `set_context_variable(...)` — set_context_variable( (PyProject)arg1, (str)name, (str)value) -> None : 
set_context_variable( (PyProject)arg1, (str)name, (str)value) -> None :
    Set the value for the specified context variable.

- `get_context_variables(...)` — get_context_variables( (PyProject)arg1) -> dict : 
get_context_variables( (PyProject)arg1) -> dict :
    Get the context variables in a dictionary.

- `reset_context_variables(...)` — reset_context_variables( (PyProject)arg1) -> None : 
reset_context_variables( (PyProject)arg1) -> None :
    Reset the context variables to their initial state from the ocio config.

## API Insight
### Autodesk Flame API Insight (2026)

`PyProject` is the root object used for project-wide automation and configuration. It centralises control of OCIO, workspaces, shared libraries, and project folders. When automating project operations consider these practical guidelines:

- `export_ocio_config(config_name, destination_folder='', overwrite_existing=False, export_as_locked=False, generate_ocioz=False)` — Use `overwrite_existing=True` and `export_as_locked=True` when publishing to shared locations; `generate_ocioz=True` packages the config for distribution.
- `reload_ocio_config(reset_colour_policy=False)` — Reload the in-memory OCIO configuration. Pass `reset_colour_policy=True` to clear custom colour policies and restore defaults when necessary.
- `set_context_variable(name, value)` / `get_context_variables()` — Use these for lightweight, session-scoped flags for automation scripts; they are not a substitute for persistent configuration.
- `create_shared_library(name)` + `refresh_shared_libraries()` — Newly created shared libraries may require a refresh before they appear in the Media Panel.
- `delete([confirm=True])` — Deleting the project (or other top-level containers) is destructive; require explicit confirmation in automation.

**Example: Export the OCIO configuration and refresh libraries**

```python
p = flame.project
ok = p.export_ocio_config('Company_OCIO_v2', destination_folder='/mnt/shared/ocio', overwrite_existing=True, export_as_locked=True, generate_ocioz=True)
if ok:
    p.refresh_shared_libraries()
```

> **Safety note:** Always test configuration changes in a non-production workspace or with a project backup before applying them globally. Use caution with `delete()` or any destructive operations.


