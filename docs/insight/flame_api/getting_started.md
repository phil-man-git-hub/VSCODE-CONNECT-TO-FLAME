# Getting Started with the Flame Python API

**Source:** Autodesk Flame Family 2026 Help | Write Your First Python API Script

## Your First Script: Creating a Batch Setup

This guide walks through creating a simple script that sets up a Batch group, creates nodes, and connects them.

### 1. Import the Module
Every script must start by importing the core module.
```python
import flame
```

### 2. Create a Batch Group
Define your reels and create the group.
```python
schematicReels = ['SchematicReel1', 'SchematicReel2']
shelfReels = ['ShelfReel1']

flame.batch.create_batch_group(
    'MyFirstScript',
    start_frame = 1,
    duration = 100,
    reels = schematicReels,
    shelf_reels = shelfReels
)
```

### 3. Switch Context
Ensure you are in the Batch tab.
```python
flame.batch.go_to()
```

### 4. Create and Connect Nodes
Create nodes and store them in variables to reference them later.
```python
# Create nodes
comp = flame.batch.create_node("Comp")
writeFile = flame.batch.create_node("Write File")

# Connect them: output node, output socket, input node, input socket
flame.batch.connect_nodes(comp, "Result", writeFile, "Front")
```
> **Tip:** Socket names are case-sensitive. Use the exact name seen in the Flame UI.

### 5. Organize
Clean up the node layout.
```python
flame.batch.organize()
```

### Full Script
```python
import flame

# Define Reels
schematicReels = ['SchematicReel1', 'SchematicReel2']
shelfReels = ['ShelfReel1']

# Create Group
flame.batch.create_batch_group(
    'MyFirstScript',
    start_frame = 1,
    duration = 100,
    reels = schematicReels,
    shelf_reels = shelfReels
)

# Go to Batch
flame.batch.go_to()

# Create Nodes
comp = flame.batch.create_node("Comp")
writeFile = flame.batch.create_node("Write File")

# Connect
flame.batch.connect_nodes(comp, "Result", writeFile, "Front")

# Organize
flame.batch.organize()
```
