# Deploying FLAME-UTILITIES

This document describes how to deploy the **FLAME-UTILITIES** toolkit into Autodesk Flame using the consolidated directory strategy.

## 1. Configure the Project
Ensure your `flame.project.json` is configured at the repo root. This file tells our scripts where to find your Flame project setups.

```json
{
  "projectId": "888_flame_code",
  "flameProjectPath": "/Volumes/Samsung-T3-1TB/Autodesk/flame/projects/888_flame_code_2027_romeo",
  "scriptsDir": "/Volumes/Samsung-T3-1TB/Autodesk/flame/projects/888_flame_code_2027_romeo/setups/python/"
}
```

## 2. Set Up Authentication
Create a `.flame.secrets.json` in the repo root containing your listener token:

```json
{ "token": "your-flame-token" }
```

## 3. Deploy the Toolkit
Run the deployment helper to copy the entire `flame-utilities/` folder into your Flame project directory:

```bash
python scripts/deploy_to_flame_project.py --copy
```

This will create a `flame-utilities/` subfolder inside your project's `setups/python/` directory.

## 4. Activate the Toolkit
To "ignite" the tools from within the archived project folder, copy the `fu_loader.py` script to the root of your project's `setups/python/` directory. 

*Note: This loader script adds the `flame-utilities/` subfolder to your Python path and executes the initialization hook.*

## 5. Launch Flame
Launch Flame for your project. Watch the console or logs for the confirmation:

```text
fu_eavesdrop_init.py version 0.0.1
FU_Eavesdrop startup hook started in background thread
```

## Why this strategy?
By archiving the entire `flame-utilities/` directory within your Flame project, you ensure that the automation tools remain functional even if the workstation is updated or the project is moved to a different system.
