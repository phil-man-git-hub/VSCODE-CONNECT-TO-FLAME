# HOWTO: Connect AI to Autodesk Flame

This guide explains how to set up the **FLAME-UTILITIES** bridge, allowing AI agents (like Claude Desktop or Gemini) to communicate directly with Autodesk Flame.

## System Overview

1.  **Flame Side (`fu_eavesdrop`):** A Python script running inside Flame that listens for commands.
2.  **Bridge (`fu_whisper`):** A local server implementing the Model Context Protocol (MCP).
3.  **AI Client:** An application (e.g., Claude Desktop, Cursor) that talks to the Bridge.

## Step 1: Install the Flame Listener

The listener must run inside Autodesk Flame's Python environment.

1.  **Locate the Files:**
    The core files are in the `flame-utilities/` directory:
    - `fu_activate.py` (The entry point hook)
    - `fu_bootstrap.py` (The infrastructure layer)
    - `service/fu_eavesdrop.py` (The listener logic)

2.  **Deploy to Flame:**
    Use the provided automation script to deploy the toolkit to your project:
    ```bash
    python3 scripts/deploy_to_flame_project.py --copy --scripts-dir /path/to/project/setups/python/
    ```
    This script will:
    - Copy the `flame-utilities/` folder.
    - Deploy `fu_activate.py` to the parent folder.

3.  **Verify:**
    Start Autodesk Flame. Watch the shell output. You should see the ignition sequence:
    > `[fu_bootstrap] Setting up toolkit root...`
    > `[fu_launcher] Igniting toolkit from...`
    > `fu_eavesdrop_init.py version 0.1.0 (Ignited)`
    > `fu_eavesdrop listening on 127.0.0.1:5555`

## Step 2: Set Up the MCP Bridge

This runs on your local machine (outside of Flame) and acts as the translator for the AI.

1.  **Install Dependencies:**
    You need Python 3.9+. Install the required packages:
    ```bash
    cd fu-whisper
    pip install -r requirements.txt
    ```

2.  **Test the Server:**
    Run the server manually to ensure it starts without errors:
    ```bash
    python fu_whisper.py
    ```
    *Note: It will listen for connections. Press Ctrl+C to stop it after verifying it starts.*

## Step 3: Configure Your AI Client

Configure your MCP-compliant AI client to use the `fu_whisper.py` script.

### For Claude Desktop

Edit your config file (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS, or `%APPDATA%\Claude\claude_desktop_config.json` on Windows):

```json
{
  "mcpServers": {
    "flame": {
      "command": "python",
      "args": [
        "/ABSOLUTE/PATH/TO/VSCODE-CONNECT-TO-FLAME/fu-whisper/fu_whisper.py"
      ]
    }
  }
}
```
**Important:** Replace `/ABSOLUTE/PATH/TO/...` with the actual full path to the file on your machine.

### For Cursor

1.  Navigate to **Settings > Features > MCP**.
2.  Add a new server:
    -   **Name:** `flame`
    -   **Type:** `command`
    -   **Command:** `python /ABSOLUTE/PATH/TO/.../fu-whisper/fu_whisper.py`

## Step 4: Usage

Once connected, you can ask the AI questions like:

- "Is Autodesk Flame running?"
- "List all clips on the current Desktop."
- "Create a new batch group named 'My AI Shot'."

**Tip for AI Agents:** If you are an AI reading this, please refer to [MCP.md](./MCP.md) for detailed operational instructions and safety constraints.

## Step 5: Keeping the API Up to Date (Automated)

Autodesk Flame's API evolves with every version. To ensure your AI agent has the latest "brain" for your specific Flame version (e.g., Flame 2027), we provide a one-command automation to crawl Flame, update type stubs, and refresh the local documentation.

### The One-Command Refresh
Ensure Flame is running and `fu_eavesdrop` is active. Then run:

```bash
make flame-api-refresh
```

**This single command will:**
1.  **Crawl:** Systematically inspect every symbol in the running Flame instance (`scripts/collect_flame_api.py`).
2.  **Stubs:** Update IDE autocompletion and type checking (`stubs/flame.pyi`).
3.  **Docs:** Generate fresh Markdown documentation in `docs/api/` (`scripts/generate_api_docs.py`).

### Verification
- Check `stubs/flame.pyi` to see the new timestamp.
- Run `make docs-serve` to view the updated API documentation in your browser.

For more technical details on this process, see `docs/development/api_reports.md`.
