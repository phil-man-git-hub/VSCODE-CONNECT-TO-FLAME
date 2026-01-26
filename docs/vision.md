# Vision

To expose **Autodesk Flame’s Python API** inside **VS Code** in the same spirit as Blender/Maya/Nuke remote‑execution bridges, you need three components working together. Flame doesn’t ship with a command port or socket server, so you’d be building the missing piece yourself — but it’s absolutely doable.

This repository provides a pragmatic path to a developer‑friendly workflow: a Flame‑side listener, a VS Code extension, and type stubs that provide IntelliSense.

## Key components

- A Flame startup hook that runs a small TCP/Unix socket listener inside Flame’s Python environment.
- A VS Code extension that sends Python code to Flame for execution and surfaces stdout/stderr/exceptions.
- Generated `.pyi` stub files to enable autocomplete and type checking in VS Code.

See `docs/protocol.md` for message formats and `docs/architecture.md` for component responsibilities.

## Per-project configuration

When you work with a specific Flame project, create a `flame.project.json` file at the repository root (see `flame.project.example.json`) to store per-project metadata and paths (for example, `flameProjectPath` and `scriptsDir`). For sensitive values such as tokens, use environment variables (for example `FLAME_TOKEN`) or a workspace-local `.flame.secrets.json` file that is ignored by git. The extension will read these values from the workspace root or from `flame.project` workspace settings and use them to populate default host/port and sync targets.
