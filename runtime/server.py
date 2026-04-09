import base64
import json
import mimetypes
import os
import re
import subprocess
import sys
import threading
import time
import traceback
import urllib.error
import urllib.request
from copy import deepcopy
from datetime import datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT_DIR = CURRENT_DIR.parent
if str(PROJECT_ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT_DIR))

from runtime.features.base import RuntimeBridge
from runtime.features.loader import FeatureManager
from runtime.server_dashboard import build_dashboard as build_dashboard_payload
from runtime.server_audio import (
    synthesize_speech as synthesize_speech_payload,
    transcribe_audio as transcribe_audio_payload,
)
from runtime.server_config import (
    bootstrap_snapshot as bootstrap_snapshot_payload,
    get_effective_secrets as get_effective_secrets_payload,
    get_google_cloud_headers as get_google_cloud_headers_payload,
    get_google_service_account_file as get_google_service_account_file_payload,
    get_secret_sources as get_secret_sources_payload,
    get_secrets_file as get_secrets_file_payload,
    load_bootstrap_status as load_bootstrap_status_payload,
    load_persisted_settings as load_persisted_settings_payload,
    load_secrets_file as load_secrets_file_payload,
    refresh_bootstrap_process_state as refresh_bootstrap_process_state_payload,
    save_bootstrap_status as save_bootstrap_status_payload,
    save_persisted_settings as save_persisted_settings_payload,
    save_secrets as save_secrets_payload,
    start_bootstrap_install as start_bootstrap_install_payload,
)
from runtime.server_voice import (
    build_last_voice_route as build_last_voice_route_payload,
    build_voice_router_snapshot as build_voice_router_snapshot_payload,
    default_last_voice_route,
    generate_assistant_reply as generate_assistant_reply_payload,
    resolve_voice_request as resolve_voice_request_payload,
)
from runtime.server_memory import (
    build_household_modules as build_household_modules_payload,
    create_local_event as create_local_event_payload,
    create_local_reminder as create_local_reminder_payload,
    default_home_memory as default_home_memory_payload,
    detect_local_assistant_action as detect_local_assistant_action_payload,
    format_datetime_local as format_datetime_local_payload,
    get_due_reminders as get_due_reminders_payload,
    get_pending_reminders as get_pending_reminders_payload,
    get_upcoming_events as get_upcoming_events_payload,
    load_home_memory as load_home_memory_payload,
    now_hhmm as now_hhmm_payload,
    now_local as now_local_payload,
    parse_iso_datetime as parse_iso_datetime_payload,
    save_home_memory as save_home_memory_payload,
    summarize_schedule as summarize_schedule_payload,
)
from runtime.server_components.greetings import build_initial_conversation, build_welcome_message
from runtime.server_components.language_detector import detect_text_locale, normalize_locale
from runtime.server_components.semantic_memory import (
    export_training_pairs,
    query_semantic_memory,
    record_semantic_example,
    semantic_backend_snapshot,
)
from runtime.cortex.architect import CortexArchitect
from runtime.cortex.models import default_agent_cortex
from runtime.server_network import (
    build_source_labels,
    build_network_lookup_reply,
    perform_controlled_network_lookup as perform_controlled_network_lookup_impl,
    perform_network_lookup as perform_network_lookup_impl,
)
from runtime.server_weather import (
    default_weather_state as default_weather_state_payload,
    load_weather_state as load_weather_state_payload,
    lookup_weather_from_query as lookup_weather_from_query_payload,
    refresh_weather_from_coordinates as refresh_weather_from_coordinates_payload,
    save_weather_state as save_weather_state_payload,
)
from runtime.server_routes import handle_get_route, handle_post_route
from runtime.server_components.task_router import build_task_spec, infer_task_spec_with_openai

ROOT = CURRENT_DIR
STATIC_DIR = ROOT / "static"
GENERATED_DIR = ROOT / "generated"
SETTINGS_FILE = ROOT / "settings.json"
CUSTOM_AUDIO_PROVIDERS_FILE = ROOT / "custom_audio_providers.json"
BOOTSTRAP_STATUS_FILE = ROOT / "bootstrap_status.json"
HOME_MEMORY_FILE = ROOT / "home_memory.json"
SECRETS_LOCAL_FILE = ROOT / "secrets.local.json"
SECRETS_PROD_FILE = ROOT / "secrets.prod.json"
USAGE_LOG_FILE = ROOT / "usage-cost-log.jsonl"
CONVERSATION_LOG_FILE = ROOT / "conversation_log.jsonl"
WEATHER_STATE_FILE = ROOT / "weather_state.json"
GOOGLE_SERVICE_ACCOUNT_FILE = ROOT / "google-cloud-service-account.json"
RUNTIME_ENV = os.environ.get("HOMEHUB_ENV", "local").lower()
RUNTIME_HOST = os.environ.get("HOMEHUB_HOST", "127.0.0.1")
RUNTIME_PORT = int(os.environ.get("HOMEHUB_PORT", "8787"))
FEATURES_DIR = ROOT / "features"
PROJECT_ROOT = ROOT.parent
BOOTSTRAP_SCRIPT = PROJECT_ROOT / "tools" / "bootstrap_homehub.py"
BOOTSTRAP_PROCESS = None
BOOTSTRAP_STALE_SECONDS = 300
OLLAMA_INVENTORY_CACHE = {"value": None, "updated_at": 0.0}
OLLAMA_INVENTORY_TTL_SECONDS = 15.0
EMAIL_SYNC_INTERVAL_SECONDS = int(os.environ.get("HOMEHUB_EMAIL_SYNC_INTERVAL", "60"))
BRIDGE_PULL_INTERVAL_SECONDS = int(os.environ.get("HOMEHUB_BRIDGE_PULL_INTERVAL", "5"))


def get_secrets_file():
    return get_secrets_file_payload(RUNTIME_ENV, SECRETS_LOCAL_FILE, SECRETS_PROD_FILE)


MODEL_PROVIDERS = [
    {
        "id": "openai",
        "name": "OpenAI",
        "type": "cloud",
        "capabilities": ["chat", "vision", "voice", "tool-use", "reasoning", "ocr", "office-docs"],
        "endpointHint": "https://api.openai.com/v1",
    },
    {
        "id": "anthropic",
        "name": "Anthropic",
        "type": "cloud",
        "capabilities": ["chat", "vision", "reasoning", "document-drafting"],
        "endpointHint": "https://api.anthropic.com",
    },
    {
        "id": "gemini",
        "name": "Google Gemini",
        "type": "cloud",
        "capabilities": ["chat", "vision", "tool-use", "ocr", "office-docs"],
        "endpointHint": "https://generativelanguage.googleapis.com",
    },
    {
        "id": "huggingface",
        "name": "Hugging Face",
        "type": "cloud",
        "capabilities": ["chat", "vision", "embeddings", "speech", "open-weight", "ocr"],
        "endpointHint": "https://api-inference.huggingface.co",
    },
    {
        "id": "ollama",
        "name": "Ollama Local",
        "type": "local",
        "capabilities": ["chat", "vision", "ocr", "office-docs"],
        "endpointHint": "http://localhost:11434",
    },
]

OLLAMA_BIN_CANDIDATES = [
    os.environ.get("HOMEHUB_OLLAMA_BIN", "").strip(),
    os.environ.get("OLLAMA_BIN", "").strip(),
    os.environ.get("LOCALAPPDATA", "").strip() + "\\Programs\\Ollama\\ollama.exe" if os.environ.get("LOCALAPPDATA") else "",
    "C:\\Users\\hy\\AppData\\Local\\Programs\\Ollama\\ollama.exe",
    "ollama",
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
        "id": "schedule",
        "name": "Local Schedule",
        "summary": "No local events yet.",
        "state": "ready",
        "actionLabel": "Create by Voice",
    },
    {
        "id": "messages",
        "name": "Reminder Center",
        "summary": "No reminders yet.",
        "state": "ready",
        "actionLabel": "Create Reminder",
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

RUNTIME_PROFILES = [
    {
        "id": "low-memory",
        "label": "Low Memory",
        "summary": "Optimized for 8GB-class machines. HomeHub avoids local 7B vision/coder workloads, keeps OCR lightweight, and prefers small local chat or cloud offload.",
        "localRoles": ["wake word", "light chat", "RapidOCR", "mail sync", "small-model fallback"],
        "cloudRoles": ["heavy planning", "vision reasoning", "document generation review"],
    },
    {
        "id": "edge-hybrid",
        "label": "Edge Hybrid",
        "summary": "Default for industrial boxes: keep wake, fallback chat, and basic routing local; use API for heavy planning and premium voice.",
        "localRoles": ["wake word", "offline fallback", "light chat", "receipt fallback"],
        "cloudRoles": ["deep planning", "image-heavy reasoning", "high-end voice", "service generation review"],
    },
    {
        "id": "local-essential",
        "label": "Local Essential",
        "summary": "Privacy-first and low-cost mode. HomeHub prefers local models even if responses are slower or less capable.",
        "localRoles": ["wake word", "chat", "vision fallback", "feature drafts", "speech stack"],
        "cloudRoles": ["only when forced"],
    },
    {
        "id": "cloud-enhanced",
        "label": "Cloud Enhanced",
        "summary": "Best experience mode. Local models stay as backup, while major reasoning and multimodal tasks go to API models.",
        "localRoles": ["wake word", "offline backup", "quick fallback"],
        "cloudRoles": ["planner", "vision", "generation review", "premium TTS", "embeddings"],
    },
]

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
    "sensevoice-local": {
        "label": "SenseVoice Local",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "manual"},
        "stt": {
            "defaultModel": "SenseVoiceSmall",
            "fallbackModel": "whisper-large-v3",
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
    "kokoro-local": {
        "label": "Kokoro Local",
        "editable": False,
        "sync": {"openclaw": "manual-import", "workbuddy": "manual"},
        "stt": {
            "defaultModel": "not-configured",
            "fallbackModel": "not-configured",
            "supportedLanguages": [],
            "runtime": "catalog",
        },
        "tts": {
            "defaultModel": "Kokoro-82M-v1.1-zh",
            "fallbackModel": "edge-multilingual-neural",
            "supportedLanguages": ["zh-CN", "en-US"],
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
    "recommendedRealtime": "Use gpt-realtime-1.5 for cloud speech-to-speech, or SenseVoice + Kokoro for a local-first stack.",
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
        "mailAddress": "",
        "mailPassword": "",
        "mailSmtpHost": "",
        "mailSmtpPort": "",
        "mailImapHost": "",
        "mailImapPort": "",
        "wechatOfficialToken": "",
        "wechatOfficialAppId": "",
        "wechatOfficialAppSecret": "",
        "wechatOfficialEncodingAesKey": "",
        "lineChannelSecret": "",
        "lineChannelAccessToken": "",
        "externalBridgeUrl": "",
        "externalBridgeToken": "",
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


def find_ollama_binary():
    for candidate in OLLAMA_BIN_CANDIDATES:
        if not candidate:
            continue
        path = Path(candidate)
        if path.exists():
            return str(path)
        if candidate.lower() == "ollama":
            return candidate
    return ""


def load_ollama_inventory(force=False):
    now = time.time()
    cached = OLLAMA_INVENTORY_CACHE.get("value")
    updated_at = float(OLLAMA_INVENTORY_CACHE.get("updated_at", 0.0) or 0.0)
    if not force and cached is not None and (now - updated_at) < OLLAMA_INVENTORY_TTL_SECONDS:
        return deepcopy(cached)

    binary = find_ollama_binary()
    if not binary:
        inventory = {"available": False, "installed": [], "error": "missing-binary"}
        OLLAMA_INVENTORY_CACHE["value"] = deepcopy(inventory)
        OLLAMA_INVENTORY_CACHE["updated_at"] = now
        return inventory
    try:
        result = subprocess.run(
            [binary, "list"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        inventory = {"available": False, "installed": [], "error": "list-failed"}
        OLLAMA_INVENTORY_CACHE["value"] = deepcopy(inventory)
        OLLAMA_INVENTORY_CACHE["updated_at"] = now
        return inventory
    if result.returncode != 0:
        inventory = {"available": True, "installed": [], "error": "list-failed"}
        OLLAMA_INVENTORY_CACHE["value"] = deepcopy(inventory)
        OLLAMA_INVENTORY_CACHE["updated_at"] = now
        return inventory

    installed = []
    for raw_line in result.stdout.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("NAME"):
            continue
        parts = re.split(r"\s{2,}", line)
        if not parts:
            continue
        item = {
            "name": parts[0],
            "size": parts[2] if len(parts) > 2 else "",
            "modified": parts[3] if len(parts) > 3 else "",
        }
        installed.append(item)
    inventory = {"available": True, "installed": installed, "error": ""}
    OLLAMA_INVENTORY_CACHE["value"] = deepcopy(inventory)
    OLLAMA_INVENTORY_CACHE["updated_at"] = now
    return inventory


def build_recommended_model_stacks(local_inventory):
    installed_names = [item["name"] for item in local_inventory.get("installed", [])]
    detected_qwen = [name for name in installed_names if name.startswith("qwen")]
    has_qwen_15 = "qwen2.5:1.5b-instruct" in installed_names
    has_qwen_coder = any(name.startswith("qwen2.5-coder:7b") for name in installed_names)
    has_qwen_vl = any(name.startswith("qwen2.5vl:7b") for name in installed_names)
    local_summary = (
        f"Detected locally via Ollama: {', '.join(installed_names[:4])}."
        if installed_names
        else "No local Ollama models detected yet."
    )
    return [
        {
            "id": "homehub-router-frontier",
            "label": "HomeHub Planner Stack",
            "source": "HomeHub Recommended",
            "summary": "Primary cloud stack for intent understanding, agent planning, tool routing, and creation review.",
            "models": ["gpt-5.4", "gpt-5.4-mini", "gpt-4o"],
            "capabilities": ["Planner", "Reasoning", "Tool Use", "Vision", "Subagents"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "manual", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
            "deployment": "API",
            "access": "Paid",
            "status": "Recommended default",
            "notes": [
                "Use the strongest model for task spec and agent creation review.",
                "Use the mini tier for follow-up questions and substeps to control cost.",
                "Switch to GPT-4o when the request includes images, receipts, or mixed media.",
            ],
            "requirements": ["OPENAI_API_KEY"],
        },
        {
            "id": "homehub-open-weight-reasoning",
            "label": "Open-weight Reasoning Stack",
            "source": "OpenAI Open Models",
            "summary": "Open-weight fallback for agentic planning, structured outputs, and self-hosted routing.",
            "models": ["gpt-oss-20b", "gpt-oss-120b"],
            "capabilities": ["Reasoning", "Tool Use", "Structured Output", "Self-hosted"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "manual", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
            "deployment": "Self-host / provider",
            "access": "Open weight",
            "status": "Ready to add",
            "notes": [
                "Best when HomeHub needs auditable reasoning and custom hosting.",
                "Use 20b for lower-latency local or edge deployment, 120b for higher-end servers.",
            ],
            "requirements": ["vLLM, Ollama, llama.cpp, or another compatible runtime"],
        },
        {
            "id": "homehub-local-general",
            "label": "Local General LLM Stack",
            "source": "Ollama Local",
            "summary": f"Free local conversation and fallback routing for HomeHub. {local_summary}",
            "models": detected_qwen or ["qwen2.5:7b-instruct", "qwen2.5:3b-instruct", "qwen2.5:1.5b-instruct"],
            "capabilities": ["Local Chat", "Fallback", "Drafting", "Offline First"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "easy", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
            "deployment": "Ollama",
            "access": "Free local",
            "status": "Installed" if detected_qwen else "Suggested",
            "notes": [
                "Use the 7B tier for everyday family requests and 3B for low-RAM fallback.",
                "Use the 1.5B tier as the emergency fallback for low-spec boxes or background watchdog tasks.",
                "Keep this as the no-cloud fallback when API keys are unavailable.",
            ],
            "requirements": ["Ollama running locally on port 11434"],
            "installCommand": "" if has_qwen_15 else "ollama pull qwen2.5:1.5b-instruct",
        },
        {
            "id": "homehub-local-coder",
            "label": "Local Agent Builder / Coder",
            "source": "Ollama Local",
            "summary": "OpenClaw-style local code and tool scaffolding stack for generating features and services.",
            "models": ["qwen2.5-coder:7b", "qwen2.5-coder:14b"],
            "capabilities": ["Code Gen", "Tool Schema", "Feature Scaffolding", "Repair"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "easy", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
            "deployment": "Ollama",
            "access": "Free local",
            "status": "Installed" if has_qwen_coder else "Suggested",
            "notes": [
                "Strong local choice for creating HomeHub feature templates and simple services.",
                "Pairs well with a stronger planner model that decides when generation is needed.",
            ],
            "requirements": ["Ollama 0.6+ recommended"],
            "installCommand": "" if has_qwen_coder else "ollama pull qwen2.5-coder:7b",
        },
        {
            "id": "homehub-vision-docs",
            "label": "Receipt / Document Vision Stack",
            "source": "Hybrid Vision",
            "summary": "For receipts, invoices, screenshots, and home paperwork that must become structured records.",
            "models": ["gpt-4o", "qwen2.5vl:7b", "RapidOCR", "PaddleOCR"],
            "capabilities": ["Vision", "OCR", "Structured Output", "Receipts", "Tables"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "easy", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
            "deployment": "API + Ollama",
            "access": "Hybrid",
            "status": "Installed" if has_qwen_vl else "Recommended for bill agents",
            "notes": [
                "Prefer GPT-4o for the best mixed text-image understanding.",
                "Use Qwen2.5-VL locally when privacy matters or API cost needs to stay near zero.",
            ],
            "requirements": ["Image upload pipeline in HomeHub"],
            "installCommand": "" if has_qwen_vl else "ollama pull qwen2.5vl:7b",
        },
        {
            "id": "homehub-office-docs",
            "label": "Office Document Agent Stack",
            "source": "Hybrid Documents",
            "summary": "Generate and update PowerPoint, Excel, and Word files for reports, family planning, and operational workflows.",
            "models": ["gpt-5.4", "gpt-5.4-mini", "qwen2.5-coder:7b", "python-pptx", "openpyxl", "python-docx"],
            "capabilities": ["PPT", "Excel", "Word", "Document Automation", "Structured Drafting"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "easy", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
            "deployment": "API + local Python",
            "access": "Hybrid",
            "status": "Recommended for office-style agents",
            "notes": [
                "Use GPT-5.4 for document planning, page structure, and drafting decisions.",
                "Use qwen2.5-coder plus Python document libraries when HomeHub needs deterministic file generation.",
                "Fits PPT reports, Excel trackers, Word summaries, and OCR-to-document pipelines.",
            ],
            "requirements": ["python-docx, openpyxl, python-pptx installed on the HomeHub machine"],
        },
        {
            "id": "homehub-retrieval-memory",
            "label": "Memory / Retrieval Stack",
            "source": "RAG / Embeddings",
            "summary": "Retrieval layer for household memory, document grounding, and agent memory search.",
            "models": ["BAAI/bge-m3", "text-embedding-3-large"],
            "capabilities": ["Embeddings", "RAG", "Long Docs", "Multilingual Search"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "manual", "workbuddy": "easy"},
            "editable": False,
            "actions": [],
            "deployment": "Local + API",
            "access": "Hybrid",
            "status": "Recommended",
            "notes": [
                "Use BGE-M3 locally for multilingual retrieval and dense+sparse hybrid search.",
                "Use OpenAI embeddings when you need turnkey managed APIs and hosted scale.",
            ],
            "requirements": ["Vector store or retrieval backend"],
        },
        {
            "id": "homehub-voice-local",
            "label": "Local Speech Stack",
            "source": "Hugging Face Local",
            "summary": "Local-first voice stack for speech recognition and TTS without depending on cloud speech APIs.",
            "models": ["SenseVoiceSmall", "Kokoro-82M-v1.1-zh", "whisper-large-v3"],
            "capabilities": ["STT", "TTS", "Emotion-aware ASR", "Voice Replies"],
            "languages": ["zh-CN", "en-US", "ja-JP"],
            "sync": {"openclaw": "manual-import", "workbuddy": "manual"},
            "editable": False,
            "actions": [],
            "deployment": "Local runtime",
            "access": "Free local",
            "status": "Ready to integrate",
            "notes": [
                "SenseVoice is better for fast multilingual speech understanding and voice events.",
                "Kokoro is a small open-weight TTS option for Chinese and English playback.",
            ],
            "requirements": ["Local Python runtime for ASR/TTS inference"],
        },
    ]


def build_ai_capability_catalog(provider_catalog, selected_audio):
    local_inventory = load_ollama_inventory()
    catalog = build_recommended_model_stacks(local_inventory) + [
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
    if local_inventory.get("available"):
        for item in local_inventory.get("installed", []):
            catalog.append(
                {
                    "id": f"ollama-installed-{item['name'].replace(':', '-').replace('.', '-')}",
                    "label": f"Ollama Installed: {item['name']}",
                    "source": "Detected Local Runtime",
                    "summary": "Already present on this HomeHub machine and available for local orchestration work.",
                    "models": [item["name"]],
                    "capabilities": ["Local Runtime", "Detected", "Ready"],
                    "languages": ["zh-CN", "en-US", "ja-JP"],
                    "sync": {"openclaw": "easy", "workbuddy": "manual"},
                    "editable": False,
                    "actions": [],
                    "deployment": "Ollama",
                    "access": "Free local",
                    "status": "Installed",
                    "notes": [
                        f"Size: {item.get('size') or 'unknown'}",
                        f"Modified: {item.get('modified') or 'unknown'}",
                    ],
                }
            )
    catalog.extend(get_custom_capability_entries())
    return catalog


def get_runtime_profile():
    selected_id = PERSISTED_SETTINGS.get("runtimeProfile", "low-memory")
    for item in RUNTIME_PROFILES:
        if item["id"] == selected_id:
            return deepcopy(item)
    return deepcopy(RUNTIME_PROFILES[0])


def build_runtime_strategy(local_inventory):
    installed_names = [item["name"] for item in local_inventory.get("installed", [])]
    profile = get_runtime_profile()
    return {
        **profile,
        "localDetected": installed_names,
        "apiReady": {
            "openai": bool(SECRETS.get("openaiApiKey")),
            "google": bool(SECRETS.get("googleAccessToken") or get_google_service_account_file().exists()),
        },
        "recommendedFlow": [
            {"stage": "Wake + watchdog", "preferred": "local", "models": ["Porcupine or sherpa wake word", "qwen2.5:1.5b-instruct"]},
            {"stage": "Daily chat fallback", "preferred": "local", "models": ["qwen2.5:3b-instruct", "qwen2.5:7b-instruct"]},
            {"stage": "Feature / service generation", "preferred": "hybrid", "models": ["qwen2.5-coder:7b", "gpt-5.4"]},
            {"stage": "Receipt and bill understanding", "preferred": "hybrid", "models": ["qwen2.5vl:7b", "gpt-4o"]},
            {"stage": "OCR and document reading", "preferred": "hybrid", "models": ["RapidOCR", "qwen2.5vl:7b", "gpt-4o"]},
            {"stage": "PPT / Excel / Word generation", "preferred": "hybrid", "models": ["gpt-5.4", "qwen2.5-coder:7b", "python-pptx", "openpyxl", "python-docx"]},
            {"stage": "Deep planning and review", "preferred": "cloud", "models": ["gpt-5.4", "gpt-5.4-mini"]},
        ],
    }


def build_tool_registry_snapshot():
    return deepcopy(TOOL_REGISTRY)


def build_tool_plan(task_spec, route):
    selected = route.get("selected") or {}
    feature_id = selected.get("featureId", "")
    plan = []
    for tool in TOOL_REGISTRY:
        handles = set(tool.get("handles", []))
        if task_spec["taskType"] in handles or task_spec["intent"] in handles or tool.get("featureId") == feature_id:
            plan.append(
                {
                    "toolId": tool["id"],
                    "label": tool["label"],
                    "execution": tool["execution"],
                    "kind": tool["kind"],
                    "selected": tool.get("featureId") == feature_id,
                }
            )
    if not plan:
        plan.append(
            {
                "toolId": "general-chat",
                "label": "General Chat",
                "execution": "hybrid",
                "kind": "core",
                "selected": True,
            }
        )
    return plan


def select_model_route(task_spec, runtime_strategy, local_inventory):
    installed = set(runtime_strategy.get("localDetected", []))
    low_memory = runtime_strategy.get("id") == "low-memory"
    route = {
        "execution": "local" if low_memory else task_spec.get("preferredExecution", "hybrid"),
        "primaryModel": "qwen2.5:1.5b-instruct" if low_memory and "qwen2.5:1.5b-instruct" in installed else ("qwen2.5:3b-instruct" if "qwen2.5:3b-instruct" in installed else "gpt-5.4-mini"),
        "fallbackModel": "qwen2.5:1.5b-instruct" if "qwen2.5:1.5b-instruct" in installed else "qwen2.5:3b-instruct",
        "reason": "Balanced default for mixed household conversations." if not low_memory else "Low Memory mode keeps the default path on the lightest local chat model available.",
    }
    task_type = task_spec.get("taskType")
    if task_type == "ui_navigation":
        return {
            "execution": "local",
            "primaryModel": "rule-based-ui-router",
            "fallbackModel": "none",
            "reason": "Direct TV navigation should stay local and deterministic.",
        }
    if task_type in {"reminder", "schedule"}:
        return {
            "execution": "local",
            "primaryModel": "rule-based-scheduler",
            "fallbackModel": "gpt-4o-mini",
            "reason": "Schedules and reminders should prefer local deterministic parsing.",
        }
    if task_type == "agent_creation":
        primary = "gpt-5.4" if runtime_strategy.get("apiReady", {}).get("openai") else ("qwen2.5-coder:7b" if not low_memory and "qwen2.5-coder:7b" in installed else route["primaryModel"])
        fallback = "qwen2.5-coder:7b" if not low_memory and "qwen2.5-coder:7b" in installed else route["fallbackModel"]
        return {
            "execution": "cloud" if low_memory and runtime_strategy.get("apiReady", {}).get("openai") else ("hybrid" if runtime_strategy.get("apiReady", {}).get("openai") else "local"),
            "primaryModel": primary,
            "fallbackModel": fallback,
            "reason": "Agent creation needs stronger planning and structured follow-up, with a local coder fallback." if not low_memory else "Low Memory mode offloads agent creation when cloud is ready and avoids local coder-heavy work.",
        }
    if task_type == "bill_intake":
        primary = "gpt-4o" if runtime_strategy.get("apiReady", {}).get("openai") else (route["primaryModel"] if low_memory else ("qwen2.5vl:7b" if "qwen2.5vl:7b" in installed else route["primaryModel"]))
        fallback = route["fallbackModel"] if low_memory else ("qwen2.5vl:7b" if "qwen2.5vl:7b" in installed else "qwen2.5:7b-instruct")
        return {
            "execution": "cloud" if low_memory and runtime_strategy.get("apiReady", {}).get("openai") else ("local" if low_memory else "hybrid"),
            "primaryModel": primary,
            "fallbackModel": fallback,
            "reason": "Bill and receipt understanding benefits from multimodal reasoning, with local vision fallback when needed." if not low_memory else "Low Memory mode prefers RapidOCR plus cloud vision, and avoids local 7B vision fallback.",
        }
    if task_type == "document_workflow":
        primary = "gpt-5.4" if runtime_strategy.get("apiReady", {}).get("openai") else ("qwen2.5-coder:7b" if not low_memory and "qwen2.5-coder:7b" in installed else route["primaryModel"])
        fallback = route["fallbackModel"] if low_memory else ("qwen2.5vl:7b" if "qwen2.5vl:7b" in installed else ("qwen2.5:7b-instruct" if "qwen2.5:7b-instruct" in installed else route["fallbackModel"]))
        return {
            "execution": "cloud" if low_memory and runtime_strategy.get("apiReady", {}).get("openai") else ("local" if low_memory else "hybrid"),
            "primaryModel": primary,
            "fallbackModel": fallback,
            "reason": "OCR and Office document work needs strong planning plus either local coder or multimodal fallback for extraction and file generation." if not low_memory else "Low Memory mode keeps document work on light local paths unless cloud is available.",
        }
    if task_type == "network_lookup":
        return {
            "execution": "hybrid",
            "primaryModel": "gpt-4o-mini" if runtime_strategy.get("apiReady", {}).get("openai") else route["primaryModel"],
            "fallbackModel": "qwen2.5:7b-instruct" if "qwen2.5:7b-instruct" in installed else route["fallbackModel"],
            "reason": "Controlled network lookup fetches approved sources first, then summarizes with a chat model.",
        }
    if task_type == "study_plan":
        return {
            "execution": "hybrid" if runtime_strategy.get("apiReady", {}).get("openai") else "local",
            "primaryModel": "gpt-5.4-mini" if runtime_strategy.get("apiReady", {}).get("openai") else route["primaryModel"],
            "fallbackModel": "qwen2.5:7b-instruct" if "qwen2.5:7b-instruct" in installed else route["fallbackModel"],
            "reason": "Study planning benefits from structured reasoning but can fall back to local chat models.",
        }
    if runtime_strategy.get("id") == "local-essential":
        route["execution"] = "local"
        route["reason"] = "Local Essential mode keeps daily work on-device whenever possible."
    elif low_memory:
        route["execution"] = "local"
        route["primaryModel"] = "qwen2.5:1.5b-instruct" if "qwen2.5:1.5b-instruct" in installed else route["primaryModel"]
        route["fallbackModel"] = "qwen2.5:3b-instruct" if "qwen2.5:3b-instruct" in installed else route["fallbackModel"]
        route["reason"] = "Low Memory mode prioritizes the lightest local models to reduce swap and UI stalls."
    elif runtime_strategy.get("id") == "cloud-enhanced" and runtime_strategy.get("apiReady", {}).get("openai"):
        route["execution"] = "cloud"
        route["primaryModel"] = "gpt-5.4-mini"
        route["fallbackModel"] = "qwen2.5:7b-instruct" if "qwen2.5:7b-instruct" in installed else route["fallbackModel"]
        route["reason"] = "Cloud Enhanced mode prefers API models for better quality while keeping local fallback."
    return route


def load_secrets_file():
    return load_secrets_file_payload(get_secrets_file(), default_secrets)


def get_effective_secrets():
    return get_effective_secrets_payload(load_secrets_file())


def get_secret_sources():
    return get_secret_sources_payload(load_secrets_file())


def save_secrets(secrets):
    save_secrets_payload(get_secrets_file(), secrets)


GOOGLE_TOKEN_CACHE = {
    "access_token": "",
    "expires_at": 0,
}


def get_google_service_account_file():
    return get_google_service_account_file_payload(GOOGLE_SERVICE_ACCOUNT_FILE)


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
    return get_google_cloud_headers_payload(SECRETS, GOOGLE_TOKEN_CACHE, get_google_service_account_file())


def load_persisted_settings():
    return load_persisted_settings_payload(SETTINGS_FILE, LANGUAGE_SETTINGS, get_audio_provider_catalog(), RUNTIME_PROFILES)


def save_persisted_settings(settings):
    save_persisted_settings_payload(SETTINGS_FILE, settings)


def load_bootstrap_status():
    return load_bootstrap_status_payload(BOOTSTRAP_STATUS_FILE)


def save_bootstrap_status(payload):
    save_bootstrap_status_payload(BOOTSTRAP_STATUS_FILE, payload)


def bootstrap_snapshot():
    global BOOTSTRAP_PROCESS, PERSISTED_SETTINGS
    snapshot, BOOTSTRAP_PROCESS, PERSISTED_SETTINGS = bootstrap_snapshot_payload(
        BOOTSTRAP_PROCESS,
        BOOTSTRAP_STALE_SECONDS,
        BOOTSTRAP_STATUS_FILE,
        PERSISTED_SETTINGS,
        load_bootstrap_status,
        lambda process, load_status, settings: refresh_bootstrap_process_state_payload(
            process,
            load_status,
            settings,
            save_persisted_settings,
        ),
    )
    return snapshot


def refresh_bootstrap_process_state():
    global BOOTSTRAP_PROCESS, PERSISTED_SETTINGS
    BOOTSTRAP_PROCESS, PERSISTED_SETTINGS = refresh_bootstrap_process_state_payload(
        BOOTSTRAP_PROCESS,
        load_bootstrap_status,
        PERSISTED_SETTINGS,
        save_persisted_settings,
    )


def start_bootstrap_install():
    global BOOTSTRAP_PROCESS
    refresh_bootstrap_process_state()
    BOOTSTRAP_PROCESS, started = start_bootstrap_install_payload(BOOTSTRAP_PROCESS, PROJECT_ROOT, BOOTSTRAP_SCRIPT, BOOTSTRAP_STATUS_FILE)
    return started


def maybe_start_bootstrap_install():
    if not PERSISTED_SETTINGS.get("bootstrapConsent", False):
        return
    if PERSISTED_SETTINGS.get("bootstrapCompleted", False):
        return
    start_bootstrap_install()


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


def default_home_memory():
    return default_home_memory_payload()


def load_home_memory():
    return load_home_memory_payload(HOME_MEMORY_FILE)


def save_home_memory(memory):
    save_home_memory_payload(HOME_MEMORY_FILE, memory)


PERSISTED_SETTINGS = load_persisted_settings()
SECRETS = get_effective_secrets()
SECRET_SOURCES = get_secret_sources()
maybe_start_bootstrap_install()
HOME_MEMORY = load_home_memory()
WEATHER = load_weather_state_payload(WEATHER_STATE_FILE)
CONVERSATION_LOG_FILE.touch(exist_ok=True)

SYSTEM_STATUS = {
    "mode": "Listening",
    "boxHealth": "Healthy",
    "remoteHint": "Use Left/Right to switch tabs, Enter to open cards.",
}

NETWORK_LOOKUP_POLICIES = {
    "safe-general": {
        "id": "safe-general",
        "label": "Safe General",
        "allowedDomains": [
            "wikipedia.org",
            "wikimedia.org",
            "openai.com",
            "platform.openai.com",
            "huggingface.co",
            "ollama.com",
            "developer.mozilla.org",
            "docs.python.org",
            "weather.gov",
            "cdc.gov",
            "who.int",
            "github.com",
        ],
        "maxSources": 3,
        "allowDirectUrls": True,
    },
    "official-only": {
        "id": "official-only",
        "label": "Official Only",
        "allowedDomains": [
            "openai.com",
            "platform.openai.com",
            "huggingface.co",
            "ollama.com",
            "weather.gov",
            "cdc.gov",
            "who.int",
            "github.com",
        ],
        "maxSources": 2,
        "allowDirectUrls": True,
    },
}

TOOL_REGISTRY = [
    {
        "id": "custom-agent-builder",
        "label": "Custom Agent Builder",
        "kind": "feature",
        "featureId": "custom-agents",
        "handles": ["agent_creation", "agent_revision", "service_scaffold"],
        "inputModes": ["text", "voice"],
        "execution": "hybrid",
    },
    {
        "id": "local-schedule",
        "label": "Local Schedule",
        "kind": "feature",
        "featureId": "local-schedule",
        "handles": ["schedule", "reminder", "calendar_query"],
        "inputModes": ["text", "voice"],
        "execution": "local",
    },
    {
        "id": "general-chat",
        "label": "General Chat",
        "kind": "core",
        "featureId": "homehub-core",
        "handles": ["general_chat", "qa", "small_talk"],
        "inputModes": ["text", "voice", "image"],
        "execution": "hybrid",
    },
    {
        "id": "vision-bill-intake",
        "label": "Bill Vision Intake",
        "kind": "pipeline",
        "featureId": "homehub-core",
        "handles": ["bill_intake", "receipt_understanding", "document_vision"],
        "inputModes": ["image", "text", "voice"],
        "execution": "hybrid",
    },
    {
        "id": "document-workbench",
        "label": "Document Workbench",
        "kind": "core",
        "featureId": "homehub-core",
        "handles": ["document_workflow", "ocr", "ppt_generation", "excel_generation", "word_generation"],
        "inputModes": ["image", "text", "voice"],
        "execution": "hybrid",
    },
    {
        "id": "network-lookup",
        "label": "Controlled Network Lookup",
        "kind": "core",
        "featureId": "homehub-core",
        "handles": ["network_lookup", "web_query", "fact_refresh"],
        "inputModes": ["text", "voice"],
        "execution": "hybrid",
    },
]

VOICE_CONVERSATION = build_initial_conversation(PERSISTED_SETTINGS["language"])

CURRENT_CONVERSATION = deepcopy(VOICE_CONVERSATION)
LAST_VOICE_ROUTE = {
    "kind": "general",
    "requestText": "",
    "selected": {
        "intent": "general-chat",
        "featureId": "homehub-core",
        "featureName": "HomeHub Core",
        "action": "reply_directly",
        "score": 0.4,
    },
    "candidates": [],
    "taskSpec": {
        "taskType": "general_chat",
        "intent": "general-chat",
        "summary": "General household conversation or Q&A.",
        "urgency": "normal",
        "inputModes": ["text"],
        "requiresImage": False,
        "requiresGeneration": False,
        "requiresScheduling": False,
        "requiresLongRunningAgent": False,
        "preferredExecution": "hybrid",
        "missingInfo": [],
    },
    "toolPlan": [{"toolId": "general-chat", "label": "General Chat", "execution": "hybrid", "kind": "core", "selected": True}],
    "modelRoute": {
        "execution": "hybrid",
        "primaryModel": "qwen2.5:3b-instruct",
        "fallbackModel": "qwen2.5:1.5b-instruct",
        "reason": "Balanced default for mixed household conversations.",
    },
}
PENDING_VOICE_CLARIFICATION = None

FEATURE_MANAGER = FeatureManager(FEATURES_DIR)
CORTEX_ARCHITECT = CortexArchitect()

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


def json_get(url, headers=None, timeout=30):
    request = urllib.request.Request(url, headers=headers or {}, method="GET")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read()
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return json.loads(body.decode("utf-8"))
        return body.decode("utf-8", errors="ignore")


def perform_controlled_network_lookup(query, locale, policy_id="safe-general", preferred_sources=None, allowed_domains=None):
    return perform_controlled_network_lookup_impl(
        query,
        locale,
        NETWORK_LOOKUP_POLICIES,
        json_get,
        policy_id=policy_id,
        preferred_sources=preferred_sources,
        allowed_domains=allowed_domains,
    )


def perform_network_lookup(query, locale, policy_id="official-only", preferred_sources=None, allowed_domains=None):
    return perform_network_lookup_impl(
        query,
        locale,
        NETWORK_LOOKUP_POLICIES,
        json_get,
        policy_id=policy_id,
        preferred_sources=preferred_sources,
        allowed_domains=allowed_domains,
    )


def openai_chat_json(system_prompt, user_prompt, model_name="gpt-4o-mini"):
    runtime_profile = PERSISTED_SETTINGS.get("runtimeProfile", "edge-hybrid")
    api_key = SECRETS.get("openaiApiKey", "")
    if not api_key or runtime_profile == "local-essential":
        return ollama_chat_json(system_prompt, user_prompt, select_local_json_model(model_name))
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
        return ollama_chat_json(system_prompt, user_prompt, select_local_json_model(model_name))


def build_runtime_bridge():
    runtime = RuntimeBridge(
        root=ROOT,
        get_setting=lambda key, default=None: PERSISTED_SETTINGS.get(key, default),
        get_secret=lambda key, default=None: SECRETS.get(key, default),
        openai_json=openai_chat_json,
        analyze_image=analyze_image_with_homehub,
        network_lookup=perform_network_lookup,
        log=lambda message: print(f"[features] {message}"),
    )
    runtime.invoke_feature = lambda feature_id, payload, locale: FEATURE_MANAGER.invoke_feature(feature_id, payload, locale, runtime)
    runtime.resolve_message = lambda message, locale: resolve_voice_request(message, locale)
    return runtime


def run_background_email_sync():
    while True:
        try:
            runtime = build_runtime_bridge()
            FEATURE_MANAGER.invoke_feature(
                "external-channels",
                {
                    "mode": "api",
                    "method": "POST",
                    "path": "/api/external-channels/email/sync",
                    "body": {"limit": 10},
                },
                PERSISTED_SETTINGS.get("language", "zh-CN"),
                runtime,
            )
        except Exception as exc:
            print(f"[mail-sync] background sync failed: {exc}")
        time.sleep(max(30, EMAIL_SYNC_INTERVAL_SECONDS))


def run_background_bridge_pull():
    while True:
        try:
            bridge_url = str(SECRETS.get("externalBridgeUrl", "")).strip().rstrip("/")
            bridge_token = str(SECRETS.get("externalBridgeToken", "")).strip()
            if bridge_url and bridge_token:
                pull_request = urllib.request.Request(
                    f"{bridge_url}/api/external-channels/bridge/pull",
                    data=json.dumps({"bridgeToken": bridge_token}).encode("utf-8"),
                    headers={"Content-Type": "application/json; charset=utf-8"},
                    method="POST",
                )
                with urllib.request.urlopen(pull_request, timeout=20) as response:
                    pull_body = json.loads(response.read().decode("utf-8", errors="replace"))
                item = pull_body.get("item") if isinstance(pull_body, dict) else None
                if isinstance(item, dict) and item:
                    sender = item.get("sender", {}) if isinstance(item.get("sender"), dict) else {}
                    sender_id = str(sender.get("displayName") or sender.get("id") or "unknown").strip()
                    message_id = str(item.get("id", "")).strip() or "unknown"
                    content_preview = str(item.get("content", "")).strip().replace("\n", " ")[:120]
                    print(f"[bridge-pull] claimed {message_id} from {sender_id}: {content_preview}")
                    runtime = build_runtime_bridge()
                    bridge_response = FEATURE_MANAGER.invoke_feature(
                        "external-channels",
                        {
                            "mode": "api",
                            "method": "POST",
                            "path": "/api/external-channels/bridge/inbound",
                            "body": {
                                "channel": item.get("channel", ""),
                                "sender": item.get("sender", {}),
                                "content": item.get("content", ""),
                                "locale": item.get("locale", PERSISTED_SETTINGS.get("language", "zh-CN")),
                                "subject": item.get("subject", ""),
                                "attachments": item.get("attachments", []),
                                "messageType": item.get("messageType", "text"),
                                "metadata": item.get("metadata", {}),
                                "bridgeToken": bridge_token,
                            },
                        },
                        PERSISTED_SETTINGS.get("language", "zh-CN"),
                        runtime,
                    ) or {}
                    bridge_body = bridge_response.get("body", {}) if isinstance(bridge_response.get("body"), dict) else {}
                    reply_preview = str(bridge_body.get("reply", "")).strip().replace("\n", " ")[:120]
                    print(f"[bridge-pull] processed {message_id}, reply: {reply_preview}")
                    result_request = urllib.request.Request(
                        f"{bridge_url}/api/external-channels/bridge/result",
                        data=json.dumps(
                            {
                                "bridgeToken": bridge_token,
                                "messageId": item.get("id", ""),
                                "reply": bridge_body.get("reply", ""),
                                "resolution": bridge_body.get("resolution", {}),
                                "artifacts": bridge_body.get("artifacts", []),
                            },
                            ensure_ascii=False,
                        ).encode("utf-8"),
                        headers={"Content-Type": "application/json; charset=utf-8"},
                        method="POST",
                    )
                    with urllib.request.urlopen(result_request, timeout=20) as response:
                        result_body = json.loads(response.read().decode("utf-8", errors="replace"))
                    send_ok = bool(result_body.get("sendOk")) if isinstance(result_body, dict) else False
                    send_error = str(result_body.get("sendError", "")).strip() if isinstance(result_body, dict) else ""
                    if send_ok:
                        print(f"[bridge-pull] delivered {message_id} back to Railway and IM send succeeded")
                    else:
                        print(f"[bridge-pull] delivered {message_id} back to Railway but IM send failed: {send_error or 'unknown_error'}")
        except Exception as exc:
            print(f"[bridge-pull] background pull failed: {exc}")
        time.sleep(max(3, BRIDGE_PULL_INTERVAL_SECONDS))


def ollama_chat_raw(system_prompt, user_prompt, model_name):
    binary = find_ollama_binary()
    if not binary or not model_name:
        return None
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "options": {"temperature": 0.2},
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            data = json.loads(response.read().decode("utf-8"))
        message = data.get("message", {})
        content = message.get("content", "")
        return str(content).strip() if content else None
    except Exception:
        return None


def ollama_chat_json(system_prompt, user_prompt, model_name):
    binary = find_ollama_binary()
    if not binary or not model_name:
        return None
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.1},
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            data = json.loads(response.read().decode("utf-8"))
        content = str((data.get("message") or {}).get("content", "")).strip()
        return json.loads(content) if content else None
    except Exception:
        return None


def select_local_json_model(model_name=""):
    inventory = load_ollama_inventory()
    installed = {item["name"] for item in inventory.get("installed", [])}
    if PERSISTED_SETTINGS.get("runtimeProfile") == "low-memory":
        if "qwen2.5:1.5b-instruct" in installed:
            return "qwen2.5:1.5b-instruct"
        if "qwen2.5:3b-instruct" in installed:
            return "qwen2.5:3b-instruct"
        return ""
    if "coder" in str(model_name).lower() and "qwen2.5-coder:7b" in installed:
        return "qwen2.5-coder:7b"
    if "qwen2.5-coder:7b" in installed:
        return "qwen2.5-coder:7b"
    if "qwen2.5:7b-instruct" in installed:
        return "qwen2.5:7b-instruct"
    if "qwen2.5:3b-instruct" in installed:
        return "qwen2.5:3b-instruct"
    if "qwen2.5:1.5b-instruct" in installed:
        return "qwen2.5:1.5b-instruct"
    return ""


def select_local_chat_model():
    inventory = load_ollama_inventory()
    installed = {item["name"] for item in inventory.get("installed", [])}
    if PERSISTED_SETTINGS.get("runtimeProfile") == "low-memory":
        if "qwen2.5:1.5b-instruct" in installed:
            return "qwen2.5:1.5b-instruct"
        if "qwen2.5:3b-instruct" in installed:
            return "qwen2.5:3b-instruct"
        return ""
    if "qwen2.5:7b-instruct" in installed:
        return "qwen2.5:7b-instruct"
    if "qwen2.5:3b-instruct" in installed:
        return "qwen2.5:3b-instruct"
    if "qwen2.5:1.5b-instruct" in installed:
        return "qwen2.5:1.5b-instruct"
    return ""


def select_local_vision_model():
    if PERSISTED_SETTINGS.get("runtimeProfile") == "low-memory":
        return ""
    inventory = load_ollama_inventory()
    installed = {item["name"] for item in inventory.get("installed", [])}
    if "qwen2.5vl:7b" in installed:
        return "qwen2.5vl:7b"
    return ""


def ollama_vision_json(prompt, image_base64, mime_type, model_name):
    binary = find_ollama_binary()
    if not binary or not model_name or not image_base64:
        return None
    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "images": [image_base64],
            }
        ],
        "stream": False,
        "format": "json",
        "options": {"temperature": 0.1},
    }
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/chat",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            data = json.loads(response.read().decode("utf-8"))
        content = str((data.get("message") or {}).get("content", "")).strip()
        return json.loads(content) if content else None
    except Exception:
        return None


def openai_vision_json(prompt, image_base64, mime_type, model_name="gpt-4o"):
    api_key = SECRETS.get("openaiApiKey", "")
    if not api_key or not image_base64:
        return None
    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{image_base64}"}},
                ],
            }
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.1,
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
        with urllib.request.urlopen(request, timeout=90) as response:
            data = json.loads(response.read().decode("utf-8"))
        content = data["choices"][0]["message"]["content"]
        if isinstance(content, list):
            content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
        return json.loads(str(content).strip())
    except Exception:
        return None


def analyze_image_with_homehub(prompt, image_base64, mime_type="image/png", preferred_model=""):
    runtime_profile = PERSISTED_SETTINGS.get("runtimeProfile", "low-memory")
    local_model = preferred_model if preferred_model.startswith("qwen2.5vl") else select_local_vision_model()
    if runtime_profile != "local-essential":
        cloud_result = openai_vision_json(prompt, image_base64, mime_type, "gpt-4o")
        if cloud_result:
            if isinstance(cloud_result, dict):
                cloud_result.setdefault("provider", "openai")
                cloud_result.setdefault("model", "gpt-4o")
            return cloud_result
    if runtime_profile == "low-memory" and not local_model:
        return None
    local_result = ollama_vision_json(prompt, image_base64, mime_type, local_model)
    if isinstance(local_result, dict):
        local_result.setdefault("provider", "ollama")
        local_result.setdefault("model", local_model or "qwen2.5vl:7b")
    return local_result


def _audio_context():
    return {
        "get_google_cloud_headers": get_google_cloud_headers,
        "get_google_service_account_file": get_google_service_account_file,
        "json_post": json_post,
        "log_external_usage": log_external_usage,
        "persisted_settings": PERSISTED_SETTINGS,
        "provider_catalog": get_audio_provider_catalog(),
        "secrets": SECRETS,
    }


def _memory_context():
    return {
        "secrets": SECRETS,
    }


def transcribe_audio(provider_id, audio_base64, mime_type, locale):
    return transcribe_audio_payload(provider_id, audio_base64, mime_type, locale, _audio_context())


def synthesize_speech(provider_id, text_value, locale):
    return synthesize_speech_payload(provider_id, text_value, locale, _audio_context())


def now_local():
    return now_local_payload()


def now_hhmm():
    return now_hhmm_payload()


def parse_iso_datetime(value):
    return parse_iso_datetime_payload(value)


def format_datetime_local(value, locale):
    return format_datetime_local_payload(value, locale)


def get_upcoming_events(limit=5):
    return get_upcoming_events_payload(HOME_MEMORY, limit=limit)


def get_pending_reminders(limit=5):
    return get_pending_reminders_payload(HOME_MEMORY, limit=limit)


def get_due_reminders(limit=3):
    return get_due_reminders_payload(HOME_MEMORY, limit=limit)


def create_local_event(title, start_at, end_at, participants=None, location="", reminder_offset_minutes=None, notes=""):
    return create_local_event_payload(
        HOME_MEMORY,
        HOME_MEMORY_FILE,
        title,
        start_at,
        end_at,
        participants=participants,
        location=location,
        reminder_offset_minutes=reminder_offset_minutes,
        notes=notes,
    )


def create_local_reminder(title, trigger_at, notes=""):
    return create_local_reminder_payload(HOME_MEMORY, HOME_MEMORY_FILE, title, trigger_at, notes=notes)


def summarize_schedule(locale):
    return summarize_schedule_payload(HOME_MEMORY, locale)


def detect_local_assistant_action(user_text, locale):
    return detect_local_assistant_action_payload(user_text, locale, _memory_context())


def append_conversation_turn(speaker, text_value, artifacts=None):
    entry = {
        "speaker": speaker,
        "text": text_value,
        "time": now_hhmm(),
        "artifacts": artifacts or [],
    }
    CURRENT_CONVERSATION.append(entry)
    if len(CURRENT_CONVERSATION) > 24:
        del CURRENT_CONVERSATION[0 : len(CURRENT_CONVERSATION) - 24]
    try:
        with CONVERSATION_LOG_FILE.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except OSError:
        pass


def refresh_weather_from_coordinates(latitude, longitude, label=""):
    global WEATHER
    WEATHER = refresh_weather_from_coordinates_payload(WEATHER_STATE_FILE, float(latitude), float(longitude), str(label or "").strip())
    return WEATHER


def build_household_modules(locale):
    return build_household_modules_payload(HOUSEHOLD_MODULES, HOME_MEMORY, locale)


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
        return f"我可以帮你创建这些智能体：{joined}。你可以直接说：“{example}”。如果你的需求里还有缺失资料，我会继续主动追问你。"
    if locale == "ja-JP":
        return "作成できるエージェントを案内します。必要な情報が足りなければこちらから追加で確認します。"
    joined = "; ".join(f"{item['name']}: {item['summary']}" for item in agent_types[:3])
    example = agent_types[0].get("examplePrompt", "")
    return f"I can create these agent types: {joined}. Try saying: '{example}'. If the request is incomplete, I will ask follow-up questions before finishing the agent."


def openai_chat_reply(system_prompt, user_prompt, model_name="gpt-4o-mini"):
    runtime_profile = PERSISTED_SETTINGS.get("runtimeProfile", "edge-hybrid")
    api_key = SECRETS.get("openaiApiKey", "")
    if not api_key or runtime_profile == "local-essential":
        return ollama_chat_raw(system_prompt, user_prompt, select_local_chat_model())
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
        return ollama_chat_raw(system_prompt, user_prompt, select_local_chat_model())


def build_grounded_network_reply(query_text, lookup_result, locale):
    fallback = build_network_lookup_reply(lookup_result, locale)
    if not isinstance(lookup_result, dict) or not lookup_result.get("ok"):
        return fallback
    sources = lookup_result.get("sources", []) if isinstance(lookup_result.get("sources", []), list) else []
    query = str(query_text or "").strip()
    lowered_query = query.lower()
    flight_like = any(token in query for token in ["航班", "机票", "飞机"]) or any(
        token in lowered_query for token in ["flight", "flights", "airfare", "ticket", "plane"]
    )
    if flight_like:
        excerpts = " ".join(str(item.get("excerpt", "")).strip() for item in sources[:3]).lower()
        has_numeric_price = bool(re.search(r"(?:¥|￥|\$)\s*\d+|\d+\s*(?:jpy|usd|cny|rmb|元|円|yen|dollars?)", excerpts))
        has_time_pattern = bool(re.search(r"\b\d{1,2}:\d{2}\b|\d{1,2}\s*(?:am|pm)|\d{1,2}时\d{0,2}分", excerpts))
        has_specific_flight_detail = has_numeric_price or has_time_pattern or any(
            token in excerpts for token in ["航班号", "flight no", "flight number", "departs at", "arrives at", "起飞于", "到达于"]
        )
        generic_search_page = any(
            token in excerpts
            for token in [
                "提供机票查询预订信息",
                "旅游搜索网站",
                "比较",
                "compare",
                "search website",
                "google flights",
                "航班动态",
                "打折特价机票",
            ]
        )
        source_labels = build_source_labels(sources)
        if not has_specific_flight_detail or generic_search_page:
            if locale == "zh-CN":
                base = (
                    "我已经查到可用的机票搜索来源，但它们目前提供的主要是搜索入口，还没有直接给出“日本全境到美国全境、5月31日”的完整航班时间和价格列表。"
                    "这类查询范围太大，时间和价格会随出发城市、到达城市、是否直飞而变化。"
                    "如果你补充出发城市和到达城市，例如“东京到洛杉矶”或“福冈到纽约”，我就可以继续按时间和价格帮你整理。"
                )
                return f"{base}\n来源：{'；'.join(source_labels)}" if source_labels else base
            base = (
                "I found usable flight search sources, but they are still returning search-entry pages rather than a concrete Japan-to-USA flight list for May 31. "
                "This route is too broad, and times and prices depend on the departure city, arrival city, and whether you want direct flights. "
                "If you tell me a concrete route such as Tokyo to Los Angeles or Fukuoka to New York, I can refine the result."
            )
            return f"{base}\nSources: {'; '.join(source_labels)}" if source_labels else base
    source_briefs = []
    for item in sources[:3]:
        title = str(item.get("title", "")).strip()
        excerpt = str(item.get("excerpt", "")).strip()
        url = str(item.get("url", "")).strip()
        source_briefs.append(
            {
                "title": title,
                "excerpt": excerpt[:600],
                "url": url,
            }
        )
    if locale == "zh-CN":
        system_prompt = (
            "你是 HomeHub 的联网结果整理助手。"
            "用户已经完成联网查询，你要把来源内容整理成简洁、自然、可直接回答用户的话。"
            "不要输出原始网页碎片，不要逐字复读标题，不要编造未在来源中出现的事实。"
            "如果来源信息不足，就基于现有来源保守回答。"
            "正文不要带链接，来源会由系统单独追加。"
        )
    elif locale == "ja-JP":
        system_prompt = (
            "You are HomeHub's grounded web-results summarizer. "
            "Turn the fetched source content into a short, natural answer for the user. "
            "Do not dump raw webpage fragments, do not invent facts, and do not include links in the main answer."
        )
    else:
        system_prompt = (
            "You are HomeHub's grounded web-results summarizer. "
            "Turn the fetched source content into a short, natural answer for the user. "
            "Do not dump raw webpage fragments, do not invent facts, and do not include links in the main answer."
        )
    user_prompt = json.dumps(
        {
            "locale": locale,
            "userQuery": str(query_text or "").strip(),
            "networkAnswer": str(lookup_result.get("answer", "")).strip(),
            "sources": source_briefs,
        },
        ensure_ascii=False,
    )
    ai_reply = ollama_chat_raw(system_prompt, user_prompt, select_local_chat_model())
    if not ai_reply:
        ai_reply = openai_chat_reply(system_prompt, user_prompt, "gpt-4o-mini")
    if ai_reply:
        source_labels = build_source_labels(sources)
        if locale == "zh-CN":
            return f"{ai_reply}\n来源：{'；'.join(source_labels)}" if source_labels else ai_reply
        return f"{ai_reply}\nSources: {'; '.join(source_labels)}" if source_labels else ai_reply
    return fallback


def build_network_unavailable_reply(query_text, locale, task_type="network_lookup"):
    query = str(query_text or "").strip()
    lowered = query.lower()
    weather_like = task_type == "weather" or any(token in query for token in ["天气", "气温", "天気"]) or any(
        token in lowered for token in ["weather", "temperature", "forecast"]
    )
    flight_like = any(token in query for token in ["航班", "机票", "飞机"]) or any(
        token in lowered for token in ["flight", "flights", "airfare", "ticket", "plane"]
    )
    if locale == "zh-CN":
        if weather_like:
            return "我已经理解成天气查询了，但当前外部天气服务没有返回可用结果。请稍后重试，或在浏览器允许定位后再查询。"
        if flight_like:
            return "我已经理解成航班与价格查询了，但当前外部检索没有返回可用结果。请稍后重试，或换成更具体的出发地、目的地和日期。"
        return "我已经理解你的联网查询需求了，但当前外部检索没有返回可用结果。请稍后重试，或把条件说得更具体一些。"
    if locale == "ja-JP":
        if weather_like:
            return "天気の問い合わせとして理解しましたが、現在は外部の天気サービスから有効な結果を取得できませんでした。後でもう一度お試しください。"
        if flight_like:
            return "フライトと料金の検索として理解しましたが、現在は外部検索から有効な結果を取得できませんでした。出発地や日付をより具体的にすると改善する場合があります。"
        return "オンライン検索の依頼として理解しましたが、現在は有効な結果を取得できませんでした。少し時間をおいて再試行してください。"
    if weather_like:
        return "I understood this as a weather request, but the external weather service did not return usable results right now. Please try again shortly."
    if flight_like:
        return "I understood this as a flight-and-price lookup, but external search did not return usable results right now. Please try again with more specific route details."
    return "I understood this as an online lookup request, but external search did not return usable results right now. Please try again shortly."


def is_weak_grounded_reply(reply_text):
    text = str(reply_text or "").strip().lower()
    if not text:
        return True
    weak_markers = [
        "无法直接确定",
        "还没有拿到可用",
        "请先允许浏览器定位",
        "you can check",
        "not enough",
        "insufficient",
        "unable to determine",
        "没有提取到足够",
        "sources did not contain enough",
    ]
    return any(marker in text for marker in weak_markers)


def build_network_query_candidates(query_text, locale, preferred_sources=None):
    query = str(query_text or "").strip()
    candidates = [query] if query else []
    preferred_sources = preferred_sources if isinstance(preferred_sources, list) else []
    lowered = query.lower()
    weather_like = any(token in query for token in ["天气", "气温", "天気"]) or any(
        token in lowered for token in ["weather", "temperature", "forecast"]
    )
    if weather_like:
        if locale == "zh-CN":
            candidates.extend(
                [
                    f"{query} 实时天气 气温",
                    f"{query} 今日天气 最高 最低 气温",
                ]
            )
        elif locale == "ja-JP":
            candidates.extend(
                [
                    f"{query} 天気 気温",
                    f"{query} 今日の天気 最高 最低 気温",
                ]
            )
        else:
            candidates.extend(
                [
                    f"{query} weather temperature today",
                    f"{query} forecast high low temperature",
                ]
            )
        for source in preferred_sources:
            candidates.append(f"{query} site:{source}")
    unique = []
    for item in candidates:
        normalized = str(item or "").strip()
        if normalized and normalized not in unique:
            unique.append(normalized)
    return unique


def perform_autonomous_network_lookup(query_text, locale, policy_id="official-only", preferred_sources=None, allowed_domains=None):
    best_result = {"ok": False, "error": "no_query"}
    best_score = -1
    for candidate in build_network_query_candidates(query_text, locale, preferred_sources):
        result = perform_network_lookup(candidate, locale, policy_id, preferred_sources, allowed_domains)
        if not isinstance(result, dict):
            continue
        sources = result.get("sources", []) if isinstance(result.get("sources", []), list) else []
        score = len(sources) * 10 + len(str(result.get("answer", "")).strip())
        if score > best_score:
            best_score = score
            best_result = result
        if result.get("ok") and sources:
            reply = build_grounded_network_reply(candidate, result, locale)
            if not is_weak_grounded_reply(reply):
                result["autonomousQuery"] = candidate
                return result
    if isinstance(best_result, dict):
        best_result["autonomousQuery"] = next(iter(build_network_query_candidates(query_text, locale, preferred_sources)), str(query_text or "").strip())
    return best_result


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


def build_general_voice_reply(user_text, locale, model_route=None):
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
    preferred_model = str((model_route or {}).get("primaryModel", "")).strip()
    preferred_execution = str((model_route or {}).get("execution", "")).strip()
    user_prompt = f"Locale: {locale}\nRecent conversation:\n{conversation_context}\nUser: {user_text}"
    if preferred_execution == "local" and preferred_model and preferred_model != "rule-based-scheduler":
        ai_reply = ollama_chat_raw(system_prompt, user_prompt, preferred_model)
    else:
        ai_reply = openai_chat_reply(system_prompt, user_prompt, "gpt-4o-mini")
        if not ai_reply and preferred_model and preferred_model.startswith("qwen"):
            ai_reply = ollama_chat_raw(system_prompt, user_prompt, preferred_model)
    if ai_reply:
        return ai_reply

    lowered = user_text.lower()
    weather_line = f"{WEATHER.get('location', '-')}: {WEATHER.get('condition', '-')}, {WEATHER.get('temperatureC', '-') }C, high {WEATHER.get('highC', '-') }C, low {WEATHER.get('lowC', '-') }C."
    if locale == "zh-CN":
        if "天气" in user_text:
            return f"当前天气是：{WEATHER.get('location', '-')}{WEATHER.get('condition', '-')}，现在 {WEATHER.get('temperatureC', '-')} 度，最高 {WEATHER.get('highC', '-')} 度，最低 {WEATHER.get('lowC', '-')} 度。"
        if "学习计划" in user_text or "智能体" in user_text:
            return "如果你想创建新的助手，可以直接说出目标，例如“帮我创建一个儿子四年级学习计划智能体”。"
        if any(token in user_text for token in ["几点", "时间"]):
            return f"现在是 {datetime.now().strftime('%H:%M')}。"
        return "你可以直接告诉我你想做什么，比如问问题、创建日程、添加提醒，或者让我帮你创建一个智能体。"
    if locale == "ja-JP":
        if "weather" in lowered or "天気" in user_text:
            return f"現在の天気です。{WEATHER.get('location', '-')}、{WEATHER.get('condition', '-')}、現在 {WEATHER.get('temperatureC', '-')} 度、最高 {WEATHER.get('highC', '-')} 度、最低 {WEATHER.get('lowC', '-')} 度です。"
        return "予定やリマインダー以外でも、そのまま用件を話してください。できる範囲で続けて案内します。"
    if "weather" in lowered:
        return weather_line
    return "You can just tell me what you need, and I will either answer directly or help you create a schedule, reminder, or agent."


def build_weather_reply(user_text, locale):
    weather_state = lookup_weather_from_query_payload(WEATHER, user_text)
    active_weather = weather_state if isinstance(weather_state, dict) else WEATHER
    location = str(active_weather.get("location", "")).strip()
    condition = str(active_weather.get("condition", "")).strip()
    temperature = active_weather.get("temperatureC")
    high_c = active_weather.get("highC")
    low_c = active_weather.get("lowC")
    if not location or temperature is None:
        lookup_result = perform_autonomous_network_lookup(
            user_text,
            locale,
            "official-only",
            preferred_sources=["weather.com", "weather.com.cn", "weathernews.jp", "weather.gov"],
            allowed_domains=["weather.com", "weather.com.cn", "weathernews.jp", "weather.gov"],
        )
        if lookup_result.get("ok"):
            return build_grounded_network_reply(user_text, lookup_result, locale)
        if locale == "zh-CN":
            return build_network_unavailable_reply(user_text, locale, "weather")
        if locale == "ja-JP":
            return build_network_unavailable_reply(user_text, locale, "weather")
        return build_network_unavailable_reply(user_text, locale, "weather")
    if locale == "zh-CN":
        return f"{location} 当前{condition}，现在 {temperature} 度，最高 {high_c} 度，最低 {low_c} 度。"
    if locale == "ja-JP":
        return f"{location} は現在 {condition}、気温 {temperature} 度、最高 {high_c} 度、最低 {low_c} 度です。"
    return f"{location} is currently {condition}, {temperature}C now, high {high_c}C, low {low_c}C."


def route_voice_request(user_text, locale):
    runtime = build_runtime_bridge()
    task_spec = build_task_spec(
        user_text,
        locale,
        detect_ui_action=detect_ui_action,
        infer_task_spec=lambda text, lang, semantic_examples: infer_task_spec_with_openai(
            text,
            lang,
            semantic_examples,
            ai_available=bool(SECRETS.get("openaiApiKey")),
            openai_chat_json=openai_chat_json,
        ),
    )
    cortex_plan = build_cortex_route_plan(user_text, locale, task_spec)
    if cortex_plan.get("shouldNetwork") and task_spec["taskType"] not in {"weather", "time_query", "ui_navigation", "reminder", "schedule"}:
        task_spec["preferredExecution"] = "hybrid"
        task_spec["requiresNetwork"] = True
    runtime_strategy = build_runtime_strategy(load_ollama_inventory())
    route = FEATURE_MANAGER.route_voice_intent(user_text, locale, runtime)
    heuristic_route = {
        "kind": "feature" if route.get("selected") else ("agent_factory" if is_generic_agent_request(user_text) or task_spec["taskType"] == "agent_creation" else "general"),
        "selected": route.get("selected")
        or (
            {
                "intent": "agent-factory",
                "featureId": "homehub-core",
                "featureName": "HomeHub Core",
                "action": "list_agent_types",
                "score": 0.82,
            }
            if is_generic_agent_request(user_text) or task_spec["taskType"] == "agent_creation"
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
    routed = orchestrate_voice_route(user_text, locale, heuristic_route)
    routed["cortex"] = cortex_plan
    routed["reasoning"] = " ".join(
        item for item in [
            str(routed.get("reasoning", "")).strip(),
            str(cortex_plan.get("reasoning", "")).strip(),
        ]
        if item
    )
    if task_spec["taskType"] == "agent_creation" and routed.get("kind") == "general":
        custom_candidate = next((item for item in route.get("candidates", []) if item.get("featureId") == "custom-agents"), None)
        if custom_candidate:
            routed["kind"] = "feature"
            routed["selected"] = custom_candidate
            routed["reasoning"] = "Task spec identified agent creation, so HomeHub pinned the request to the custom agent builder."
        else:
            routed["kind"] = "agent_factory"
            routed["reasoning"] = "Task spec identified agent creation, so HomeHub kept the request in agent factory mode."
    if task_spec["taskType"] in {"reminder", "schedule"} and routed.get("kind") == "general":
        schedule_candidate = next((item for item in route.get("candidates", []) if item.get("featureId") == "local-schedule"), None)
        if schedule_candidate:
            routed["kind"] = "feature"
            routed["selected"] = schedule_candidate
            routed["reasoning"] = "Task spec identified schedule work, so HomeHub pinned the request to the local schedule feature."
    if looks_like_local_file_request(user_text):
        local_files_candidate = next((item for item in route.get("candidates", []) if item.get("featureId") == "local-files"), None)
        if local_files_candidate:
            routed["kind"] = "feature"
            routed["selected"] = local_files_candidate
            routed["clarificationQuestion"] = ""
            routed["reasoning"] = "HomeHub detected a local file-system request and pinned the request to the Local Files feature."
    if task_spec["taskType"] == "weather":
        routed["kind"] = "general"
        routed["selected"] = {
            "intent": "weather-query",
            "featureId": "homehub-core",
            "featureName": "HomeHub Core",
            "action": "weather_reply_directly",
            "score": 0.95,
        }
        routed["clarificationQuestion"] = ""
        routed["reasoning"] = "Task spec identified a weather request, so HomeHub answered through the dedicated weather path."
    if cortex_plan.get("shouldNetwork") and routed.get("kind") == "general" and task_spec["taskType"] != "weather":
        routed["selected"] = {
            **(routed.get("selected") or {}),
            "intent": "cortex-general",
            "featureId": "homehub-core",
            "featureName": "HomeHub Core",
            "action": "cortex_network_grounded_reply",
            "score": max(0.62, float((routed.get("selected") or {}).get("score", 0.4) or 0.4)),
        }
    routed["taskSpec"] = task_spec
    routed["toolPlan"] = build_tool_plan(task_spec, routed)
    routed["modelRoute"] = select_model_route(task_spec, runtime_strategy, {"installed": runtime_strategy.get("localDetected", [])})
    if cortex_plan.get("plannerModel"):
        routed["modelRoute"]["plannerModel"] = cortex_plan.get("plannerModel")
    if cortex_plan.get("executorModel"):
        routed["modelRoute"]["executorModel"] = cortex_plan.get("executorModel")
    if cortex_plan.get("responseModel"):
        routed["modelRoute"]["responseModel"] = cortex_plan.get("responseModel")
    return routed


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
        "taskSpec": route.get("taskSpec"),
        "toolPlan": route.get("toolPlan", []),
        "modelRoute": route.get("modelRoute"),
        "cortex": route.get("cortex"),
    }


def build_pending_clarification_snapshot():
    if not PENDING_VOICE_CLARIFICATION:
        return None
    return dict(PENDING_VOICE_CLARIFICATION)


def learn_from_clarification(clarification_context, route, combined_text, locale, clarification_answer=""):
    if not clarification_context or not isinstance(route, dict):
        return
    task_spec = route.get("taskSpec", {})
    if not isinstance(task_spec, dict) or not task_spec:
        return
    original_request = str(clarification_context.get("originalRequest", "")).strip()
    if not original_request:
        return
    clarified_text = str(clarification_answer or "").strip()
    if not clarified_text:
        return
    record_semantic_example(
        original_request,
        locale,
        task_spec,
        correction_text=clarified_text,
    )


def record_route_semantic_example(user_text, locale, route):
    if not isinstance(route, dict):
        return
    normalized = str(user_text or "").strip()
    if not normalized or len(normalized) > 400:
        return
    if normalized.startswith("[") and "content:" in normalized:
        return
    task_spec = route.get("taskSpec", {}) if isinstance(route.get("taskSpec", {}), dict) else {}
    if not task_spec:
        return
    task_type = str(task_spec.get("taskType", "")).strip()
    if task_type not in {"weather", "network_lookup", "reminder", "schedule", "agent_creation", "document_workflow", "bill_intake"}:
        return
    selected = route.get("selected", {}) if isinstance(route.get("selected", {}), dict) else {}
    score = float(selected.get("score", 0.0) or 0.0)
    if score < 0.72:
        return
    record_semantic_example(
        normalized,
        locale,
        task_spec,
        agent_id=str(selected.get("featureId", "")).strip(),
        agent_name=str(selected.get("featureName", "")).strip(),
        accepted=True,
    )


def detect_ui_action(user_text, locale):
    normalized = str(user_text or "").strip().lower()
    if not normalized:
        return None
    focus_patterns = [
        (
            {
                "type": "focus_element",
                "tab": "settings",
                "targetId": "language-title",
                "selector": "#languages .remote-target",
                "source": "voice_command",
            },
            ["语言设置", "语言模式", "language mode", "language settings", "言語モード"],
        ),
        (
            {
                "type": "focus_element",
                "tab": "settings",
                "targetId": "audio-stack-title",
                "selector": "#model-stack-cards .focusable-card",
                "source": "voice_command",
            },
            ["语音设置", "音频设置", "模型目录", "audio settings", "voice settings", "model stack", "音声設定", "モデル一覧"],
        ),
        (
            {
                "type": "focus_element",
                "tab": "test",
                "targetId": "test-input",
                "selector": "#test-input",
                "source": "voice_command",
            },
            ["文字测试", "测试输入", "text test", "test input", "テキストテスト"],
        ),
        (
            {
                "type": "focus_element",
                "tab": "test",
                "targetId": "test-blueprints-title",
                "selector": "#studio-blueprints .remote-target",
                "source": "voice_command",
            },
            ["蓝图工作室", "蓝图列表", "blueprint studio", "blueprint list", "ブループリント"],
        ),
        (
            {
                "type": "focus_element",
                "tab": "pairing",
                "targetId": "pairing-code",
                "selector": ".fake-qr",
                "source": "voice_command",
            },
            ["配对码", "二维码", "pairing qr", "pairing code", "qr code", "qr", "qrコード"],
        ),
        (
            {
                "type": "focus_element",
                "tab": "agents",
                "targetId": "agents-title",
                "selector": "#agents .remote-target",
                "source": "voice_command",
            },
            ["智能体面板", "agent panel", "agents panel", "agent list", "エージェント一覧"],
        ),
    ]
    for action, patterns in focus_patterns:
        if any(pattern in normalized for pattern in patterns):
            return action
    tab_patterns = [
        ("home", ["进入首页", "回到首页", "打开首页", "go home", "open home", "home tab", "ホーム", "ホームに"]),
        ("agents", ["进入智能体", "打开智能体", "进入agents", "open agents", "show agents", "agent tab", "エージェント"]),
        ("voice", ["进入语音", "打开语音", "voice tab", "open voice", "音声"]),
        ("test", ["进入测试", "打开测试", "进入测试台", "打开测试台", "text test", "open test", "test tab", "テスト"]),
        ("pairing", ["进入配对", "打开配对", "pairing tab", "open pairing", "ペアリング"]),
        ("settings", ["进入设置", "打开设置", "go to settings", "open settings", "settings tab", "設定"]),
    ]
    for tab_name, patterns in tab_patterns:
        if any(pattern in normalized for pattern in patterns):
            return {
                "type": "switch_tab",
                "tab": tab_name,
                "source": "voice_command",
            }
    return None


def build_ui_action_reply(action, locale):
    if not action:
        return ""
    action_type = str(action.get("type", "")).strip()
    tab_name = str(action.get("tab", "")).strip()
    labels = {
        "home": {"zh-CN": "首页", "ja-JP": "ホーム", "default": "Home"},
        "agents": {"zh-CN": "智能体", "ja-JP": "エージェント", "default": "Agents"},
        "voice": {"zh-CN": "语音", "ja-JP": "音声", "default": "Voice"},
        "test": {"zh-CN": "测试", "ja-JP": "テスト", "default": "Test"},
        "pairing": {"zh-CN": "配对", "ja-JP": "ペアリング", "default": "Pairing"},
        "settings": {"zh-CN": "设置", "ja-JP": "設定", "default": "Settings"},
    }
    label = labels.get(tab_name, {}).get(locale) or labels.get(tab_name, {}).get("default") or tab_name
    if action_type == "focus_element":
        if locale == "zh-CN":
            return f"好的，正在打开{label}里的相关区域。"
        if locale == "ja-JP":
            return f"{label}内の関連エリアを表示します。"
        return f"Opening the relevant area inside {label}."
    if locale == "zh-CN":
        return f"好的，正在进入{label}。"
    if locale == "ja-JP":
        return f"{label}タブを表示します。"
    return f"Opening the {label} tab."


def _get_pending_voice_clarification():
    return PENDING_VOICE_CLARIFICATION


def _set_pending_voice_clarification(payload):
    global PENDING_VOICE_CLARIFICATION
    PENDING_VOICE_CLARIFICATION = payload


def _voice_context():
    return {
        "build_agent_factory_reply": build_agent_factory_reply,
        "build_clarification_reply": build_clarification_reply,
        "build_general_voice_reply": build_general_voice_reply,
        "build_grounded_network_reply": build_grounded_network_reply,
        "perform_autonomous_network_lookup": perform_autonomous_network_lookup,
        "build_network_unavailable_reply": build_network_unavailable_reply,
        "build_weather_reply": build_weather_reply,
        "build_network_lookup_reply": build_network_lookup_reply,
        "build_pending_clarification_snapshot": build_pending_clarification_snapshot,
        "build_runtime_bridge": build_runtime_bridge,
        "build_runtime_strategy": build_runtime_strategy,
        "build_tool_plan": build_tool_plan,
        "build_ui_action_reply": build_ui_action_reply,
        "build_tool_registry_snapshot": build_tool_registry_snapshot,
        "clear_pending_voice_clarification": clear_pending_voice_clarification,
        "detect_ui_action": detect_ui_action,
        "feature_manager": FEATURE_MANAGER,
        "get_pending_voice_clarification": _get_pending_voice_clarification,
        "learn_from_clarification": learn_from_clarification,
        "load_ollama_inventory": load_ollama_inventory,
        "looks_like_local_file_request": looks_like_local_file_request,
        "perform_network_lookup": perform_network_lookup,
        "record_route_semantic_example": record_route_semantic_example,
        "route_voice_request": route_voice_request,
        "select_model_route": select_model_route,
        "serialize_voice_route": serialize_voice_route,
        "set_pending_voice_clarification": _set_pending_voice_clarification,
    }


def resolve_voice_request(user_text, locale):
    return resolve_voice_request_payload(user_text, locale, _voice_context())


def build_voice_router_snapshot(locale):
    return build_voice_router_snapshot_payload(locale, _voice_context())


def set_last_voice_route(route, request_text=""):
    global LAST_VOICE_ROUTE
    payload = dict(route or {})
    payload["requestText"] = str(request_text or "").strip()
    LAST_VOICE_ROUTE = payload


def clear_pending_voice_clarification():
    global PENDING_VOICE_CLARIFICATION
    PENDING_VOICE_CLARIFICATION = None


def reset_last_voice_route():
    set_last_voice_route(default_last_voice_route())


def is_generic_agent_request(user_text):
    lowered = user_text.lower()
    zh_targets = ["智能体", "助手", "代理", "机器人"]
    zh_verbs = ["创建", "新建", "做一个", "做个", "帮我做", "帮我创建", "能创建", "有哪些", "什么"]
    en_targets = ["agent", "assistant", "bot", "workflow"]
    en_verbs = ["create", "make", "build", "what", "available", "design"]
    zh_request = any(target in user_text for target in zh_targets) and any(token in user_text for token in zh_verbs)
    en_request = any(target in lowered for target in en_targets) and any(token in lowered for token in en_verbs)
    return zh_request or en_request


def generate_assistant_reply(user_text, locale):
    return generate_assistant_reply_payload(user_text, locale, _voice_context())


def build_last_voice_route(user_text, locale):
    return build_last_voice_route_payload(user_text, locale, _voice_context())


def should_cortex_require_network(user_text, task_spec):
    lowered = str(user_text or "").lower()
    task_type = str(task_spec.get("taskType", "")).strip()
    if task_type in {"ui_navigation", "reminder", "schedule", "time_query"}:
        return False
    if task_type == "weather":
        return False
    return (
        task_type == "network_lookup"
        or any(token in lowered for token in ["latest", "news", "official", "search", "lookup", "look up", "research", "价格", "最新", "官网", "上网", "联网"])
    )


def looks_like_local_file_request(user_text):
    text = str(user_text or "")
    lowered = text.lower()
    tokens = [
        "文件", "文件夹", "目录", "文档", "文稿", "桌面", "下载", "路径", "读取", "打开文件", "发给我", "发送文件", "附件",
        "documents", "downloads", "desktop", "directory", "folder", "file", "path", "read file", "open file", "send me", "attachment",
        "~/", "/users/", "/volumes/", ".pptx", ".ppt", ".xlsx", ".xls", ".docx", ".doc", ".pdf", ".txt", ".csv",
    ]
    return any(token in text or token in lowered for token in tokens)


def build_cortex_route_plan(user_text, locale, task_spec, route=None):
    route = route if isinstance(route, dict) else {}
    seed_state = default_agent_cortex("homehub-shared-brain", "HomeHub Shared Brain")
    seed_state["stage"] = "shared-brain"
    seed_state["blueprint"]["mission"] = "Understand HomeHub requests, choose the right execution lane, and keep outputs grounded in current runtime state."
    seed_state["blueprint"]["networkEnabled"] = True
    request = {
        "command": str(user_text or "").strip(),
        "locale": locale,
        "taskType": str(task_spec.get("taskType", "general_chat")).strip() or "general_chat",
        "inputModes": list(task_spec.get("inputModes", ["text"])) or ["text"],
        "requireArtifacts": bool(task_spec.get("requiresGeneration", False)),
        "requiresNetwork": should_cortex_require_network(user_text, task_spec),
        "speakReply": False,
    }
    brain = CORTEX_ARCHITECT.design_state(seed_state, request)
    requirement = brain.get("requirementSpec", {}) if isinstance(brain.get("requirementSpec", {}), dict) else {}
    decision_hints = requirement.get("decisionHints", {}) if isinstance(requirement.get("decisionHints", {}), dict) else {}
    model_plan = brain.get("modelPlan", {}) if isinstance(brain.get("modelPlan", {}), dict) else {}
    assignments = model_plan.get("assignments", {}) if isinstance(model_plan.get("assignments", {}), dict) else {}
    capability_list = requirement.get("requiredCapabilities", []) if isinstance(requirement.get("requiredCapabilities", []), list) else []
    return {
        "request": request,
        "summary": brain.get("summary", {}),
        "requirementSpec": requirement,
        "decisionHints": decision_hints,
        "taskflow": brain.get("taskflow", {}),
        "requestLoop": brain.get("requestLoop", {}),
        "technologyStack": brain.get("technologyStack", []),
        "autonomousCreation": brain.get("autonomousCreation", {}),
        "modelPlan": model_plan,
        "selectedModels": assignments,
        "capabilities": capability_list,
        "reasoning": (
            f"Cortex classified task={request['taskType']} and inferred capabilities: "
            f"{', '.join(capability_list) if capability_list else 'semantic-understanding'}."
        ),
        "shouldNetwork": bool(request.get("requiresNetwork")) or bool(decision_hints.get("requireSearch")),
        "plannerModel": assignments.get("planner", ""),
        "executorModel": assignments.get("executor", ""),
        "responseModel": assignments.get("response", ""),
    }


def build_dashboard():
    return build_dashboard_payload(
        {
            "audio_stack": AUDIO_STACK,
            "base_agents": BASE_AGENTS,
            "base_timeline": BASE_TIMELINE,
            "bootstrap_snapshot": bootstrap_snapshot,
            "box_profile": BOX_PROFILE,
            "build_ai_capability_catalog": build_ai_capability_catalog,
            "build_feature_household_modules": build_feature_household_modules,
            "build_runtime_bridge": build_runtime_bridge,
            "build_runtime_strategy": build_runtime_strategy,
            "build_voice_router_snapshot": build_voice_router_snapshot,
            "current_conversation": CURRENT_CONVERSATION,
            "feature_manager": FEATURE_MANAGER,
            "get_audio_provider_catalog": get_audio_provider_catalog,
            "get_google_service_account_file": get_google_service_account_file,
            "language_settings": LANGUAGE_SETTINGS,
            "last_voice_route": LAST_VOICE_ROUTE,
            "load_ollama_inventory": load_ollama_inventory,
            "model_providers": MODEL_PROVIDERS,
            "pairing": PAIRING,
            "persisted_settings": PERSISTED_SETTINGS,
            "relay_messages": RELAY_MESSAGES,
            "secret_sources": SECRET_SOURCES,
            "secrets": SECRETS,
            "semantic_backend_snapshot": semantic_backend_snapshot,
            "skills": SKILLS,
            "system_status": SYSTEM_STATUS,
            "voice_profile": VOICE_PROFILE,
            "weather": WEATHER,
        }
    )


def build_cortex_unpacked(request: dict | None = None):
    request = request if isinstance(request, dict) else {}
    locale = normalize_locale(request.get("locale", PERSISTED_SETTINGS.get("language", "zh-CN")), PERSISTED_SETTINGS.get("language", "zh-CN"))
    input_modes = normalize_string_list(request.get("inputModes", ["text"])) or ["text"]
    normalized_request = {
        "command": str(request.get("command", "")).strip()
        or ("请帮我分析这个需求，并说明 HomeHub 应该如何执行。" if locale == "zh-CN" else "Analyze this request and explain how HomeHub should execute it."),
        "locale": locale,
        "taskType": str(request.get("taskType", "general_chat")).strip() or "general_chat",
        "inputModes": sorted(set(input_modes)) or ["text"],
        "requireArtifacts": bool(request.get("requireArtifacts", False)),
        "requiresNetwork": bool(request.get("requiresNetwork", False)),
        "speakReply": bool(request.get("speakReply", False)),
    }
    seed_state = default_agent_cortex("homehub-shared-brain", "HomeHub Shared Brain")
    seed_state["stage"] = "shared-brain"
    seed_state["blueprint"]["mission"] = "Understand multimodal user requests, decide whether to reuse or create smart units, and explain the execution path."
    seed_state["blueprint"]["networkEnabled"] = True
    return {
        "ok": True,
        "seed": {
            "agentId": seed_state["agentId"],
            "agentName": seed_state["agentName"],
            "stage": seed_state["stage"],
        },
        "request": normalized_request,
        "item": CORTEX_ARCHITECT.design_state(seed_state, normalized_request),
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
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError):
            # The browser canceled or replaced the request before the response finished.
            return

    def _send_raw(self, payload, status=200, content_type="text/plain; charset=utf-8"):
        body = payload if isinstance(payload, bytes) else str(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, OSError):
            return

    def _send_feature_response(self, response):
        if "rawBody" in response:
            self._send_raw(
                response.get("rawBody", ""),
                status=response.get("status", 200),
                content_type=response.get("contentType", "text/plain; charset=utf-8"),
            )
            return
        self._send_json(response.get("body", {}), status=response.get("status", 200))

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

    def _read_request_body(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return b""
        if length <= 0:
            return b""
        return self.rfile.read(length)

    def _parse_request_body(self, raw):
        if not raw:
            return None
        try:
            return json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return {"_raw": raw.decode("utf-8", errors="ignore")}

    def _route_context(self):
        return {
            "append_conversation_turn": append_conversation_turn,
            "audio_provider_catalog": AUDIO_PROVIDER_CATALOG,
            "bootstrap_snapshot": bootstrap_snapshot,
            "build_assistant_memory_snapshot": build_assistant_memory_snapshot,
            "build_dashboard": build_dashboard,
            "build_cortex_unpacked": build_cortex_unpacked,
            "build_initial_conversation": build_initial_conversation,
            "clear_pending_voice_clarification": clear_pending_voice_clarification,
            "current_conversation": CURRENT_CONVERSATION,
            "detect_text_locale": detect_text_locale,
            "export_training_pairs": export_training_pairs,
            "feature_manager": FEATURE_MANAGER,
            "generated_dir": GENERATED_DIR,
            "get_audio_provider_catalog": get_audio_provider_catalog,
            "get_google_service_account_file": get_google_service_account_file,
            "get_secret_sources": get_secret_sources,
            "json": json,
            "language_settings": LANGUAGE_SETTINGS,
            "load_custom_audio_providers": load_custom_audio_providers,
            "load_secrets_file": load_secrets_file,
            "mimetypes": mimetypes,
            "model_providers": MODEL_PROVIDERS,
            "network_lookup_policies": NETWORK_LOOKUP_POLICIES,
            "normalize_locale": normalize_locale,
            "normalize_string_list": normalize_string_list,
            "normalize_supported_languages": normalize_supported_languages,
            "pairing": PAIRING,
            "perform_network_lookup": perform_network_lookup,
            "persisted_settings": PERSISTED_SETTINGS,
            "query_semantic_memory": query_semantic_memory,
            "record_semantic_example": record_semantic_example,
            "refresh_weather_from_coordinates": refresh_weather_from_coordinates,
            "refresh_secrets_state": lambda: self._refresh_secrets_state(),
            "relay_messages": RELAY_MESSAGES,
            "resolve_voice_request": resolve_voice_request,
            "reset_last_voice_route": reset_last_voice_route,
            "save_custom_audio_providers": save_custom_audio_providers,
            "save_persisted_settings": save_persisted_settings,
            "save_secrets": save_secrets,
            "semantic_backend_snapshot": semantic_backend_snapshot,
            "set_last_voice_route": set_last_voice_route,
            "skills": SKILLS,
            "start_bootstrap_install": start_bootstrap_install,
            "static_dir": STATIC_DIR,
            "synthesize_speech": synthesize_speech,
            "transcribe_audio": transcribe_audio,
            "usage_log_file": USAGE_LOG_FILE,
            "weather_state_file": WEATHER_STATE_FILE,
            "voice_conversation": VOICE_CONVERSATION,
            "voice_profile": VOICE_PROFILE,
        }

    def _refresh_secrets_state(self):
        global SECRETS, SECRET_SOURCES
        SECRETS = get_effective_secrets()
        SECRET_SOURCES = get_secret_sources()
        return SECRETS

    def do_GET(self):
        try:
            parsed = urlparse(self.path)
            if parsed.path == "/api/cortex/unpacked":
                params = {}
                for key, values in parse_qs(parsed.query).items():
                    params[key] = values[0] if isinstance(values, list) and values else values
                request = {
                    "command": str(params.get("command", "")).strip(),
                    "locale": normalize_locale(params.get("locale", PERSISTED_SETTINGS.get("language", "zh-CN")), PERSISTED_SETTINGS.get("language", "zh-CN")),
                    "taskType": str(params.get("taskType", "general_chat")).strip() or "general_chat",
                    "inputModes": normalize_string_list(params.get("inputModes", "text")) or ["text"],
                    "requireArtifacts": str(params.get("requireArtifacts", "")).strip().lower() in {"1", "true", "yes", "on"},
                    "requiresNetwork": str(params.get("requiresNetwork", "true")).strip().lower() in {"1", "true", "yes", "on"},
                    "speakReply": str(params.get("speakReply", "")).strip().lower() in {"1", "true", "yes", "on"},
                }
                self._send_json(build_cortex_unpacked(request))
                return
            runtime = build_runtime_bridge()
            if handle_get_route(self, parsed, runtime, self._route_context()):
                return
            self.send_error(404)
        except Exception:
            traceback.print_exc()
            self._send_json({"error": "GET route failed", "path": self.path}, status=500)

    def do_POST(self):
        try:
            parsed = urlparse(self.path)
            if parsed.path == "/api/cortex/unpacked":
                raw_body = self._read_request_body()
                preview_body = self._parse_request_body(raw_body)
                body = preview_body if isinstance(preview_body, dict) else {}
                request = {
                    "command": str(body.get("command", "")).strip(),
                    "locale": normalize_locale(body.get("locale", PERSISTED_SETTINGS.get("language", "zh-CN")), PERSISTED_SETTINGS.get("language", "zh-CN")),
                    "taskType": str(body.get("taskType", "general_chat")).strip() or "general_chat",
                    "inputModes": normalize_string_list(body.get("inputModes", ["text"])) or ["text"],
                    "requireArtifacts": bool(body.get("requireArtifacts", False)),
                    "requiresNetwork": bool(body.get("requiresNetwork", False)),
                    "speakReply": bool(body.get("speakReply", False)),
                }
                self._send_json(build_cortex_unpacked(request))
                return
            runtime = build_runtime_bridge()
            raw_body = self._read_request_body()
            preview_body = self._parse_request_body(raw_body)
            raw_text = raw_body.decode("utf-8", errors="ignore") if raw_body else ""
            request_headers = {str(key).lower(): str(value) for key, value in self.headers.items()}
            if preview_body is None:
                preview_body = {"_headers": request_headers, "_raw": raw_text}
            elif isinstance(preview_body, dict):
                preview_body["_headers"] = request_headers
                preview_body.setdefault("_raw", raw_text)
            if handle_post_route(self, parsed, runtime, preview_body, raw_text, request_headers, self._route_context()):
                return
            self.send_error(404)
        except Exception:
            traceback.print_exc()
            self._send_json({"error": "POST route failed", "path": self.path}, status=500)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    email_sync_thread = threading.Thread(target=run_background_email_sync, daemon=True)
    email_sync_thread.start()
    bridge_pull_thread = threading.Thread(target=run_background_bridge_pull, daemon=True)
    bridge_pull_thread.start()
    server = ThreadingHTTPServer((RUNTIME_HOST, RUNTIME_PORT), Handler)
    print(f"HomeHub runtime started at http://{RUNTIME_HOST}:{RUNTIME_PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nHomeHub runtime stopped")
        server.server_close()
