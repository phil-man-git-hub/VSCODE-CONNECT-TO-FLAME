# Flame Python API Cookbook

**Source:** Autodesk Flame Family 2026 Help | Flame Python API Code Samples

## Clips & Media

### Import a Clip
```python
flame.import_clips("/var/tmp/clip.mov", <PyLibrary>)
```

### Reformat a Clip
```python
<PyClip>.reformat(width=1920, height=1080, ratio=1.778)
```

### Accessing Frame Metadata
```python
# Get In/Out Marks (Frames)
print(<PyClip>.in_mark.get_value().frame)
print(<PyClip>.out_mark.get_value().frame)

# Get Duration
print(<PyClip>.duration.frame)
```

## Rendering

### Render Timeline FX
```python
# Proxy resolution with Burn
<PyClip>.render(render_mode="All", render_option="Burn", render_quality="Proxy Resolution")
```

### Render Batch FX
```python
<PyClip>.render(effect_type="Batch FX")
```

## Timeline Operations

### Select Segments
```python
# Select all segments on the bottom video track
for seg in <PyVersion>.tracks[0].segments:
    seg.selected = True
```

### Markers
```python
# Create a marker at frame 10
<PyClip>.create_marker(10)

# Move a marker to the middle of a segment
marker.location = <PySegment>.record_in + (<PySegment>.record_duration.frame / 2)
```

## Batch Operations

### Looping Over Nodes
```python
# Change blend mode of all Comp nodes to Add
for n in flame.batch.nodes:
    if n.type == "Comp":
        n.flame_blend_mode = "Add"
```

### Creating Specialized Nodes
```python
# Matchbox with Shader
flame.batch.create_node("Matchbox", "Blur.mx")

# Pybox with Handler
flame.batch.create_node("Pybox", "sendmail.py")

# OpenFX with Plugin
ofx = flame.batch.create_node("OpenFX")
ofx.change_plugin("S_Distort")
```

## UI & Views

### Switching Views
```python
# Switch to Desktop Reels
flame.projects.current_project.current_workspace.desktop.set_desktop_reels()
```

### Controlling the Media Panel
```python
# Hide Media Panel
flame.media_panel.visible = False

# Set to Dual Mode
flame.media_panel.dual = True
```
