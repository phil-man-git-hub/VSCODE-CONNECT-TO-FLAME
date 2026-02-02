from fastmcp import FastMCP
import os
import sys

# Ensure the whisper directory is in path for imports
sys.path.append(os.path.dirname(__file__))
from fu_relay import FlameRelay

import json
import logging
from datetime import datetime
from dotenv import load_dotenv

# RAG imports
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
import chromadb

# Load environment variables from repo root
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# Setup logging
import logging
logging.basicConfig(level=logging.INFO, format='[fu_whisper][%(levelname)s] %(message)s')
logger = logging.getLogger("fu_whisper")

# Setup Audit Logging
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "mcp_audit.log")

# ... rest of logging ...

# Code Library Setup
LIBRARY_DIR = os.path.join(os.path.dirname(__file__), "library")
os.makedirs(LIBRARY_DIR, exist_ok=True)

# Initialize the MCP Server
mcp = FastMCP("FU_Whisper")

# Configuration
READ_ONLY = os.getenv("FLAME_READ_ONLY", "false").lower() == "true"
COMFY_ENABLED = os.getenv("COMFY_ENABLED", "false").lower() == "true"

# Initialize the Relay
relay = FlameRelay(
    host=os.getenv("FLAME_HOST", "127.0.0.1"),
    port=int(os.getenv("FLAME_PORT", 5555))
)

# Initialize RAG Index
rag_index = None
try:
    chroma_client = chromadb.PersistentClient(path=os.path.join(os.path.dirname(os.path.dirname(__file__)), "chroma_db"))
    chroma_collection = chroma_client.get_collection("flame_docs")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    rag_index = VectorStoreIndex.from_vector_store(vector_store, storage_context=storage_context, embed_model=OllamaEmbedding(model_name="nomic-embed-text"))
    logger.info("RAG index loaded successfully.")
except Exception as e:
    logger.warning(f"Failed to load RAG index: {e}. query_flame_docs will be unavailable.")

# Optional ComfyUI Integration
comfy_client = None
if COMFY_ENABLED:
    try:
        # Add fu-comfyui to path
        sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "fu-comfyui"))
        from fu_comfyui import ComfyUIClient, get_comfy_status
        comfy_client = ComfyUIClient(os.getenv("COMFY_SERVER", "127.0.0.1:8188"))
        logger.info("ComfyUI Integration enabled.")
    except Exception as e:
        logger.error(f"Failed to initialize ComfyUI Integration: {e}")
        COMFY_ENABLED = False

def audit_log(tool_name: str, input_data: any, result: str):
    """Logs the details of every tool execution for security and debugging."""
    timestamp = datetime.now().isoformat()
    
    # Full entry for file log
    full_entry = {
        "timestamp": timestamp,
        "tool": tool_name,
        "input": input_data,
        "read_only_mode": READ_ONLY,
        "result": result 
    }
    
    # Summary for console
    summary_msg = f"TOOL: {tool_name} | STATUS: {'Success' if 'Error' not in result[:50] else 'Possible Error'}"
    
    # Log with extra data for the file handler to pick up
    logger.info(summary_msg, extra={'json_data': full_entry})

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

@mcp.tool()
def query_flame_docs(query: str) -> str:
    """Queries the Flame API documentation using RAG to find relevant information about Flame Python API."""
    if rag_index is None:
        msg = "RAG index not available. Please ensure the documentation has been indexed."
        audit_log("query_flame_docs", {"query": query}, msg)
        return msg
    
    try:
        query_engine = rag_index.as_query_engine(similarity_top_k=5)
        response = query_engine.query(query)
        result = str(response)
        audit_log("query_flame_docs", {"query": query}, "Success")
        return result
    except Exception as e:
        msg = f"Error querying documentation: {str(e)}"
        audit_log("query_flame_docs", {"query": query}, msg)
        return msg

# --- Code Library Tools ---

@mcp.tool()
def save_snippet(name: str, code: str, description: str = "") -> str:
    """Saves a working Python code snippet to the local library for future reuse.
    
    Args:
        name: A short, descriptive name for the function/snippet (e.g., 'export_selected_clips').
              Alphanumeric and underscores only.
        code: The Python code to save.
        description: A brief explanation of what the code does.
    """
    if READ_ONLY:
        return "REJECTED: Cannot save snippets in Read-Only mode."
        
    # Sanitize name
    safe_name = "".join(c for c in name if c.isalnum() or c == '_')
    if not safe_name:
        return "Error: Invalid name. Use alphanumeric characters and underscores."
        
    filename = os.path.join(LIBRARY_DIR, f"{safe_name}.py")
    
    # Add docstring to code if description is provided
    final_code = code
    if description:
        final_code = f'"""\n{description}\n"""\n\n{code}'
        
    try:
        with open(filename, 'w') as f:
            f.write(final_code)
        msg = f"Successfully saved snippet '{safe_name}' to library."
        audit_log("save_snippet", {"name": safe_name, "description": description}, msg)
        return msg
    except Exception as e:
        msg = f"Error saving snippet: {str(e)}"
        audit_log("save_snippet", {"name": safe_name}, msg)
        return msg

@mcp.tool()
def read_snippet(name: str) -> str:
    """Retrieves the code for a saved snippet from the library."""
    safe_name = "".join(c for c in name if c.isalnum() or c == '_')
    filename = os.path.join(LIBRARY_DIR, f"{safe_name}.py")
    
    if not os.path.exists(filename):
        msg = f"Error: Snippet '{safe_name}' not found."
        audit_log("read_snippet", {"name": safe_name}, msg)
        return msg
        
    try:
        with open(filename, 'r') as f:
            content = f.read()
        audit_log("read_snippet", {"name": safe_name}, "Success (content retrieved)")
        return content
    except Exception as e:
        msg = f"Error reading snippet: {str(e)}"
        audit_log("read_snippet", {"name": safe_name}, msg)
        return msg

@mcp.tool()
def list_library() -> str:
    """Lists all available snippets in the local library."""
    try:
        files = [f[:-3] for f in os.listdir(LIBRARY_DIR) if f.endswith('.py')]
        if not files:
            result = "Library is empty."
        else:
            result = "Available Snippets:\n" + "\n".join(f"- {f}" for f in sorted(files))
        
        audit_log("list_library", {}, result)
        return result
    except Exception as e:
        return f"Error listing library: {str(e)}"

if __name__ == "__main__":
    # Ensure logger is defined before use
    try:
        logger
    except NameError:
        import logging
        logging.basicConfig(level=logging.INFO, format='[fu_whisper][%(levelname)s] %(message)s')
        logger = logging.getLogger("fu_whisper")

    try:
        import flame # type: ignore
        # We are inside Flame (auto-hook crawl). Do nothing.
    except ImportError:
        logger.info(f"Starting Flame MCP Server (Read-Only: {READ_ONLY})")
        mcp.run()