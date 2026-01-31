.PHONY: docs:build docs:serve docs:clean flame:api:refresh flame:deploy

# Build the documentation site locally
docs:build:
	./.venv/bin/python -m mkdocs build --clean

# Serve docs locally for development
docs:serve:
	./.venv/bin/python -m mkdocs serve

# Clean generated site
docs:clean:
	rm -rf site/

# --- NEW: Automated API Refresh ---

# Refresh the entire API intelligence suite (Crawls Flame -> Generates Stubs -> Generates Docs)
# Prerequisite: Autodesk Flame must be running with fu_eavesdrop active.
flame:api:refresh:
	./.venv/bin/python scripts/collect_flame_api.py --include-all
	./.venv/bin/python scripts/generate_stubs_from_reports.py --latest
	./.venv/bin/python scripts/generate_api_docs.py --latest
	@echo "--- API Intelligence Refresh Complete ---"

# Deploy the toolkit to the Flame project directory
# Prerequisite: flame-utilities/config/fu_eavesdrop.json must be configured
flame:deploy:
	./.venv/bin/python scripts/deploy_to_flame_project.py --copy