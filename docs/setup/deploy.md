# Deploying FLAME-UTILITIES

This document describes how to deploy the **FLAME-UTILITIES** toolkit into Autodesk Flame using the consolidated directory strategy.

## 1. Configure the Project
Ensure your `fu_eavesdrop.json` is configured in `flame-utilities/config/`. This file tells our scripts where to find your Flame project setups.

```json
{
  "scriptsDir": "/path/to/flame/projects/<project_name>/setups/python/",
  "listener": {
    "host": "127.0.0.1",
    "port": 5555
  }
}
```

## 2. Set Up Authentication (Optional but Recommended)
Create a `fu_secrets.json` in `flame-utilities/config/` (or a `.flame.secrets.json` in the repo root) containing your listener token:

```json
{ "token": "your-secure-token" }
```

## 3. Deploy the Toolkit
The easiest way to deploy is using the provided `Makefile` target:

```bash
make flame-deploy
```

**What this does:**
1.  Copies the entire `flame-utilities/` directory into your project's `setups/python/` folder.
2.  Installs the `fu_activate.py` entry point into the `python/` root.
3.  Optimizes the installation by removing redundant scripts from sub-directories.

## 4. Launch Flame
Launch Flame for your project. Watch the console or logs for the confirmation:

```text
fu_eavesdrop_init.py version 0.0.1 (Ignited)
FU_Eavesdrop startup hook started in background thread
fu_eavesdrop listening on 127.0.0.1:5555
```

## Why this strategy?
By archiving the entire `flame-utilities/` directory within your Flame project, you ensure that the automation tools remain functional even if the workstation is updated or the project is moved to a different system. The `fu_activate.py` script acts as a clean, single-point entry that prevents Flame's auto-hook mechanism from loading internal scripts prematurely.