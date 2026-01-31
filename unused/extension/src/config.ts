import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export type FlameProjectConfig = {
  projectId?: string;
  flameProjectPath?: string;
  scriptsDir?: string;
  autoSync?: boolean;
  syncMethod?: string;
  listener?: { host?: string; port?: number };
};

export async function loadFlameProjectConfig(): Promise<FlameProjectConfig> {
  const folders = vscode.workspace.workspaceFolders;
  if (!folders || folders.length === 0) return {};
  const root = folders[0].uri.fsPath;
  const filePath = path.join(root, 'flame.project.json');
  try {
    const content = await fs.promises.readFile(filePath, 'utf8');
    return JSON.parse(content) as FlameProjectConfig;
  } catch (e) {
    // Fallback to workspace configuration
    const cfg = vscode.workspace.getConfiguration('flame.project');
    return {
      projectId: cfg.get('projectId'),
      flameProjectPath: cfg.get('flameProjectPath'),
      scriptsDir: cfg.get('scriptsDir'),
      autoSync: cfg.get('autoSync'),
      syncMethod: cfg.get('syncMethod'),
      listener: {
        host: cfg.get('listener.host') || '127.0.0.1',
        port: cfg.get('listener.port') || 5555,
      },
    };
  }
}

export async function getAuthToken(): Promise<string | undefined> {
  // 1) env var
  if (process.env.FLAME_TOKEN) return process.env.FLAME_TOKEN;
  // 2) workspace-level secrets file
  const folders = vscode.workspace.workspaceFolders;
  if (!folders || folders.length === 0) return undefined;
  const root = folders[0].uri.fsPath;
  const secretsPath = path.join(root, '.flame.secrets.json');
  try {
    const content = await fs.promises.readFile(secretsPath, 'utf8');
    const data = JSON.parse(content);
    return data.token;
  } catch (e) {
    return undefined;
  }
}