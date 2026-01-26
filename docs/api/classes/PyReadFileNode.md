
# Class: PyReadFileNode

**Module**: `flame`

## Inheritance & Hierarchy
* **Base Class:** PyNode
* **Context:** Used for reading media files into node-based compositing.

## Functional Role & Context
* **Functional Role:** Represents a ReadFile node, providing access to file reading operations in node graphs.
* **Context:** Used for automating file input and media management in Batch and TimelineFX.

## Description
The PyReadFileNode class provides programmatic access to file reading nodes, supporting automation of media input and file management in node-based workflows.

---

Class derived from PyNode. This class represents a ReadFile node.

### Example
```python
# Create a Read File node in Batch and inspect its name
# Assume 'batch' is a PyBatch object
read_node = batch.create_node('Read File')
print('Created read node:', read_node.attributes.name)
```

