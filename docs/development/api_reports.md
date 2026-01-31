# How to Generate Flame API Reports

This guide explains how to systematically crawl the running Autodesk Flame Python API to generate detailed JSON reports of all available modules, classes, functions, and properties.

**Target Audience:** Developers and AI Agents (Gemini).

## Prerequisites

1.  **Autodesk Flame** must be running.
2.  The **fu_eavesdrop** listener must be deployed and active.
    *   *Check:* You should see `fu_eavesdrop listening on 127.0.0.1:5555` in the Flame console.
*   **Deploy:** If not running, follow the instructions in `docs/setup/deploy.md`.

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

### 3. Generate Type Stubs (Optional but Recommended)
To update the IDE autocompletion and type checking files, run:

```bash
python scripts/generate_stubs_from_reports.py --latest
```

This will update `stubs/flame.pyi` with the signatures and docstrings extracted from the latest crawl.

## Instructions for AI Agents (Gemini)

If you are an AI assistant tasked with updating the API definitions or checking for version compatibility, follow this protocol:

1.  **Verify Connection:**
    Run a ping check via the **fu_whisper** bridge or use `nc -zv 127.0.0.1 5555`.
2.  **Execute Crawl:**
    Run `python scripts/collect_flame_api.py --include-all`.
3.  **Ingest Results:**
    Read the generated `reports/api_dump/<latest_timestamp>/index.json` to understand the scope.
    Read specific `<Symbol>.json` files to update your internal knowledge or generate type stubs (`.pyi`).

## Troubleshooting

*   **Connection Refused:** `fu_eavesdrop` is not running in Flame. Check `flame.project.json` or your manual deployment.
*   **Timeout:** The API might be busy. The script waits 10s per request. Ensure Flame is not blocked by a modal dialog.