# Getting Started with FU_Whisper (Flame MCP Bridge)

The **FU_Whisper** bridge allows you to connect AI models (like Claude or Gemini) directly to your Autodesk Flame session via the **fu_eavesdrop** listener.

## 1. Prerequisites
- **Autodesk Flame**: Installed and running.
- **Python 3.9+**: Installed on your system.
- **fu_eavesdrop**: The `fu_eavesdrop.py` script must be running inside Flame (archived in your project setup).

## 2. Local Setup

1. **Install Dependencies**:
   ```bash
   cd flame-utilities/whisper
   pip install -r requirements.txt
   ```

2. **Verify Connection**:
   Ensure the **fu_eavesdrop** listener is active in Flame, then run the bridge locally:
   ```bash
   python fu_whisper.py
   ```
   You should see a message saying `Starting FU_Whisper Server`.

## 3. Connecting to AI Clients

### Claude Desktop
1. Open your Claude Desktop configuration file:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the FU_Whisper server to the `mcpServers` object:
   ```json
   {
     "mcpServers": {
       "fu_whisper": {
         "command": "python",
         "args": ["/ABSOLUTE/PATH/TO/VSCODE-CONNECT-TO-FLAME/flame-utilities/whisper/fu_whisper.py"]
       }
     }
   }
   ```
3. Restart Claude Desktop.

### Cursor
1. Go to **Settings** -> **Features** -> **MCP**.
2. Click **+ Add New MCP Server**.
3. Name: `FU_Whisper`
4. Type: `command`
5. Command: `python /ABSOLUTE/PATH/TO/VSCODE-CONNECT-TO-FLAME/flame-utilities/whisper/fu_whisper.py`

## 4. First Steps with the AI
Try asking the AI:
- "Check the connection to Flame."
- "What project am I currently in?"
- "List the clips on my desktop."

---
*The whisper bridge is part of the archived flame-utilities toolkit.*