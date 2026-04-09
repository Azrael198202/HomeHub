from __future__ import annotations

from datetime import datetime
from typing import Any


def normalize_resolution_reply(reply_value: Any, fallback: str) -> str:
    text = str(reply_value if reply_value is not None else "").strip()
    if not text or text.lower() in {"none", "null", "undefined"}:
        return str(fallback or "").strip()
    return text


def is_simple_greeting(text: str) -> bool:
    normalized = str(text or "").strip().lower()
    return normalized in {
        "你好",
        "您好",
        "嗨",
        "hi",
        "hello",
        "hey",
        "早上好",
        "下午好",
        "晚上好",
        "good morning",
        "good afternoon",
        "good evening",
    }


def maybe_resolve_autonomous_agent_request(user_text, locale, runtime, route, context: dict[str, Any]) -> dict[str, Any] | None:
    feature = context["feature_manager"].get_feature("custom-agents", runtime)
    if feature is None or not hasattr(feature, "maybe_autonomous_agent_response"):
        return None
    normalized = str(user_text or "").strip().lower()
    if normalized in {
        "你好",
        "您好",
        "嗨",
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "こんばんは",
        "おはよう",
    }:
        return None
    task_spec = route.get("taskSpec", {}) if isinstance(route.get("taskSpec", {}), dict) else {}
    task_type = str(task_spec.get("taskType", "general_chat")).strip() or "general_chat"
    if task_type in {"weather", "clock", "time_query"}:
        return None
    handler = getattr(feature, "maybe_autonomous_agent_response", None)
    if not callable(handler):
        return None
    result = handler(
        user_text,
        locale,
        runtime,
        task_type=task_type,
        requires_network=True,
        attachments=[],
    )
    return result if isinstance(result, dict) else None


def should_attempt_default_network_research(route) -> bool:
    task_spec = route.get("taskSpec", {}) if isinstance(route.get("taskSpec", {}), dict) else {}
    cortex = route.get("cortex", {}) if isinstance(route.get("cortex", {}), dict) else {}
    cortex_should_network = bool(cortex.get("shouldNetwork")) or bool(((cortex.get("decisionHints") or {}).get("requireSearch")))
    task_type = str(task_spec.get("taskType", "general_chat")).strip() or "general_chat"
    kind = str(route.get("kind", "")).strip()
    if task_type in {"weather", "clock", "time_query", "ui_navigation", "reminder", "schedule"}:
        return False
    if cortex_should_network:
        return True
    return kind in {"general", "agent_factory"} or task_type in {
        "general_chat",
        "agent_creation",
        "document_workflow",
        "study_plan",
        "bill_intake",
        "network_lookup",
    }


def resolve_voice_request(user_text, locale, context: dict[str, Any]) -> dict[str, Any]:
    runtime = context["build_runtime_bridge"]()
    original_text = user_text
    combined_text = user_text
    clarification_context = context["get_pending_voice_clarification"]()
    if is_simple_greeting(original_text) and not clarification_context:
        reply = (
            "你好，有什么可以帮忙的？"
            if locale == "zh-CN"
            else ("こんにちは。何をお手伝いしましょうか？" if locale == "ja-JP" else "Hello, how can I help?")
        )
        return {
            "reply": normalize_resolution_reply(reply, "你好，有什么可以帮忙的？" if locale == "zh-CN" else "Hello, how can I help?"),
            "route": {
                "kind": "general",
                "selected": {
                    "intent": "general-chat",
                    "featureId": "homehub-core",
                    "featureName": "HomeHub Core",
                    "action": "general_reply",
                    "score": 0.99,
                },
                "candidates": [],
                "reasoning": "Detected a simple greeting and kept the response local.",
                "taskSpec": {
                    "taskType": "general_chat",
                    "summary": "Simple greeting exchange.",
                },
            },
            "pendingClarification": None,
            "uiAction": None,
        }
    ui_action = context["detect_ui_action"](original_text, locale)
    text_lower = str(original_text or "").lower()
    network_hint = any(token in original_text for token in ["查询", "搜索", "查一下", "上网查", "联网查", "官网", "官方网站", "官方消息", "最新消息", "最新新闻"]) or any(
        token in text_lower for token in ["search", "lookup", "look up", "official website", "latest news", "breaking news", "web search", "online search"]
    )

    if ui_action and not clarification_context:
        context["clear_pending_voice_clarification"]()
        return {
            "reply": context["build_ui_action_reply"](ui_action, locale),
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
        runtime_strategy = context["build_runtime_strategy"](context["load_ollama_inventory"]())
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
            "toolPlan": context["build_tool_plan"](task_spec, {"selected": {"featureId": "homehub-core"}}),
            "modelRoute": context["select_model_route"](task_spec, runtime_strategy, {"installed": runtime_strategy.get("localDetected", [])}),
        }
        lookup_result = context["perform_autonomous_network_lookup"](original_text, locale, "official-only")
        if not lookup_result.get("ok"):
            fallback_reply = context["build_general_voice_reply"](original_text, locale, route.get("modelRoute"))
            return {
                "reply": fallback_reply,
                "route": context["serialize_voice_route"](route),
                "pendingClarification": None,
                "uiAction": None,
                "lookupResult": lookup_result,
            }
        return {
            "reply": context["build_grounded_network_reply"](original_text, lookup_result, locale),
            "route": context["serialize_voice_route"](route),
            "pendingClarification": None,
            "uiAction": None,
            "lookupResult": lookup_result,
        }

    if clarification_context:
        combined_text = (
            f"Original request: {clarification_context.get('originalRequest', '')}\n"
            f"Clarification answer: {user_text}"
        )

    route = context["route_voice_request"](combined_text, locale)
    lookup_result = None
    ui_action = None

    if route.get("kind") == "clarify":
        pending = {
            "originalRequest": clarification_context.get("originalRequest", original_text) if clarification_context else original_text,
            "latestUserMessage": original_text,
            "clarificationQuestion": context["build_clarification_reply"](route, locale),
            "selected": route.get("selected"),
            "createdAt": datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes"),
        }
        context["set_pending_voice_clarification"](pending)
        return {
            "reply": pending["clarificationQuestion"],
            "route": context["serialize_voice_route"](route),
            "pendingClarification": context["build_pending_clarification_snapshot"](),
        }

    if clarification_context:
        context["learn_from_clarification"](clarification_context, route, combined_text, locale, user_text)

    fallback_reply = context["build_general_voice_reply"](combined_text if clarification_context else original_text, locale, route.get("modelRoute"))

    if route.get("kind") == "feature":
        result = context["feature_manager"].dispatch_voice_intent(route, combined_text, locale, runtime) or {}
        reply = normalize_resolution_reply(result.get("reply"), fallback_reply)
        ui_action = result.get("uiAction")
        artifacts = result.get("artifacts", [])
    elif (route.get("taskSpec") or {}).get("taskType") == "weather":
        reply = normalize_resolution_reply(context["build_weather_reply"](combined_text if clarification_context else original_text, locale), fallback_reply)
        artifacts = []
    elif (route.get("taskSpec") or {}).get("taskType") == "network_lookup":
        lookup_result = context["perform_autonomous_network_lookup"](combined_text if clarification_context else original_text, locale, "official-only")
        if not lookup_result.get("ok"):
            reply = fallback_reply
        else:
            reply = normalize_resolution_reply(context["build_grounded_network_reply"](combined_text if clarification_context else original_text, lookup_result, locale), fallback_reply)
        artifacts = []
    elif route.get("kind") == "agent_factory":
        autonomous = maybe_resolve_autonomous_agent_request(combined_text if clarification_context else original_text, locale, runtime, route, context)
        if autonomous:
            reply = normalize_resolution_reply(autonomous.get("reply"), context["build_agent_factory_reply"](locale))
            ui_action = autonomous.get("uiAction")
            artifacts = autonomous.get("artifacts", [])
        else:
            lookup_result = context["perform_autonomous_network_lookup"](combined_text if clarification_context else original_text, locale, "official-only")
            reply = normalize_resolution_reply(
                context["build_grounded_network_reply"](combined_text if clarification_context else original_text, lookup_result, locale) if lookup_result.get("ok") else "",
                context["build_agent_factory_reply"](locale),
            )
            artifacts = []
    else:
        autonomous = maybe_resolve_autonomous_agent_request(combined_text if clarification_context else original_text, locale, runtime, route, context)
        if autonomous:
            reply = normalize_resolution_reply(autonomous.get("reply"), fallback_reply)
            ui_action = autonomous.get("uiAction")
            artifacts = autonomous.get("artifacts", [])
        else:
            if should_attempt_default_network_research(route):
                lookup_result = context["perform_autonomous_network_lookup"](combined_text if clarification_context else original_text, locale, "official-only")
            reply = normalize_resolution_reply((
                context["build_grounded_network_reply"](combined_text if clarification_context else original_text, lookup_result, locale)
                if lookup_result and lookup_result.get("ok")
                else fallback_reply
            ), fallback_reply)
            artifacts = []

    context["clear_pending_voice_clarification"]()
    return {
        "reply": normalize_resolution_reply(reply, fallback_reply),
        "route": context["serialize_voice_route"](route),
        "pendingClarification": None,
        "uiAction": ui_action,
        "lookupResult": lookup_result,
        "artifacts": artifacts,
    }


def build_voice_router_snapshot(locale, context: dict[str, Any]) -> dict[str, Any]:
    runtime = context["build_runtime_bridge"]()
    features = context["feature_manager"].list_features(runtime)
    return {
        "pendingVoiceClarification": context["build_pending_clarification_snapshot"](),
        "toolRegistry": context["build_tool_registry_snapshot"](),
        "featureIntents": [
            {
                "featureId": item.get("id"),
                "featureName": item.get("name"),
                "intents": item.get("voiceIntents", []),
            }
            for item in features
            if item.get("voiceIntents")
        ],
    }


def default_last_voice_route() -> dict[str, Any]:
    return {
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


def generate_assistant_reply(user_text, locale, context: dict[str, Any]) -> str:
    return resolve_voice_request(user_text, locale, context)["reply"]


def build_last_voice_route(user_text, locale, context: dict[str, Any]) -> dict[str, Any]:
    return context["serialize_voice_route"](context["route_voice_request"](user_text, locale))
