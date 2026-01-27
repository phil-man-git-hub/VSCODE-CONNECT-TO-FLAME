# Flame VS Code Integration (Flame‑Code)

Expose Autodesk Flame's Python API inside Visual Studio Code by building a small remote execution bridge (Flame listener) and a VS Code extension that talks to it.

## Quickstart

1.  **Install Listener:** Deploy `flame-listener/` into Flame's Python startup hooks.
2.  **Install Extension:** Open `extension/` in VS Code and run the development host, or package as a `.vsix`.
3.  **Run Code:** Use the `Run in Flame` command to execute selections or files inside Flame.

## Goals

- **Rapid Feedback:** Instant execution of Flame scripts without restarting or manual importing.
- **Deep IntelliSense:** Over 2,400 lines of documented API stubs for autocompletion.
- **Automated Docs:** Self-updating API reference gathered from the live Flame runtime.

For technical details, see:
- `docs/vision.md` - Project overview and architecture.
- `docs/architecture.md` - Component breakdown and threading model.
- `docs/protocol.md` - Communication message formats.
- `docs/HOWTO_GENERATE_API_REPORTS.md` - How to update the API reference and stubs.

## Status ✅

- **Execution Bridge:** Working. The Flame listener captures output and handles main-thread dispatching automatically.
- **API Pipeline:** Working. Comprehensive JSON reports and high-quality stubs are fully automated.
- **Next:** Enable remote debugging by integrating `debugpy` (see `docs/TODO.md`).
