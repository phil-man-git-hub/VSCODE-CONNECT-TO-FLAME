# Advanced Python API Workflows

**Source:** Autodesk Flame Family 2026 Help | Python API Examples

## 1. Importing and Compositing Multi-Channel Clips

This workflow demonstrates how to import a multi-channel OpenEXR clip and automatically break it out into a composite using the extracted channels.

```python
import flame

# 1. Setup
schematicReels = ['Multi-Channel_Clip']
shelfReels = ['Extra_Data']

flame.batch.create_batch_group(
    'Learning_Multi-Channel',
    start_frame = 1001,
    duration = 5,
    reels = schematicReels,
    shelf_reels = shelfReels
)
flame.batch.go_to()

# 2. Import
clip1 = flame.batch.import_clip("/var/tmp/robot_CGI.clip", "Multi-Channel_Clip")
clip1.name = "CGI_Render"

# 3. Create Nodes
action1 = flame.batch.create_node("Action")
action1.name = "Comping_CGI"
writeFile = flame.batch.create_node("Write File")

# 4. Extract Channels (Add Media inputs to Action)
# Create input sockets on the Action node for specific passes
passes = [
    ("Direct_Diffuse", "robot_direct_diffuse"),
    ("Indirect_Diffuse", "robot_indirect_diffuse"),
    ("Direct_Specular", "robot_direct_specular"),
    ("Indirect_Specular", "robot_indirect_specular"),
    ("Reflection", "robot_reflection")
]

for pass_name, channel_name in passes:
    media_node = action1.add_media()
    media_node.name = pass_name
    # Connect the multi-channel clip's specific socket to the new Action media input
    flame.batch.connect_nodes(clip1, channel_name, media_node, "Front")

# 5. Output
flame.batch.connect_nodes(action1, "output1 [ Comp ]", writeFile, "Front")
flame.batch.organize()
```

## 2. Multi-Pass Render Setup (Manual Comp)

This example manually reconstructs a beauty pass from separate file sequences using standard Comp nodes.

```python
import flame

# Setup
flame.batch.create_batch_group('RenderPasses_Setup', start_frame=1001, duration=5)
flame.batch.go_to()

# Import separate pass files
diffuse = flame.batch.import_clip("/tmp/diffuse.[001-005].exr", "Schematic Reel 1")
spec = flame.batch.import_clip("/tmp/spec.[001-005].exr", "Schematic Reel 1")
reflection = flame.batch.import_clip("/tmp/refl.[001-005].exr", "Schematic Reel 1")

# Create Comps
comp_diff = flame.batch.create_node("Comp")
comp_diff.flame_blend_mode = "Add"

comp_final = flame.batch.create_node("Comp")
comp_final.flame_blend_mode = "Screen"

# Connect
flame.batch.connect_nodes(diffuse, "BGR", comp_diff, "Front")
flame.batch.connect_nodes(spec, "BGR", comp_diff, "Back")

flame.batch.connect_nodes(comp_diff, "Result", comp_final, "Back")
flame.batch.connect_nodes(reflection, "BGR", comp_final, "Front")

flame.batch.organize()
```
