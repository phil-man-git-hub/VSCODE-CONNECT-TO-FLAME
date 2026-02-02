#!/usr/bin/env python3
"""
Session Initialization Script for FLAME-UTILITIES
-------------------------------------------------
This script prepares the environment for an AI Agent (Copilot, Gemini, etc.)
by verifying connectivity, starting the MCP bridge, and generating a 
concise context summary.
"""

import os
import sys
import socket
import json
import subprocess
import time

# Constants
PORT = 5555
MCP_PATH = "fu-whisper/fu_whisper.py"
VENV_PYTHON = ".venv/bin/python"

def check_listener():
    """Checks if the fu_eavesdrop listener is running inside Flame."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            s.connect(("127.0.0.1", PORT))
            return True
    except:
        return False

def check_mcp_server():
    """Checks if the fu_whisper MCP server is running (via pgrep)."""
    try:
        result = subprocess.check_output(["pgrep", "-f", MCP_PATH])
        return True
    except:
        return False

def get_flame_context():
    """Retrieves basic context from Flame if reachable."""
    if not check_listener():
        return None
    
    code = "import flame; print(json.dumps({'project': flame.project.current_project.name, 'version': flame.get_version()}))"
    try:
        # Use simple relay-style execution
        from fu_relay import FlameRelay
        relay = FlameRelay()
        resp = relay.execute("import flame, json; print(json.dumps({'p': flame.project.current_project.name, 'v': flame.get_version()}))")
        return json.loads(resp.get("stdout", "{}"))
    except:
        return None

def main():
    print("🚀 Initializing FLAME-UTILITIES Session...\n")

    # 1. Check Listener
    listener_active = check_listener()
    if not listener_active:
        print("❌ ERROR: fu_eavesdrop listener not found on port 5555.")
        print("   Please ensure Autodesk Flame is running and the fu_eavesdrop startup hook is active.")
        sys.exit(1)
    print("✅ Flame Listener: Active")

    # 2. Check/Start MCP Bridge
    mcp_active = check_mcp_server()
    if not mcp_active:
        print("🌀 Starting FU_Whisper MCP Bridge in background...")
        log_file = "fu-whisper/logs/mcp_server.log"
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        # Construct path for PYTHONPATH
        abs_root = os.getcwd()
        env = os.environ.copy()
        env["PYTHONPATH"] = f"{env.get('PYTHONPATH', '')}:{abs_root}/fu-whisper"
        
        with open(log_file, "a") as f:
            subprocess.Popen([VENV_PYTHON, MCP_PATH], stdout=f, stderr=f, env=env)
        time.sleep(2) # Give it a moment to bind
    print("✅ MCP Bridge: Running")

    # 3. Check RAG
    rag_exists = os.path.exists("chroma_db")
    print(f"{('✅' if rag_exists else '⚠️')} RAG Knowledge Layer: {'Indexed' if rag_exists else 'Not Found (run build_rag.py)')}")

    # 4. Gather context
    ctx = get_flame_context()
    p_name = ctx.get("p", "Unknown") if ctx else "Unknown"
    v_name = ctx.get("v", "Unknown") if ctx else "Unknown"

    # 5. Generate Handshake Prompt
    print("\n" + "="*60)
    print("📋 COPY AND PASTE THE PROMPT BELOW TO YOUR AI AGENT")
    print("="*60 + "\n")
    
    bootstrap_prompt = (
        f"I am working in the FLAME-UTILITIES repository. "
        f"The environment is ACTIVE. "
        f"Flame Version: {v_name} | Current Project: {p_name}\n\n"
        "Please perform the following initialization steps:\n"
        "1. Read MCP.md to understand your profile as a 'Flame Finishing Specialist' and your MCP tools.\n"
        "2. Read GEMINI.md for the current technical state and recent achievements (OTIO, Batch, Wiretap).\n"
        "3. Use the 'query_flame_docs' tool if you need to look up specific Flame API or architecture details from the RAG database.\n"
        "4. Use 'ping_flame' to confirm you can reach the live instance."
    )
    
    print(bootstrap_prompt)
    print("\n" + "="*60)

if __name__ == "__main__":
    # Add fu-whisper to sys.path so we can import FlameRelay for the context check
    sys.path.append(os.path.join(os.getcwd(), "fu-whisper"))
    main()
