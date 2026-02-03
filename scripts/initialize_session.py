#!/usr/bin/env python3
"""
Session Initialization Script for FLAME-UTILITIES
-------------------------------------------------
This script prepares the environment for an AI Agent (Copilot, Gemini, etc.)
by verifying connectivity, starting the MCP bridge, and generating a 
concise context summary.
"""

import sys
import socket
import json
import subprocess
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, Union

# Constants
PORT = 5555
MCP_REL_PATH = Path("fu-whisper/fu_whisper.py")
VENV_PYTHON = Path(".venv/bin/python")

# Ensure critical paths exist relative to CWD or Script
# If running from repo root (standard), these should exist.
if not VENV_PYTHON.exists():
    # Fallback/Warnings could go here, but for now we just define them.
    # We will check them in main() before usage to be safe.
    pass

# Global Logger
logger = logging.getLogger("session_init")

def setup_logging() -> Path:
    """Configures logging to both console and file."""
    # Use Path for log directory resolving
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"session_init_{timestamp}.log"

    # File Handler - Detailed Debug info
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    # Console Handler - User friendly (Info level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # Simple format for console to mimic print()
    console_format = logging.Formatter('%(message)s')
    console_handler.setFormatter(console_format)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    logger.debug(f"Logging initialized. Log file: {log_file}")
    return log_file

def check_listener() -> bool:
    """Checks if the fu_eavesdrop listener is running inside Flame."""
    logger.debug(f"Checking for Flame Listener on 127.0.0.1:{PORT}...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            s.connect(("127.0.0.1", PORT))
            logger.debug("Listener connection successful.")
            return True
    except ConnectionRefusedError:
        logger.debug("Listener connection refused (not running?).")
        return False
    except Exception as e:
        logger.debug(f"Listener connection failed: {e}")
        return False

def check_mcp_server() -> bool:
    """Checks if the fu_whisper MCP server is running (via pgrep)."""
    try:
        # pgrep returns exit code 0 if found, 1 if not
        # -f matches against the full command line
        result = subprocess.check_output(["pgrep", "-f", str(MCP_REL_PATH)], text=True)
        logger.debug(f"MCP Server check (pgrep) found process: {result.strip()}")
        return True
    except subprocess.CalledProcessError:
        logger.debug("MCP Server check (pgrep) found no process.")
        return False
    except FileNotFoundError:
        logger.warn("pgrep command not found on system. Assuming MCP not active.")
        return False
    except Exception as e:
        logger.debug(f"Unexpected error checking MCP server: {e}")
        return False

def get_flame_context() -> Optional[Dict[str, Any]]:
    """Retrieves basic context from Flame if reachable."""
    if not check_listener():
        return None
    
    # We construct a python script to run inside Flame
    payload = (
        "import flame, json; "
        "print(json.dumps({'p': flame.project.current_project.name, 'v': flame.get_version()}))"
    )
    
    try:
        # Use simple relay-style execution
        # Ensure fu-whisper is in sys.path to import FlameRelay
        mcp_dir = Path.cwd() / "fu-whisper"
        if str(mcp_dir) not in sys.path:
            sys.path.append(str(mcp_dir))
            
        from fu_relay import FlameRelay # type: ignore
        relay = FlameRelay()
        resp = relay.execute(payload)
        
        stdout_str = resp.get("stdout", "{}")
        ctx = json.loads(stdout_str)
        logger.debug(f"Retrieved Flame Context: {ctx}")
        return ctx
    except ImportError:
        logger.error("Could not import FlameRelay. Ensure fu-whisper is available.")
        return None
    except Exception as e:
        logger.debug(f"Failed to retrieve Flame Context: {e}")
        return None

def main() -> None:
    log_file = setup_logging()
    
    cwd = Path.cwd()
    logger.info("🚀 Initializing FLAME-UTILITIES Session...\n")
    logger.debug(f"Script started from: {cwd}")
    logger.debug(f"Python executable: {sys.executable}")

    # 1. Check Listener
    listener_active = check_listener()
    if not listener_active:
        logger.error("❌ ERROR: fu_eavesdrop listener not found on port 5555.")
        logger.info("   Please ensure Autodesk Flame is running and the fu_eavesdrop startup hook is active.")
        sys.exit(1)
    logger.info("✅ Flame Listener: Active")

    # 2. Check/Start MCP Bridge
    mcp_active = check_mcp_server()
    if not mcp_active:
        logger.info("🌀 Starting FU_Whisper MCP Bridge in background...")
        
        mcp_log_file = Path("fu-whisper/logs/mcp_server.log")
        mcp_log_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Validation
        if not VENV_PYTHON.exists():
            logger.error(f"❌ Critical Error: Virtual environment python not found at {VENV_PYTHON}.")
            logger.info("   Please run 'uv sync' or create the .venv before proceeding.")
            sys.exit(1)
            
        if not MCP_REL_PATH.exists():
             logger.error(f"❌ Critical Error: MCP Server script not found at {MCP_REL_PATH}.")
             sys.exit(1)

        # Construct path for PYTHONPATH
        # Add the 'fu-whisper' directory so imports inside it work correctly
        env = os.environ.copy() # Need os for environ
        env["PYTHONPATH"] = f"{env.get('PYTHONPATH', '')}:{cwd / 'fu-whisper'}"
        
        logger.debug(f"Launching MCP with PYTHONPATH: {env['PYTHONPATH']}")
        
        try:
            with open(mcp_log_file, "a") as f:
                subprocess.Popen(
                    [str(VENV_PYTHON), str(MCP_REL_PATH)], 
                    stdout=f, 
                    stderr=f, 
                    env=env
                )
            time.sleep(2) # Give it a moment to bind
            logger.debug("MCP Bridge launch command issued.")
        except FileNotFoundError:
            logger.error(f"Failed to launch MCP Bridge. Could not find binary or script: {VENV_PYTHON} or {MCP_REL_PATH}")
    else:
        logger.debug("MCP Bridge already running.")
        
    logger.info("✅ MCP Bridge: Running")

    # 3. Check RAG
    rag_exists = Path("chroma_db").exists()
    logger.info(f"{('✅' if rag_exists else '⚠️')} RAG Knowledge Layer: {'Indexed' if rag_exists else 'Not Found (run build_rag.py)'}")

    # 4. Gather context
    ctx = get_flame_context()
    p_name = ctx.get("p", "Unknown") if ctx else "Unknown"
    v_name = ctx.get("v", "Unknown") if ctx else "Unknown"

    # 5. Generate Handshake Prompt
    logger.info("\n" + "="*60)
    logger.info("📋 COPY AND PASTE THE PROMPT BELOW TO YOUR AI AGENT")
    logger.info("="*60 + "\n")
    
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
    
    logger.info(bootstrap_prompt)
    logger.info("\n" + "="*60)
    logger.debug(f"Session initialization complete. Log saved to: {log_file}")

if __name__ == "__main__":
    import os # Needed because we removed it from top-level but main uses it partially or env copy
    # Re-adding os to top imports to be clean
    main()
