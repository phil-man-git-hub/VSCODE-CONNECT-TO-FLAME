# FLAME-UTILITIES (fu_)

A professional suite of tools designed to bridge the gap between **Autodesk Flame's internal Python API** and modern development workflows. This project provides a real-time execution bridge, AI-native interaction via MCP, comprehensive API documentation, and high-quality type stubs.

## The Suite

*   **`fu_eavesdrop`**: The high-performance, thread-safe listener that runs inside Flame.
*   **`fu_whisper`**: The Model Context Protocol (MCP) bridge that allows AI agents (Claude, Cursor, Gemini) to "talk" to Flame.
*   **`fu_relay`**: The secure communication conduit between external tools and the Flame runtime.
*   **VS Code Extension**: A dedicated UI for human developers to execute code and debug scripts in Flame.

## Quickstart

1.  **Install Listener:** Deploy the `flame-utilities/` directory into Flame's Python startup hooks.
2.  **Start the Bridge:** Navigate to `flame-utilities/whisper/` and run `python fu_whisper.py`.
3.  **Connect AI:** Add the bridge to your AI client (see `flame-utilities/whisper/GETTING_STARTED.md`).
4.  **Run Code:** Use the VS Code extension or talk directly to your AI agent to manipulate Flame.

## Goals

- **AI-Native Finishing:** Enable AI agents to autonomously perform conforms, metadata extraction, and batch automation.
- **Rapid Feedback:** Instant execution of Flame scripts without restarting or manual importing.
- **Deep IntelliSense:** Over 2,400 lines of documented API stubs for autocompletion.
- **Automated Docs:** Self-updating API reference gathered from the live Flame runtime.

For technical details, see:
- `docs/goals/flame-mcp-creation.md` - The vision for AI-native Flame interaction.
- `docs/research/understanding-AI_acronyms.md` - Educational resources for AI integration.
- `docs/architecture.md` - Component breakdown and threading model.
- `docs/HOWTO_GENERATE_API_REPORTS.md` - How to update the API reference and stubs.

## Status ✅

- **MCP Bridge:** Working. AI agents can retrieve project info, list desktop clips, and execute autonomous logic.
- **Execution Bridge:** Working. Thread-safe main-thread dispatching is fully implemented.
- **API Pipeline:** Working. Comprehensive JSON reports and high-quality stubs are fully automated.
- **Next:** Enable remote debugging by integrating `debugpy` (see `TODO.md`).
