import base64
import io
import json
import mimetypes
import os
import random
import re
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
import wave
from copy import deepcopy
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlencode, urlparse

try:
    from features.base import RuntimeBridge
    from features.loader import FeatureManager
    from server_components.greetings import build_initial_conversation, build_welcome_message
    from server_components.language_detector import detect_text_locale, normalize_locale
    from server_components.task_router import build_task_spec, infer_task_spec_with_openai
except ModuleNotFoundError:
    from runtime.features.base import RuntimeBridge
    from runtime.features.loader import FeatureManager
    from runtime.server_components.greetings import build_initial_conversation, build_welcome_message
    from runtime.server_components.language_detector import detect_text_locale, normalize_locale
    from runtime.server_components.task_router import build_task_spec, infer_task_spec_with_openai

ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
GENERATED_DIR = ROOT / "generated"
SETTINGS_FILE = ROOT / "settings.json"
CUSTOM_AUDIO_PROVIDERS_FILE = ROOT / "custom_audio_providers.json"
BOOTSTRAP_STATUS_FILE = ROOT / "bootstrap_status.json"
SECRETS_LOCAL_FILE = ROOT / "secrets.local.json"
SECRETS_PROD_FILE = ROOT / "secrets.prod.json"
USAGE_LOG_FILE = ROOT / "usage-cost-log.jsonl"
GOOGLE_SERVICE_ACCOUNT_FILE = ROOT / "google-cloud-service-account.json"
RUNTIME_ENV = os.environ.get("HOMEHUB_ENV", "local").lower()
RUNTIME_HOST = os.environ.get("HOMEHUB_HOST", "0.0.0.0")
RUNTIME_PORT = int(os.environ.get("PORT") or os.environ.get("HOMEHUB_PORT", "8787"))
FEATURES_DIR = ROOT / "features"
PROJECT_ROOT = ROOT.parent
BOOTSTRAP_SCRIPT = PROJECT_ROOT / "tools" / "bootstrap_homehub.py"
BOOTSTRAP_PROCESS = None
OLLAMA_INVENTORY_CACHE = {"value": None, "updated_at": 0.0}
OLLAMA_INVENTORY_TTL_SECONDS = 15.0
EMAIL_SYNC_INTERVAL_SECONDS = int(os.environ.get("HOMEHUB_EMAIL_SYNC_INTERVAL", "90"))


def get_secrets_file():
    if RUNTIME_ENV == "prod":
        return SECRETS_PROD_FILE
    return SECRETS_LOCAL_FILE


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
        "mailAddress": data.get("mailAddress", ""),
        "mailPassword": data.get("mailPassword", ""),
        "mailSmtpHost": data.get("mailSmtpHost", ""),
        "mailSmtpPort": data.get("mailSmtpPort", ""),
        "mailImapHost": data.get("mailImapHost", ""),
        "mailImapPort": data.get("mailImapPort", ""),
        "wechatOfficialToken": data.get("wechatOfficialToken", ""),
        "wechatOfficialAppId": data.get("wechatOfficialAppId", ""),
        "wechatOfficialAppSecret": data.get("wechatOfficialAppSecret", ""),
        "wechatOfficialEncodingAesKey": data.get("wechatOfficialEncodingAesKey", ""),
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
    mail_address = os.environ.get("HOMEHUB_MAIL_ADDRESS") or file_secrets.get("mailAddress", "")
    mail_password = os.environ.get("HOMEHUB_MAIL_PASSWORD") or file_secrets.get("mailPassword", "")
    mail_smtp_host = os.environ.get("HOMEHUB_MAIL_SMTP_HOST") or file_secrets.get("mailSmtpHost", "")
    mail_smtp_port = os.environ.get("HOMEHUB_MAIL_SMTP_PORT") or file_secrets.get("mailSmtpPort", "")
    mail_imap_host = os.environ.get("HOMEHUB_MAIL_IMAP_HOST") or file_secrets.get("mailImapHost", "")
    mail_imap_port = os.environ.get("HOMEHUB_MAIL_IMAP_PORT") or file_secrets.get("mailImapPort", "")
    wechat_official_token = os.environ.get("HOMEHUB_WECHAT_OFFICIAL_TOKEN") or file_secrets.get("wechatOfficialToken", "")
    wechat_official_app_id = os.environ.get("HOMEHUB_WECHAT_OFFICIAL_APP_ID") or file_secrets.get("wechatOfficialAppId", "")
    wechat_official_app_secret = os.environ.get("HOMEHUB_WECHAT_OFFICIAL_APP_SECRET") or file_secrets.get("wechatOfficialAppSecret", "")
    wechat_official_encoding_aes_key = os.environ.get("HOMEHUB_WECHAT_OFFICIAL_ENCODING_AES_KEY") or file_secrets.get("wechatOfficialEncodingAesKey", "")
    return {
        "googleApiKey": google_api_key,
        "googleAccessToken": google_access_token,
        "openaiApiKey": openai_api_key,
        "mailAddress": mail_address,
        "mailPassword": mail_password,
        "mailSmtpHost": mail_smtp_host,
        "mailSmtpPort": mail_smtp_port,
        "mailImapHost": mail_imap_host,
        "mailImapPort": mail_imap_port,
        "wechatOfficialToken": wechat_official_token,
        "wechatOfficialAppId": wechat_official_app_id,
        "wechatOfficialAppSecret": wechat_official_app_secret,
        "wechatOfficialEncodingAesKey": wechat_official_encoding_aes_key,
    }


def get_secret_sources():
    file_secrets = load_secrets_file()
    return {
        "googleApiKey": "env" if (os.environ.get("HOMEHUB_GOOGLE_API_KEY") or os.environ.get("GOOGLE_API_KEY")) else ("file" if file_secrets.get("googleApiKey") else "missing"),
        "googleAccessToken": "env" if (os.environ.get("HOMEHUB_GOOGLE_ACCESS_TOKEN") or os.environ.get("GOOGLE_ACCESS_TOKEN")) else ("file" if file_secrets.get("googleAccessToken") else "missing"),
        "openaiApiKey": "env" if (os.environ.get("HOMEHUB_OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")) else ("file" if file_secrets.get("openaiApiKey") else "missing"),
        "mailAddress": "env" if os.environ.get("HOMEHUB_MAIL_ADDRESS") else ("file" if file_secrets.get("mailAddress") else "missing"),
        "mailPassword": "env" if os.environ.get("HOMEHUB_MAIL_PASSWORD") else ("file" if file_secrets.get("mailPassword") else "missing"),
        "mailSmtpHost": "env" if os.environ.get("HOMEHUB_MAIL_SMTP_HOST") else ("file" if file_secrets.get("mailSmtpHost") else "missing"),
        "mailSmtpPort": "env" if os.environ.get("HOMEHUB_MAIL_SMTP_PORT") else ("file" if file_secrets.get("mailSmtpPort") else "missing"),
        "mailImapHost": "env" if os.environ.get("HOMEHUB_MAIL_IMAP_HOST") else ("file" if file_secrets.get("mailImapHost") else "missing"),
        "mailImapPort": "env" if os.environ.get("HOMEHUB_MAIL_IMAP_PORT") else ("file" if file_secrets.get("mailImapPort") else "missing"),
        "wechatOfficialToken": "env" if os.environ.get("HOMEHUB_WECHAT_OFFICIAL_TOKEN") else ("file" if file_secrets.get("wechatOfficialToken") else "missing"),
        "wechatOfficialAppId": "env" if os.environ.get("HOMEHUB_WECHAT_OFFICIAL_APP_ID") else ("file" if file_secrets.get("wechatOfficialAppId") else "missing"),
        "wechatOfficialAppSecret": "env" if os.environ.get("HOMEHUB_WECHAT_OFFICIAL_APP_SECRET") else ("file" if file_secrets.get("wechatOfficialAppSecret") else "missing"),
        "wechatOfficialEncodingAesKey": "env" if os.environ.get("HOMEHUB_WECHAT_OFFICIAL_ENCODING_AES_KEY") else ("file" if file_secrets.get("wechatOfficialEncodingAesKey") else "missing"),
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
            "runtimeProfile": "low-memory",
            "bootstrapConsent": False,
            "bootstrapCompleted": False,
        }

    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {
            "language": LANGUAGE_SETTINGS["current"],
            "sttProvider": "google",
            "ttsProvider": "google",
            "runtimeProfile": "low-memory",
            "bootstrapConsent": False,
            "bootstrapCompleted": False,
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

    supported_profiles = {item["id"] for item in RUNTIME_PROFILES}
    runtime_profile = data.get("runtimeProfile", "low-memory")
    if runtime_profile not in supported_profiles:
        runtime_profile = "low-memory"

    return {
        "language": language,
        "sttProvider": stt_provider,
        "ttsProvider": tts_provider,
        "runtimeProfile": runtime_profile,
        "bootstrapConsent": bool(data.get("bootstrapConsent", False)),
        "bootstrapCompleted": bool(data.get("bootstrapCompleted", False)),
    }


def save_persisted_settings(settings):
    SETTINGS_FILE.write_text(
        json.dumps(settings, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_bootstrap_status():
    if not BOOTSTRAP_STATUS_FILE.exists():
        return {
            "stage": "idle",
            "message": "",
            "completed": False,
        }
    try:
        data = json.loads(BOOTSTRAP_STATUS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {
            "stage": "idle",
            "message": "",
            "completed": False,
        }
    if not isinstance(data, dict):
        return {
            "stage": "idle",
            "message": "",
            "completed": False,
        }
    return data


def save_bootstrap_status(payload):
    BOOTSTRAP_STATUS_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def bootstrap_snapshot():
    refresh_bootstrap_process_state()
    status = load_bootstrap_status()
    approved = bool(PERSISTED_SETTINGS.get("bootstrapConsent", False))
    completed = bool(PERSISTED_SETTINGS.get("bootstrapCompleted", False))
    in_progress = bool(status.get("stage") in {"starting", "installing-tools", "installing-python", "installing-models"})
    blocking = bool(status.get("stage") in {"starting", "installing-tools", "installing-python"})
    return {
        "approved": approved,
        "completed": completed,
        "inProgress": in_progress,
        "blocking": blocking,
        "stage": status.get("stage", "idle"),
        "message": status.get("message", ""),
        "missingCommands": status.get("missingCommands", []),
        "missingPythonModules": status.get("missingPythonModules", []),
        "missingOllamaModels": status.get("missingOllamaModels", []),
    }


def refresh_bootstrap_process_state():
    global BOOTSTRAP_PROCESS, PERSISTED_SETTINGS
    if BOOTSTRAP_PROCESS is None:
        return
    code = BOOTSTRAP_PROCESS.poll()
    if code is None:
        return
    BOOTSTRAP_PROCESS = None
    status = load_bootstrap_status()
    if status.get("completed"):
        PERSISTED_SETTINGS["bootstrapCompleted"] = True
        save_persisted_settings(PERSISTED_SETTINGS)


def start_bootstrap_install():
    global BOOTSTRAP_PROCESS
    refresh_bootstrap_process_state()
    if BOOTSTRAP_PROCESS is not None and BOOTSTRAP_PROCESS.poll() is None:
        return False
    save_bootstrap_status({"stage": "starting", "message": "Preparing first-run bootstrap.", "completed": False})
    BOOTSTRAP_PROCESS = subprocess.Popen(
        [
            sys.executable,
            str(BOOTSTRAP_SCRIPT),
            "--apply",
            "--quiet",
            "--status-file",
            str(BOOTSTRAP_STATUS_FILE),
        ],
        cwd=str(PROJECT_ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return True


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


PERSISTED_SETTINGS = load_persisted_settings()
SECRETS = get_effective_secrets()
SECRET_SOURCES = get_secret_sources()
maybe_start_bootstrap_install()


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
        "id": "study-plan-agents",
        "label": "Study Plan Agents",
        "kind": "feature",
        "featureId": "study-plan-agents",
        "handles": ["study_plan", "learning_agent"],
        "inputModes": ["text", "voice"],
        "execution": "hybrid",
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


def normalize_domain(value):
    host = str(value or "").strip().lower()
    if not host:
        return ""
    if "://" in host:
        host = urlparse(host).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    return host.split(":")[0]


def domain_allowed(host, allowed_domains):
    normalized = normalize_domain(host)
    return any(normalized == item or normalized.endswith(f".{item}") for item in allowed_domains)


def extract_urls_from_text(text):
    return re.findall(r"https?://[^\s)>\"]+", str(text or ""))


def strip_html_excerpt(html_text, limit=420):
    text = re.sub(r"(?is)<script.*?>.*?</script>", " ", html_text)
    text = re.sub(r"(?is)<style.*?>.*?</style>", " ", text)
    title_match = re.search(r"(?is)<title[^>]*>(.*?)</title>", text)
    title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", title_match.group(1))).strip() if title_match else ""
    plain = re.sub(r"(?s)<[^>]+>", " ", text)
    plain = re.sub(r"\s+", " ", plain).strip()
    return {"title": title, "excerpt": plain[:limit]}


def fetch_allowed_url(url, allowed_domains):
    host = normalize_domain(url)
    if not domain_allowed(host, allowed_domains):
        return {"ok": False, "error": f"domain_not_allowed:{host}"}
    try:
        content = json_get(url, headers={"User-Agent": "HomeHub/0.1"})
    except Exception as exc:
        return {"ok": False, "error": f"fetch_failed:{exc}"}
    if isinstance(content, dict):
        return {"ok": True, "url": url, "title": str(content.get("title", "")).strip(), "excerpt": json.dumps(content, ensure_ascii=False)[:420]}
    parsed = strip_html_excerpt(str(content))
    return {"ok": True, "url": url, "title": parsed.get("title", ""), "excerpt": parsed.get("excerpt", "")}


def wikipedia_lookup(query, locale):
    language = "zh" if str(locale).startswith("zh") else ("ja" if str(locale).startswith("ja") else "en")
    params = urlencode({"action": "opensearch", "search": query, "limit": 1, "namespace": 0, "format": "json"})
    search_url = f"https://{language}.wikipedia.org/w/api.php?{params}"
    try:
        response = json_get(search_url, headers={"User-Agent": "HomeHub/0.1"})
    except Exception as exc:
        return {"ok": False, "error": f"wikipedia_search_failed:{exc}"}
    if not isinstance(response, list) or len(response) < 4 or not response[1]:
        return {"ok": False, "error": "no_wikipedia_match"}
    title = str(response[1][0]).strip()
    summary_url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{quote(title)}"
    try:
        summary = json_get(summary_url, headers={"User-Agent": "HomeHub/0.1"})
    except Exception as exc:
        return {"ok": False, "error": f"wikipedia_summary_failed:{exc}"}
    if not isinstance(summary, dict):
        return {"ok": False, "error": "invalid_wikipedia_summary"}
    return {
        "ok": True,
        "url": str(summary.get("content_urls", {}).get("desktop", {}).get("page", "")).strip() or summary_url,
        "title": str(summary.get("title", title)).strip(),
        "excerpt": str(summary.get("extract", "")).strip(),
    }


def build_network_lookup_reply(result, locale):
    if not result.get("ok"):
        if locale == "zh-CN":
            return f"这次受控联网查询没有拿到结果：{result.get('error', 'unknown error')}。"
        if locale == "ja-JP":
            return f"制御付きネット検索は結果を返せませんでした: {result.get('error', 'unknown error')}."
        return f"The controlled network lookup did not return a usable result: {result.get('error', 'unknown error')}."
    answer = str(result.get("answer", "")).strip()
    sources = result.get("sources", [])
    if locale == "zh-CN":
        if sources:
            return f"{answer}\n来源：{'；'.join(str(item.get('url', '')) for item in sources[:3])}"
        return answer
    if sources:
        return f"{answer}\nSources: {'; '.join(str(item.get('url', '')) for item in sources[:3])}"
    return answer


def perform_controlled_network_lookup(query, locale, policy_id="safe-general", preferred_sources=None, allowed_domains=None):
    policy = NETWORK_LOOKUP_POLICIES.get(policy_id) or NETWORK_LOOKUP_POLICIES["safe-general"]
    merged_domains = [normalize_domain(item) for item in policy.get("allowedDomains", [])]
    for item in preferred_sources or []:
        normalized = normalize_domain(item)
        if normalized and "." in normalized and normalized not in merged_domains:
            merged_domains.append(normalized)
    for item in allowed_domains or []:
        normalized = normalize_domain(item)
        if normalized and normalized not in merged_domains:
            merged_domains.append(normalized)

    sources = []
    direct_urls = extract_urls_from_text(query)
    for url in direct_urls[: policy.get("maxSources", 3)]:
        fetched = fetch_allowed_url(url, merged_domains)
        if fetched.get("ok"):
            sources.append(fetched)
    if not sources and domain_allowed("wikipedia.org", merged_domains):
        wiki = wikipedia_lookup(query, locale)
        if wiki.get("ok"):
            sources.append(wiki)
    if not sources:
        return {
            "ok": False,
            "error": "no_allowed_source_found",
            "policy": policy["id"],
            "allowedDomains": merged_domains,
            "sources": [],
        }

    answer = sources[0].get("excerpt", "").strip()
    if len(answer) > 320:
        answer = answer[:320].rstrip() + "..."
    title = str(sources[0].get("title", "")).strip()
    if title:
        answer = f"{title}: {answer}" if answer else title
    return {
        "ok": True,
        "policy": policy["id"],
        "allowedDomains": merged_domains,
        "answer": answer,
        "sources": sources[: policy.get("maxSources", 3)],
    }


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
        network_lookup=perform_controlled_network_lookup,
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


def append_conversation_turn(speaker, text_value, artifacts=None):
    CURRENT_CONVERSATION.append(
        {
            "speaker": speaker,
            "text": text_value,
            "time": now_hhmm(),
            "artifacts": artifacts or [],
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
    local_inventory = load_ollama_inventory()
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
        "networkLookup": {
            "policies": list(NETWORK_LOOKUP_POLICIES.values()),
        },
        "modelCatalog": build_ai_capability_catalog(
            provider_catalog,
            {"stt": stt_provider_id, "tts": tts_provider_id},
        ),
        "runtimeProfile": build_runtime_strategy(local_inventory),
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
    task_spec = build_task_spec(
        user_text,
        locale,
        detect_ui_action=detect_ui_action,
        infer_task_spec=lambda text, lang: infer_task_spec_with_openai(
            text,
            lang,
            ai_available=bool(SECRETS.get("openaiApiKey")),
            openai_chat_json=openai_chat_json,
        ),
    )
    runtime_strategy = build_runtime_strategy(load_ollama_inventory())
    route = FEATURE_MANAGER.route_voice_intent(user_text, locale, runtime)
    selected = route.get("selected") or {}
    if selected.get("featureId") == "custom-agents" and float(selected.get("score", 0.0) or 0.0) >= 0.9:
        direct_route = {
            "kind": "feature",
            "selected": selected,
            "candidates": route.get("candidates", []),
            "reasoning": "High-confidence custom agent builder intent matched locally.",
        }
        direct_route["taskSpec"] = task_spec
        direct_route["toolPlan"] = build_tool_plan(task_spec, direct_route)
        direct_route["modelRoute"] = select_model_route(task_spec, runtime_strategy, {"installed": runtime_strategy.get("localDetected", [])})
        return direct_route
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
    routed["taskSpec"] = task_spec
    routed["toolPlan"] = build_tool_plan(task_spec, routed)
    routed["modelRoute"] = select_model_route(task_spec, runtime_strategy, {"installed": runtime_strategy.get("localDetected", [])})
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
    }


def build_pending_clarification_snapshot():
    if not PENDING_VOICE_CLARIFICATION:
        return None
    return dict(PENDING_VOICE_CLARIFICATION)


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


def resolve_voice_request(user_text, locale):
    global PENDING_VOICE_CLARIFICATION

    runtime = build_runtime_bridge()
    original_text = user_text
    combined_text = user_text
    clarification_context = PENDING_VOICE_CLARIFICATION
    ui_action = detect_ui_action(original_text, locale)
    network_hint = any(token in original_text for token in ["查询", "搜索", "查一下", "上网查", "联网查", "官网", "官方", "最新"]) or any(
        token in str(original_text or "").lower() for token in ["search", "lookup", "look up", "web", "online", "official", "latest", "news", "weather", "price"]
    )

    if ui_action and not clarification_context:
        PENDING_VOICE_CLARIFICATION = None
        return {
            "reply": build_ui_action_reply(ui_action, locale),
            "route": {
                "kind": "ui_action",
                "selected": {
                    "intent": "ui-action",
                    "featureId": "tv-shell",
                    "featureName": "TV Shell",
                    "action": ui_action.get("type"),
                    "target": ui_action.get("tab"),
                    "score": 0.99,
                },
                "candidates": [],
                "clarificationQuestion": "",
                "reasoning": "Detected a direct TV navigation command.",
            },
            "pendingClarification": None,
            "uiAction": ui_action,
        }

    if network_hint and not clarification_context:
        task_spec = {
            "taskType": "network_lookup",
            "intent": "network-lookup",
            "summary": "Query approved external sources and return a sourced summary.",
            "urgency": "normal",
            "inputModes": ["text"],
            "requiresImage": False,
            "requiresGeneration": False,
            "requiresScheduling": False,
            "requiresLongRunningAgent": False,
            "preferredExecution": "hybrid",
            "missingInfo": [],
        }
        runtime_strategy = build_runtime_strategy(load_ollama_inventory())
        route = {
            "kind": "general",
            "selected": {
                "intent": "network-lookup",
                "featureId": "homehub-core",
                "featureName": "HomeHub Core",
                "action": "controlled_network_lookup",
                "score": 0.91,
            },
            "candidates": [],
            "reasoning": "Detected a controlled network lookup request from the message.",
            "taskSpec": task_spec,
            "toolPlan": build_tool_plan(task_spec, {"selected": {"featureId": "homehub-core"}}),
            "modelRoute": select_model_route(task_spec, runtime_strategy, {"installed": runtime_strategy.get("localDetected", [])}),
        }
        lookup_result = perform_controlled_network_lookup(original_text, locale)
        return {
            "reply": build_network_lookup_reply(lookup_result, locale),
            "route": serialize_voice_route(route),
            "pendingClarification": None,
            "uiAction": None,
            "lookupResult": lookup_result,
        }

    if clarification_context:
        combined_text = (
            f"Original request: {clarification_context.get('originalRequest', '')}\n"
            f"Clarification answer: {user_text}"
        )

    route = route_voice_request(combined_text, locale)
    lookup_result = None
    ui_action = None

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
        reply = result.get("reply") or build_general_voice_reply(original_text, locale, route.get("modelRoute"))
        ui_action = result.get("uiAction")
        artifacts = result.get("artifacts", [])
    elif (route.get("taskSpec") or {}).get("taskType") == "network_lookup":
        lookup_result = perform_controlled_network_lookup(combined_text if clarification_context else original_text, locale)
        reply = build_network_lookup_reply(lookup_result, locale)
        artifacts = []
    elif route.get("kind") == "agent_factory":
        reply = build_agent_factory_reply(locale)
        artifacts = []
    else:
        reply = build_general_voice_reply(combined_text if clarification_context else original_text, locale, route.get("modelRoute"))
        artifacts = []

    PENDING_VOICE_CLARIFICATION = None
    return {
        "reply": reply,
        "route": serialize_voice_route(route),
        "pendingClarification": None,
        "uiAction": ui_action,
        "lookupResult": lookup_result,
        "artifacts": artifacts,
    }


def build_voice_router_snapshot(locale):
    runtime = build_runtime_bridge()
    features = FEATURE_MANAGER.list_features(runtime)
    return {
        "pendingVoiceClarification": build_pending_clarification_snapshot(),
        "toolRegistry": build_tool_registry_snapshot(),
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
    zh_targets = ["智能体", "助手", "代理", "机器人"]
    zh_verbs = ["创建", "新建", "做一个", "做个", "帮我做", "帮我创建", "能创建", "有哪些", "什么"]
    en_targets = ["agent", "assistant", "bot", "workflow"]
    en_verbs = ["create", "make", "build", "what", "available", "design"]
    zh_request = any(target in user_text for target in zh_targets) and any(token in user_text for token in zh_verbs)
    en_request = any(target in lowered for target in en_targets) and any(token in lowered for token in en_verbs)
    return zh_request or en_request


def generate_assistant_reply(user_text, locale):
    return resolve_voice_request(user_text, locale)["reply"]


def build_last_voice_route(user_text, locale):
    return serialize_voice_route(route_voice_request(user_text, locale))


def build_dashboard():
    provider_catalog = get_audio_provider_catalog()
    local_inventory = load_ollama_inventory()
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
        "runtimeProfile": build_runtime_strategy(local_inventory),
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
        "bootstrap": bootstrap_snapshot(),
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

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        runtime = build_runtime_bridge()
        feature_response = FEATURE_MANAGER.handle_api("GET", path, parse_qs(parsed.query), None, runtime)
        if feature_response:
            self._send_feature_response(feature_response)
            return

        if path == "/api/health":
            self._send_json({"ok": True, "service": "homehub-runtime"})
            return

        if path == "/api/dashboard":
            self._send_json(build_dashboard())
            return

        if path == "/api/bootstrap/status":
            self._send_json(bootstrap_snapshot())
            return

        if path == "/api/providers":
            self._send_json(MODEL_PROVIDERS)
            return

        if path == "/api/network/policies":
            self._send_json({"items": list(NETWORK_LOOKUP_POLICIES.values())})
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

        if path.startswith("/generated/"):
            relative = path.removeprefix("/generated/").strip("/")
            target = (GENERATED_DIR / relative).resolve()
            try:
                target.relative_to(GENERATED_DIR.resolve())
            except ValueError:
                self.send_error(403)
                return
            if not target.exists() or not target.is_file():
                self.send_error(404)
                return
            content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
            self._send_file(target, content_type)
            return

        self.send_error(404)

    def do_POST(self):
        global PERSISTED_SETTINGS, SECRETS, SECRET_SOURCES, LAST_VOICE_ROUTE, PENDING_VOICE_CLARIFICATION

        parsed = urlparse(self.path)
        runtime = build_runtime_bridge()
        raw_body = self._read_request_body()
        preview_body = self._parse_request_body(raw_body)
        feature_response = FEATURE_MANAGER.handle_api("POST", parsed.path, parse_qs(parsed.query), preview_body, runtime)
        if feature_response:
            self._send_feature_response(feature_response)
            return

        if parsed.path == "/api/settings/language":
            body = preview_body
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

        if parsed.path == "/api/bootstrap/approve":
            PERSISTED_SETTINGS["bootstrapConsent"] = True
            PERSISTED_SETTINGS["bootstrapCompleted"] = False
            save_persisted_settings(PERSISTED_SETTINGS)
            start_bootstrap_install()
            self._send_json({"ok": True, "bootstrap": bootstrap_snapshot()})
            return

        if parsed.path == "/api/settings/audio":
            body = preview_body
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
            body = preview_body
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
                "mailAddress": body.get("mailAddress", file_secrets.get("mailAddress", "")),
                "mailPassword": body.get("mailPassword", file_secrets.get("mailPassword", "")),
                "mailSmtpHost": body.get("mailSmtpHost", file_secrets.get("mailSmtpHost", "")),
                "mailSmtpPort": body.get("mailSmtpPort", file_secrets.get("mailSmtpPort", "")),
                "mailImapHost": body.get("mailImapHost", file_secrets.get("mailImapHost", "")),
                "mailImapPort": body.get("mailImapPort", file_secrets.get("mailImapPort", "")),
                "wechatOfficialToken": body.get("wechatOfficialToken", file_secrets.get("wechatOfficialToken", "")),
                "wechatOfficialAppId": body.get("wechatOfficialAppId", file_secrets.get("wechatOfficialAppId", "")),
                "wechatOfficialAppSecret": body.get("wechatOfficialAppSecret", file_secrets.get("wechatOfficialAppSecret", "")),
                "wechatOfficialEncodingAesKey": body.get("wechatOfficialEncodingAesKey", file_secrets.get("wechatOfficialEncodingAesKey", "")),
            })
            SECRETS = get_effective_secrets()
            SECRET_SOURCES = get_secret_sources()
            self._send_json(
                {
                    "ok": True,
                    "googleConfigured": bool(SECRETS.get("googleAccessToken") or get_google_service_account_file().exists()),
                    "openaiConfigured": bool(SECRETS.get("openaiApiKey")),
                    "mailConfigured": bool(SECRETS.get("mailAddress") and SECRETS.get("mailPassword")),
                    "wechatOfficialConfigured": bool(SECRETS.get("wechatOfficialToken") and SECRETS.get("wechatOfficialAppId")),
                    "googleSource": "service-account-file" if get_google_service_account_file().exists() else SECRET_SOURCES.get("googleAccessToken", "missing"),
                    "openaiSource": SECRET_SOURCES.get("openaiApiKey", "missing"),
                    "mailAddressSource": SECRET_SOURCES.get("mailAddress", "missing"),
                    "wechatOfficialTokenSource": SECRET_SOURCES.get("wechatOfficialToken", "missing"),
                    "wechatOfficialAppIdSource": SECRET_SOURCES.get("wechatOfficialAppId", "missing"),
                }
            )
            return

        if parsed.path == "/api/audio/transcribe":
            body = preview_body
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
            transcript_text = str(result.get("transcript", "")).strip()
            detected_locale = detect_text_locale(transcript_text, normalize_locale(locale, PERSISTED_SETTINGS["language"]))
            result["detectedLocale"] = detected_locale
            self._send_json({"ok": True, **result})
            return

        if parsed.path == "/api/audio/synthesize":
            body = preview_body
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

        if parsed.path == "/api/network/query":
            body = preview_body
            if not body or "query" not in body:
                self._send_json({"error": "query is required"}, status=400)
                return
            locale = body.get("locale", PERSISTED_SETTINGS["language"])
            policy_id = str(body.get("policyId", "safe-general")).strip() or "safe-general"
            preferred_sources = body.get("preferredSources", []) if isinstance(body.get("preferredSources", []), list) else []
            allowed_domains = body.get("allowedDomains", []) if isinstance(body.get("allowedDomains", []), list) else []
            result = perform_controlled_network_lookup(str(body.get("query", "")).strip(), locale, policy_id, preferred_sources, allowed_domains)
            self._send_json({"ok": result.get("ok", False), **result})
            return

        if parsed.path == "/api/voice/chat":
            body = preview_body
            if not body or "message" not in body:
                self._send_json({"error": "message is required"}, status=400)
                return

            message = str(body["message"]).strip()
            if not message:
                self._send_json({"error": "message is empty"}, status=400)
                return

            requested_locale = normalize_locale(body.get("locale", PERSISTED_SETTINGS["language"]), PERSISTED_SETTINGS["language"])
            locale = detect_text_locale(message, requested_locale)
            append_conversation_turn("You", message)
            resolution = resolve_voice_request(message, locale)
            voice_route = resolution["route"]
            LAST_VOICE_ROUTE = voice_route
            reply_text = resolution["reply"]
            append_conversation_turn("HomeHub", reply_text, resolution.get("artifacts", []))

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
                    "detectedLocale": locale,
                    "conversation": CURRENT_CONVERSATION,
                    "voiceRoute": voice_route,
                    "pendingVoiceClarification": resolution.get("pendingClarification"),
                    "uiAction": resolution.get("uiAction"),
                    "lookupResult": resolution.get("lookupResult"),
                    "artifacts": resolution.get("artifacts", []),
                    "assistantMemory": build_assistant_memory_snapshot(),
                    "audio": audio_payload,
                }
            )
            return

        if parsed.path == "/api/settings/audio-provider":
            body = preview_body
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
            welcome_seed = build_initial_conversation(PERSISTED_SETTINGS["language"])
            VOICE_CONVERSATION.clear()
            VOICE_CONVERSATION.extend(deepcopy(welcome_seed))
            CURRENT_CONVERSATION.clear()
            CURRENT_CONVERSATION.extend(deepcopy(welcome_seed))
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
            FEATURE_MANAGER.reset(runtime)
            self._send_json({"ok": True, "conversation": CURRENT_CONVERSATION})
            return

        self.send_error(404)

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    email_sync_thread = threading.Thread(target=run_background_email_sync, daemon=True)
    email_sync_thread.start()
    server = ThreadingHTTPServer((RUNTIME_HOST, RUNTIME_PORT), Handler)
    print(f"HomeHub runtime started at http://{RUNTIME_HOST}:{RUNTIME_PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nHomeHub runtime stopped")
        server.server_close()
