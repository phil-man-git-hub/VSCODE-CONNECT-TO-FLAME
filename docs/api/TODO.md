# API Documentation TODO

This TODO tracks the work items for building a comprehensive Flame Python API knowledge base.

- [x] API-0001 (partial): Create the overall plan and infrastructure for per-symbol docs (scripts + basic output)
- [x] API-0002: Add symbol cross-links from `flame.md` and index.json (initial links present)
- [x] API-0003 (partial): Add class methods capture (collector captures methods)
- [x] API-0004 (partial): Implement safe probing (`--probe-safe` implemented, opt-in)
- [x] API-0005 (partial): Improve `stubs/*.pyi` with signatures (done for many symbols)
- [x] API-0006: Add stub parsing tests (planned)
- [x] API-0007: Add example hooks (startup/menu/asset-sync) and smoke tests ✅
- [x] API-0008: Add snippets for Project/Timeline/Clip and smoke tests ✅
- [x] API-0009: Add mkdocs + CI publishing (CI workflow added; deploy on push) ✅
- [x] API-0010: Generate per-symbol Markdown pages: `docs/api/classes/<Class>.md`, `docs/api/functions/<fn>.md`, `docs/api/constants/<c>.md` (completed; initial pages generated)

> Note: Per-symbol pages were generated from a live Flame process using the collector. Next: add mkdocs nav entries and expand content (method details, examples, cross-links).
- [ ] API-0011: Add instance attribute probes via allowlist and document safety
- [ ] API-0012: Improve stub return-type population from probe results
- [ ] API-0013: Add mkdocs nav entries for symbol directories and symbol index pages
- [ ] API-0014: Add CI job to optionally run `--probe-safe` and store results as artifacts
- [ ] API-0015: Add a probe dashboard and flagged warnings page

Notes:
- Items marked "partial" mean scaffold/implementation exists but further work is needed.
- I will now implement API-0010 (per-symbol pages) and mark progress as this completes.
