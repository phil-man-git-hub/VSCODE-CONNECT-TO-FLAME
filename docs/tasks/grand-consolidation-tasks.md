# Tasks: The Grand Consolidation

## Phase 1: File Migration
- [x] Move `flame-listener/fu_eavesdrop.py` -> `flame-utilities/fu_eavesdrop.py`.
- [x] Move `flame-listener/fu_eavesdrop_init.py` -> `flame-utilities/fu_eavesdrop_init.py`.
- [x] Move `flame-listener/generate_stubs.py` -> `flame-utilities/scripts/fu_generate_stubs.py`.
- [x] Move `flame-mcp/` (entire folder) -> `flame-utilities/whisper/`.
- [x] Clean up: Remove `flame-listener/` and `flame-mcp/` root directories.

## Phase 2: Script & Logic Updates
- [x] **Deployment Scripts**: Update `scripts/deploy_to_flame_project.py` with new `flame-utilities/` source paths.
- [x] **Version Management**: Update `scripts/bump_flame_versions.py` to track files in the new location.
- [x] **Relay Logic**: Update `flame-utilities/whisper/fu_relay.py` to correctly locate secrets within the new hierarchy.
- [x] **Bridge Imports**: Update `flame-utilities/whisper/fu_whisper.py` to import from the new relative paths.
- [x] **Startup Logic**: Update `flame-utilities/fu_eavesdrop_init.py` to handle being inside the consolidated folder.

## Phase 3: Test Suite Repair
- [x] Update `tests/deploy_test.py` paths.
- [x] Update `tests/test_listener_robustness.py` paths.
- [x] Update `tests/test_listener_more.py` paths.
- [x] Run full test suite to verify no path-related regressions.

## Phase 4: Documentation Refresh
- [x] Update `README.md` (root).
- [x] Update `GEMINI.md`.
- [x] Update `flame-utilities/whisper/GETTING_STARTED.md`.
- [x] Update `docs/deploy.md`, `docs/architecture.md`, `docs/HOWTO_GENERATE_API_REPORTS.md`.
- [x] Update `docs/goals/flame-utilities-rebrand.md` and `docs/goals/flame-mcp-creation.md` to use the new folder names.

## Phase 5: Verification & Loader
- [x] Create `flame-utilities/fu_loader.py`.
- [x] Verify end-to-end connection: `AI -> whisper -> relay -> eavesdrop -> Flame`.
- [x] Update `CHANGELOG.md` with the consolidation milestone.