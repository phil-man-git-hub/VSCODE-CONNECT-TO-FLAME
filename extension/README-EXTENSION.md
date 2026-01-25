# Flame VS Code Extension (dev)

This folder contains the VS Code extension source. Development steps:

1. Open this folder in VS Code.
2. Run `npm install` and `npm run compile` (configure `tsconfig.json` as needed).
3. Run the extension in the Extension Development Host to test connecting to the mock server.

Commands:
- `Flame: Connect` — connect to the listener (default localhost:5555).
- `Flame: Run in Flame` — send selected text or file contents to Flame.
