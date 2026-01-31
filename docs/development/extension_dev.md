# Extension development — quick start

Follow these steps to run and debug the Flame VS Code extension locally.

## Run in Extension Development Host (fast)
1. Open this repository in VS Code.
2. Open the `extension/` folder in the Explorer.
3. Press `F5` (Run → Start Debugging) to launch the Extension Development Host.
4. In the host window, open the Command Palette and run:
   - `Flame: Connect` to connect to the **fu_eavesdrop** listener,
   - `Flame: Start debug server` to request Flame start a debug server,
   - `Flame: Run in Flame` to send the current file/selection to Flame.

## Development virtual environment
We recommend using a system Python virtual environment for running tests and development tools.

Quick setup:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Environment Variables
- `FLAME_TOKEN`: Your security token for connecting to the listener.
- `FLAME_READ_ONLY`: If `true`, the **fu_whisper** bridge will block destructive commands.
- `FLAME_LISTENER_LOG`: Path to the listener log (defaults to `/tmp/fu_eavesdrop.log`).

## Build & package
- **Install deps**: `npm ci` (in `extension/`).
- **Build**: `npm run compile`.
- **Package**: `npx vsce package` to produce a `.vsix`.

## Component Testing
- **fu_eavesdrop**: Run `tests/test_listener_robustness.py`.
- **fu_whisper**: Run `python flame-mcp/fu_whisper.py` and test with Claude Desktop.
- **Mock Server**: Use `tests/mock_flame_server.py` for CI testing without Flame.
