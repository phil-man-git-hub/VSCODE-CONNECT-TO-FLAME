# Deploying the listener into a Flame project

This document describes how to deploy the repository's listener and helpers into a Flame project so they run when Flame starts.

1. Configure `flame.project.json` at the repo root with an appropriate `scriptsDir` pointing to your project's `setups/python/` directory. Example:

```json
{
  "projectId": "888_flame_code",
  "flameProjectPath": "/Volumes/Samsung-T3-1TB/Autodesk/flame/projects/888_flame_code_2027_romeo",
  "scriptsDir": "/Volumes/Samsung-T3-1TB/Autodesk/flame/projects/888_flame_code_2027_romeo/setups/python/"
}
```

2. (Optional) Create a `.flame.secrets.json` in the repo root containing your listener token:

```json
{ "token": "your-flame-token" }
```

This file is **ignored by git** by default. For CI and automation, prefer environment variable `FLAME_TOKEN`.

3. Run the deploy helper:

```
python scripts/deploy_to_flame_project.py --copy
```

This copies `flame_listener.py`, `generate_stubs.py`, and `startup_flame_listener.py` into your project's `setups/python/` directory and (optionally) copies `.flame.secrets.json`.

4. Launch Flame for the project:

```
/opt/Autodesk/flame_2027.pr235/bin/startApplication -J "888_flame_code_2027_romeo" -W "romeo"
```

Watch Flame's stdout for the listener startup message (the startup hook prints `Flame listener startup hook started in background thread`). The listener will check the token on incoming requests and reject requests with invalid tokens.

5. Run the extension's `Flame: Connect` command in VS Code (it will set the token automatically if `FLAME_TOKEN` or `.flame.secrets.json` is present in your workspace). Then use `Flame: Run in Flame` to send code.

Notes

- The listener must be started by Flame's Python startup process — the `startup_flame_listener.py` hook will start the listener in a background thread.
- If you prefer to manually install files, copy the three files above into your project's `setups/python/` directory and ensure the `.flame.secrets.json` token is present.
