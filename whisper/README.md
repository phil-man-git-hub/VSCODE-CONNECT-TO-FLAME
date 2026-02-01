# FU_Whisper (Flame MCP Bridge)

This is a Model Context Protocol (MCP) server that allows AI agents to interact directly with Autodesk Flame via the **fu_eavesdrop** listener.

## Prerequisites
- Python 3.9+
- A running instance of Autodesk Flame with the `fu_eavesdrop.py` active.

## Installation

1.  Navigate to this directory:
    ```bash
    cd flame-mcp
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running Locally
You can run the server directly to test it:
```bash
python fu_whisper.py
```

### Connecting to an AI Client
To use this with a client like **Claude Desktop**, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "fu_whisper": {
      "command": "python",
      "args": ["/path/to/flame-mcp/fu_whisper.py"]
    }
  }
}
```

## Available Tools
- `ping_flame`: Verifies the connection to Flame.
- `get_mcp_status`: Returns current bridge health and mode.
- `execute_python`: Runs Python code in Flame.
- `get_flame_context`: Gets project/user info.
- `list_desktop_clips`: Lists media on desktop.
- `inspect_symbol`: API discovery tool.

---
*Part of the FLAME-UTILITIES (fu_) suite.*
