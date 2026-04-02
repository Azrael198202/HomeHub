# HomeHub

HomeHub is a TV-box style AI household hub inspired by WorkBuddy, adapted for the living room.

## VS Code Debug

1. Open this folder in VS Code.
2. Make sure the recommended Python extensions are installed.
3. Press `F5` and choose `Debug HomeHub Runtime`.
4. Open `http://127.0.0.1:8787`.
5. If the browser still shows an older screen, press `Ctrl + F5` once to hard refresh.

## Secrets Profiles

HomeHub supports separate local and production secret files, with environment variables taking priority.

- Local development file: `runtime/secrets.local.json`
- Production file: `runtime/secrets.prod.json`
- Production template: `runtime/secrets.prod.example.json`

Environment variable priority:

- `HOMEHUB_GOOGLE_API_KEY`
- `GOOGLE_API_KEY`
- `HOMEHUB_GOOGLE_ACCESS_TOKEN`
- `GOOGLE_ACCESS_TOKEN`
- `HOMEHUB_OPENAI_API_KEY`
- `OPENAI_API_KEY`

When `HOMEHUB_ENV=prod`, the runtime reads `runtime/secrets.prod.json` after checking environment variables.

Example:

```powershell
$env:HOMEHUB_ENV = "prod"
$env:HOMEHUB_GOOGLE_API_KEY = "your-google-key"
$env:HOMEHUB_OPENAI_API_KEY = "your-openai-key"
$env:HOMEHUB_PORT = "8787"
python .\runtime\server.py
```

## Audio APIs

The runtime now exposes provider-agnostic voice endpoints:

- `POST /api/audio/transcribe`
- `POST /api/audio/synthesize`
- `POST /api/settings/audio`
- `POST /api/settings/language`
- `POST /api/settings/secrets`

Current provider support:

- Google via Cloud Speech-to-Text and Cloud Text-to-Speech
- OpenAI via `gpt-4o-transcribe` and `gpt-4o-mini-tts`

For Google Cloud speech services, this runtime prefers an OAuth access token, but will also try a Google API key when provided:

```powershell
$env:HOMEHUB_GOOGLE_ACCESS_TOKEN = "your-google-oauth-access-token"
$env:HOMEHUB_GOOGLE_API_KEY = "your-google-api-key"
```

## Quick Start

1. Run `python runtime/server.py`
2. Open `http://127.0.0.1:8787`
3. Or double-click `start_homehub.bat`
4. If port `8787` is occupied, run:

```powershell
$env:HOMEHUB_PORT = "8788"
python .\runtime\server.py
```

5. If the page looks older than the current code, hard refresh with `Ctrl + F5`.

## What Starts

- a runnable TV-box style home screen
- local mock APIs for dashboard, pairing, providers, skills, voice, and relay
- configurable multilingual voice provider settings
- simulated multi-agent progress updates every 5 seconds

## Workspace Layout

- `runtime/server.py`: zero-dependency Python runtime server
- `runtime/static`: directly served TV UI
- `apps/tv-shell`: React-style TV shell source scaffold for future Node/Vite migration
- `apps/mobile-companion`: Flutter phone and tablet companion scaffold
- `services/core-engine`: model routing, multi-agent orchestration, and skills runtime skeleton
- `services/companion-api`: pairing, relay, and box-state API skeleton
- `services/voice-gateway`: STT and TTS gateway abstraction
- `packages/shared`: shared contracts and demo data
- `docs/architecture.md`: layered product architecture
