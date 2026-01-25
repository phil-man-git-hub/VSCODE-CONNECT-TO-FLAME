# Stub files for IntelliSense

VS Code cannot inspect Flame's embedded Python interpreter at design time, so the extension ships `.pyi` stub files to provide types and docstrings.

Generation strategy:

1. Inside Flame: run a script that imports `flame` and uses `dir()` and `inspect` to enumerate modules, classes, and callable signatures.
2. Emit `.pyi` files for the main `flame` interface and common classes like `PyClip`, `PySequence`, `PySegment`.
3. Ship stubs in `extension/stubs/` and add to `python.analysis.extraPaths` when using the extension in development.

`flame-listener/generate_stubs.py` contains a starting point to generate `.pyi` files from a running Flame instance.
