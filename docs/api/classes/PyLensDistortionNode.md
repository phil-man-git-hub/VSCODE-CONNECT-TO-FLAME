
# Class: PyLensDistortionNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base class:** `PyNode` (inherits from `PyFlameObject`)
* **Functional Role:** Lens Distortion node in the schematic, used for lens distortion analysis and correction.

## Description
Represents a Lens Distortion node, providing tools for importing, analyzing, and correcting lens distortion in the node graph.

---


## Methods
### Built-in methods
- `import_lens_distortion(...)` — import_lens_distortion( (PyLensDistortionNode)arg1, (str)filename) -> None : 
import_lens_distortion( (PyLensDistortionNode)arg1, (str)filename) -> None :
    Import the Lens Distortion file.

- `calculate(...)` — calculate( (PyLensDistortionNode)arg1) -> None : 
calculate( (PyLensDistortionNode)arg1) -> None :
    Calculate the amount of distorsion based on the position of vertices.

## API Insight

- Use `import_lens_distortion(filename)` to load lens distortion metadata, then call `calculate()` to analyse it on the node.
- Typical workflows import an external lens file and then run `calculate()` to apply corrections or generate analysis results.

**Example:**

```python
# Import a lens distortion file and run the analysis
node.import_lens_distortion('/path/to/lens_distortion.ld')
node.calculate()
```

