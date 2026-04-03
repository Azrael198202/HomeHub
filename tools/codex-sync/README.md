# Codex Records Sync to GitHub

This tool copies Codex records from one machine into a Git repository and pushes them to GitHub.

Each machine writes into its own folder inside the target repository to reduce merge conflicts:

```text
records/
  MACHINE-A/
    ...
  MACHINE-B/
    ...
```

## Files

- `sync_codex_records.py`: core sync logic
- `sync_codex_records.bat`: Windows launcher
- `sync_codex_records.sh`: macOS/Linux launcher
- `codex-sync.config.example.json`: config template

## Setup

1. Create a private GitHub repository for synced records.
2. Clone that repository on each machine.
3. Copy `codex-sync.config.example.json` to `codex-sync.config.json`.
4. Edit the config values for that machine.
5. Double-click the launcher on Windows, or run the shell script on macOS/Linux.

## Config

```json
{
  "sourceDir": "C:/Users/you/AppData/Local/Codex/logs",
  "repoDir": "D:/repos/codex-records",
  "machineName": "DESKTOP-01",
  "branch": "main",
  "targetRoot": "records",
  "deleteMissing": false,
  "includePatterns": ["**/*"],
  "excludePatterns": [".git/**", ".DS_Store", "Thumbs.db"]
}
```

### Notes

- `sourceDir`: the local Codex records directory you want to upload
- `repoDir`: a local clone of your GitHub repository
- `machineName`: optional, defaults to the system hostname
- `deleteMissing`: if `true`, deletes files in the machine folder that no longer exist in `sourceDir`

## What the script does

1. Loads the config file next to the script.
2. Pulls the latest branch from the target repository.
3. Mirrors files from `sourceDir` into `repoDir/<targetRoot>/<machineName>/`.
4. Writes `.codex-sync-meta.json` with sync metadata.
5. Creates a commit if anything changed.
6. Pushes the commit to GitHub.

## Recommended GitHub repo setup

- Use a private repository.
- Give each machine its own `machineName`.
- Avoid storing secrets in the synced record files.
- Keep the source directory focused on logs and summaries, not large caches.

## Example use

Windows:

```bat
sync_codex_records.bat
```

macOS/Linux:

```sh
chmod +x sync_codex_records.sh
./sync_codex_records.sh
```
