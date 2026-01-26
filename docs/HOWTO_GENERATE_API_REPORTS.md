# How to Generate Flame API Reports

This guide explains how to systematically crawl the running Autodesk Flame Python API to generate detailed JSON reports of all available modules, classes, functions, and properties.

**Target Audience:** Developers and AI Agents (Gemini).

## Prerequisites

1.  **Autodesk Flame** must be running.
2.  The **Flame Listener** must be deployed and active in the current project.
    *   *Check:* You should see `Flame listener listening on 127.0.0.1:5555` in the Flame shell/logs.
    *   *Deploy:* If not running, use `python scripts/deploy_to_flame_project.py --copy --scripts-dir <PATH_TO_PROJECT_PYTHON_SETUPS>` and restart Flame.

## Step-by-Step Guide

### 1. Run the Collector Script
Open a terminal in the repository root and run:

```bash
python scripts/collect_flame_api.py --include-all
```

*   `--include-all`: Forces the script to inspect **every** discovered symbol (classes, functions, singletons) instead of just the core `Py*` classes.

### 2. Locate the Output
The script creates a timestamped directory for each run:

```text
reports/api_dump/YYYY-MM-DD_HH-MM-SS/
```

Inside you will find:
*   `index.json`: A summary of all crawled items.
*   `<SymbolName>.json`: Detailed introspection for each object (e.g., `PyBatch.json`, `execute_command.json`).

### 3. Compare Versions (Optional)
To see what changed between Flame versions (e.g., `pr235` vs `pr236`):
1.  Run the collector on the old version.
2.  Run the collector on the new version.
3.  Compare the two timestamped directories using `diff` or a visual diff tool.

## Instructions for AI Agents (Gemini)

If you are an AI assistant tasked with updating the API definitions or checking for version compatibility, follow this protocol:

1.  **Verify Connection:**
    Run `python scripts/verify_listener.py` to confirm the bridge is active.
2.  **Execute Crawl:**
    Run `python scripts/collect_flame_api.py --include-all`.
3.  **Ingest Results:**
    Read the generated `reports/api_dump/<latest_timestamp>/index.json` to understand the scope.
    Read specific `<Symbol>.json` files to update your internal knowledge or generate type stubs (`.pyi`).

## Troubleshooting

*   **Connection Refused:** The listener is not running in Flame. Check `flame.project.json` or your deployment paths.
*   **Timeout:** The API might be busy. The script waits 10s per request. Ensure Flame is not blocked by a modal dialog.
