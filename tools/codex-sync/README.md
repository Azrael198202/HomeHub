# Codex Records Sync to GitHub

This tool copies Codex records from one machine into a Git repository and pushes them to GitHub. It can also pull the latest records from that repository back into a local Codex directory when VS Code opens the workspace.

Each machine writes into its own folder inside the target repository to reduce merge conflicts:

```text
records/
  MACHINE-A/
    ...
  MACHINE-B/
    ...
```

## Files

- `sync_codex_records.py`: push local Codex records into the Git repository
- `sync_codex_records.bat`: Windows launcher for push sync
- `sync_codex_records.sh`: macOS/Linux launcher for push sync
- `pull_codex_records.py`: pull latest records from the Git repository into the local Codex folder
- `pull_codex_records.bat`: Windows launcher for import sync
- `pull_codex_records.sh`: macOS/Linux launcher for import sync
- `codex-sync.config.example.json`: config template

## Setup

1. Create a private GitHub repository for synced records.
2. Clone that repository on each machine.
3. Copy `codex-sync.config.example.json` to `codex-sync.config.json`.
4. Edit the config values for that machine.
5. On Windows, double-click the launcher you need. On macOS/Linux, run the shell script.

## Config

```json
{
  "sourceDir": "C:/Users/you/AppData/Local/Codex/logs",
  "repoDir": "D:/repos/codex-records",
  "machineName": "DESKTOP-01",
  "branch": "main",
  "targetRoot": "records",
  "deleteMissing": false,
  "includePatterns": ["**/*", "*"],
  "excludePatterns": [".git/**", ".DS_Store", "Thumbs.db"],
  "importFromMachines": []
}
```

### Notes

- `sourceDir`: the local Codex records directory you want to upload or import into
- `repoDir`: a local clone of your GitHub repository
- `machineName`: optional, defaults to the system hostname
- `deleteMissing`: if `true`, deletes files in the machine folder that no longer exist in `sourceDir`
- `importFromMachines`: the machine folders to import from when pulling records into a local Codex folder; use `[]` on a primary machine that should only push and never import

## Push sync

Use push sync to upload local Codex records into GitHub.

1. Loads the config file next to the script.
2. Pulls the latest branch from the target repository.
3. Mirrors files from `sourceDir` into `repoDir/<targetRoot>/<machineName>/`.
4. Writes `.codex-sync-meta.json` with sync metadata.
5. Creates a commit if anything changed.
6. Pushes the commit to GitHub.

Windows:

```bat
sync_codex_records.bat
```

macOS/Linux:

```sh
chmod +x sync_codex_records.sh
./sync_codex_records.sh
```

## Pull sync

Use pull sync to bring the latest repository records into a local Codex folder.

1. Pulls the latest branch from the target repository.
2. Looks at the machine folders listed in `importFromMachines`.
3. Imports missing files.
4. Skips files that are already identical.
5. Avoids overwriting files that changed locally after the last import.
6. If `importFromMachines` is empty, it only refreshes the Git repository and stops.

Windows:

```bat
pull_codex_records.bat
```

macOS/Linux:

```sh
chmod +x pull_codex_records.sh
./pull_codex_records.sh
```

## VS Code auto-import

This repo includes a VS Code task that runs the pull sync script on folder open.

- Task label: `Import Codex Records On Folder Open`
- It uses `runOn: folderOpen`
- Workspace settings enable `task.allowAutomaticTasks`

## Recommended GitHub repo setup

- Use a private repository.
- Give each machine its own `machineName`.
- Avoid storing secrets in the synced record files.
- Keep the source directory focused on logs and summaries, not large caches.
