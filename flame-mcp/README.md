# Flame MCP Bridge

This is a Model Context Protocol (MCP) server that allows AI agents to interact directly with Autodesk Flame via the `flame-listener`.

## Prerequisites
- Python 3.9+
- A running instance of Autodesk Flame with the `flame-listener.py` active.

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
python server.py
```

### Connecting to an AI Client
To use this with a client like **Claude Desktop**, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "flame": {
      "command": "python",
      "args": ["/path/to/flame-mcp/server.py"]
    }
  }
}
```

## Available Tools
- `ping_flame`: Verifies the connection to Flame.
- `get_mcp_status`: Returns current bridge health.

---
*Part of the VSCODE-CONNECT-TO-FLAME project.*
