# Extension development — quick start

Follow these steps to run and debug the Flame VS Code extension locally.

## Run in Extension Development Host (fast)
1. Open this repository in VS Code.
2. Open the `extension/` folder in the Explorer.
3. Press `F5` (Run → Start Debugging) to launch the Extension Development Host.
4. In the host window, open the Command Palette and run:
   - `Flame: Connect` to connect to a listener (or use the mock server in `tests/`),
   - `Flame: Start debug server` to request Flame start a debug server,
   - `Flame: Run in Flame` to send the current file/selection to Flame.

## Development virtual environment
We recommend using a system Python virtual environment for running tests and development tools so your environment is stable across Flame preview upgrades.

Quick setup:

```bash
# Create a system venv in repo root using system python3
python3 -m venv .venv
# Activate
source .venv/bin/activate
# Install dev deps
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

Or run the helper script:

```bash
scripts/setup_dev_env.sh [python3]
```

VS Code: select the interpreter from the Command Palette or rely on the workspace setting `python.defaultInterpreterPath` which points to `${workspaceFolder}/.venv/bin/python`.

If you want me to create the `.venv` now I can (I'll use system `python3` unless you prefer otherwise).

## Flame package dependencies & notes

- The repository includes a set of runtime packages commonly used with Flame which we install into the dev venv for testing: **PySide6**, **OpenImageIO**, **OpenTimelineIO**, **OpenColorIO**.
- Import names can differ from the pip package names (for example, `opentimelineio` is the import for OpenTimelineIO). In our smoke test `OpenColorIO` was **not** importable under `OpenColorIO` or `opencolorio` but is available as the `PyOpenColorIO` package (import as `PyOpenColorIO`). The PyPI package name is `opencolorio` and docs are at https://opencolorio.readthedocs.io/en/latest/quick_start/installation.html. Prefer Flame-provided libraries when available.
- These packages include native/binary wheels that are tied to the Python ABI and macOS platform. If you upgrade Python (or change OS/architecture) you may need to reinstall or rebuild wheels.
- Verify imports in your dev venv with the included helper:

```bash
source .venv/bin/activate
python scripts/smoke_imports.py
```

**Environment variables**
- `FLAME_LISTENER_LOG` — path to append structured listener logs (defaults to `/tmp/flame_listener.log`).
- `FLAME_LISTENER_RECV_TIMEOUT` — socket recv timeout in seconds for each client connection (defaults to `5.0`).

**Collecting debug info**
- Use `scripts/collect_flame_debug_logs.py` to collect a small bundle (ps, lsof, listener ping, a short breakpoint test, and head/tail of listener log) into `/tmp` for easier triage.


- To verify behavior inside a running Flame instance, use `Flame: Run in Flame` to execute a short script that prints import/version info, or run a small end-to-end test against the real Flame runtime.

**Example script:** `examples/inspect_flame_env.py` prints the detected import names and versions for the common Flame runtime packages. Run it locally in your dev venv (`python examples/inspect_flame_env.py`) or send it to Flame with `Flame: Run in Flame`.

**Automated smoke test:** `tests/test_imports.py` will attempt the same imports and will *skip* if packages are not available in the environment (so CI can opt-in by installing the binary deps).
- When Flame's Python ABI or installation changes, recreate your venv (`rm -rf .venv && python3 -m venv .venv && scripts/setup_dev_env.sh`) before running dependent tests.

## Build & package
- Install deps: `npm ci` (run in `extension/` or use the provided task `Install extension deps`).
- Build: `npm run compile` (task: `Build extension`).
- Package: `npx vsce package` (task: `Package extension`) to produce a `.vsix`.

## Test the debug flow locally with the mock server
1. Run the mock server once: `python tests/mock_flame_server.py` (it accepts one request and exits).
2. Use `tests/test_start_debug.py` to verify the `start_debug_server` command is handled by the mock server.

## Useful files
- `.vscode/launch.json` — run the extension or attach to Flame (port 5678)
- `examples/debug_test.py` — example script that starts `debugpy` and waits for an attach
- `tests/mock_flame_server.py` — small single-request mock of Flame listener

If you want, I can run the build and package steps now and run the test for `start_debug_server`.