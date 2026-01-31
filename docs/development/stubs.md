# Flame API Stubs

VS Code cannot inspect Flame's embedded Python interpreter at design time. To provide IntelliSense, autocompletion, and hover documentation, we ship high-quality `.pyi` stub files.

## Generation Pipeline

We use a two-phase automated pipeline to ensure the stubs are always accurate and up-to-date with your current Flame version.

### 1. JSON Report Collection
The first step is to crawl the running Flame API using `scripts/collect_flame_api.py`. This script uses deep introspection to capture:
- Class hierarchies and inheritance.
- Method signatures and parameter default values.
- Property descriptions and docstrings.
- Global managers (singletons) and utility functions.

### 2. Stub Generation
Once the JSON reports are gathered, `scripts/generate_stubs_from_reports.py` parses the reports and generates a consolidated `stubs/flame.pyi` file.

This script is highly specialized for Flame's Boost.Python implementation, extracting signatures directly from docstrings when standard introspection is blocked by the C++ bridge.

## How to Update Stubs

If you upgrade Flame or want to ensure your stubs are fresh:

```bash
# 1. Gather latest API data from a running Flame instance
python scripts/collect_flame_api.py --include-all

# 2. Generate the .pyi file from the reports
python scripts/generate_stubs_from_reports.py --latest
```

## Using Stubs in VS Code

The `flame-vscode` extension automatically configures the environment to use these stubs. If you are developing scripts locally without the extension, add the `stubs/` directory to your `python.analysis.extraPaths` setting.