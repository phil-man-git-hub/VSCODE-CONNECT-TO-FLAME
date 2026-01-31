from fastmcp import FastMCP
from relay import FlameRelay
import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup Audit Logging
LOG_FILE = "mcp_audit.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("FlameMCP")

# Initialize the MCP Server
mcp = FastMCP("FlameConnector")

# Configuration
READ_ONLY = os.getenv("FLAME_READ_ONLY", "false").lower() == "true"

# Initialize the Relay
relay = FlameRelay(
    host=os.getenv("FLAME_HOST", "127.0.0.1"),
    port=int(os.getenv("FLAME_PORT", 5555))
)

def audit_log(tool_name: str, input_data: any, result: str):
    """Logs the details of every tool execution for security and debugging."""
    entry = {
        "timestamp": datetime.now().isoformat(),
        "tool": tool_name,
        "input": input_data,
        "read_only_mode": READ_ONLY,
        "result_summary": result[:200] + "..." if len(result) > 200 else result
    }
    logger.info(f"TOOL_CALL: {json.dumps(entry)}")

@mcp.tool()
def ping_flame() -> str:
    """Verifies the end-to-end connection: AI -> MCP -> Listener -> Flame."""
    success = relay.ping()
    result = "Pong! Successfully connected to Autodesk Flame." if success else "Failed to connect to Flame."
    audit_log("ping_flame", {}, result)
    return result

@mcp.tool()
def execute_python(code: str, timeout: float = 5.0) -> str:
    """Executes arbitrary Python code inside Autodesk Flame and returns the output."""
    if READ_ONLY:
        msg = "REJECTED: Flame MCP is in Read-Only mode. python_execute is disabled."
        audit_log("execute_python", {"code": code}, msg)
        return msg

    logger.info(f"Executing Python code in Flame (Timeout: {timeout}s)")
    result = relay.execute(code, timeout=timeout)
    
    output = []
    if result.get("stdout"):
        output.append(f"STDOUT:\n{result['stdout']}")
    if result.get("stderr"):
        output.append(f"STDERR:\n{result['stderr']}")
    if result.get("exception"):
        output.append(f"EXCEPTION: {result['exception']}")
        
    final_result = "\n\n".join(output) if output else "Execution completed with no output."
    audit_log("execute_python", {"code": code}, final_result)
    return final_result

@mcp.tool()
def get_flame_context() -> str:
    """Retrieves current Flame environment details (Project, User, Version)."""
    code = """
import flame
import json

context = {
    "project": flame.project.current_project.name if hasattr(flame, 'project') else "Unknown",
    "user": flame.users.current_user.name if hasattr(flame, 'users') else "Unknown",
    "version": f"{flame.get_version()}" if hasattr(flame, 'get_version') else "Unknown",
    "host": flame.get_home_directory() if hasattr(flame, 'get_home_directory') else "Unknown"
}
print(json.dumps(context))    """
    result = relay.execute(code)
    response = result.get("stdout", "Error")
    audit_log("get_flame_context", {}, response)
    
    if result.get("stdout"):
        try:
            data = json.loads(result["stdout"])
            return json.dumps(data, indent=2)
        except:
            return result["stdout"]
    return f"Error retrieving context: {result.get('stderr', 'Unknown error')}"

@mcp.tool()
def list_desktop_clips() -> str:
    """Lists all clips and sequences currently on the Flame Desktop."""
    code = """
import flame
import json

desktop = flame.project.current_project.current_workspace.desktop
entries = []

for clip in desktop.clips:
    entries.append({"type": "Clip", "name": clip.name.decode('utf-8') if isinstance(clip.name, bytes) else clip.name})

for seq in desktop.sequences:
    entries.append({"type": "Sequence", "name": seq.name.decode('utf-8') if isinstance(seq.name, bytes) else seq.name})

print(json.dumps(entries))    """
    result = relay.execute(code)
    response = result.get("stdout", "Error")
    audit_log("list_desktop_clips", {}, response)

    if result.get("stdout"):
        try:
            data = json.loads(result["stdout"])
            if not data:
                return "The Desktop is empty."
            return "\n".join([f"-[{item['type']}] {item['name']}" for item in data])
        except:
            return result["stdout"]
    return f"Error listing clips: {result.get('stderr', 'Unknown error')}"

@mcp.tool()
def inspect_symbol(symbol_name: str) -> str:
    """Provides documentation and properties for a specific Flame Python symbol (e.g., 'flame.PyClip')."""
    code = f"""
import flame
import json

try:
    target = eval("{symbol_name}")
    info = {{
        "name": "{symbol_name}",
        "type": str(type(target)),
        "doc": target.__doc__ if hasattr(target, '__doc__') else "No documentation available.",
        "dir": [item for item in dir(target) if not item.startswith('_')]
    }}
    print(json.dumps(info))
except Exception as e:
    print(f"Error inspecting {symbol_name}: {{str(e)}}")    """
    result = relay.execute(code)
    response = result.get("stdout", "Error")
    audit_log("inspect_symbol", {"symbol": symbol_name}, response)

    if result.get("stdout"):
        try:
            data = json.loads(result["stdout"])
            output = [
                f"Symbol: {data['name']}",
                f"Type: {data['type']}",
                f"Documentation: {data['doc']}",
                "\nAvailable Methods/Properties:",
                ", ".join(data['dir'])
            ]
            return "\n".join(output)
        except:
            return result["stdout"]
    return f"Error inspecting symbol: {result.get('stderr', 'Unknown error')}"

@mcp.tool()
def get_mcp_status() -> str:
    """Returns the current status of the Flame MCP Bridge."""
    status = "Online" if relay.ping() else "Offline"
    mode = "Read-Only" if READ_ONLY else "Full-Access"
    result = f"Flame MCP Bridge is {status} (Mode: {mode})."
    audit_log("get_mcp_status", {}, result)
    return result

if __name__ == "__main__":
    logger.info(f"Starting Flame MCP Server (Read-Only: {READ_ONLY})")
    mcp.run()