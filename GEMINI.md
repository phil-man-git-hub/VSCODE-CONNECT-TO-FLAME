# Gemini Repo Analysis: FLAME-UTILITIES

This document provides a technical overview and analysis of the `FLAME-UTILITIES` repository, conducted by Gemini.

## Repository Purpose
The primary goal of this repository is to bridge the gap between **Autodesk Flame's internal Python API** and modern development workflows. It provides a real-time execution bridge, comprehensive API documentation, and high-quality type stubs for local development, as well as an AI-native interface via the Model Context Protocol (MCP).

> [!IMPORTANT]
> **Virtual Environment Requirement**
> All Python scripts in this repository MUST be executed using the local virtual environment to ensure all dependencies are met.
> Always use: `.venv/bin/python <script_name.py>` instead of system `python` or `python3`.

## Gemini Expert Profile: Autodesk Flame Python Specialist
As of January 2026, Gemini is configured as a specialized expert in the Autodesk Flame development ecosystem:
- **API Deep Knowledge:** Full mastery of the Flame Python API (up to version 2027.0.0 preview release pr236), including class hierarchies, methods, and properties.
- **Execution Environment Mastery:** Deep understanding of Flame's threading model and the necessity of main-thread execution (via `schedule_idle_event`) for API safety.
- **Domain-Specific Constraints:** Acute awareness of Flame's unique script loading behaviors, such as filename uniqueness requirements and the strict prohibition of `__init__.py` files.
- **Workflow Architecture:** Expert-level proficiency in managing the "Decoupled Bridge Architecture," spanning TypeScript (VS Code extension), Python (Flame Listener), and introspection-based stub generation.
- **AI Agent Integration:** Mastery of the Model Context Protocol (MCP) for enabling autonomous AI interaction with the Flame API.

## Core Components: The "FU_" Suite

### 1. fu_bootstrap (`flame-utilities/fu_bootstrap.py`)
The central infrastructure component.
- **Role**: Resolves the toolkit root and injects all core subdirectories into `sys.path`.
- **Purpose**: Overcomes Flame's `__init__.py` prohibition while ensuring consistent imports across the suite.

### 2. fu_eavesdrop (`flame-utilities/service/fu_eavesdrop.py`)
A Python service designed to run inside Autodesk Flame.
- **Role:** Listens on a local port (default 5555) for incoming Python code snippets.
- **Key Feature:** Enforces **main-thread execution** via `flame.schedule_idle_event` to ensure API safety.
- **Initialization:** Handled by `fu_eavesdrop_init.py` (located in `service/`).

### 3. FU_Whisper (`flame-mcp/fu_whisper.py`)
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
- **Role:** Indexes synthesized documentation and API stubs using ChromaDB and LlamaIndex.
- **Status:** **Active**. The `chroma_db` is populated with Flame API references and `insight` research documents.
- **Access:** AI Agents can query this layer via the `query_flame_docs` tool in `FU_Whisper`.
- **Goal:** Provide semantic search to AI agents to reduce context window bloat and improve workflow accuracy.

### 5. FU_PyBox v3.13 SDK (`flame-utilities/lib/fu_pybox_v3_13.py`)
A modern, clean-room implementation of the PyBox protocol.
- **Role:** Provides a Python 3.13 native SDK for developing high-performance Flame handlers.
- **Key Feature:** Native Pathlib integration and PEP 484 type hinting for AI-assisted development.

### 6. VS Code Extension (`extension/`)
A TypeScript-based extension that provides the UI bridge for human developers.

### 6. API Intelligence Pipeline (`scripts/`)
A robust data collection system that generates documentation and 2,400+ lines of `.pyi` stubs.

### 7. Session Logging (`scripts/logs/`)
All session initialization attempts are logged to `scripts/logs/` with timestamps (e.g., `session_init_20260203_122037.log`). These logs provide granular debugging info (DEBUG level) that is not visible in the standard console output.

## Key Technical Achievements (as of Feb 2026)

- **AI-Native Flame Workflow:** Successfully implemented the world's first MCP bridge for Autodesk Flame, allowing AI agents to autonomously inspect and manipulate Flame projects.
- **Batch Group Automation:** Demonstrated autonomous creation of complex Batch groups, including schematic reel management and inter-node connection logic (e.g., Mux to Timewarp to Write File).
- **Deep Metadata Extraction (Wiretap Integration):** Bypassed Python API limitations by integrating `wiretap_get_metadata` CLI to extract and parse XML metadata, retrieving frame-accurate handles, resolutions, and ARRI LogC4/ACES color management data.
- **Semantic OTIO Export:** Implemented a robust `otio_exporter.py` that maps Flame sequences to the OpenTimelineIO schema.
- **Advanced Timewarp Mapping:** Solved the mapping of Flame Timewarp effects (Speed/Timing modes) to OTIO `LinearTimeWarp` effects, preserving retime intent and custom metadata for round-tripping.
- **Thread-Safety Implementation:** All API calls are safely dispatched to the main UI thread via `schedule_idle_event`.

## OTIO & Timewarp Research Analysis
Recent research (see `docs/research/understanding-OTIO-flame-timewarps.md`) has established a schema for representing Flame-specific retime semantics within OTIO files:
- **Attachment Point:** Retimes are attached as `otio.schema.TimeEffect` or `otio.schema.LinearTimeWarp` objects on the `Clip`.
- **Metadata Schema:** A dedicated `metadata["flame"]["timewarp"]` block carries schema-versioned data including mode, input/output FPS, and keyframe-based curve representations.
- **Robustness:** The implementation handles both Flame's "Speed" and "Timing" modes by dynamically sampling the node state if native Python properties are unavailable.

## Python Script Loading Constraints
...
---
*Analysis performed by Gemini CLI on 2026-02-02.*
