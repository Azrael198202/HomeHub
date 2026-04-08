from __future__ import annotations

from copy import deepcopy
from datetime import datetime
import random


def build_dashboard(context: dict) -> dict:
    provider_catalog = context["get_audio_provider_catalog"]()
    local_inventory = context["load_ollama_inventory"]()
    agents = deepcopy(context["base_agents"])
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

    timeline = deepcopy(context["base_timeline"])
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

    persisted_settings = context["persisted_settings"]
    stt_provider_id = persisted_settings["sttProvider"]
    tts_provider_id = persisted_settings["ttsProvider"]
    stt_provider = provider_catalog[stt_provider_id]
    tts_provider = provider_catalog[tts_provider_id]
    runtime = context["build_runtime_bridge"]()
    feature_payload = context["feature_manager"].dashboard_payload(persisted_settings["language"], runtime)
    voice_router = context["build_voice_router_snapshot"](persisted_settings["language"])

    return {
        "hero": {
            "title": "HomeHub",
            "subtitle": "AI Box for the Living Room",
            "tagline": "Boot like a TV box, collaborate like a multi-agent team.",
        },
        "boxProfile": context["box_profile"],
        "householdModules": context["build_feature_household_modules"](persisted_settings["language"]),
        "activeAgents": agents,
        "timelineEvents": timeline,
        "modelProviders": context["model_providers"],
        "skillCatalog": context["skills"],
        "pairingSession": context["pairing"],
        "relayMessages": context["relay_messages"],
        "voiceProfile": {
            **context["voice_profile"],
            "sttProvider": f"{stt_provider['label']} / {stt_provider['stt']['defaultModel']}",
            "ttsProvider": f"{tts_provider['label']} / {tts_provider['tts']['defaultModel']}",
            "locale": persisted_settings["language"],
        },
        "audioStack": {
            **context["audio_stack"],
            "stt": {
                **context["audio_stack"]["stt"],
                "provider": stt_provider["label"],
                "primaryModel": stt_provider["stt"]["defaultModel"],
                "fallbackModel": stt_provider["stt"]["fallbackModel"],
            },
            "tts": {
                **context["audio_stack"]["tts"],
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
                "googleConfigured": bool(context["secrets"].get("googleAccessToken") or context["get_google_service_account_file"]().exists()),
                "openaiConfigured": bool(context["secrets"].get("openaiApiKey")),
                "googleSource": "service-account-file" if context["get_google_service_account_file"]().exists() else context["secret_sources"].get("googleAccessToken", "missing"),
                "openaiSource": context["secret_sources"].get("openaiApiKey", "missing"),
            },
            "counts": {
                "total": len(provider_catalog),
                "editable": sum(1 for provider in provider_catalog.values() if provider.get("editable")),
            },
        },
        "modelCatalog": context["build_ai_capability_catalog"](
            provider_catalog,
            {"stt": stt_provider_id, "tts": tts_provider_id},
        ),
        "runtimeProfile": context["build_runtime_strategy"](local_inventory),
        "languageSettings": {
            **context["language_settings"],
            "current": persisted_settings["language"],
        },
        "weather": context["weather"],
        "systemStatus": context["system_status"],
        "conversation": context["current_conversation"],
        "lastVoiceRoute": context["last_voice_route"],
        "semanticMemory": context["semantic_backend_snapshot"](),
        "features": context["feature_manager"].list_features(runtime),
        "agentTypes": context["feature_manager"].list_agent_types(persisted_settings["language"], runtime),
        "bootstrap": context["bootstrap_snapshot"](),
        **voice_router,
        **feature_payload,
    }
