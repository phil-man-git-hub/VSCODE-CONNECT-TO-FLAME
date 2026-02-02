#!/usr/bin/env python3
"""
FLAME Project Metadata Inspector
===============================

This utility script gathers comprehensive information about the current Autodesk Flame project,
including basic properties, paths, workspace/desktop details, and extensive Wiretap metadata.

It demonstrates how to:
- Access Flame project objects via Python API
- Use Wiretap tools to retrieve detailed project metadata from XML
- Parse and extract metadata fields for analysis or integration

Author: GitHub Copilot (assisted by FLAME-UTILITIES framework)
Date: February 2, 2026
Version: 1.0
License: MIT (see project LICENSE)

Usage:
    python inspect_project_metadata.py
    # Or import and call: from inspect_project_metadata import gather_project_info; info = gather_project_info()

Dependencies:
    - flame (Autodesk Flame Python API)
    - subprocess (for running Wiretap tools)
    - xml.etree.ElementTree (for parsing XML metadata)
    - json (for output formatting)
    - fu_relay (for executing code in Flame from external scripts)

Note: This script must be run within the Flame Python environment or via fu_relay.
"""

import flame
import subprocess
import xml.etree.ElementTree as ET
import json


def safe_val(val):
    """
    Safely convert a value to a string, handling None values and stripping quotes.

    Args:
        val: The value to convert (can be None, string, or other type)

    Returns:
        str or None: The string representation, or None if input was None
    """
    if val is None:
        return None
    # Strip surrounding quotes that Flame sometimes adds
    return str(val).strip("'")


def gather_wiretap_metadata(node_id):
    """
    Retrieve comprehensive metadata for a project using Wiretap tools.

    This function uses the wiretap_get_metadata command-line tool to fetch
    detailed XML metadata about the project node, then parses it into a dictionary.

    Args:
        node_id (str): The Wiretap node ID (e.g., '/projects/uuid')

    Returns:
        dict: Dictionary of metadata key-value pairs from the XML, or None if failed
    """
    # Path to the Wiretap metadata tool (standard Flame installation location)
    tool_path = '/opt/Autodesk/wiretap/tools/current/wiretap_get_metadata'

    # Command to get XML metadata for the specified node
    cmd = [tool_path, '-n', node_id, '-m', 'XML']

    try:
        # Run the command with a 10-second timeout
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)

        if res.returncode == 0 and res.stdout.strip():
            # Parse the XML output
            root = ET.fromstring(res.stdout)

            # Extract all non-empty text elements into a dictionary
            metadata = {}
            for elem in root.iter():
                if elem.text and elem.text.strip():
                    metadata[elem.tag] = elem.text.strip()

            return metadata
        else:
            print(f"Error running wiretap_get_metadata: {res.stderr}")
            return None

    except subprocess.TimeoutExpired:
        print("Timeout while running wiretap_get_metadata")
        return None
    except Exception as e:
        print(f"Exception while gathering Wiretap metadata: {e}")
        return None


def gather_project_info():
    """
    Gather comprehensive information about the current Flame project.

    This is the main function that collects all available project information
    from multiple sources: Flame Python API and Wiretap metadata.

    Returns:
        dict: Complete project information including:
            - Basic properties (name, nickname, description)
            - Wiretap identifiers (node_id, storage_id)
            - File system paths
            - Current workspace and desktop info
            - Desktop structure (batch/reel counts)
            - Full Wiretap metadata dictionary
    """
    # Get the current project object
    p = flame.project.current_project

    # Get the current workspace
    w = p.current_workspace

    # Get the current desktop (may be None if no desktop is active)
    d = w.desktop if w else None

    # Build the basic project information dictionary
    data = {
        'name': safe_val(p.name),  # Project display name
        'nickname': safe_val(p.nickname),  # Project short name
        'description': safe_val(p.description),  # Project description
        'wiretap_node_id': safe_val(p.get_wiretap_node_id()),  # Unique Wiretap identifier
        'wiretap_storage_id': safe_val(p.get_wiretap_storage_id()) if hasattr(p, 'get_wiretap_storage_id') else None,  # Storage identifier if available
        'paths': {
            'project_folder': safe_val(p.project_folder),  # Root project directory
            'setups_folder': safe_val(p.setups_folder),   # Setups directory
            'media_folder': safe_val(p.media_folder),     # Media directory
        },
        'workspace': {
            'name': safe_val(w.name),  # Current workspace name
            'desktop_name': safe_val(d.name) if d else None  # Current desktop name
        },
        'desktop': {
            'batch_groups_count': len(d.batch_groups) if d else 0,  # Number of batch groups
            'reel_groups_count': len(d.reel_groups) if d else 0     # Number of reel groups
        }
    }

    # Gather Wiretap metadata using the node ID
    node_id = p.get_wiretap_node_id()
    if node_id:
        wiretap_metadata = gather_wiretap_metadata(node_id)
        if wiretap_metadata:
            data['wiretap_metadata'] = wiretap_metadata
        else:
            data['wiretap_metadata'] = None  # Indicate metadata gathering failed
    else:
        data['wiretap_metadata'] = None  # No node ID available

    return data


def main():
    """
    Main entry point when running this script directly.

    Gathers project information and prints it as formatted JSON.
    This allows the script to be used both as a module and as a standalone tool.
    """
    # Gather all project information
    project_info = gather_project_info()

    # Print the information as nicely formatted JSON
    print(json.dumps(project_info, indent=2))


if __name__ == "__main__":
    # Only run main() if this script is executed directly (not imported)
    main()</content>
<parameter name="filePath">/Users/pman/workspace/GitHub/phil-man-git-hub/VSCODE-CONNECT-TO-FLAME/fu-whisper/library/inspect_project_metadata.py