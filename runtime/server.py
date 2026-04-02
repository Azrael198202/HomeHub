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

try:
    from features.base import RuntimeBridge
    from features.loader import FeatureManager
except ModuleNotFoundError:
    from runtime.features.base import RuntimeBridge
    from runtime.features.loader import FeatureManager

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
FEATURES_DIR = ROOT / "features"


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
LAST_VOICE_ROUTE = {
    "kind": "general",
    "selected": {
        "intent": "general-chat",
        "featureId": "homehub-core",
        "featureName": "HomeHub Core",
        "action": "reply_directly",
        "score": 0.4,
    },
    "candidates": [],
}
PENDING_VOICE_CLARIFICATION = None

FEATURE_MANAGER = FeatureManager(FEATURES_DIR)

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


def openai_chat_json(system_prompt, user_prompt, model_name="gpt-4o-mini"):
    api_key = SECRETS.get("openaiApiKey", "")
    if not api_key:
        return None
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = json.loads(response.read().decode("utf-8"))
        content = data["choices"][0]["message"]["content"]
        if isinstance(content, list):
            content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
        return json.loads(content)
    except Exception:
        return None


def build_runtime_bridge():
    return RuntimeBridge(
        root=ROOT,
        get_setting=lambda key, default=None: PERSISTED_SETTINGS.get(key, default),
        get_secret=lambda key, default=None: SECRETS.get(key, default),
        openai_json=openai_chat_json,
        log=lambda message: print(f"[features] {message}"),
    )


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


def now_local():
    return datetime.now().replace(second=0, microsecond=0)


def now_hhmm():
    return datetime.now().strftime("%H:%M")


def parse_iso_datetime(value):
    try:
        return datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def make_memory_id(prefix):
    return f"{prefix}-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"


def format_datetime_local(value, locale):
    dt = parse_iso_datetime(value)
    if not dt:
        return str(value)
    if locale == "zh-CN":
        return dt.strftime("%m月%d日 %H:%M")
    if locale == "ja-JP":
        return dt.strftime("%m月%d日 %H:%M")
    return dt.strftime("%b %d %H:%M")


def sort_records_by_datetime(items, key_name):
    return sorted(
        items,
        key=lambda item: parse_iso_datetime(item.get(key_name)) or datetime.max,
    )


def get_upcoming_events(limit=5):
    now_value = now_local()
    events = []
    for event in HOME_MEMORY.get("events", []):
        start_at = parse_iso_datetime(event.get("startAt"))
        if start_at and start_at >= now_value - timedelta(hours=1):
            events.append(event)
    return sort_records_by_datetime(events, "startAt")[:limit]


def get_pending_reminders(limit=5):
    now_value = now_local()
    reminders = []
    for reminder in HOME_MEMORY.get("reminders", []):
        trigger_at = parse_iso_datetime(reminder.get("triggerAt"))
        if reminder.get("status", "pending") != "done" and trigger_at and trigger_at >= now_value - timedelta(hours=12):
            reminders.append(reminder)
    return sort_records_by_datetime(reminders, "triggerAt")[:limit]


def get_due_reminders(limit=3):
    now_value = now_local()
    due = []
    for reminder in HOME_MEMORY.get("reminders", []):
        trigger_at = parse_iso_datetime(reminder.get("triggerAt"))
        if reminder.get("status", "pending") != "done" and trigger_at and trigger_at <= now_value:
            due.append(reminder)
    return sort_records_by_datetime(due, "triggerAt")[:limit]


def record_memory_action(kind, summary):
    HOME_MEMORY.setdefault("recentActions", []).insert(
        0,
        {
            "id": make_memory_id("act"),
            "kind": kind,
            "summary": summary,
            "createdAt": now_local().isoformat(timespec="minutes"),
        },
    )
    del HOME_MEMORY["recentActions"][12:]


def create_local_event(title, start_at, end_at, participants=None, location="", reminder_offset_minutes=None, notes=""):
    event_id = make_memory_id("evt")
    reminder_ids = []
    event = {
        "id": event_id,
        "title": title,
        "startAt": start_at.isoformat(timespec="minutes"),
        "endAt": end_at.isoformat(timespec="minutes"),
        "participants": participants or [],
        "location": location,
        "source": "homehub-local",
        "createdAt": now_local().isoformat(timespec="minutes"),
        "notes": notes,
        "linkedReminderIds": reminder_ids,
    }
    HOME_MEMORY.setdefault("events", []).append(event)
    created_reminder = None
    if reminder_offset_minutes is not None:
        reminder_time = start_at - timedelta(minutes=reminder_offset_minutes)
        reminder_id = make_memory_id("rem")
        created_reminder = {
            "id": reminder_id,
            "title": f"Reminder: {title}",
            "triggerAt": reminder_time.isoformat(timespec="minutes"),
            "eventId": event_id,
            "status": "pending",
            "channels": ["voice", "tv", "mobile"],
            "createdAt": now_local().isoformat(timespec="minutes"),
        }
        HOME_MEMORY.setdefault("reminders", []).append(created_reminder)
        reminder_ids.append(reminder_id)
    record_memory_action("create-event", f"Created schedule '{title}' for {start_at.isoformat(timespec='minutes')}.")
    save_home_memory(HOME_MEMORY)
    return event, created_reminder


def create_local_reminder(title, trigger_at, notes=""):
    reminder = {
        "id": make_memory_id("rem"),
        "title": title,
        "triggerAt": trigger_at.isoformat(timespec="minutes"),
        "eventId": "",
        "status": "pending",
        "channels": ["voice", "tv", "mobile"],
        "createdAt": now_local().isoformat(timespec="minutes"),
        "notes": notes,
    }
    HOME_MEMORY.setdefault("reminders", []).append(reminder)
    record_memory_action("create-reminder", f"Created reminder '{title}' for {trigger_at.isoformat(timespec='minutes')}.")
    save_home_memory(HOME_MEMORY)
    return reminder


def detect_day_offset(text_value):
    lowered = text_value.lower()
    if "后天" in text_value:
        return 2
    if "明天" in text_value or "明早" in text_value or "明晚" in text_value or "tomorrow" in lowered:
        return 1
    return 0


def parse_zh_number(text_value):
    digits = {"零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
    if not text_value:
        return None
    if text_value == "十":
        return 10
    if "十" in text_value:
        left, _, right = text_value.partition("十")
        tens = 1 if left == "" else digits.get(left)
        ones = 0 if right == "" else digits.get(right)
        if tens is None or ones is None:
            return None
        return tens * 10 + ones
    if len(text_value) == 1:
        return digits.get(text_value)
    return None


def detect_time_from_text(text_value):
    lowered = text_value.lower()
    hour = None
    minute = 0
    match = re.search(r"(\d{1,2})[:：](\d{2})", text_value)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2))
    else:
        match = re.search(r"(\d{1,2})点半", text_value)
        if match:
            hour = int(match.group(1))
            minute = 30
        else:
            match = re.search(r"(\d{1,2})点(?:(\d{1,2})分?)?", text_value)
            if match:
                hour = int(match.group(1))
                minute = int(match.group(2) or 0)
            else:
                match = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b", lowered)
                if match:
                    hour = int(match.group(1))
                    minute = int(match.group(2) or 0)
                    if match.group(3) == "pm" and hour < 12:
                        hour += 12
                    if match.group(3) == "am" and hour == 12:
                        hour = 0
                else:
                    match = re.search(r"\b(\d{1,2})\b", text_value)
                    if match and any(token in text_value for token in ["点", "时", "hour", "pm", "am"]):
                        hour = int(match.group(1))
    if hour is None:
        zh_match = re.search(r"([零一二两三四五六七八九十]{1,3})点(半|([零一二两三四五六七八九十]{1,3})分?)?", text_value)
        if zh_match:
            hour = parse_zh_number(zh_match.group(1))
            if zh_match.group(2) == "半":
                minute = 30
            else:
                minute = parse_zh_number(zh_match.group(3) or "") or 0

    if hour is None:
        return None
    if any(token in text_value for token in ["下午", "晚上", "今晚", "傍晚"]) and hour < 12:
        hour += 12
    if any(token in text_value for token in ["中午"]) and hour < 11:
        hour += 12
    if any(token in lowered for token in ["afternoon", "evening", "tonight"]) and hour < 12:
        hour += 12
    return hour, minute


def detect_reminder_offset_minutes(text_value):
    if "提前半小时" in text_value or "提前半個小時" in text_value:
        return 30
    match = re.search(r"提前(\d{1,3})\s*分钟", text_value)
    if match:
        return int(match.group(1))
    match = re.search(r"提前(\d{1,2})\s*小时", text_value)
    if match:
        return int(match.group(1)) * 60
    match = re.search(r"(\d{1,3})\s*minutes?\s+before", text_value.lower())
    if match:
        return int(match.group(1))
    match = re.search(r"(\d{1,2})\s*hours?\s+before", text_value.lower())
    if match:
        return int(match.group(1)) * 60
    return 30 if "提前提醒" in text_value or "remind me ahead" in text_value.lower() else None


def infer_title_from_text(text_value):
    quoted = re.search(r"[\"“](.+?)[\"”]", text_value)
    if quoted:
        return quoted.group(1).strip()
    person_meeting = re.search(r"和(.+?)的(会议|会面|聚餐|通话|视频|课程)", text_value)
    if person_meeting:
        return f"和{person_meeting.group(1).strip()}的{person_meeting.group(2).strip()}"
    remind_match = re.search(r"提醒我(.+)", text_value)
    if remind_match:
        return remind_match.group(1).strip("，。 ")
    generic = re.search(r"(创建|添加|安排|设定|新建)(.+?)(日程|会议|提醒|行程)", text_value)
    if generic:
        core = generic.group(2).strip("，。 ")
        suffix = generic.group(3).strip()
        return f"{core}{suffix}"
    return "家庭日程"


def build_datetime_from_text(text_value):
    time_parts = detect_time_from_text(text_value)
    if not time_parts:
        return None
    hour, minute = time_parts
    base = now_local() + timedelta(days=detect_day_offset(text_value))
    candidate = base.replace(hour=hour, minute=minute)
    if detect_day_offset(text_value) == 0 and candidate < now_local() - timedelta(minutes=5):
        candidate += timedelta(days=1)
    return candidate


def summarize_schedule(locale):
    events = get_upcoming_events(limit=3)
    reminders = get_pending_reminders(limit=3)
    if locale == "zh-CN":
        if not events and not reminders:
            return "本地日程里暂时没有新的安排或提醒。"
        lines = []
        if events:
            lines.append("接下来日程有：" + "；".join(f"{event['title']}（{format_datetime_local(event['startAt'], locale)}）" for event in events))
        if reminders:
            lines.append("提醒有：" + "；".join(f"{item['title']}（{format_datetime_local(item['triggerAt'], locale)}）" for item in reminders))
        return " ".join(lines)
    if locale == "ja-JP":
        return "ローカル予定とリマインダーを表示しました。"
    return "I pulled the upcoming local schedule and reminders."


def try_extract_schedule_with_openai(user_text, locale):
    api_key = SECRETS.get("openaiApiKey", "")
    if not api_key:
        return None
    schema_prompt = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You extract household scheduling intent. "
                    "Return JSON only with keys: action, title, startAt, endAt, reminderOffsetMinutes, location, participants, confidence. "
                    "Valid action values: create_event, create_reminder, show_schedule, none. "
                    f"Current local time is {now_local().isoformat(timespec='minutes')}."
                ),
            },
            {"role": "user", "content": f"Locale={locale}\nUser message: {user_text}"},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(schema_prompt).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = json.loads(response.read().decode("utf-8"))
        content = payload["choices"][0]["message"]["content"]
        if isinstance(content, list):
            content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
        data = json.loads(content)
        if not isinstance(data, dict):
            return None
        return data
    except Exception:
        return None


def detect_local_assistant_action(user_text, locale):
    lowered = user_text.lower()
    ai_result = try_extract_schedule_with_openai(user_text, locale)
    if isinstance(ai_result, dict) and ai_result.get("action") in {"create_event", "create_reminder", "show_schedule"}:
        return ai_result
    if any(token in user_text for token in ["查看日程", "看看日程", "我的日程", "有什么安排", "提醒列表"]) or "show my schedule" in lowered:
        return {"action": "show_schedule"}
    if any(token in user_text for token in ["提醒", "日程", "会议", "安排", "行程", "闹钟"]) or "remind me" in lowered or "schedule" in lowered:
        start_at = build_datetime_from_text(user_text)
        offset = detect_reminder_offset_minutes(user_text)
        title = infer_title_from_text(user_text)
        if start_at and any(token in user_text for token in ["日程", "会议", "安排", "行程", "schedule", "meeting"]):
            return {
                "action": "create_event",
                "title": title,
                "startAt": start_at.isoformat(timespec="minutes"),
                "endAt": (start_at + timedelta(minutes=60)).isoformat(timespec="minutes"),
                "reminderOffsetMinutes": offset,
                "location": "",
                "participants": [],
            }
        if start_at and any(token in user_text for token in ["提醒", "闹钟"]) or ("remind me" in lowered and start_at):
            return {
                "action": "create_reminder",
                "title": title if title != "家庭日程" else "HomeHub reminder",
                "startAt": start_at.isoformat(timespec="minutes"),
            }
    return {"action": "none"}


def generate_assistant_reply(user_text, locale):
    action = detect_local_assistant_action(user_text, locale)
    action_name = action.get("action", "none")
    if action_name == "show_schedule":
        return summarize_schedule(locale)

    if action_name == "create_event":
        start_at = parse_iso_datetime(action.get("startAt"))
        end_at = parse_iso_datetime(action.get("endAt")) or (start_at + timedelta(minutes=60) if start_at else None)
        if not start_at or not end_at:
            return "我还没完全听清时间，你可以再说一次具体几点吗？" if locale == "zh-CN" else "I still need a specific time."
        title = str(action.get("title", "")).strip() or infer_title_from_text(user_text)
        reminder_offset = action.get("reminderOffsetMinutes")
        if reminder_offset is not None:
            try:
                reminder_offset = int(reminder_offset)
            except (TypeError, ValueError):
                reminder_offset = None
        event, reminder = create_local_event(
            title,
            start_at,
            end_at,
            participants=action.get("participants") or [],
            location=str(action.get("location", "")).strip(),
            reminder_offset_minutes=reminder_offset,
            notes=f"Original request: {user_text}",
        )
        if locale == "zh-CN":
            if reminder:
                return (
                    f"已经帮你把“{event['title']}”加入 HomeHub 本地日程，时间是 {format_datetime_local(event['startAt'], locale)}。"
                    f" 我也加了一个提前 {reminder_offset} 分钟的提醒，会在电视、语音和手机端一起显示。"
                )
            return f"已经帮你把“{event['title']}”加入 HomeHub 本地日程，时间是 {format_datetime_local(event['startAt'], locale)}。"
        if locale == "ja-JP":
            return f"ローカル予定に「{event['title']}」を追加しました。"
        return f"I added '{event['title']}' to HomeHub local schedule for {format_datetime_local(event['startAt'], locale)}."

    if action_name == "create_reminder":
        trigger_at = parse_iso_datetime(action.get("startAt"))
        if not trigger_at:
            return "我还需要一个更具体的提醒时间。" if locale == "zh-CN" else "I still need a reminder time."
        title = str(action.get("title", "")).strip() or infer_title_from_text(user_text)
        reminder = create_local_reminder(title, trigger_at, notes=f"Original request: {user_text}")
        if locale == "zh-CN":
            return f"已经创建提醒“{reminder['title']}”，触发时间是 {format_datetime_local(reminder['triggerAt'], locale)}。"
        if locale == "ja-JP":
            return f"リマインダー「{reminder['title']}」を追加しました。"
        return f"I created reminder '{reminder['title']}' for {format_datetime_local(reminder['triggerAt'], locale)}."

    if locale == "zh-CN":
        return "我已收到你的语音，也可以继续直接说“帮我创建明天下午三点的日程，提前半小时提醒”。"
    if locale == "ja-JP":
        return "音声を受け取りました。予定やリマインダーも追加できます。"
    return "I received your voice. You can also ask me to create a schedule item or reminder."


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


def build_household_modules(locale):
    modules = deepcopy(HOUSEHOLD_MODULES)
    upcoming_events = get_upcoming_events(limit=3)
    pending_reminders = get_pending_reminders(limit=3)
    due_reminders = get_due_reminders(limit=2)

    for module in modules:
        if module["id"] == "schedule":
            if upcoming_events:
                next_event = upcoming_events[0]
                if locale == "zh-CN":
                    module["summary"] = f"已记录 {len(upcoming_events)} 个本地日程。下一个是 {next_event['title']}，时间 {format_datetime_local(next_event['startAt'], locale)}。"
                    module["actionLabel"] = "查看日程"
                elif locale == "ja-JP":
                    module["summary"] = f"ローカル予定 {len(upcoming_events)} 件。次は {next_event['title']}、{format_datetime_local(next_event['startAt'], locale)}。"
                    module["actionLabel"] = "予定を見る"
                else:
                    module["summary"] = f"{len(upcoming_events)} local events tracked. Next: {next_event['title']} at {format_datetime_local(next_event['startAt'], locale)}."
                    module["actionLabel"] = "Open Schedule"
                module["state"] = "attention" if due_reminders else "active"
            else:
                if locale == "zh-CN":
                    module["summary"] = "还没有本地日程。你可以直接对 HomeHub 说出要创建的安排。"
                    module["actionLabel"] = "语音创建"
                elif locale == "ja-JP":
                    module["summary"] = "ローカル予定はまだありません。音声で追加できます。"
                    module["actionLabel"] = "音声で作成"
                else:
                    module["summary"] = "No local schedule items yet. Ask HomeHub by voice to create one."
                    module["actionLabel"] = "Create by Voice"
                module["state"] = "ready"
        if module["id"] == "messages" and pending_reminders:
            next_reminder = pending_reminders[0]
            if locale == "zh-CN":
                module["summary"] = f"已有 {len(pending_reminders)} 条提醒。下一条是 {next_reminder['title']}，将在 {format_datetime_local(next_reminder['triggerAt'], locale)} 触发。"
                module["actionLabel"] = "查看提醒"
            elif locale == "ja-JP":
                module["summary"] = f"リマインダー {len(pending_reminders)} 件。次は {next_reminder['title']}、{format_datetime_local(next_reminder['triggerAt'], locale)}。"
                module["actionLabel"] = "通知を見る"
            else:
                module["summary"] = f"{len(pending_reminders)} reminders queued. Next: {next_reminder['title']} at {format_datetime_local(next_reminder['triggerAt'], locale)}."
                module["actionLabel"] = "View Reminders"
            module["state"] = "attention" if due_reminders else "active"
    return modules


def build_assistant_memory_snapshot():
    upcoming_events = get_upcoming_events(limit=5)
    pending_reminders = get_pending_reminders(limit=5)
    due_reminders = get_due_reminders(limit=3)
    return {
        "upcomingEvents": upcoming_events,
        "pendingReminders": pending_reminders,
        "dueReminders": due_reminders,
        "recentActions": HOME_MEMORY.get("recentActions", [])[:5],
    }


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
        "householdModules": build_household_modules(PERSISTED_SETTINGS["language"]),
        "activeAgents": agents,
        "timelineEvents": timeline,
        "modelProviders": MODEL_PROVIDERS,
        "skillCatalog": SKILLS,
        "pairingSession": PAIRING,
        "relayMessages": RELAY_MESSAGES,
        "assistantMemory": build_assistant_memory_snapshot(),
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


def build_feature_household_modules(locale):
    runtime = build_runtime_bridge()
    modules = FEATURE_MANAGER.enhance_household_modules(deepcopy(HOUSEHOLD_MODULES), locale, runtime)
    agent_types = FEATURE_MANAGER.list_agent_types(locale, runtime)
    if agent_types:
        if locale == "zh-CN":
            summary = f"HomeHub 当前可创建 {len(agent_types)} 类智能体。比如：{agent_types[0]['name']}。"
            action = "语音创建"
            name = "智能体工厂"
        elif locale == "ja-JP":
            summary = f"HomeHub can create {len(agent_types)} agent types."
            action = "音声で作成"
            name = "エージェント工房"
        else:
            summary = f"HomeHub can create {len(agent_types)} agent types."
            action = "Create by Voice"
            name = "Agent Factory"
        modules.append(
            {
                "id": "agent-factory",
                "name": name,
                "summary": summary,
                "state": "active",
                "actionLabel": action,
            }
        )
    return modules


def build_assistant_memory_snapshot(locale=None):
    runtime = build_runtime_bridge()
    payload = FEATURE_MANAGER.dashboard_payload(locale or PERSISTED_SETTINGS["language"], runtime)
    return payload.get(
        "assistantMemory",
        {
            "upcomingEvents": [],
            "pendingReminders": [],
            "dueReminders": [],
            "recentActions": [],
        },
    )


def build_agent_type_catalog(locale):
    runtime = build_runtime_bridge()
    return FEATURE_MANAGER.list_agent_types(locale, runtime)


def build_agent_factory_reply(locale):
    agent_types = build_agent_type_catalog(locale)
    if not agent_types:
        return "我还没有可创建的智能体模板。" if locale == "zh-CN" else "I do not have any agent templates yet."
    if locale == "zh-CN":
        joined = "；".join(f"{item['name']}：{item['summary']}" for item in agent_types[:3])
        example = agent_types[0].get("examplePrompt", "")
        return f"我可以帮你创建这些智能体：{joined}。你可以直接说：“{example}”。"
    if locale == "ja-JP":
        return "作成できるエージェントを案内します。"
    joined = "; ".join(f"{item['name']}: {item['summary']}" for item in agent_types[:3])
    example = agent_types[0].get("examplePrompt", "")
    return f"I can create these agent types: {joined}. Try saying: '{example}'."


def openai_chat_reply(system_prompt, user_prompt, model_name="gpt-4o-mini"):
    api_key = SECRETS.get("openaiApiKey", "")
    if not api_key:
        return None
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.6,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = json.loads(response.read().decode("utf-8"))
        content = data["choices"][0]["message"]["content"]
        if isinstance(content, list):
            content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
        text = str(content or "").strip()
        return text or None
    except Exception:
        return None


def build_feature_intent_catalog(locale):
    runtime = build_runtime_bridge()
    features = FEATURE_MANAGER.list_features(runtime)
    return [
        {
            "featureId": item.get("id"),
            "featureName": item.get("name"),
            "summary": item.get("summary", ""),
            "intents": item.get("voiceIntents", []),
        }
        for item in features
        if item.get("voiceIntents")
    ]


def openai_route_voice_request(user_text, locale, heuristic_route):
    catalog = build_feature_intent_catalog(locale)
    agent_types = build_agent_type_catalog(locale)
    system_prompt = (
        "You are the HomeHub intent router and agent orchestrator. "
        "Classify the user's voice request and decide whether HomeHub should route it to a feature, "
        "the agent factory, general chat, or ask a clarification question. "
        "Return JSON only with keys: kind, targetFeatureId, targetIntentId, action, confidence, "
        "needsClarification, clarificationQuestion, reasoning. "
        "Valid kind values: feature, agent_factory, general, clarify. "
        "Only choose targetFeatureId values that exist in the provided feature catalog."
    )
    user_prompt = json.dumps(
        {
            "locale": locale,
            "userText": user_text,
            "featureCatalog": catalog,
            "agentTypes": agent_types,
            "heuristicRoute": heuristic_route,
        },
        ensure_ascii=False,
    )
    payload = openai_chat_json(system_prompt, user_prompt, "gpt-4o-mini")
    return payload if isinstance(payload, dict) else None


def orchestrate_voice_route(user_text, locale, heuristic_route):
    selected = heuristic_route.get("selected")
    model_route = openai_route_voice_request(user_text, locale, heuristic_route)
    if not model_route:
        return heuristic_route

    kind = str(model_route.get("kind", "")).strip().lower() or heuristic_route.get("kind", "general")
    target_feature_id = str(model_route.get("targetFeatureId", "")).strip()
    target_intent_id = str(model_route.get("targetIntentId", "")).strip()
    action = str(model_route.get("action", "")).strip()
    try:
        confidence = float(model_route.get("confidence", 0.0))
    except (TypeError, ValueError):
        confidence = 0.0
    needs_clarification = bool(model_route.get("needsClarification"))
    clarification_question = str(model_route.get("clarificationQuestion", "")).strip()

    candidates = heuristic_route.get("candidates", [])
    matched_candidate = None
    if target_feature_id:
        for item in candidates:
            if item.get("featureId") == target_feature_id:
                matched_candidate = dict(item)
                break

    selected_route = matched_candidate or dict(selected or {})
    if kind == "feature" and target_feature_id:
        selected_route.setdefault("featureId", target_feature_id)
        if target_intent_id:
            selected_route["intent"] = target_intent_id
        if action:
            selected_route["action"] = action
        if confidence:
            selected_route["score"] = confidence
        selected_route.setdefault("featureName", selected_route.get("featureName", target_feature_id))

    if kind == "clarify" and clarification_question:
        return {
            "kind": "clarify",
            "selected": {
                "intent": "clarify",
                "featureId": selected_route.get("featureId", "homehub-core"),
                "featureName": selected_route.get("featureName", "HomeHub Core"),
                "action": action or "clarify",
                "score": confidence or 0.6,
            },
            "candidates": candidates,
            "clarificationQuestion": clarification_question,
            "reasoning": model_route.get("reasoning", ""),
        }

    if kind in {"feature", "agent_factory", "general"}:
        return {
            "kind": kind,
            "selected": selected_route or heuristic_route.get("selected"),
            "candidates": candidates,
            "reasoning": model_route.get("reasoning", ""),
            "modelRoute": model_route,
        }
    return heuristic_route


def build_general_voice_reply(user_text, locale):
    recent_turns = CURRENT_CONVERSATION[-6:]
    conversation_context = "\n".join(f"{item['speaker']}: {item['text']}" for item in recent_turns)
    if locale == "zh-CN":
        system_prompt = (
            "你是 HomeHub，家庭生活助手。"
            "如果用户不是在创建日程或提醒，就自然地直接回答用户当前的话。"
            "回答要简短、温和、实用，像家庭里的语音助手。"
            "不要提自己已经收到语音，不要把回答变成固定模板，不要编造你已经执行过的动作。"
        )
    elif locale == "ja-JP":
        system_prompt = (
            "You are HomeHub, a household voice assistant. "
            "Reply naturally and briefly when the user is not creating a schedule or reminder. "
            "Do not say that you merely received the voice input, and do not claim actions you did not perform."
        )
    else:
        system_prompt = (
            "You are HomeHub, a household voice assistant. "
            "Reply naturally and briefly when the user is not creating a schedule or reminder. "
            "Do not say that you merely received the voice input, and do not claim actions you did not perform."
        )
    ai_reply = openai_chat_reply(
        system_prompt,
        f"Locale: {locale}\nRecent conversation:\n{conversation_context}\nUser: {user_text}",
    )
    if ai_reply:
        return ai_reply

    lowered = user_text.lower()
    if locale == "zh-CN":
        if "天气" in user_text:
            return "你可以切到天气卡片查看当前天气；如果你愿意，我后面也可以把天气问答接成直接语音回答。"
        if "学习计划" in user_text or "智能体" in user_text:
            return "如果你想创建新的助手，可以直接说出目标，例如“帮我创建一个儿子四年级学习计划智能体”。"
        if any(token in user_text for token in ["几点", "时间"]):
            return f"现在是 {datetime.now().strftime('%H:%M')}。"
        return "你可以直接告诉我你想做什么，比如问问题、创建日程、添加提醒，或者让我帮你创建一个智能体。"
    if locale == "ja-JP":
        if "weather" in lowered:
            return "天気カードも確認できます。必要なら音声で直接答える流れも続けて追加できます。"
        return "予定やリマインダー以外でも、そのまま用件を話してください。できる範囲で続けて案内します。"
    if "weather" in lowered:
        return "You can also open the weather card, and I can keep expanding direct voice answers from here."
    return "You can just tell me what you need, and I will either answer directly or help you create a schedule, reminder, or agent."


def route_voice_request(user_text, locale):
    runtime = build_runtime_bridge()
    route = FEATURE_MANAGER.route_voice_intent(user_text, locale, runtime)
    heuristic_route = {
        "kind": "feature" if route.get("selected") else ("agent_factory" if is_generic_agent_request(user_text) else "general"),
        "selected": route.get("selected")
        or (
            {
                "intent": "agent-factory",
                "featureId": "homehub-core",
                "featureName": "HomeHub Core",
                "action": "list_agent_types",
                "score": 0.82,
            }
            if is_generic_agent_request(user_text)
            else {
                "intent": "general-chat",
                "featureId": "homehub-core",
                "featureName": "HomeHub Core",
                "action": "reply_directly",
                "score": 0.4,
            }
        ),
        "candidates": route.get("candidates", []),
    }
    return orchestrate_voice_route(user_text, locale, heuristic_route)


def build_clarification_reply(route, locale):
    question = str(route.get("clarificationQuestion", "")).strip()
    if question:
        return question
    if locale == "zh-CN":
        return "我还需要再确认一点信息，你可以再具体说一下你的目标吗？"
    if locale == "ja-JP":
        return "もう少しだけ確認したいので、目的をもう少し具体的に教えてください。"
    return "I need one more detail before I can route that correctly. Could you say a bit more?"


def serialize_voice_route(route):
    return {
        "kind": route.get("kind"),
        "selected": route.get("selected"),
        "candidates": route.get("candidates", []),
        "clarificationQuestion": route.get("clarificationQuestion", ""),
        "reasoning": route.get("reasoning", ""),
    }


def build_pending_clarification_snapshot():
    if not PENDING_VOICE_CLARIFICATION:
        return None
    return dict(PENDING_VOICE_CLARIFICATION)


def resolve_voice_request(user_text, locale):
    global PENDING_VOICE_CLARIFICATION

    runtime = build_runtime_bridge()
    original_text = user_text
    combined_text = user_text
    clarification_context = PENDING_VOICE_CLARIFICATION

    if clarification_context:
        combined_text = (
            f"Original request: {clarification_context.get('originalRequest', '')}\n"
            f"Clarification answer: {user_text}"
        )

    route = route_voice_request(combined_text, locale)

    if route.get("kind") == "clarify":
        PENDING_VOICE_CLARIFICATION = {
            "originalRequest": clarification_context.get("originalRequest", original_text) if clarification_context else original_text,
            "latestUserMessage": original_text,
            "clarificationQuestion": build_clarification_reply(route, locale),
            "selected": route.get("selected"),
            "createdAt": datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes"),
        }
        return {
            "reply": PENDING_VOICE_CLARIFICATION["clarificationQuestion"],
            "route": serialize_voice_route(route),
            "pendingClarification": build_pending_clarification_snapshot(),
        }

    if route.get("kind") == "feature":
        result = FEATURE_MANAGER.dispatch_voice_intent(route, combined_text, locale, runtime) or {}
        reply = result.get("reply") or build_general_voice_reply(original_text, locale)
    elif route.get("kind") == "agent_factory":
        reply = build_agent_factory_reply(locale)
    else:
        reply = build_general_voice_reply(combined_text if clarification_context else original_text, locale)

    PENDING_VOICE_CLARIFICATION = None
    return {
        "reply": reply,
        "route": serialize_voice_route(route),
        "pendingClarification": None,
    }


def build_voice_router_snapshot(locale):
    runtime = build_runtime_bridge()
    features = FEATURE_MANAGER.list_features(runtime)
    return {
        "pendingVoiceClarification": build_pending_clarification_snapshot(),
        "featureIntents": [
            {
                "featureId": item.get("id"),
                "featureName": item.get("name"),
                "intents": item.get("voiceIntents", []),
            }
            for item in features
            if item.get("voiceIntents")
        ]
    }


def is_generic_agent_request(user_text):
    lowered = user_text.lower()
    zh_request = "智能体" in user_text and any(token in user_text for token in ["创建", "新建", "能创建", "有哪些", "什么"])
    en_request = "agent" in lowered and any(token in lowered for token in ["create", "make", "what", "available"])
    return zh_request or en_request


def generate_assistant_reply(user_text, locale):
    return resolve_voice_request(user_text, locale)["reply"]


def build_last_voice_route(user_text, locale):
    return serialize_voice_route(route_voice_request(user_text, locale))


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
    runtime = build_runtime_bridge()
    feature_payload = FEATURE_MANAGER.dashboard_payload(PERSISTED_SETTINGS["language"], runtime)
    voice_router = build_voice_router_snapshot(PERSISTED_SETTINGS["language"])

    return {
        "hero": {
            "title": "HomeHub",
            "subtitle": "AI Box for the Living Room",
            "tagline": "Boot like a TV box, collaborate like a multi-agent team.",
        },
        "boxProfile": BOX_PROFILE,
        "householdModules": build_feature_household_modules(PERSISTED_SETTINGS["language"]),
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
        "lastVoiceRoute": LAST_VOICE_ROUTE,
        "features": FEATURE_MANAGER.list_features(runtime),
        "agentTypes": FEATURE_MANAGER.list_agent_types(PERSISTED_SETTINGS["language"], runtime),
        **voice_router,
        **feature_payload,
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
        runtime = build_runtime_bridge()
        feature_response = FEATURE_MANAGER.handle_api("GET", path, parse_qs(parsed.query), None, runtime)
        if feature_response:
            self._send_json(feature_response.get("body", {}), status=feature_response.get("status", 200))
            return

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

        if path == "/api/features":
            self._send_json(FEATURE_MANAGER.list_features(runtime))
            return

        if path == "/api/agent-types":
            self._send_json(FEATURE_MANAGER.list_agent_types(PERSISTED_SETTINGS["language"], runtime))
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
        global PERSISTED_SETTINGS, SECRETS, SECRET_SOURCES, LAST_VOICE_ROUTE, PENDING_VOICE_CLARIFICATION

        parsed = urlparse(self.path)
        runtime = build_runtime_bridge()
        preview_body = self._read_json_body()
        feature_response = FEATURE_MANAGER.handle_api("POST", parsed.path, parse_qs(parsed.query), preview_body, runtime)
        if feature_response:
            self._send_json(feature_response.get("body", {}), status=feature_response.get("status", 200))
            return

        if parsed.path == "/api/settings/language":
            body = preview_body or self._read_json_body()
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
            body = preview_body or self._read_json_body()
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
            body = preview_body or self._read_json_body()
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
            body = preview_body or self._read_json_body()
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
            body = preview_body or self._read_json_body()
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
            body = preview_body or self._read_json_body()
            if not body or "message" not in body:
                self._send_json({"error": "message is required"}, status=400)
                return

            message = str(body["message"]).strip()
            if not message:
                self._send_json({"error": "message is empty"}, status=400)
                return

            locale = body.get("locale", PERSISTED_SETTINGS["language"])
            append_conversation_turn("You", message)
            resolution = resolve_voice_request(message, locale)
            voice_route = resolution["route"]
            LAST_VOICE_ROUTE = voice_route
            reply_text = resolution["reply"]
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
                    "voiceRoute": voice_route,
                    "pendingVoiceClarification": resolution.get("pendingClarification"),
                    "assistantMemory": build_assistant_memory_snapshot(),
                    "audio": audio_payload,
                }
            )
            return

        if parsed.path == "/api/settings/audio-provider":
            body = preview_body or self._read_json_body()
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
            LAST_VOICE_ROUTE = {
                "kind": "general",
                "selected": {
                    "intent": "general-chat",
                    "featureId": "homehub-core",
                    "featureName": "HomeHub Core",
                    "action": "reply_directly",
                    "score": 0.4,
                },
                "candidates": [],
                "clarificationQuestion": "",
                "reasoning": "",
            }
            PENDING_VOICE_CLARIFICATION = None
            FEATURE_MANAGER.reset(runtime)
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
