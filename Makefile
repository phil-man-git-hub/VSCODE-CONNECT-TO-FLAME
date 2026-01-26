.PHONY: docs:build docs:serve docs:clean

# Build the documentation site locally
docs:build:
	python -m pip install -r requirements.txt
	python -m pip install mkdocs-material
	mkdocs build --clean

# Serve docs locally for development
docs:serve:
	python -m pip install -r requirements.txt
	python -m pip install mkdocs-material
	mkdocs serve

# Clean generated site
docs:clean:
	rm -rf site/
