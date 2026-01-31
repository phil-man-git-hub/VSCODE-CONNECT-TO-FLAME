# Tasks: FU_Whisper (Flame MCP Bridge) Implementation

This document tracks the technical steps required to implement the Model Context Protocol (MCP) bridge for Autodesk Flame.

## Phase 1: Environment & Scaffolding
- [x] Create `flame-mcp/` directory structure.
- [x] Initialize `requirements.txt` for the MCP server (e.g., `fastmcp`, `requests`, `pydantic`).
- [x] Set up a basic `fu_whisper.py` (formerly `server.py`) using `fastmcp`.
- [x] Create a README in `flame-mcp/` explaining how to start the server.

## Phase 2: Core Communication Layer
- [x] Implement the `fu_relay` client: a module to handle network communication with the existing `fu_eavesdrop.py` (port 5555).
- [x] Standardize the error handling for relay failures (e.g., Flame is not running, Listener is down).
- [x] Implement a "Ping" tool to verify the end-to-end connection: `AI -> fu_whisper -> fu_relay -> fu_eavesdrop -> Flame`.

## Phase 3: Core AI Tools
- [x] **Tool: `execute_python`**
    - [x] Basic execution of strings.
    - [x] Return stdout and stderr to the AI.
- [x] **Tool: `get_flame_context`**
    - [x] Return JSON containing: Current Project, User, Workspace, and Version.
- [x] **Tool: `list_desktop_clips`**
    - [x] Query Flame for all clips on the current Desktop.
- [x] **Tool: `inspect_symbol`**
    - [x] Use Python's `dir()` and `help()` inside Flame to give the AI real-time documentation for any Flame object.


## Phase 4: Integration & Security
- [ ] Test the bridge with an MCP-compliant client (e.g., Claude Desktop or Cursor).
- [x] Implement basic logging of all AI-generated commands for auditability.
- [x] (Optional) Add a "Read-Only" mode toggle to prevent accidental modifications during inspection.

## Phase 5: Documentation & Examples
- [x] Write a "Getting Started" guide for users to connect their LLM to the FU_Whisper bridge.
- [x] Create a folder `flame-mcp/prompts/` with system prompt templates that help the AI understand how to use the Flame tools effectively.
- [ ] Record a demo of an AI autonomously interacting with the Flame Desktop.
