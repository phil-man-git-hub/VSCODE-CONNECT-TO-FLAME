# Architectural Discovery: Logik-Projekt

This document outlines the methodology and findings from the architectural discovery process of the `logik-projekt` toolset.

## 1. Methodology
The discovery process utilized a combination of manual code inspection and automated analysis tools to map the internal structure of the repository.

### Discovery Phases
1.  **Entry Point Identification**: Scanning the `hooks/` directory to identify how Autodesk Flame triggers specific tools.
2.  **Logic Path Tracing**: Following function calls from the hooks into the `src/` directory to locate core business logic.
3.  **Data Dependency Mapping**: Identifying how JSON and XML files in the `cfg/` directory influence the behavior of the initialization scripts.
4.  **Integration Analysis**: Examining the relationship between `logik-projekt` and the `flame-utilities` suite.

## 2. Key Discovery Findings

### Decoupled Logic Pattern
The system demonstrates a clear separation of concerns:
- **Triggers**: Lightweight Python scripts in `hooks/` (e.g., `create_projekt_layout.py`).
- **Engine**: Reusable modules in `src/core/` (e.g., `create_or_validate_object.py`).
- **Blueprints**: Data templates in `cfg/` (e.g., `library_template_04.json`).

### Data-Driven Project Construction
A significant finding was that project structures are not hardcoded. Instead, the logic iterates over JSON definitions, allowing for dynamic project layout creation without modifying the source code.

### Bootstrapping Mechanism
Discovery revealed a manual bootstrapping process in each hook to handle Flame's unique Python environment constraints (the prohibition of `__init__.py` files and the need for explicit `sys.path` management).

## 3. Summary of Discovered Relationships
| From | To | Purpose |
| :--- | :--- | :--- |
| `hooks/*.py` | `src/core/` | Executes business logic |
| `src/core/` | `cfg/*.json` | Loads project structure templates |
| `hooks/*.py` | `lp_bootstrap.py` | Initializes environment and paths |
| `src/core/` | `flame_api` | Manipulates the Flame environment |

---
*Created during Architectural Discovery phase on 2026-02-03.*
