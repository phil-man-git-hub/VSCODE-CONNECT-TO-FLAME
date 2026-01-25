# Flame VS Code Integration (Flame‑Code)

Expose Autodesk Flame's Python API inside Visual Studio Code by building a small remote execution bridge (Flame listener) and a VS Code extension that talks to it.

Quickstart

1. Install the Flame listener into Flame's Python startup hooks.
2. Install the VS Code extension from the `extension/` folder (development mode) or the Marketplace (when published).
3. Use the `Run in Flame` command to execute selections or files inside Flame and see stdout/stderr in the Output panel.

Goals

- Provide fast feedback loop for developing Flame Python scripts.
- Offer IntelliSense by shipping generated `.pyi` stubs.
- Support secure local-only communication (localhost or Unix domain socket).

For details, see `docs/vision.md`, `docs/architecture.md`, `docs/protocol.md`, and `docs/roadmap.md`.
