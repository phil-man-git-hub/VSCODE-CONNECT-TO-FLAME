# Flame VS Code Extension (dev)

This folder contains the VS Code extension source. Development steps:

1. Open this folder in VS Code.
2. Run `npm install` and `npm run compile` (configure `tsconfig.json` as needed).
3. Run the extension in the Extension Development Host to test connecting to the mock server.

Commands:
- `Flame: Connect` — connect to the listener (default localhost:5555). The extension will attempt to read `flame.project.json` from the workspace root or `flame.project` workspace settings to discover the listener host/port and `scriptsDir`.
- `Flame: Run in Flame` — send selected text or file contents to Flame.

Configuration & secrets

- Add a `flame.project.json` file at the repository root (see `flame.project.example.json`) to store per-project metadata such as `flameProjectPath`, `scriptsDir`, and `listener` host/port.
- For authentication tokens, set the `FLAME_TOKEN` environment variable or add a `.flame.secrets.json` file at the workspace root with the shape `{ "token": "your-token" }`. The `.flame.secrets.json` file is ignored by git by default.
