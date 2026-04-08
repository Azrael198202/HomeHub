from __future__ import annotations

from datetime import datetime


def _parse_iso(value) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None


def _safe_time(value) -> str:
    parsed = _parse_iso(value)
    if parsed:
        return parsed.strftime("%H:%M")
    text = str(value or "").strip()
    return text[-5:] if len(text) >= 5 else text


def _safe_summary(item) -> str:
    return str((item or {}).get("summary", "")).strip()


def _build_live_agents(context: dict, feature_payload: dict, features: list[dict], locale: str) -> list[dict]:
    conversation = context.get("current_conversation", [])
    last_user = next((item for item in reversed(conversation) if item.get("speaker") == "You"), None)
    last_voice_route = context.get("last_voice_route") or {}
    assistant_memory = feature_payload.get("assistantMemory", {}) if isinstance(feature_payload.get("assistantMemory"), dict) else {}
    external_channels = feature_payload.get("externalChannels", {}) if isinstance(feature_payload.get("externalChannels"), dict) else {}
    custom_agents = feature_payload.get("customAgents", []) if isinstance(feature_payload.get("customAgents"), list) else []
    custom_recent = feature_payload.get("customAgentRecentActions", []) if isinstance(feature_payload.get("customAgentRecentActions"), list) else []
    study_agents = feature_payload.get("studyPlanAgents", []) if isinstance(feature_payload.get("studyPlanAgents"), list) else []
    study_recent = feature_payload.get("studyPlanRecentActions", []) if isinstance(feature_payload.get("studyPlanRecentActions"), list) else []

    agents: list[dict] = []

    if last_user or last_voice_route:
        route_kind = str(last_voice_route.get("kind", "")).strip() or "general"
        task_spec = last_voice_route.get("taskSpec", {}) if isinstance(last_voice_route.get("taskSpec"), dict) else {}
        reasoning = str(last_voice_route.get("reasoning", "")).strip() or str(last_voice_route.get("clarificationQuestion", "")).strip()
        target = (last_voice_route.get("selected") or {}).get("featureName") or route_kind
        progress = 58 if route_kind == "clarify" else 82 if route_kind in {"feature", "agent_factory"} else 96
        status = "planning" if route_kind == "clarify" else "running" if last_user else "ready"
        agents.append(
            {
                "id": "voice-router-live",
                "name": "Voice Router",
                "role": f"{route_kind} -> {target}",
                "status": status,
                "model": ((last_voice_route.get("modelRoute") or {}).get("primaryModel") or "runtime"),
                "progress": progress,
                "lastUpdate": reasoning or str(task_spec.get("summary", "")).strip() or str((last_user or {}).get("text", "")).strip(),
            }
        )

    due = assistant_memory.get("dueReminders", []) if isinstance(assistant_memory.get("dueReminders"), list) else []
    pending = assistant_memory.get("pendingReminders", []) if isinstance(assistant_memory.get("pendingReminders"), list) else []
    upcoming = assistant_memory.get("upcomingEvents", []) if isinstance(assistant_memory.get("upcomingEvents"), list) else []
    memory_recent = assistant_memory.get("recentActions", []) if isinstance(assistant_memory.get("recentActions"), list) else []
    if due or pending or upcoming or memory_recent:
        next_line = _safe_summary(memory_recent[0]) if memory_recent else ""
        if not next_line and pending:
            next_line = str(pending[0].get("title", "")).strip()
        agents.append(
            {
                "id": "local-schedule-live",
                "name": "Local Schedule",
                "role": f"{len(upcoming)} events / {len(pending)} reminders",
                "status": "attention" if due else ("running" if pending or upcoming else "ready"),
                "model": "local-memory",
                "progress": min(100, 24 + len(upcoming) * 12 + len(pending) * 10),
                "lastUpdate": next_line or "No schedule activity yet.",
            }
        )

    apps = external_channels.get("apps", {}) if isinstance(external_channels.get("apps"), dict) else {}
    mail = external_channels.get("mail", {}) if isinstance(external_channels.get("mail"), dict) else {}
    external_recent = external_channels.get("recentActions", []) if isinstance(external_channels.get("recentActions"), list) else []
    wechat = apps.get("wechatOfficial", {}) if isinstance(apps.get("wechatOfficial"), dict) else {}
    line = apps.get("line", {}) if isinstance(apps.get("line"), dict) else {}
    inbound_count = len(wechat.get("inbox", []) or []) + len(line.get("inbox", []) or []) + len(mail.get("inbox", []) or [])
    outbound_count = len(mail.get("outbox", []) or []) + len(wechat.get("outbox", []) or []) + len(line.get("outbox", []) or [])
    if inbound_count or outbound_count or external_recent:
        agents.append(
            {
                "id": "external-channels-live",
                "name": "External Channels",
                "role": f"{inbound_count} inbound / {outbound_count} outbound",
                "status": "running" if inbound_count or outbound_count else "ready",
                "model": "bridge",
                "progress": min(100, 26 + inbound_count * 10 + outbound_count * 8),
                "lastUpdate": _safe_summary(external_recent[0]) if external_recent else "External channels hub is idle.",
            }
        )

    if custom_agents or custom_recent:
        collecting = [item for item in custom_agents if item.get("status") in {"collecting", "review"}]
        completed = [item for item in custom_agents if item.get("status") == "complete"]
        latest_agent = custom_agents[0] if custom_agents else {}
        agents.append(
            {
                "id": "custom-agents-live",
                "name": "Custom Agents",
                "role": f"{len(custom_agents)} created / {len(completed)} complete",
                "status": "planning" if collecting else ("running" if custom_agents else "ready"),
                "model": "cortex",
                "progress": min(100, 20 + len(completed) * 15 + len(collecting) * 8),
                "lastUpdate": _safe_summary(custom_recent[0]) if custom_recent else str(latest_agent.get("name", "")).strip() or "No custom agents yet.",
            }
        )

    if study_agents or study_recent:
        collecting = [item for item in study_agents if item.get("status") in {"collecting", "review"}]
        completed = [item for item in study_agents if item.get("status") == "complete"]
        agents.append(
            {
                "id": "study-plan-live",
                "name": "Study Plan Agents",
                "role": f"{len(study_agents)} study units / {len(completed)} complete",
                "status": "planning" if collecting else ("running" if study_agents else "ready"),
                "model": "planner",
                "progress": min(100, 18 + len(study_agents) * 14),
                "lastUpdate": _safe_summary(study_recent[0]) if study_recent else "Study-plan agents are ready.",
            }
        )

    if features:
        feature_names = [str(item.get("name", "")).strip() for item in features[:3] if str(item.get("name", "")).strip()]
        agents.append(
            {
                "id": "feature-runtime-live",
                "name": "Feature Runtime",
                "role": f"{len(features)} loaded features",
                "status": "running" if features else "ready",
                "model": "runtime",
                "progress": min(100, 30 + len(features) * 8),
                "lastUpdate": " / ".join(feature_names) if feature_names else "No feature modules loaded.",
            }
        )

    return agents


def _build_live_timeline(context: dict, feature_payload: dict) -> list[dict]:
    timeline: list[dict] = []
    conversation = context.get("current_conversation", [])
    last_user = next((item for item in reversed(conversation) if item.get("speaker") == "You"), None)
    if last_user:
        timeline.append(
            {
                "id": f"conversation-{last_user.get('time', '')}",
                "time": str(last_user.get("time", "")).strip() or _safe_time(datetime.now().isoformat()),
                "title": "Incoming Request",
                "detail": str(last_user.get("text", "")).strip(),
                "stream": "conversation",
                "_sort": _parse_iso(last_user.get("createdAt")) or datetime.now(),
            }
        )

    route = context.get("last_voice_route") or {}
    if route:
        selected = route.get("selected") or {}
        timeline.append(
            {
                "id": "voice-route",
                "time": _safe_time(datetime.now().isoformat()),
                "title": f"Route: {route.get('kind', 'general')}",
                "detail": str(route.get("reasoning", "")).strip()
                or str(route.get("clarificationQuestion", "")).strip()
                or str(selected.get("featureName", "")).strip()
                or "Voice route updated.",
                "stream": "routing",
                "_sort": datetime.now(),
            }
        )

    sources = [
        ("assistantMemory", "recentActions", "Memory Update", "memory"),
        ("externalChannels", "recentActions", "External Channel", "external"),
        ("customAgentRecentActions", None, "Custom Agent", "agents"),
        ("studyPlanRecentActions", None, "Study Plan", "study"),
    ]
    for root_key, nested_key, title, stream in sources:
        if nested_key:
            root = feature_payload.get(root_key, {}) if isinstance(feature_payload.get(root_key), dict) else {}
            items = root.get(nested_key, []) if isinstance(root.get(nested_key), list) else []
        else:
            items = feature_payload.get(root_key, []) if isinstance(feature_payload.get(root_key), list) else []
        for item in items[:3]:
            summary = _safe_summary(item)
            if not summary:
                continue
            created_at = item.get("createdAt") or item.get("created_at") or ""
            timeline.append(
                {
                    "id": str(item.get("id", f"{stream}-{created_at}")),
                    "time": _safe_time(created_at),
                    "title": title,
                    "detail": summary,
                    "stream": stream,
                    "_sort": _parse_iso(created_at) or datetime.min,
                }
            )

    timeline.sort(key=lambda item: item.get("_sort") or datetime.min)
    for item in timeline:
        item.pop("_sort", None)
    return timeline[-12:]


def build_dashboard(context: dict) -> dict:
    provider_catalog = context["get_audio_provider_catalog"]()
    local_inventory = context["load_ollama_inventory"]()
    persisted_settings = context["persisted_settings"]
    stt_provider_id = persisted_settings["sttProvider"]
    tts_provider_id = persisted_settings["ttsProvider"]
    stt_provider = provider_catalog[stt_provider_id]
    tts_provider = provider_catalog[tts_provider_id]
    runtime = context["build_runtime_bridge"]()
    feature_payload = context["feature_manager"].dashboard_payload(persisted_settings["language"], runtime)
    voice_router = context["build_voice_router_snapshot"](persisted_settings["language"])
    features = context["feature_manager"].list_features(runtime)
    agents = _build_live_agents(context, feature_payload, features, persisted_settings["language"])
    timeline = _build_live_timeline(context, feature_payload)

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
        "features": features,
        "agentTypes": context["feature_manager"].list_agent_types(persisted_settings["language"], runtime),
        "bootstrap": context["bootstrap_snapshot"](),
        **voice_router,
        **feature_payload,
    }
