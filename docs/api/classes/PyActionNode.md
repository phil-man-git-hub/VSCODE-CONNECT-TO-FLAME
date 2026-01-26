
# Class: PyActionNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyActionFamilyNode` (inherits from `PyNode` → `PyFlameObject`)
* **Functional Role:** The main 3D compositing node in the schematic (Action environment).

## API Foundation & Inherited Features
PyActionNode ultimately inherits from `PyArchiveEntry` via `PyNode` and `PyFlameObject`. This means it shares foundational properties and methods common to all objects managed in the Flame Media Panel:

### Common Attributes (from PyArchiveEntry)
| Attribute   | Type   | Description |
|-------------|--------|-------------|
| id          | str    | Unique database identifier for the node. |
| name        | str    | Display name in the Media Panel. |
| colour      | tuple  | Colour assigned for labelling. |
| modified    | datetime | Last modified timestamp. |
| archived    | bool   | Archive status. |
| online      | bool   | Media availability status. |

### Common Methods (from PyArchiveEntry)
| Method                | Returns         | Description |
|-----------------------|----------------|-------------|
| delete([confirm=True])| bool           | Deletes the node, optionally with confirmation. |
| duplicate()           | PyArchiveEntry | Creates a copy of the node. |
| move(destination)     | bool           | Moves the node to a new container. |
| reveal_in_ui()        | bool           | Selects and displays the node in the UI. |
| get_children()        | list           | Retrieves immediate children of the node. |

This inheritance ensures PyActionNode supports robust media management, organization, and UI integration consistent with all Flame database objects.


## Description
Represents an Action node object, providing the core compositing and 3D environment in the schematic.

---

## Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| pos_x     | int  | The x position of a node in the Batch schematic. Range: -2147483647 to 2147483647 |
| pos_y     | int  | The y position of a node in the Batch schematic. Range: -2147483647 to 2147483647 |
| name      | str  | The name of the node in the Batch schematic. |
| collapsed | bool | The collapsed status of a node in the Batch schematic. Values: True/False |
| note      | str  | The Node's note. |

---

### Example
```python
# Example: Import an FBX into Action and enable outputs
# Assume 'action' is a PyActionNode object
fbx_result = action.import_fbx('/mnt/assets/scene_001.fbx', lights=True, cameras=True)
action.enable_output('Comp')
print('Imported FBX result:', fbx_result)
```

## Methods
### Properties
- `media_nodes(...)` — None( (flame.PyActionNode)arg1) -> list 
None( (flame.PyActionNode)arg1) -> list

- `output_types(...)` — None( (flame.PyActionNode)arg1) -> list 
None( (flame.PyActionNode)arg1) -> list


### Built-in methods
- `add_media(...)` — add_media( (PyActionFamilyNode)arg1) -> object : 
add_media( (PyActionFamilyNode)arg1) -> object :
    Add a Media layer to the Batch Action node.
    Also instantiates a matching Surface node (and Axis) in the Action node schematic.

- `import_fbx(...)` — import_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)create_media=True [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]]) -> list : 
import_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)create_media=True [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]]) -> list :
    Import an FBX file into the Action schematic using the Action Objects mode.
    Keyword argument:
    file_path -- Path to the FBX file. Mandatory.
    input_colour_space -- Colour space name used as input for textures. Optional.

- `export_fbx(...)` — export_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)only_selected_nodes=False [, (float)pixel_to_units=0.10000000149011612 [, (str)frame_rate='23.976 fps' [, (bool)bake_animation=False [, (bool)export_axes=True [, (bool)export_point_locators=False [, (bool)combine_material=True [, (bool)duplicate_material=False]]]]]]]]) -> bool : 
export_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)only_selected_nodes=False [, (float)pixel_to_units=0.10000000149011612 [, (str)frame_rate='23.976 fps' [, (bool)bake_animation=False [, (bool)export_axes=True [, (bool)export_point_locators=False [, (bool)combine_material=True [, (bool)duplicate_material=False]]]]]]]]) -> bool :
    Export Action nodes to an FBX file.
    Keyword argument:
    file_path -- Path to the output FBX file. Mandatory.

- `read_fbx(...)` — read_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]) -> object : 
read_fbx( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (bool)keep_frame_rate=True [, (bool)bake_animation=False [, (bool)object_properties=True [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)is_udim=False [, (bool)relink_material=True [, (str)input_colour_space='']]]]]]]]]]]]]) -> object :
    Import an FBX file into the Action schematic using the Read File mode.
    Keyword argument:
    file_path -- Path to the FBX file. Mandatory.
    input_colour_space -- Colour space name used as input for textures. Optional.

- `import_abc(...)` — import_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> list : 
import_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> list :
    Import an Alembic (ABC) file into the Action schematic using the Action Objects mode.
    Keyword argument:
    file_path -- Path to the ABC file. Mandatory.

- `read_abc(...)` — read_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> object : 
read_abc( (PyActionFamilyNode)arg1, (str)file_path [, (bool)lights=True [, (bool)cameras=True [, (bool)models=True [, (bool)normals=True [, (bool)mesh_animations=True [, (str)frame_rate='23.976 fps' [, (bool)auto_fit=False [, (float)unit_to_pixels=10.0 [, (bool)consolidate_geometry=True [, (bool)create_object_group=False]]]]]]]]]]) -> object :
    Import an Alembic (ABC) file into the Action schematic using the Read File mode.
    Keyword argument:
    file_path -- Path to the ABC file. Mandatory.

- `import_psd(...)` — import_psd( (PyActionFamilyNode)arg1, (str)file_path [, (str)input_colour_space='']) -> list : 
import_psd( (PyActionFamilyNode)arg1, (str)file_path [, (str)input_colour_space='']) -> list :
    Import a PSD file into the Action schematic.
    Keyword arguments:
    file_path -- Path to the PSD file. Mandatory.
    input_colour_space -- The colour space used as input. Optional.

- `enable_output(...)` — enable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool : 
enable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool :
    Enable the render output_type for the Action node.
    Keyword argument:
    output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectoars Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)

- `disable_output(...)` — disable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool : 
disable_output( (PyActionFamilyNode)arg1, (str)output_type) -> bool :
    Disable the render output_type for the Action node.
    Keyword argument:
    output_type -- The output to enable. (Comp, Matte, 3D Motion, Albedo, AO, Background, Emissive, GMask, Lens Flare, Motion Vectors, Normals, Object ID, Occluder, Position, Projectors Matte, Reflection, Roughness, Shadow, Specular, UV, Z-Depth HQ, Z-Depth)


