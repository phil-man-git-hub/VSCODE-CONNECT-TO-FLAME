# Class: PyProject

**Module**: `flame`

Object representing a Project.

## Methods
### `name(...)`

None( (flame.PyProject)arg1) -> str

### `nickname(...)`

None( (flame.PyProject)arg1) -> str

### `description(...)`

None( (flame.PyProject)arg1) -> str

### `project_name(...)`

None( (flame.PyProject)arg1) -> str

### `workspaces_count(...)`

None( (flame.PyProject)arg1) -> int

### `current_workspace(...)`

None( (flame.PyProject)arg1) -> object

### `shared_libraries(...)`

None( (flame.PyProject)arg1) -> list

### `project_folder(...)`

None( (flame.PyProject)arg1) -> str

### `setups_folder(...)`

None( (flame.PyProject)arg1) -> str

### `media_folder(...)`

None( (flame.PyProject)arg1) -> str

### `create_shared_library(...)`

create_shared_library( (PyProject)arg1, (str)name) -> object :
    Create a new Shared Library in the Project.

### `refresh_shared_libraries(...)`

refresh_shared_libraries( (PyProject)arg1) -> bool :
    Refresh the Shared Libraries list in the Media Panel.

### `reload_ocio_config(...)`

reload_ocio_config( (PyProject)arg1 [, (bool)reset_colour_policy=False]) -> bool :
    Reload the OCIO config file.
    Keyword argument:
    reset_colour_policy -- Delete the project's custom colour spaces, roles, and rules (false by default).

### `export_ocio_config(...)`

export_ocio_config( (PyProject)arg1, (str)config_name [, (str)destination_folder='' [, (bool)overwrite_existing=False [, (bool)export_as_locked=False [, (bool)generate_ocioz=False]]]]) -> bool :
    Export the OCIO config file.
    Keyword arguments:
    config_name -- Specifies the name that will be written inside the exported OCIO config and used as the parent folder name where the config will be exported. It should not contain the '.ocio' extension. Mandatory.
    destination_folder -- Specifies the absolute destination folder for the exported OCIO config. It will use the default colour management shared path if empty.
    overwrite_existing -- Specifies if the export should overwrite an existing OCIO config with the same name located in the same destination_folder.
    export_as_locked -- Specifies if the exported OCIO config should be locked (the 'LockedPolicy' parameter inside the settings.cfg sidecar file).
    generate_ocioz -- Specifies if an OCIOZ archive should be created alongside the exported OCIO config.

### `set_context_variable(...)`

set_context_variable( (PyProject)arg1, (str)name, (str)value) -> None :
    Set the value for the specified context variable.

### `get_context_variables(...)`

get_context_variables( (PyProject)arg1) -> dict :
    Get the context variables in a dictionary.

### `reset_context_variables(...)`

reset_context_variables( (PyProject)arg1) -> None :
    Reset the context variables to their initial state from the ocio config.

