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
- `generate_handoff.py`: build a portable handoff summary from the latest local Codex session
- `generate_handoff.bat`: Windows launcher for handoff generation
- `generate_handoff.sh`: macOS/Linux launcher for handoff generation
- `codex-sync.config.example.json`: config template

## Setup

1. Create a private GitHub repository for synced records.
2. Clone that repository on each machine.
3. Run a launcher script once.
4. If `codex-sync.config.json` does not exist, the launcher will create it from `codex-sync.config.example.json` and stop.
5. Edit the config values for that machine.
6. Run the launcher again.

## Auto bootstrap behavior

- The launchers try to ensure required tools are present before running:
- macOS/Linux `.sh`: checks `git` and `python3`, installs via Homebrew when missing.
- Windows `.bat`: checks `git` and Python 3, installs via `winget` when missing.
- If auto-install is unavailable, the script prints what to install manually and exits.

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

## Cross-machine handoff

Use this when you want to continue work on another machine/chat environment.

1. Run handoff generator on current machine.
2. Sync and pull the repository on the other machine.
3. On the other machine, open `~/.codex/handoff.md` (or your configured `sourceDir/handoff.md`) and paste key parts into the new chat as context.

Windows:

```bat
generate_handoff.bat
```

macOS/Linux:

```sh
./generate_handoff.sh
```

In VS Code task runner:

- Task label: `Generate Codex Handoff`
- Task label: `Generate And Sync Codex Handoff` (generate then push in one step)
- Task label: `Resume From Synced Handoff` (pull, import, copy handoff to clipboard, open handoff file)
- `Resume From Synced Handoff` is configured with `runOn: folderOpen` for auto resume on workspace open.

Default output path:

- `sourceDir/handoff.md` (for example: `~/.codex/handoff.md`)
- It will be included in normal sync and land in repo at `records/<machineName>/handoff.md`.

Fast workflow:

1. On machine A (before switching): run `Generate And Sync Codex Handoff`.
2. On machine B (when you start): run `Resume From Synced Handoff`.
3. Paste clipboard content into the new chat and continue.

## Recommended GitHub repo setup

- Use a private repository.
- Give each machine its own `machineName`.
- Avoid storing secrets in the synced record files.
- Keep the source directory focused on logs and summaries, not large caches.
