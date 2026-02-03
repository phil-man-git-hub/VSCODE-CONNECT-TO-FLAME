# FLAME-UTILITIES (fu_)

![Visitors](https://hits.dwyl.com/phil-man-git-hub/VSCODE-CONNECT-TO-FLAME.svg)

A professional suite of tools designed to bridge the gap between **Autodesk Flame's internal Python API** and modern development workflows. This project provides a real-time execution bridge, AI-native interaction via MCP, comprehensive API documentation, and high-quality type stubs.

## The Suite

*   **`fu_bootstrap`**: The central infrastructure layer that manages paths and overcomes Flame's `__init__.py` limitations.
*   **`fu_eavesdrop`**: The high-performance, thread-safe listener running inside Flame (`service/`).
*   **`fu_whisper`**: The Model Context Protocol (MCP) bridge for AI-native interaction.
*   **Knowledge Layer (RAG)**: Semantic documentation search via `llama-index` and `chroma_db`.
*   **Persistent Library**: A self-expanding library of successful Flame snippets.

## 📢 Commercial Support & Newsletter
As the world's first AI-native bridge for Autodesk Flame, we are building a community of forward-thinking finishing artists and developers.

*   **Newsletter:** [Sign up here for release updates and AI workflows](#) *(Replace with your link)*
*   **Commercial Inquiry:** For enterprise support, custom tool development, or commercial licensing, please [contact the author](mailto:pman@example.com?subject=FLAME-UTILITIES%20Inquiry).

## Quickstart

1.  **Install Listener:** Deploy the `flame-utilities/` directory and `fu_activate.py` hook into Flame's Python setup folder.
2.  **Initialize Session:** Run `./scripts/initialize_session.py` to start the bridge and generate an AI handshake prompt.
3.  **Connect AI:** Paste the generated handshake into your AI client (see `HOWTO.md`).
4.  **Run Code:** Talk directly to your AI agent to manipulate Flame. Successful patterns are automatically saved to your local library.

## Goals

- **AI-Native Finishing:** Enable AI agents to autonomously perform conforms, metadata extraction, and batch automation.
- **Rapid Feedback:** Instant execution of Flame scripts without restarting or manual importing.
- **Deep IntelliSense:** Over 2,400 lines of documented API stubs for autocompletion.
- **Automated Docs:** Self-updating API reference gathered from the live Flame runtime.

For technical details, see:
- `HOWTO.md` - Comprehensive connection and setup guide.
- `MCP.md` - Operational guide for AI Agents (Claude, Cursor, Gemini).
- `docs/architecture/overview.md` - Component breakdown and threading model.
- `docs/development/api_reports.md` - How to update the API reference and stubs.

## Status ✅

- **MCP Bridge:** Working. AI agents can retrieve project info, list desktop clips, and execute autonomous logic.
- **Audit System:** Working. Full interaction logs are stored in `fu-whisper/logs/`.
- **Code Library:** Working. AI builds its own persistent toolset in `fu-whisper/library/`.
- **Next:** Enable remote debugging by integrating `debugpy` (see `docs/tasks/TODO.md`).

---
*Note: The legacy VS Code Extension has been moved to `unused/` as the MCP bridge provides a more powerful, AI-integrated interface.*