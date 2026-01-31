# Changelog

## Unreleased

### Added
- **FU_Whisper (Flame MCP Bridge)**: Implemented a Model Context Protocol (MCP) server that allows AI agents (Claude, Cursor, Gemini) to interact autonomously with Autodesk Flame.
- **FLAME-UTILITIES (fu_) Branding**: Established a cohesive naming convention for the project's core components:
    - `fu_eavesdrop`: The internal Flame listener.
    - `fu_whisper`: The external AI bridge.
    - `fu_relay`: The communication conduit.
    - `fu_eavesdrop_init`: The startup hook.
- **AI Documentation Suite**: Added comprehensive "Understanding AI" research documents covering MCP, RAG, Agents, Model Types, and more.
- **Enhanced AI Tools**: Added specialized tools for AI agents, including `get_flame_context`, `list_desktop_clips`, and `inspect_symbol` for live API discovery.

### Improved
- **Audit Logging**: Implemented `mcp_audit.log` in `fu_whisper` to track all AI-generated tool calls and their results.
- **Safety Modes**: Added a `FLAME_READ_ONLY` mode to the MCP bridge to prevent accidental modifications during inspection.
- **TCP Relay Robustness**: Standardized the `fu_relay` logic for handling TCP communication and authentication tokens.

### Fixed
- **Naming Collisions**: Renamed startup hooks to avoid conflicts with Flame's internal "Igniter" tool.
- **API Iteration**: Improved logic for iterating over Flame collections (Clips, Sequences, Reels) to prevent `NoneType` errors in scripts.

### Added (Jan 2026)
- **Enhanced API Stubs Pipeline**: Created `scripts/generate_stubs_from_reports.py` which extracts detailed method signatures, default values, and inheritance from JSON reports.
- **Deep IntelliSense**: Regenerated `stubs/flame.pyi` with over 2,400 lines of documented API definitions.
- **Comprehensive Repo Analysis**: Added `GEMINI.md` with a technical breakdown of the project architecture and roadmap.
- **Stub Generation Guide**: Updated `docs/HOWTO_GENERATE_API_REPORTS.md` with the new stub generation workflow.

### Improved
- **API Collector**: Updated `scripts/collect_flame_api.py` to handle non-serializable Boost.Python property objects and capture runtime constant values.
- **CI/CD Reliability**: Updated GitHub Actions to use latest versions (`upload-artifact@v4`, `setup-python@v5`) and added necessary permissions for Docs deployment.

### Fixes
- **Critical Threading Fix**: Refactored `flame_listener.py` to execute commands on the Flame main thread using `flame.schedule_idle_event`. This prevents crashes caused by accessing the non-thread-safe Flame API from background threads.
- Added `scripts/test_thread_safety.py` to verify safe execution context.
- Fixed `pytest` failures in CI by adding skip logic when the Flame Listener is unavailable.

- Repository scaffolded with docs, listener prototype, extension skeleton, and mock server.

### Harden listener and diagnostics (flame-listener)

- Add thread tracking and `atexit` cleanup to join background threads on shutdown. ✅
- Surface background-thread and unhandled exceptions using `threading.excepthook` and `sys.excepthook`. 🔍
- Run `execute` requests in worker threads with configurable per-request timeout (`timeout` request field). ⏱️
- Add configurable socket recv timeout (`FLAME_LISTENER_RECV_TIMEOUT`) and structured logs written to `FLAME_LISTENER_LOG` (default `/tmp/flame_listener.log`). 📁
- Make `start_debug_server` non-blocking: immediate ACK + background in-process debug adapter with attach logging and diagnostics (uses `wait_for_client` with timeout). 🧩
- Add unit/integration tests for timeout, thread-exception logging, debug start lifecycle, and recv-timeout behavior; add CI workflow. ✅

