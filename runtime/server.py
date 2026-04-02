import base64
import io
import json
import os
import random
import subprocess
import urllib.error
import urllib.request
import wave
from copy import deepcopy
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
SETTINGS_FILE = ROOT / "settings.json"
CUSTOM_AUDIO_PROVIDERS_FILE = ROOT / "custom_audio_providers.json"
SECRETS_LOCAL_FILE = ROOT / "secrets.local.json"
SECRETS_PROD_FILE = ROOT / "secrets.prod.json"
USAGE_LOG_FILE = ROOT / "usage-cost-log.jsonl"
GOOGLE_SERVICE_ACCOUNT_FILE = ROOT / "google-cloud-service-account.json"
RUNTIME_ENV = os.environ.get("HOMEHUB_ENV", "local").lower()
RUNTIME_PORT = int(os.environ.get("HOMEHUB_PORT", "8787"))


def get_secrets_file():
    if RUNTIME_ENV == "prod":
        return SECRETS_PROD_FILE
    return SECRETS_LOCAL_FILE


MODEL_PROVIDERS = [
    {
        "id": "openai",
        "name": "OpenAI",
        "type": "cloud",
        "capabilities": ["chat", "vision", "voice", "tool-use", "reasoning"],
        "endpointHint": "https://api.openai.com/v1",
    },
    {
        "id": "anthropic",
        "name": "Anthropic",
        "type": "cloud",
        "capabilities": ["chat", "vision", "reasoning"],
        "endpointHint": "https://api.anthropic.com",
    },
    {
        "id": "gemini",
        "name": "Google Gemini",
        "type": "cloud",
        "capabilities": ["chat", "vision", "tool-use"],
        "endpointHint": "https://generativelanguage.googleapis.com",
    },
    {
        "id": "ollama",
        "name": "Ollama Local",
        "type": "local",
        "capabilities": ["chat", "vision"],
        "endpointHint": "http://localhost:11434",
    },
]

SKILLS = [
    {
        "id": "daily-briefing",
        "name": "Daily Briefing",
        "category": "lifestyle",
        "description": "Build a family morning digest with weather, schedule, bills, and reminders.",
        "inputModes": ["text", "voice", "event"],
    },
    {
        "id": "family-schedule-sync",
        "name": "Family Schedule Sync",
        "category": "lifestyle",
        "description": "Merge family events and surface conflicts on the TV home screen.",
        "inputModes": ["text", "event"],
    },
    {
        "id": "knowledge-qa",
        "name": "Local Knowledge Q&A",
        "category": "knowledge",
        "description": "Search private household docs and answer with local citations.",
        "inputModes": ["text", "voice", "image"],
    },
    {
        "id": "im-command-bridge",
        "name": "IM Command Bridge",
        "category": "communication",
        "description": "Accept commands from LINE, WeChat, and the companion app.",
        "inputModes": ["text", "voice", "image", "event"],
    },
]

BASE_AGENTS = [
    {
        "id": "planner",
        "name": "Planner Agent",
        "role": "Task decomposition and routing",
        "status": "running",
        "model": "OpenAI",
        "progress": 84,
        "lastUpdate": "Mapped the household request into three tracks.",
    },
    {
        "id": "device",
        "name": "Device Agent",
        "role": "Pairing, box state, and automation",
        "status": "running",
        "model": "Gemini",
        "progress": 61,
        "lastUpdate": "Refreshing pairing status for companion clients.",
    },
    {
        "id": "lifestyle",
        "name": "Lifestyle Agent",
        "role": "Family assistant orchestration",
        "status": "planning",
        "model": "Anthropic",
        "progress": 39,
        "lastUpdate": "Preparing the morning briefing and reminders.",
    },
    {
        "id": "developer",
        "name": "Developer Agent",
        "role": "AI-driven development stream",
        "status": "running",
        "model": "OpenAI",
        "progress": 72,
        "lastUpdate": "Publishing workflow updates to the TV shell.",
    },
]

BASE_TIMELINE = [
    {
        "id": "t1",
        "time": "07:05",
        "title": "Request Parsed",
        "detail": "Planner Agent split the job into device setup, family sync, and voice configuration.",
        "stream": "analysis",
    },
    {
        "id": "t2",
        "time": "07:07",
        "title": "Parallel Agents Started",
        "detail": "Four agents are running with separate skills and model providers.",
        "stream": "implementation",
    },
    {
        "id": "t3",
        "time": "07:10",
        "title": "Voice Link Ready",
        "detail": "Local STT is active with cloud TTS fallback.",
        "stream": "voice",
    },
    {
        "id": "t4",
        "time": "07:12",
        "title": "Morning Briefing Built",
        "detail": "The family summary is ready for the living room screen.",
        "stream": "family",
    },
]

HOUSEHOLD_MODULES = [
    {
        "id": "briefing",
        "name": "Morning Briefing",
        "summary": "Weather, calendar, tasks, and bills have been merged.",
        "state": "active",
        "actionLabel": "Open Briefing",
    },
    {
        "id": "schedule",
        "name": "Family Schedule Sync",
        "summary": "Two time conflicts were detected for tonight.",
        "state": "attention",
        "actionLabel": "Resolve Now",
    },
    {
        "id": "travel",
        "name": "Travel Checklist",
        "summary": "Power bank and document copies are still missing.",
        "state": "ready",
        "actionLabel": "Open List",
    },
    {
        "id": "knowledge",
        "name": "Local Knowledge Q&A",
        "summary": "Policies, manuals, and receipts are locally indexed.",
        "state": "ready",
        "actionLabel": "Ask Now",
    },
    {
        "id": "messages",
        "name": "Unified Messages",
        "summary": "Recent updates from LINE, WeChat, and the companion app.",
        "state": "active",
        "actionLabel": "View Inbox",
    },
]

BOX_PROFILE = {
    "id": "homehub-living-room",
    "name": "Living Room Box",
    "location": "Home / TV Console",
    "networkState": "online",
    "pairedClients": 3,
    "voiceReady": True,
}

VOICE_PROFILE = {
    "wakeWord": "Hello HomeHub",
    "sttProvider": "Local Whisper Runtime",
    "ttsProvider": "Cloud Neural Voice",
    "locale": "en-US",
}

AUDIO_PROVIDER_CATALOG = {
    "openai": {
        "label": "OpenAI",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "gpt-4o-transcribe",
            "fallbackModel": "whisper-1",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "openai",
        },
        "tts": {
            "defaultModel": "gpt-4o-mini-tts",
            "fallbackModel": "system-tts",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "openai",
        },
    },
    "google": {
        "label": "Google Cloud",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "cloud-speech-to-text",
            "fallbackModel": "cloud-speech-default",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "google",
        },
        "tts": {
            "defaultModel": "cloud-text-to-speech",
            "fallbackModel": "chirp-3-hd",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "google",
        },
    },
    "deepgram": {
        "label": "Deepgram",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "nova-3",
            "fallbackModel": "enhanced-general",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
        "tts": {
            "defaultModel": "not-configured",
            "fallbackModel": "not-configured",
            "supportedLanguages": [],
            "runtime": "catalog",
        },
    },
    "elevenlabs": {
        "label": "ElevenLabs",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "scribe-v1",
            "fallbackModel": "not-configured",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
        "tts": {
            "defaultModel": "eleven-multilingual-v2",
            "fallbackModel": "turbo-v2.5",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
    },
    "azure-openai": {
        "label": "Azure OpenAI",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "gpt-4o-transcribe",
            "fallbackModel": "whisper",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
        "tts": {
            "defaultModel": "gpt-4o-mini-tts",
            "fallbackModel": "azure-neural",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
    },
    "edge-tts": {
        "label": "Edge TTS",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "not-configured",
            "fallbackModel": "not-configured",
            "supportedLanguages": [],
            "runtime": "catalog",
        },
        "tts": {
            "defaultModel": "edge-multilingual-neural",
            "fallbackModel": "system-tts",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
    },
    "local-whisper": {
        "label": "Local Whisper",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "whisper-large-v3",
            "fallbackModel": "whisper-small",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
        "tts": {
            "defaultModel": "system-tts",
            "fallbackModel": "edge-tts",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
    },
    "sherpa-onnx": {
        "label": "Sherpa ONNX",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "sherpa-onnx-streaming",
            "fallbackModel": "sherpa-onnx-offline",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
        "tts": {
            "defaultModel": "vits-local",
            "fallbackModel": "system-tts",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
    },
    "openclaw-gateway": {
        "label": "OpenClaw Gateway",
        "editable": False,
        "sync": {"openclaw": "config-compatible", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": "provider-managed",
            "fallbackModel": "provider-managed",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
        "tts": {
            "defaultModel": "provider-managed",
            "fallbackModel": "provider-managed",
            "supportedLanguages": ["zh-CN", "en-US", "ja-JP"],
            "runtime": "catalog",
        },
    },
}

AUDIO_STACK = {
    "stt": {
        "primaryModel": "gpt-4o-transcribe",
        "fallbackModel": "whisper-1",
        "mode": "multilingual transcription",
    },
    "tts": {
        "primaryModel": "gpt-4o-mini-tts",
        "fallbackModel": "system-tts",
        "mode": "multilingual speech synthesis",
    },
    "recommendedRealtime": "Realtime API speech-to-speech for low-latency dialogue",
}

LANGUAGE_SETTINGS = {
    "current": "en-US",
    "supported": [
        {"code": "zh-CN", "label": "简体中文", "sample": "你好，欢迎使用 HomeHub。"},
        {"code": "en-US", "label": "English", "sample": "Hello, welcome to HomeHub."},
        {"code": "ja-JP", "label": "日本語", "sample": "こんにちは、HomeHub へようこそ。"},
    ],
}


def default_secrets():
    return {
        "googleApiKey": "",
        "googleAccessToken": "",
        "openaiApiKey": "",
    }


def default_custom_audio_providers():
    return {"items": []}


def load_custom_audio_providers():
    if not CUSTOM_AUDIO_PROVIDERS_FILE.exists():
        return default_custom_audio_providers()
    try:
        data = json.loads(CUSTOM_AUDIO_PROVIDERS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default_custom_audio_providers()
    if not isinstance(data, dict) or not isinstance(data.get("items", []), list):
        return default_custom_audio_providers()
    return {"items": data.get("items", [])}


def save_custom_audio_providers(payload):
    CUSTOM_AUDIO_PROVIDERS_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def normalize_supported_languages(value):
    if isinstance(value, list):
        items = value
    else:
        items = str(value or "").split(",")
    normalized = [item.strip() for item in items if str(item).strip()]
    return normalized or ["zh-CN", "en-US", "ja-JP"]


def build_provider_entry(raw):
    provider_id = str(raw.get("id", "")).strip().lower()
    if not provider_id:
        raise ValueError("Provider id is required.")
    label = str(raw.get("label", provider_id)).strip() or provider_id
    stt_runtime = str(raw.get("sttRuntime", "catalog")).strip() or "catalog"
    tts_runtime = str(raw.get("ttsRuntime", "catalog")).strip() or "catalog"
    if stt_runtime not in {"openai", "google", "catalog"}:
        raise ValueError("Unsupported STT runtime.")
    if tts_runtime not in {"openai", "google", "catalog"}:
        raise ValueError("Unsupported TTS runtime.")
    supported_languages = normalize_supported_languages(raw.get("supportedLanguages"))
    return {
        "label": label,
        "editable": True,
        "sync": {"openclaw": "manual-import", "workbuddy": "not-supported"},
        "stt": {
            "defaultModel": str(raw.get("sttDefaultModel", "not-configured")).strip() or "not-configured",
            "fallbackModel": str(raw.get("sttFallbackModel", "not-configured")).strip() or "not-configured",
            "supportedLanguages": supported_languages,
            "runtime": stt_runtime,
        },
        "tts": {
            "defaultModel": str(raw.get("ttsDefaultModel", "not-configured")).strip() or "not-configured",
            "fallbackModel": str(raw.get("ttsFallbackModel", "not-configured")).strip() or "not-configured",
            "supportedLanguages": supported_languages,
            "runtime": tts_runtime,
        },
    }


def get_audio_provider_catalog():
    catalog = deepcopy(AUDIO_PROVIDER_CATALOG)
    for item in load_custom_audio_providers().get("items", []):
        if item.get("entryType") and item.get("entryType") != "provider":
            continue
        try:
            catalog[item["id"]] = build_provider_entry(item)
        except Exception:
            continue
    return catalog


def normalize_string_list(value):
    if isinstance(value, list):
        items = value
    else:
        items = str(value or "").split(",")
    return [str(item).strip() for item in items if str(item).strip()]


def get_custom_capability_entries():
    entries = []
    for item in load_custom_audio_providers().get("items", []):
        if item.get("entryType", "provider") != "capability":
            continue
        entries.append(
            {
                "id": str(item.get("id", "")).strip().lower(),
                "label": str(item.get("label", "Custom Entry")).strip() or "Custom Entry",
                "source": str(item.get("source", "Custom")).strip() or "Custom",
                "summary": str(item.get("summary", "Custom AI capability entry.")).strip() or "Custom AI capability entry.",
                "models": normalize_string_list(item.get("models")) or ["Custom model"],
                "capabilities": normalize_string_list(item.get("capabilities")) or ["Custom"],
                "languages": normalize_supported_languages(item.get("supportedLanguages")),
                "sync": {
                    "openclaw": str(item.get("syncOpenclaw", "manual")).strip() or "manual",
                    "workbuddy": str(item.get("syncWorkbuddy", "manual")).strip() or "manual",
                },
                "editable": True,
                "actions": [],
            }
        )
    return entries


def build_ai_capability_catalog(provider_catalog, selected_audio):
    catalog = [
        {
            "id": "openclaw-wake-word",
            "label": "OpenClaw Wake Word",
            "source": "OpenClaw",
            "summary": "Hotword entry layer for living-room voice wakeup.",
            "models": ["Porcupine", "Snowboy", "Custom lightweight wake model"],
            "capabilities": ["Wake Word", "Voice Wake", "Always-on Listening"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "aligned", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
        {
            "id": "openclaw-asr",
            "label": "OpenClaw ASR Layer",
            "source": "OpenClaw",
            "summary": "Speech recognition choices for local-first and cloud-hybrid voice flows.",
            "models": ["Whisper", "Vosk", "OpenAI Transcribe", "Google Cloud Speech", "Deepgram", "Sherpa ONNX"],
            "capabilities": ["ASR", "Continuous Dialogue", "Command Capture"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "aligned", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
        {
            "id": "openclaw-llm",
            "label": "OpenClaw LLM Layer",
            "source": "OpenClaw",
            "summary": "Reasoning and task-routing layer for skills, tools, and multi-turn orchestration.",
            "models": ["LLaMA 3", "Qwen2.5", "Mistral", "OpenAI", "Claude", "Gemini"],
            "capabilities": ["LLM", "Intent Parsing", "Task Routing", "Tool Use", "Multi-turn"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "aligned", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
        {
            "id": "openclaw-tts",
            "label": "OpenClaw TTS Layer",
            "source": "OpenClaw",
            "summary": "Voice reply layer for natural spoken responses on the box.",
            "models": ["Coqui TTS", "OpenVoice", "OpenAI TTS", "ElevenLabs", "Edge TTS"],
            "capabilities": ["TTS", "Voice Reply", "Streaming Playback"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "aligned", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
        {
            "id": "openclaw-skills",
            "label": "OpenClaw Skills and Tools",
            "source": "OpenClaw",
            "summary": "Framework layer for plugins, skills, API calls, IoT control, and mixed local/cloud execution.",
            "models": ["Plugin Router", "Skill Executor", "Tool Bridge"],
            "capabilities": ["Skills", "Plugins", "IoT", "API Calls", "Hybrid Runtime"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "aligned", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
        {
            "id": "workbuddy-llm",
            "label": "WorkBuddy-style LLM Core",
            "source": "WorkBuddy-style",
            "summary": "Enterprise-facing assistant core for document understanding, drafting, and automation.",
            "models": ["GPT-4", "Claude", "Gemini"],
            "capabilities": ["LLM", "Document QA", "Auto Reply", "Agent Automation"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "manual", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
        {
            "id": "workbuddy-embedding",
            "label": "WorkBuddy-style Embedding and RAG",
            "source": "WorkBuddy-style",
            "summary": "Semantic retrieval layer for enterprise knowledge, search, and grounding.",
            "models": ["text-embedding-3-large", "BGE", "E5"],
            "capabilities": ["Embedding", "RAG", "Semantic Search", "Knowledge Base"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "manual", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
        {
            "id": "workbuddy-voice",
            "label": "WorkBuddy-style Optional Voice",
            "source": "WorkBuddy-style",
            "summary": "Optional speech I/O for notes, commands, and assistant replies.",
            "models": ["Whisper", "Edge TTS", "ElevenLabs"],
            "capabilities": ["ASR", "TTS", "Voice Notes"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "manual", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
        {
            "id": "workbuddy-automation",
            "label": "WorkBuddy-style Office Agent",
            "source": "WorkBuddy-style",
            "summary": "Automation layer for reports, summaries, CRM support, ticketing, and workflows.",
            "models": ["Agent Workflow", "Function Calling", "Report Generator"],
            "capabilities": ["Agent", "Reporting", "CRM", "Tickets", "Workflow"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "manual", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
        },
    ]

    for provider_id, provider in provider_catalog.items():
        actions = []
        if provider["stt"].get("runtime") != "catalog":
            actions.append({"type": "stt", "label": "Use STT", "selected": provider_id == selected_audio.get("stt")})
        if provider["tts"].get("runtime") != "catalog":
            actions.append({"type": "tts", "label": "Use TTS", "selected": provider_id == selected_audio.get("tts")})
        capabilities = []
        if provider["stt"].get("defaultModel") != "not-configured":
            capabilities.append("STT")
        if provider["tts"].get("defaultModel") != "not-configured":
            capabilities.append("TTS")
        catalog.append(
            {
                "id": f"provider-{provider_id}",
                "label": provider["label"],
                "source": "Provider Stack",
                "summary": "Runtime provider stack available to HomeHub.",
                "models": [provider["stt"]["defaultModel"], provider["tts"]["defaultModel"]],
                "capabilities": capabilities or ["Catalog"],
                "languages": sorted(set(provider["stt"]["supportedLanguages"] + provider["tts"]["supportedLanguages"])),
                "sync": provider.get("sync", {"openclaw": "manual", "workbuddy": "manual"}),
                "editable": provider.get("editable", False),
                "actions": actions,
            }
        )
    catalog.extend(get_custom_capability_entries())
    return catalog


def load_secrets_file():
    secrets_file = get_secrets_file()
    if not secrets_file.exists():
        return default_secrets()

    try:
        data = json.loads(secrets_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default_secrets()

    return {
        "googleApiKey": data.get("googleApiKey", ""),
        "googleAccessToken": data.get("googleAccessToken", ""),
        "openaiApiKey": data.get("openaiApiKey", ""),
    }


def get_effective_secrets():
    file_secrets = load_secrets_file()
    google_api_key = (
        os.environ.get("HOMEHUB_GOOGLE_API_KEY")
        or os.environ.get("GOOGLE_API_KEY")
        or file_secrets.get("googleApiKey", "")
    )
    google_access_token = (
        os.environ.get("HOMEHUB_GOOGLE_ACCESS_TOKEN")
        or os.environ.get("GOOGLE_ACCESS_TOKEN")
        or file_secrets.get("googleAccessToken", "")
    )
    openai_api_key = (
        os.environ.get("HOMEHUB_OPENAI_API_KEY")
        or os.environ.get("OPENAI_API_KEY")
        or file_secrets.get("openaiApiKey", "")
    )
    return {
        "googleApiKey": google_api_key,
        "googleAccessToken": google_access_token,
        "openaiApiKey": openai_api_key,
    }


def get_secret_sources():
    file_secrets = load_secrets_file()
    return {
        "googleApiKey": "env" if (os.environ.get("HOMEHUB_GOOGLE_API_KEY") or os.environ.get("GOOGLE_API_KEY")) else ("file" if file_secrets.get("googleApiKey") else "missing"),
        "googleAccessToken": "env" if (os.environ.get("HOMEHUB_GOOGLE_ACCESS_TOKEN") or os.environ.get("GOOGLE_ACCESS_TOKEN")) else ("file" if file_secrets.get("googleAccessToken") else "missing"),
        "openaiApiKey": "env" if (os.environ.get("HOMEHUB_OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")) else ("file" if file_secrets.get("openaiApiKey") else "missing"),
    }


def save_secrets(secrets):
    secrets_file = get_secrets_file()
    secrets_file.write_text(
        json.dumps(secrets, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


GOOGLE_TOKEN_CACHE = {
    "access_token": "",
    "expires_at": 0,
}


def get_google_service_account_file():
    path_value = os.environ.get("HOMEHUB_GOOGLE_SERVICE_ACCOUNT_JSON") or os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if path_value:
        return Path(path_value)
    return GOOGLE_SERVICE_ACCOUNT_FILE


def mint_google_access_token_from_service_account(service_account_path: Path):
    script = f"""
$svc = Get-Content -LiteralPath '{str(service_account_path)}' -Raw | ConvertFrom-Json
function B64Url([byte[]]$bytes) {{
  [Convert]::ToBase64String($bytes).TrimEnd('=') -replace '\\+','-' -replace '/','_'
}}
$now = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$headerJson = '{{"alg":"RS256","typ":"JWT"}}'
$claimJson = (@{{
  iss = $svc.client_email
  scope = 'https://www.googleapis.com/auth/cloud-platform'
  aud = 'https://oauth2.googleapis.com/token'
  exp = $now + 3600
  iat = $now
}} | ConvertTo-Json -Compress)
$unsigned = (B64Url ([Text.Encoding]::UTF8.GetBytes($headerJson))) + '.' + (B64Url ([Text.Encoding]::UTF8.GetBytes($claimJson)))
$pkcs8 = [Convert]::FromBase64String(($svc.private_key -replace '-----BEGIN PRIVATE KEY-----','' -replace '-----END PRIVATE KEY-----','' -replace '\\s',''))
$key = [System.Security.Cryptography.CngKey]::Import($pkcs8, [System.Security.Cryptography.CngKeyBlobFormat]::Pkcs8PrivateBlob)
$rsa = New-Object System.Security.Cryptography.RSACng($key)
$sig = $rsa.SignData([Text.Encoding]::UTF8.GetBytes($unsigned), [System.Security.Cryptography.HashAlgorithmName]::SHA256, [System.Security.Cryptography.RSASignaturePadding]::Pkcs1)
$jwt = $unsigned + '.' + (B64Url $sig)
$body = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=' + $jwt
$resp = Invoke-RestMethod -Method Post -Uri 'https://oauth2.googleapis.com/token' -ContentType 'application/x-www-form-urlencoded' -Body $body
$resp | ConvertTo-Json -Compress
"""
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", script],
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to mint Google access token from service account. {result.stderr.strip()}")
    payload = json.loads(result.stdout.strip())
    GOOGLE_TOKEN_CACHE["access_token"] = payload.get("access_token", "")
    GOOGLE_TOKEN_CACHE["expires_at"] = int(datetime.now().timestamp()) + int(payload.get("expires_in", 3600)) - 60
    return GOOGLE_TOKEN_CACHE["access_token"]


def get_google_cloud_headers():
    access_token = SECRETS.get("googleAccessToken", "")
    api_key = SECRETS.get("googleApiKey", "")
    service_account_file = get_google_service_account_file()
    if not access_token and service_account_file.exists():
        if GOOGLE_TOKEN_CACHE["access_token"] and GOOGLE_TOKEN_CACHE["expires_at"] > int(datetime.now().timestamp()):
            access_token = GOOGLE_TOKEN_CACHE["access_token"]
        else:
            access_token = mint_google_access_token_from_service_account(service_account_file)
    if not access_token:
        if api_key:
            return {"x-goog-api-key": api_key}
        raise RuntimeError(
            "Google Cloud credentials are not configured. "
            "Set HOMEHUB_GOOGLE_ACCESS_TOKEN / GOOGLE_ACCESS_TOKEN, "
            "or provide HOMEHUB_GOOGLE_API_KEY / GOOGLE_API_KEY, "
            "or place a service account JSON at runtime/google-cloud-service-account.json."
        )
    return {"Authorization": f"Bearer {access_token}"}


def load_persisted_settings():
    provider_catalog = get_audio_provider_catalog()
    if not SETTINGS_FILE.exists():
        return {
            "language": LANGUAGE_SETTINGS["current"],
            "sttProvider": "google",
            "ttsProvider": "google",
        }

    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {
            "language": LANGUAGE_SETTINGS["current"],
            "sttProvider": "google",
            "ttsProvider": "google",
        }

    supported_codes = {item["code"] for item in LANGUAGE_SETTINGS["supported"]}
    language = data.get("language", LANGUAGE_SETTINGS["current"])
    if language not in supported_codes:
        language = LANGUAGE_SETTINGS["current"]

    supported_providers = set(provider_catalog.keys())
    stt_provider = data.get("sttProvider", "google")
    tts_provider = data.get("ttsProvider", "google")
    if stt_provider not in supported_providers:
        stt_provider = "google"
    if tts_provider not in supported_providers:
        tts_provider = "google"

    return {
        "language": language,
        "sttProvider": stt_provider,
        "ttsProvider": tts_provider,
    }


def save_persisted_settings(settings):
    SETTINGS_FILE.write_text(
        json.dumps(settings, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def log_external_usage(provider, model, operation, locale, text_value="", transcript="", audio_base64=""):
    record = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "provider": provider,
        "model": model,
        "operation": operation,
        "locale": locale,
        "text_chars": len(text_value or ""),
        "transcript_chars": len(transcript or ""),
        "audio_bytes": len(base64.b64decode(audio_base64)) if audio_base64 else 0,
    }
    with USAGE_LOG_FILE.open("a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(record, ensure_ascii=False) + "\n")


PERSISTED_SETTINGS = load_persisted_settings()
SECRETS = get_effective_secrets()
SECRET_SOURCES = get_secret_sources()

WEATHER = {
    "location": "Tokyo",
    "condition": "Cloudy",
    "temperatureC": 22,
    "highC": 25,
    "lowC": 18,
}

SYSTEM_STATUS = {
    "mode": "Listening",
    "boxHealth": "Healthy",
    "remoteHint": "Use Left/Right to switch tabs, Enter to open cards.",
}

VOICE_CONVERSATION = [
    {
        "speaker": "HomeHub",
        "text": "Good evening. The living room box is online and ready.",
        "time": "19:40",
    },
    {
        "speaker": "You",
        "text": "Show my family schedule and remind me about tonight's meeting.",
        "time": "19:41",
    },
    {
        "speaker": "HomeHub",
        "text": "Two schedule conflicts were found. I pinned them in the Home tab and created an 8 PM reminder.",
        "time": "19:41",
    },
]

CURRENT_CONVERSATION = deepcopy(VOICE_CONVERSATION)

RELAY_MESSAGES = [
    {
        "id": "r1",
        "source": "mobile-app",
        "kind": "voice",
        "preview": "Remind me about the family meeting at 8 PM.",
        "createdAt": "07:13",
        "retentionPolicy": "delete-after-delivery",
    },
    {
        "id": "r2",
        "source": "wechat",
        "kind": "image",
        "preview": "A bill screenshot is waiting for OCR and filing.",
        "createdAt": "07:14",
        "retentionPolicy": "delete-after-delivery",
    },
]

PAIRING = {
    "code": "HH-7K2P",
    "expiresInSeconds": 180,
    "qrPayload": "homehub://pair?box=homehub-living-room&code=HH-7K2P",
}


def json_post(url, payload, headers=None):
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request_headers = {
        "Content-Type": "application/json; charset=utf-8",
    }
    if headers:
        request_headers.update(headers)
    request = urllib.request.Request(url, data=data, headers=request_headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            content_type = response.headers.get("Content-Type", "")
            if "application/json" in content_type:
                return json.loads(body.decode("utf-8"))
            return body
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        if exc.code == 403 and "Generative Language API" in detail:
            raise RuntimeError(
                "Google Gemini API is not enabled for this API key or project. "
                "Enable the Generative Language API for the linked Google project, "
                "or switch STT/TTS provider in Settings."
            ) from exc
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error: {exc}") from exc


def build_wav_from_pcm(pcm_bytes, channels=1, rate=24000, sample_width=2):
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(rate)
        wav_file.writeframes(pcm_bytes)
    return buffer.getvalue()


def build_google_stt_config(mime_type, locale):
    mime = (mime_type or "").lower()
    config = {
        "languageCode": locale,
        "enableAutomaticPunctuation": True,
    }
    # Google Cloud Speech models are language-dependent.
    # `latest_long` is not accepted for some locales such as zh-CN.
    if locale.startswith("en"):
        config["model"] = "latest_long"
    if "webm" in mime:
        config["encoding"] = "WEBM_OPUS"
        config["sampleRateHertz"] = 48000
    elif "ogg" in mime or "opus" in mime:
        config["encoding"] = "OGG_OPUS"
        config["sampleRateHertz"] = 48000
    elif "wav" in mime or "wave" in mime:
        config["encoding"] = "LINEAR16"
        config["sampleRateHertz"] = 48000
    return config


def google_transcribe_audio(audio_base64, mime_type, locale):
    provider_catalog = get_audio_provider_catalog()
    selected_provider = provider_catalog.get(PERSISTED_SETTINGS.get("sttProvider", "google"), provider_catalog["google"])
    headers = get_google_cloud_headers()
    payload = {
        "config": build_google_stt_config(mime_type, locale),
        "audio": {
            "content": audio_base64,
        },
    }
    response_json = json_post(
        "https://speech.googleapis.com/v1/speech:recognize",
        payload,
        headers=headers,
    )
    transcript = " ".join(
        result.get("alternatives", [{}])[0].get("transcript", "")
        for result in response_json.get("results", [])
    ).strip()
    log_external_usage(
        "google",
        selected_provider["stt"]["defaultModel"],
        "stt",
        locale,
        transcript=transcript,
        audio_base64=audio_base64,
    )
    return {
        "provider": "google",
        "model": selected_provider["stt"]["defaultModel"],
        "transcript": transcript,
    }


def google_synthesize_speech(text_value, locale, voice_name="Kore"):
    provider_catalog = get_audio_provider_catalog()
    selected_provider = provider_catalog.get(PERSISTED_SETTINGS.get("ttsProvider", "google"), provider_catalog["google"])
    headers = get_google_cloud_headers()
    payload = {
        "input": {"text": text_value},
        "voice": {
            "languageCode": locale,
            "name": voice_name if locale.startswith("en") else "",
        },
        "audioConfig": {
            "audioEncoding": "LINEAR16",
        },
    }
    response_json = json_post(
        "https://texttospeech.googleapis.com/v1/text:synthesize",
        payload,
        headers=headers,
    )
    audio_b64 = response_json.get("audioContent")
    if not audio_b64:
        raise RuntimeError("Google TTS did not return audio data.")
    log_external_usage(
        "google",
        selected_provider["tts"]["defaultModel"],
        "tts",
        locale,
        text_value=text_value,
    )
    return {
        "provider": "google",
        "model": selected_provider["tts"]["defaultModel"],
        "audioBase64": audio_b64,
        "mimeType": "audio/wav",
    }


def build_multipart_form(fields, file_field, filename, file_bytes, mime_type):
    boundary = "----HomeHubBoundary7MA4YWxkTrZu0gW"
    lines = []
    for key, value in fields.items():
        lines.append(f"--{boundary}\r\n".encode("utf-8"))
        lines.append(f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode("utf-8"))
        lines.append(f"{value}\r\n".encode("utf-8"))
    lines.append(f"--{boundary}\r\n".encode("utf-8"))
    lines.append(f'Content-Disposition: form-data; name="{file_field}"; filename="{filename}"\r\n'.encode("utf-8"))
    lines.append(f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"))
    lines.append(file_bytes)
    lines.append(b"\r\n")
    lines.append(f"--{boundary}--\r\n".encode("utf-8"))
    body = b"".join(lines)
    return boundary, body


def openai_transcribe_audio(audio_base64, mime_type, locale, model_name):
    api_key = SECRETS.get("openaiApiKey", "")
    if not api_key:
        raise RuntimeError("OpenAI API key is not configured.")

    audio_bytes = base64.b64decode(audio_base64)
    boundary, body = build_multipart_form(
        {"model": model_name},
        "file",
        "input.wav",
        audio_bytes,
        mime_type,
    )
    request = urllib.request.Request(
        "https://api.openai.com/v1/audio/transcriptions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error: {exc}") from exc

    transcript = payload.get("text", "")
    log_external_usage(
        "openai",
        model_name,
        "stt",
        locale,
        transcript=transcript,
        audio_base64=audio_base64,
    )
    return {
        "provider": "openai",
        "model": model_name,
        "transcript": transcript,
    }


def openai_synthesize_speech(text_value, locale, model_name):
    api_key = SECRETS.get("openaiApiKey", "")
    if not api_key:
        raise RuntimeError("OpenAI API key is not configured.")

    payload = {
        "model": model_name,
        "input": text_value,
        "voice": "alloy",
        "response_format": "wav",
        "instructions": f"Speak naturally in locale {locale}.",
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            wav_bytes = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error: {exc}") from exc

    log_external_usage(
        "openai",
        model_name,
        "tts",
        locale,
        text_value=text_value,
    )
    return {
        "provider": "openai",
        "model": model_name,
        "audioBase64": base64.b64encode(wav_bytes).decode("utf-8"),
        "mimeType": "audio/wav",
    }


def transcribe_audio(provider_id, audio_base64, mime_type, locale):
    catalog = get_audio_provider_catalog()
    provider = catalog.get(provider_id)
    if not provider:
        raise RuntimeError(f"Unsupported STT provider: {provider_id}")
    runtime = provider["stt"].get("runtime", "catalog")
    model_name = provider["stt"].get("defaultModel", "unknown")
    if runtime == "google":
        return google_transcribe_audio(audio_base64, mime_type, locale)
    if runtime == "openai":
        return openai_transcribe_audio(audio_base64, mime_type, locale, model_name)
    raise RuntimeError(f"Provider {provider['label']} is listed in the catalog but its STT runtime is not wired yet.")


def synthesize_speech(provider_id, text_value, locale):
    catalog = get_audio_provider_catalog()
    provider = catalog.get(provider_id)
    if not provider:
        raise RuntimeError(f"Unsupported TTS provider: {provider_id}")
    runtime = provider["tts"].get("runtime", "catalog")
    model_name = provider["tts"].get("defaultModel", "unknown")
    if runtime == "google":
        return google_synthesize_speech(text_value, locale)
    if runtime == "openai":
        return openai_synthesize_speech(text_value, locale, model_name)
    raise RuntimeError(f"Provider {provider['label']} is listed in the catalog but its TTS runtime is not wired yet.")


def now_hhmm():
    return datetime.now().strftime("%H:%M")


def generate_assistant_reply(user_text, locale):
    if locale == "zh-CN":
        return "我已收到你的语音。"
    if locale == "ja-JP":
        return "音声を受け取りました。"
    return "I received your voice."


def append_conversation_turn(speaker, text_value):
    CURRENT_CONVERSATION.append(
        {
            "speaker": speaker,
            "text": text_value,
            "time": now_hhmm(),
        }
    )
    if len(CURRENT_CONVERSATION) > 24:
        del CURRENT_CONVERSATION[0 : len(CURRENT_CONVERSATION) - 24]


def build_dashboard():
    provider_catalog = get_audio_provider_catalog()
    agents = deepcopy(BASE_AGENTS)
    for agent in agents:
        delta = random.randint(-4, 6)
        agent["progress"] = max(12, min(100, agent["progress"] + delta))
        if agent["progress"] > 92:
            agent["status"] = "complete"
            agent["lastUpdate"] = "Task finished and result published to the TV shell."
        elif agent["progress"] < 45 and agent["id"] == "lifestyle":
            agent["status"] = "planning"
        else:
            agent["status"] = "running"

    timeline = deepcopy(BASE_TIMELINE)
    timeline.append(
        {
            "id": f"live-{datetime.now().strftime('%H%M%S')}",
            "time": datetime.now().strftime("%H:%M"),
            "title": "Live Box Update",
            "detail": random.choice(
                [
                    "Companion app heartbeat confirmed.",
                    "Travel checklist refreshed from latest family note.",
                    "Voice pipeline pushed a partial transcript to the screen.",
                    "Relay message delivered and removed from transient storage.",
                ]
            ),
            "stream": random.choice(["system", "implementation", "family", "voice"]),
        }
    )

    stt_provider_id = PERSISTED_SETTINGS["sttProvider"]
    tts_provider_id = PERSISTED_SETTINGS["ttsProvider"]
    stt_provider = provider_catalog[stt_provider_id]
    tts_provider = provider_catalog[tts_provider_id]

    return {
        "hero": {
            "title": "HomeHub",
            "subtitle": "AI Box for the Living Room",
            "tagline": "Boot like a TV box, collaborate like a multi-agent team.",
        },
        "boxProfile": BOX_PROFILE,
        "householdModules": HOUSEHOLD_MODULES,
        "activeAgents": agents,
        "timelineEvents": timeline,
        "modelProviders": MODEL_PROVIDERS,
        "skillCatalog": SKILLS,
        "pairingSession": PAIRING,
        "relayMessages": RELAY_MESSAGES,
        "voiceProfile": {
            **VOICE_PROFILE,
            "sttProvider": f"{stt_provider['label']} / {stt_provider['stt']['defaultModel']}",
            "ttsProvider": f"{tts_provider['label']} / {tts_provider['tts']['defaultModel']}",
            "locale": PERSISTED_SETTINGS["language"],
        },
        "audioStack": {
            **AUDIO_STACK,
            "stt": {
                **AUDIO_STACK["stt"],
                "provider": stt_provider["label"],
                "primaryModel": stt_provider["stt"]["defaultModel"],
                "fallbackModel": stt_provider["stt"]["fallbackModel"],
            },
            "tts": {
                **AUDIO_STACK["tts"],
                "provider": tts_provider["label"],
                "primaryModel": tts_provider["tts"]["defaultModel"],
                "fallbackModel": tts_provider["tts"]["fallbackModel"],
            },
        },
        "audioProviders": {
            "selected": {
                "stt": stt_provider_id,
                "tts": tts_provider_id,
            },
            "catalog": provider_catalog,
            "secrets": {
                "googleConfigured": bool(SECRETS.get("googleAccessToken") or get_google_service_account_file().exists()),
                "openaiConfigured": bool(SECRETS.get("openaiApiKey")),
                "googleSource": "service-account-file" if get_google_service_account_file().exists() else SECRET_SOURCES.get("googleAccessToken", "missing"),
                "openaiSource": SECRET_SOURCES.get("openaiApiKey", "missing"),
            },
            "counts": {
                "total": len(provider_catalog),
                "editable": sum(1 for provider in provider_catalog.values() if provider.get("editable")),
            },
        },
        "modelCatalog": build_ai_capability_catalog(
            provider_catalog,
            {"stt": stt_provider_id, "tts": tts_provider_id},
        ),
        "languageSettings": {
            **LANGUAGE_SETTINGS,
            "current": PERSISTED_SETTINGS["language"],
        },
        "weather": WEATHER,
        "systemStatus": SYSTEM_STATUS,
        "conversation": CURRENT_CONVERSATION,
    }


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, file_path: Path, content_type: str):
        if not file_path.exists() or not file_path.is_file():
            self.send_error(404)
            return
        data = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        self.wfile.write(data)

    def _read_json_body(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return None
        if length <= 0:
            return None
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return None

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/health":
            self._send_json({"ok": True, "service": "homehub-runtime"})
            return

        if path == "/api/dashboard":
            self._send_json(build_dashboard())
            return

        if path == "/api/providers":
            self._send_json(MODEL_PROVIDERS)
            return

        if path == "/api/skills":
            self._send_json(SKILLS)
            return

        if path == "/api/pairing":
            self._send_json(PAIRING)
            return

        if path == "/api/relay":
            self._send_json(RELAY_MESSAGES)
            return

        if path == "/api/voice":
            self._send_json(VOICE_PROFILE)
            return

        if path == "/api/usage/logs":
            if not USAGE_LOG_FILE.exists():
                self._send_json({"items": []})
                return
            lines = USAGE_LOG_FILE.read_text(encoding="utf-8").splitlines()[-200:]
            items = [json.loads(line) for line in lines if line.strip()]
            self._send_json({"items": items})
            return

        if path == "/api/run":
            params = parse_qs(parsed.query)
            task = params.get("task", ["Plan a family trip and show progress on TV"])[0]
            self._send_json(
                {
                    "task": task,
                    "fanout": 4,
                    "strategy": "planner -> device | lifestyle | developer | voice",
                    "status": "running",
                }
            )
            return

        if path == "/" or path == "/index.html":
            self._send_file(STATIC_DIR / "index.html", "text/html; charset=utf-8")
            return

        if path == "/assets/app.css":
            self._send_file(STATIC_DIR / "assets" / "app.css", "text/css; charset=utf-8")
            return

        if path == "/assets/app.js":
            self._send_file(STATIC_DIR / "assets" / "app.js", "application/javascript; charset=utf-8")
            return

        self.send_error(404)

    def do_POST(self):
        global PERSISTED_SETTINGS, SECRETS, SECRET_SOURCES

        parsed = urlparse(self.path)
        if parsed.path == "/api/settings/language":
            body = self._read_json_body()
            if not body or "language" not in body:
                self._send_json({"error": "Invalid request body"}, status=400)
                return

            supported_codes = {item["code"] for item in LANGUAGE_SETTINGS["supported"]}
            language = body["language"]
            if language not in supported_codes:
                self._send_json({"error": "Unsupported language"}, status=400)
                return

            PERSISTED_SETTINGS["language"] = language
            save_persisted_settings(PERSISTED_SETTINGS)
            self._send_json({"ok": True, "language": language})
            return

        if parsed.path == "/api/settings/audio":
            body = self._read_json_body()
            if not body:
                self._send_json({"error": "Invalid request body"}, status=400)
                return

            provider_catalog = get_audio_provider_catalog()
            supported_providers = set(provider_catalog.keys())
            stt_provider = body.get("sttProvider", PERSISTED_SETTINGS["sttProvider"])
            tts_provider = body.get("ttsProvider", PERSISTED_SETTINGS["ttsProvider"])
            if stt_provider not in supported_providers or tts_provider not in supported_providers:
                self._send_json({"error": "Unsupported provider"}, status=400)
                return
            if provider_catalog[stt_provider]["stt"].get("runtime") == "catalog":
                self._send_json({"error": "Selected STT provider is catalog-only."}, status=400)
                return
            if provider_catalog[tts_provider]["tts"].get("runtime") == "catalog":
                self._send_json({"error": "Selected TTS provider is catalog-only."}, status=400)
                return

            PERSISTED_SETTINGS["sttProvider"] = stt_provider
            PERSISTED_SETTINGS["ttsProvider"] = tts_provider
            save_persisted_settings(PERSISTED_SETTINGS)
            self._send_json(
                {
                    "ok": True,
                    "sttProvider": stt_provider,
                    "ttsProvider": tts_provider,
                }
            )
            return

        if parsed.path == "/api/settings/secrets":
            body = self._read_json_body()
            if not body:
                self._send_json({"error": "Invalid request body"}, status=400)
                return

            file_secrets = load_secrets_file()
            google_api_key = body.get("googleApiKey", file_secrets.get("googleApiKey", ""))
            openai_api_key = body.get("openaiApiKey", file_secrets.get("openaiApiKey", ""))
            save_secrets({
                "googleApiKey": google_api_key,
                "googleAccessToken": body.get("googleAccessToken", file_secrets.get("googleAccessToken", "")),
                "openaiApiKey": openai_api_key,
            })
            SECRETS = get_effective_secrets()
            SECRET_SOURCES = get_secret_sources()
            self._send_json(
                {
                    "ok": True,
                    "googleConfigured": bool(SECRETS.get("googleAccessToken") or get_google_service_account_file().exists()),
                    "openaiConfigured": bool(SECRETS.get("openaiApiKey")),
                    "googleSource": "service-account-file" if get_google_service_account_file().exists() else SECRET_SOURCES.get("googleAccessToken", "missing"),
                    "openaiSource": SECRET_SOURCES.get("openaiApiKey", "missing"),
                }
            )
            return

        if parsed.path == "/api/audio/transcribe":
            body = self._read_json_body()
            if not body or "audioBase64" not in body:
                self._send_json({"error": "audioBase64 is required"}, status=400)
                return

            provider = body.get("provider", PERSISTED_SETTINGS["sttProvider"])
            mime_type = body.get("mimeType", "audio/wav")
            locale = body.get("locale", PERSISTED_SETTINGS["language"])
            try:
                result = transcribe_audio(provider, body["audioBase64"], mime_type, locale)
            except RuntimeError as exc:
                self._send_json({"error": str(exc)}, status=502)
                return
            except Exception as exc:
                self._send_json({"error": f"Unexpected transcription error: {exc}"}, status=500)
                return
            self._send_json({"ok": True, **result})
            return

        if parsed.path == "/api/audio/synthesize":
            body = self._read_json_body()
            if not body or "text" not in body:
                self._send_json({"error": "text is required"}, status=400)
                return

            provider = body.get("provider", PERSISTED_SETTINGS["ttsProvider"])
            locale = body.get("locale", PERSISTED_SETTINGS["language"])
            try:
                result = synthesize_speech(provider, body["text"], locale)
            except RuntimeError as exc:
                self._send_json({"error": str(exc)}, status=502)
                return
            except Exception as exc:
                self._send_json({"error": f"Unexpected synthesis error: {exc}"}, status=500)
                return
            self._send_json({"ok": True, **result})
            return

        if parsed.path == "/api/voice/chat":
            body = self._read_json_body()
            if not body or "message" not in body:
                self._send_json({"error": "message is required"}, status=400)
                return

            message = str(body["message"]).strip()
            if not message:
                self._send_json({"error": "message is empty"}, status=400)
                return

            locale = body.get("locale", PERSISTED_SETTINGS["language"])
            append_conversation_turn("You", message)
            reply_text = generate_assistant_reply(message, locale)
            append_conversation_turn("HomeHub", reply_text)

            audio_payload = None
            if body.get("speakReply", True):
                try:
                    audio_payload = synthesize_speech(PERSISTED_SETTINGS["ttsProvider"], reply_text, locale)
                except Exception as exc:
                    audio_payload = {
                        "error": str(exc),
                    }

            self._send_json(
                {
                    "ok": True,
                    "reply": reply_text,
                    "conversation": CURRENT_CONVERSATION,
                    "audio": audio_payload,
                }
            )
            return

        if parsed.path == "/api/settings/audio-provider":
            body = self._read_json_body()
            if not body:
                self._send_json({"error": "Invalid request body"}, status=400)
                return
            try:
                entry_type = str(body.get("entryType", "capability")).strip().lower() or "capability"
                provider_id = str(body.get("id", "")).strip().lower()
                if not provider_id:
                    raise ValueError("Entry id is required.")
                if provider_id in AUDIO_PROVIDER_CATALOG:
                    raise ValueError("This provider id is reserved by a built-in stack.")
                existing = load_custom_audio_providers()
                items = [item for item in existing.get("items", []) if item.get("id") != provider_id]
                if entry_type == "provider":
                    items.append(
                        {
                            "entryType": "provider",
                            "id": provider_id,
                            "label": body.get("label", provider_id),
                            "sttRuntime": body.get("sttRuntime", "catalog"),
                            "ttsRuntime": body.get("ttsRuntime", "catalog"),
                            "sttDefaultModel": body.get("sttDefaultModel", "not-configured"),
                            "sttFallbackModel": body.get("sttFallbackModel", "not-configured"),
                            "ttsDefaultModel": body.get("ttsDefaultModel", "not-configured"),
                            "ttsFallbackModel": body.get("ttsFallbackModel", "not-configured"),
                            "supportedLanguages": normalize_supported_languages(body.get("supportedLanguages")),
                        }
                    )
                else:
                    items.append(
                        {
                            "entryType": "capability",
                            "id": provider_id,
                            "label": body.get("label", provider_id),
                            "source": body.get("source", "Custom"),
                            "summary": body.get("summary", "Custom AI capability entry."),
                            "models": normalize_string_list(body.get("models")),
                            "capabilities": normalize_string_list(body.get("capabilities")),
                            "supportedLanguages": normalize_supported_languages(body.get("supportedLanguages")),
                            "syncOpenclaw": body.get("syncOpenclaw", "manual"),
                            "syncWorkbuddy": body.get("syncWorkbuddy", "manual"),
                        }
                    )
                save_custom_audio_providers({"items": items})
            except ValueError as exc:
                self._send_json({"error": str(exc)}, status=400)
                return
            self._send_json({"ok": True, "providerId": provider_id, "catalog": get_audio_provider_catalog()})
            return

        if parsed.path == "/api/voice/reset":
            CURRENT_CONVERSATION.clear()
            CURRENT_CONVERSATION.extend(deepcopy(VOICE_CONVERSATION))
            self._send_json({"ok": True, "conversation": CURRENT_CONVERSATION})
            return

        self.send_error(404)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", RUNTIME_PORT), Handler)
    print(f"HomeHub runtime started at http://127.0.0.1:{RUNTIME_PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nHomeHub runtime stopped")
        server.server_close()
