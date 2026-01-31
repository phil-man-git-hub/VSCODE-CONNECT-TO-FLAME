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

### 4. VS Code Extension (`extension/`)
A TypeScript-based extension that provides the UI bridge for human developers.

### 5. API Intelligence Pipeline (`scripts/`)
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

## Architecture Analysis
The project follows a **Decoupled Bridge Architecture**:
- **Execution** is remote (inside Flame via `fu_eavesdrop`).
- **Authoring** is local (VS Code or AI Client).
- **Intelligence** is static (Stubs/Docs) and dynamic (MCP Tools).

This is the most effective way to handle proprietary, closed-runtime environments like Autodesk Flame.

## Future Roadmap Recommendations

1.  **Debugging Enrichment:** Integrate `debugpy` more deeply to allow line-by-line debugging.
2.  **Visual Reasoning:** Add a `take_screenshot` tool to the MCP bridge so AI agents can "see" the Flame UI.
3.  **Autonomous Conform Helper:** Build a suite of "fu_" tools specifically for automating the conform process (e.g., matching sources, checking color space).

---
*Analysis performed by Gemini CLI on 2026-01-30.*
