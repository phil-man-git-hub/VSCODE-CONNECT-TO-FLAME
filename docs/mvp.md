# MVP Acceptance Criteria

The Minimal Viable Product should provide a usable development loop for writing and testing Flame Python scripts.

Acceptance criteria:

- `Run in Flame` executes code in a running Flame instance (or the `mock_flame_server.py` during local dev).
- Output (stdout/stderr) and exceptions are displayed in VS Code's Output panel.
- Connection must be secure by default (localhost or Unix socket) and support token auth.
- `.pyi` stubs are available to provide basic autocomplete for common Flame types.
- Automated tests cover the extension client's serialization and a mock server interaction.
