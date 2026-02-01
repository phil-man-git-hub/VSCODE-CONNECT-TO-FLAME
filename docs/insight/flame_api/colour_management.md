# Colour Management API

**Source:** Autodesk Flame Family 2026 Help | Colour Management API

The Colour Management API allows you to control Flame's colour pipeline, including tagging clips, applying transforms, and managing OCIO context variables.

## Core Concepts

-   **Tagging:** Setting the metadata that identifies the colour space of source media.
-   **Transforms:** Converting from one space to another (Input, View, or Colour Transform).
-   **Context Variables:** Changing OCIO variables (e.g., `SHOT`, `SEQ`) to dynamically load looks or transforms.

## Workflows

### 1. Tagging Media
You can tag the colour space of clips in Batch, Timeline, or MediaHub.

**Batch:**
```python
# Get a node's output colour space
cs = flame.batch.get_node("Read").colour_space

# Tag a stream using a Colour Mgmt node
tagger = flame.batch.create_node("Colour Mgmt")
tagger.mode = "Tag Only"
tagger.tagged_colour_space = "ACEScg"
```

**Timeline:**
```python
# Get colour space at specific frame
seq = flame.timeline.current_segment
cs = seq.get_colour_space(flame.PyTime(10))

# Apply Tagging FX
fx = seq.create_effect("Source Colour Mgmt")
fx.mode = "Tag Only"
fx.tagged_colour_space = "ACEScct"
```

**MediaHub:**
```python
flame.mediahub.files.options.set_tagged_colour_space("ACES2065-1")
```

### 2. Applying Transforms
Use the `Colour Mgmt` node or effect to apply transforms.

```python
cm = flame.batch.create_node("Colour Mgmt")

# Method A: Standard Transforms
cm.mode = "Input Transform"
cm.tagged_colour_space = "ACEScct" # Input
cm.working_space = "ACEScg"      # Output

# Method B: View Transform
cm.mode = "View Transform"
cm.display = "sRGB - Display"
cm.view = "ACES 1.0 - SDR Video"

# Method C: Load External File (CTF/LUT)
cm.import_transform("/path/to/transform.ctf")
```

### 3. OCIO Context Variables
You can manipulate context variables at the **Project** level or **Node** level. This is powerful for shot-based look management.

**Project Level:**
```python
prj = flame.projects.current_project
prj.set_context_variable("SHOT", "sh010")
prj.set_context_variable("SEQ", "sq02")
```

**Node Level:**
```python
node = flame.batch.get_node("LMT_Load")
node.context_variables_from_project = False # Decouple from project
node.set_context_variable("SHOT", "sh020")
```

## OCIO Python Binding
Flame includes the `PyOpenColorIO` library, allowing you to inspect configs directly.

```python
import PyOpenColorIO as ocio
import os

# Load project config
prj = flame.projects.current_project
config_path = os.path.realpath(os.path.join(prj.setups_folder, "colour_mgmt", "config.ocio"))
cfg = ocio.Config.CreateFromFile(config_path)

# List available views
print(list(cfg.getViews("sRGB - Display")))
```
