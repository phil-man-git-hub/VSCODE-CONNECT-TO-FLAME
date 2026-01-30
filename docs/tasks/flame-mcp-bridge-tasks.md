# Tasks: Flame-MCP Bridge Implementation

This document tracks the technical steps required to implement the Model Context Protocol (MCP) bridge for Autodesk Flame.

## Phase 1: Environment & Scaffolding
- [ ] Create `flame-mcp/` directory structure.
- [ ] Initialize `requirements.txt` for the MCP server (e.g., `fastmcp`, `requests`, `pydantic`).
- [ ] Set up a basic `server.py` using `fastmcp`.
- [ ] Create a README in `flame-mcp/` explaining how to start the server.

## Phase 2: Core Communication Layer
- [ ] Implement the `Relay` client: a module to handle network communication with the existing `flame-listener.py` (port 5555).
- [ ] Standardize the error handling for relay failures (e.g., Flame is not running, Listener is down).
- [ ] Implement a "Ping" tool to verify the end-to-end connection: `AI -> MCP -> Listener -> Flame`.

## Phase 3: Core AI Tools
- [ ] **Tool: `execute_python`**
    - [ ] Basic execution of strings.
    - [ ] Return stdout and stderr to the AI.
- [ ] **Tool: `get_flame_context`**
    - [ ] Return JSON containing: Current Project, User, Workspace, and Version.
- [ ] **Tool: `list_desktop_clips`**
    - [ ] Query Flame for all clips on the current Desktop.
- [ ] **Tool: `inspect_symbol`**
    - [ ] Use Python's `dir()` and `help()` inside Flame to give the AI real-time documentation for any Flame object.

## Phase 4: Integration & Security
- [ ] Test the bridge with an MCP-compliant client (e.g., Claude Desktop or Cursor).
- [ ] Implement basic logging of all AI-generated commands for auditability.
- [ ] (Optional) Add a "Read-Only" mode toggle to prevent accidental modifications during inspection.

## Phase 5: Documentation & Examples
- [ ] Write a "Getting Started" guide for users to connect their LLM to the Flame MCP.
- [ ] Create a folder `flame-mcp/prompts/` with system prompt templates that help the AI understand how to use the Flame tools effectively.
- [ ] Record a demo of an AI autonomously interacting with the Flame Desktop.
