# Gemini Repo Analysis: FLAME-UTILITIES

This document provides a technical overview and analysis of the `FLAME-UTILITIES` repository, conducted by Gemini.

## Repository Purpose
The primary goal of this repository is to bridge the gap between **Autodesk Flame's internal Python API** and modern development workflows. It provides a real-time execution bridge, comprehensive API documentation, and high-quality type stubs for local development, as well as an AI-native interface via the Model Context Protocol (MCP).

## Gemini Expert Profile: Autodesk Flame Python Specialist
As of January 2026, Gemini is configured as a specialized expert in the Autodesk Flame development ecosystem:
- **API Deep Knowledge:** Full mastery of the Flame Python API (up to version 2027.0.0 preview release pr236), including class hierarchies, methods, and properties.
- **Execution Environment Mastery:** Deep understanding of Flame's threading model and the necessity of main-thread execution (via `schedule_idle_event`) for API safety.
- **Domain-Specific Constraints:** Acute awareness of Flame's unique script loading behaviors, such as filename uniqueness requirements and the strict prohibition of `__init__.py` files.
- **Workflow Architecture:** Expert-level proficiency in managing the "Decoupled Bridge Architecture," spanning TypeScript (VS Code extension), Python (Flame Listener), and introspection-based stub generation.
- **AI Agent Integration:** Mastery of the Model Context Protocol (MCP) for enabling autonomous AI interaction with the Flame API.

## Core Components: The "FU_" Suite

### 1. fu_eavesdrop (`flame-listener/fu_eavesdrop.py`)
A Python service designed to run inside Autodesk Flame.
- **Role:** Listens on a local port (default 5555) for incoming Python code snippets.
- **Key Feature:** Enforces **main-thread execution** via `flame.schedule_idle_event` to ensure API safety.
- **Initialization:** Handled by `fu_eavesdrop_init.py`, a standard Flame startup hook.

### 2. FU_Whisper (`flame-mcp/fu_whisper.py`)
An MCP-compliant server that connects AI models to Flame.
- **Role:** Translates AI tool calls into Flame Python commands.
- **Tools:** Includes `execute_python`, `get_flame_context`, `list_desktop_clips`, and `inspect_symbol`.
- **Safety:** Implements an audit logging system (`mcp_audit.log`) and a `FLAME_READ_ONLY` mode.

### 3. fu_relay (`flame-mcp/fu_relay.py`)
The communication layer managing the TCP connection.
- **Role:** Handles the JSON-over-TCP protocol between the bridge and the listener.
- **Security:** Manages authentication via the `.flame.secrets.json` token system.

### 4. FU_Encyclopedia (`fu-encyclopedia/fu_encyclopedia.py`)
The Knowledge Layer (RAG) for the suite.
- **Role:** Indexes synthesized documentation and API stubs using Vertex AI RAG.
- **Goal:** Provide semantic search to AI agents to reduce context window bloat and improve workflow accuracy.

### 5. FU_PyBox v3.13 SDK (`flame-utilities/lib/fu_pybox_v3_13.py`)
A modern, clean-room implementation of the PyBox protocol.
- **Role:** Provides a Python 3.13 native SDK for developing high-performance Flame handlers.
- **Key Feature:** Native Pathlib integration and PEP 484 type hinting for AI-assisted development.

### 6. VS Code Extension (`extension/`)
A TypeScript-based extension that provides the UI bridge for human developers.

### 6. API Intelligence Pipeline (`scripts/`)
A robust data collection system that generates documentation and 2,400+ lines of `.pyi` stubs.

## Key Technical Achievements (as of Jan 2026)

- **AI-Native Flame Workflow:** Successfully implemented the world's first MCP bridge for Autodesk Flame, allowing AI agents to autonomously inspect and manipulate Flame projects.
- **Unified Branding:** Rebranded the entire ecosystem under the `FLAME-UTILITIES` (`fu_`) namespace for professional identity and collision avoidance.
- **Thread-Safety Implementation:** All API calls are safely dispatched to the main UI thread.
- **Deep Metadata Extraction:** Demonstrated the ability for AI agents to retrieve frame-accurate handles, resolutions, and ARRI LogC4/ACES color management data across connected segments.

## Python Script Loading Constraints
Autodesk Flame has specific requirements for loading Python scripts and hooks:
- **Unique Filenames:** Flame can only load scripts or hooks that have unique filenames.
- **No `__init__.py`:** Conventional Python packages with `__init__.py` files are strictly not permitted within Flame's search paths.
- **Alternative Strategies:** Developers must use unique naming conventions (like our `fu_` prefix).

## Deployment Standards
To ensure consistent behavior across environments, the following paths and configurations are standard:
- **Flame Hooks/Scripts:**
  - Global: `/opt/Autodesk/shared/python/`
  - Project: `/opt/Autodesk/project/<project_name>/setups/python/`
- **MCP Configuration:**
  - Standard Client Config: `claude_desktop_config.json` (macOS: `~/Library/Application Support/Claude/`, Win: `%APPDATA%\Claude\`).
  - Required Fields: `command` (python path) and `args` (absolute path to `fu_whisper.py`).

## Architecture Analysis
The project follows a **Decoupled Bridge Architecture**:
- **Execution** is remote (inside Flame via `fu_eavesdrop`).
- **Authoring** is local (VS Code or AI Client).
- **Intelligence** is static (Stubs/Docs) and dynamic (MCP Tools).

This is the most effective way to handle proprietary, closed-runtime environments like Autodesk Flame.

## Pybox Architecture Analysis
Introspection of the active Flame 2027.pr236 environment revealed the following technical details about the "Pybox" feature:

-   **Nature:** Pybox is **not** a class in the `flame` module. It is a Batch/Timeline node type that allows external Python scripts ("handlers") to act as image processors.
-   **SDK Location:** The `pybox_v1` module is importable in the main Flame Python environment and is located at `/opt/Autodesk/presets/<version>/shared/pybox/pybox_v1.py` (e.g., `2027.pr236`).
-   **Handler Structure:** Handlers inherit from `pybox_v1.BaseClass` and utilize methods like `create_page`, `create_float_numeric`, and `create_file_browser` to build the node's UI dynamically.
-   **Communication Protocol:** The bridge between Flame and the Pybox handler process is a stateless **JSON-over-stdio** protocol. Flame writes state to stdin, and the handler writes requests/responses to stdout/stderr.
-   **Creation:** New nodes are instantiated via `flame.batch.create_node("Pybox", "handler_name.py")`.
-   **Deployment:** Standard handlers are distributed in `/opt/Autodesk/presets/<version>/pybox/`.

## Future Roadmap Recommendations

1.  **Debugging Enrichment:** Integrate `debugpy` more deeply to allow line-by-line debugging.
2.  **Visual Reasoning:** Add a `take_screenshot` tool to the MCP bridge so AI agents can "see" the Flame UI.
3.  **Autonomous Conform Helper:** Build a suite of "fu_" tools specifically for automating the conform process (e.g., matching sources, checking color space).

---
*Analysis performed by Gemini CLI on 2026-02-01.*
