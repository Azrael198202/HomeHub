from __future__ import annotations

import re
from datetime import datetime
from typing import Any

from runtime.network_lookup_extensions import (
    lookup_from_source_references,
    remember_lookup_sources,
    should_attempt_source_reference_lookup,
)
from runtime.voice_route_guards import should_block_network_for_local_request


def normalize_resolution_reply(reply_value: Any, fallback: str) -> str:
    text = str(reply_value if reply_value is not None else "").strip()
    if not text or text.lower() in {"none", "null", "undefined"}:
        return str(fallback or "").strip()
    return text


def is_simple_greeting(text: str) -> bool:
    normalized = re.sub(r"[，。！？!?,.\s]+", "", str(text or "").strip().lower())
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
        "goodmorning",
        "goodafternoon",
        "goodevening",
    }


def is_information_request(text: str) -> bool:
    value = str(text or "").strip()
    lowered = value.lower()
    if not value:
        return False
    if any(token in value for token in ["？", "?", "什么", "怎么", "如何", "多少", "几点", "哪里", "哪儿", "哪", "谁", "为何", "为什么", "多久"]):
        return True
    return any(
        token in lowered
        for token in ["what", "how", "why", "when", "where", "who", "which", "how much", "how many", "can you find", "look up"]
    )


def reply_looks_incomplete(reply_text: str) -> bool:
    text = str(reply_text or "").strip()
    lowered = text.lower()
    if not text:
        return True
    weak_phrases = [
        "你可以直接告诉我你想做什么",
        "比如问问题、创建日程、添加提醒",
        "可以直接告诉我你想做什么",
        "i can help you create",
        "just tell me what you need",
        "how can i help",
        "请稍后重试",
        "没有返回可用结果",
        "需要更具体",
        "请补充",
        "could not find",
        "did not return usable results",
        "try again",
    ]
    return any(token in text or token in lowered for token in weak_phrases)


def should_promote_to_network(user_text: str, route: dict[str, Any], reply_text: str) -> bool:
    task_spec = route.get("taskSpec", {}) if isinstance(route.get("taskSpec", {}), dict) else {}
    task_type = str(task_spec.get("taskType", "general_chat")).strip() or "general_chat"
    if task_type in {"weather", "time_query", "clock", "reminder", "schedule", "ui_navigation", "agent_creation"}:
        return False
    if str(route.get("kind", "")).strip() == "feature":
        return False
    if not is_information_request(user_text):
        return False
    return reply_looks_incomplete(reply_text)


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
    if context["looks_like_local_file_request"](user_text):
        return None
    selected = route.get("selected", {}) if isinstance(route.get("selected", {}), dict) else {}
    if str(selected.get("featureId", "")).strip() in {"local-files", "custom-agents"}:
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


def is_probably_realtime_request(user_text: str, route: dict[str, Any]) -> bool:
    text = str(user_text or "").strip()
    lowered = text.lower()
    task_spec = route.get("taskSpec", {}) if isinstance(route.get("taskSpec", {}), dict) else {}
    task_type = str(task_spec.get("taskType", "general_chat")).strip() or "general_chat"
    if task_type == "weather":
        return True
    realtime_tokens = [
        "latest",
        "today",
        "news",
        "price",
        "current",
        "stock",
        "forecast",
        "breaking",
        "recent",
        "weather",
        "today's",
        "price",
        "fare",
        "ticket",
        "flight",
        "train",
        "shinkansen",
        "macbook air price",
        "macbook pro price",
    ]
    if any(token in lowered for token in realtime_tokens):
        return True
    return any(token in text for token in ["最新", "今天", "今日", "新闻", "价格", "票价", "费用", "天气", "现在", "实时", "株価", "机票", "火车票", "新干线"])


def should_attempt_knowledge_lookup(user_text: str, route: dict[str, Any]) -> bool:
    if not is_information_request(user_text):
        return False
    if is_probably_realtime_request(user_text, route):
        return False
    if str(route.get("kind", "")).strip() == "feature":
        return False
    task_spec = route.get("taskSpec", {}) if isinstance(route.get("taskSpec", {}), dict) else {}
    task_type = str(task_spec.get("taskType", "general_chat")).strip() or "general_chat"
    return task_type in {"general_chat", "document_workflow", "study_plan", "bill_intake", "agent_creation"}


def build_knowledge_reply(items: list[dict[str, Any]], locale: str) -> str:
    if not items:
        return ""
    top = items[0] if isinstance(items[0], dict) else {}
    summary = str(top.get("summary", "")).strip()
    source = str(top.get("source", "")).strip()
    title = str(top.get("title", "")).strip()
    if locale == "zh-CN":
        if source and title:
            return f"根据本地知识库里的已整理信息，{summary} 来源：{title} ({source})。"
        return f"根据本地知识库里的已整理信息，{summary}"
    if locale == "ja-JP":
        if source and title:
            return f"ローカル知識メモリの整理済み情報では、{summary} 出典: {title} ({source})。"
        return f"ローカル知識メモリの整理済み情報では、{summary}"
    if source and title:
        return f"Based on HomeHub's local knowledge memory: {summary} Source: {title} ({source})."
    return f"Based on HomeHub's local knowledge memory: {summary}"


def resolve_voice_request(user_text, locale, context: dict[str, Any]) -> dict[str, Any]:
    runtime = context["build_runtime_bridge"]()
    original_text = user_text
    combined_text = user_text
    execution_context = context["create_execution_context"](original_text, locale)
    clarification_context = context["get_pending_voice_clarification"]()
    if is_simple_greeting(original_text) and not clarification_context:
        reply = (
            "你好，有什么可以帮忙的？"
            if locale == "zh-CN"
            else ("こんにちは。何をお手伝いしましょうか？" if locale == "ja-JP" else "Hello, how can I help?")
        )
        route_payload = {
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
        }
        return {
            "reply": normalize_resolution_reply(reply, "你好，有什么可以帮忙的？" if locale == "zh-CN" else "Hello, how can I help?"),
            "route": route_payload,
            "pendingClarification": None,
            "uiAction": None,
        }
    ui_action = context["detect_ui_action"](original_text, locale)

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

    if clarification_context:
        combined_text = (
            f"Original request: {clarification_context.get('originalRequest', '')}\n"
            f"Clarification answer: {user_text}"
        )

    route = context["route_voice_request"](combined_text, locale)
    execution_context.set_route_payload(route)
    lookup_result = None
    ui_action = None
    research_packet = None
    knowledge_hits: list[dict[str, Any]] = []

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

    effective_text = combined_text if clarification_context else original_text
    fallback_reply = context["build_general_voice_reply"](combined_text if clarification_context else original_text, locale, route.get("modelRoute"))
    block_network_for_local_request = should_block_network_for_local_request(effective_text, route, context["looks_like_local_file_request"])

    source_reference_lookup = None
    if not block_network_for_local_request and should_attempt_knowledge_lookup(effective_text, route):
        knowledge_hits = context["query_knowledge_memory"](effective_text, 3, 0.2)
        execution_context.add_knowledge(knowledge_hits)
    if not block_network_for_local_request and should_attempt_source_reference_lookup(effective_text, route, knowledge_hits, is_information_request):
        source_reference_lookup = lookup_from_source_references(effective_text, context)
        if source_reference_lookup:
            execution_context.add_tool_result(
                {
                    "tool": "source_reference_lookup",
                    "ok": True,
                    "query": effective_text,
                    "count": len(source_reference_lookup.get("sourceReferenceHits", [])),
                }
            )

    if route.get("kind") == "feature":
        result = context["feature_manager"].dispatch_voice_intent(route, combined_text, locale, runtime) or {}
        reply = normalize_resolution_reply(result.get("reply"), fallback_reply)
        ui_action = result.get("uiAction")
        artifacts = result.get("artifacts", [])
    elif (route.get("taskSpec") or {}).get("taskType") == "weather":
        if source_reference_lookup and source_reference_lookup.get("ok"):
            lookup_result = source_reference_lookup
        else:
            hints = context["infer_research_hints"](effective_text)
            research_packet = context["perform_research_lookup"](
                effective_text,
                locale,
                "official-only",
                hints.get("preferredSources"),
                hints.get("allowedDomains"),
            )
            lookup_result = research_packet
        if lookup_result.get("ok"):
            reply = normalize_resolution_reply(context["build_grounded_network_reply"](effective_text, lookup_result, locale), fallback_reply)
        else:
            reply = normalize_resolution_reply(context["build_weather_reply"](combined_text if clarification_context else original_text, locale), fallback_reply)
        artifacts = []
    elif (route.get("taskSpec") or {}).get("taskType") == "network_lookup":
        if source_reference_lookup and source_reference_lookup.get("ok"):
            lookup_result = source_reference_lookup
        else:
            hints = context["infer_research_hints"](effective_text)
            if is_probably_realtime_request(effective_text, route):
                lookup_result = context["perform_autonomous_network_lookup"](
                    effective_text,
                    locale,
                    "official-only",
                    hints.get("preferredSources"),
                    hints.get("allowedDomains"),
                )
            else:
                research_packet = context["perform_research_lookup"](
                    effective_text,
                    locale,
                    "official-only",
                    hints.get("preferredSources"),
                    hints.get("allowedDomains"),
                )
                lookup_result = research_packet
        if not lookup_result.get("ok"):
            reply = context["build_network_unavailable_reply"](combined_text if clarification_context else original_text, locale, "network_lookup")
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
        elif knowledge_hits:
            reply = normalize_resolution_reply(build_knowledge_reply(knowledge_hits, locale), fallback_reply)
            artifacts = []
        else:
            if not block_network_for_local_request and should_attempt_default_network_research(route):
                if source_reference_lookup and source_reference_lookup.get("ok"):
                    lookup_result = source_reference_lookup
                else:
                    hints = context["infer_research_hints"](effective_text)
                    research_packet = context["perform_research_lookup"](
                        effective_text,
                        locale,
                        "official-only",
                        hints.get("preferredSources"),
                        hints.get("allowedDomains"),
                    )
                    lookup_result = research_packet
            reply = normalize_resolution_reply((
                context["build_grounded_network_reply"](combined_text if clarification_context else original_text, lookup_result, locale)
                if lookup_result and lookup_result.get("ok")
                else fallback_reply
            ), fallback_reply)
            artifacts = []

    if not block_network_for_local_request and should_promote_to_network(effective_text, route, reply):
        if source_reference_lookup and source_reference_lookup.get("ok"):
            lookup_result = source_reference_lookup
        else:
            hints = context["infer_research_hints"](effective_text)
            research_packet = context["perform_research_lookup"](
                effective_text,
                locale,
                "official-only",
                hints.get("preferredSources"),
                hints.get("allowedDomains"),
            )
            lookup_result = research_packet
        if lookup_result.get("ok"):
            reply = normalize_resolution_reply(context["build_grounded_network_reply"](effective_text, lookup_result, locale), reply)
        elif should_attempt_default_network_research(route):
            reply = normalize_resolution_reply(context["build_network_unavailable_reply"](effective_text, locale, "network_lookup"), reply)

    remember_lookup_sources(effective_text, lookup_result, context, execution_context)

    if isinstance(research_packet, dict):
        execution_context.add_evidence(research_packet.get("evidence", []))
        execution_context.add_tool_result({"tool": "research_lookup", "ok": bool(research_packet.get("ok")), "query": effective_text})
        if research_packet.get("ok") and not is_probably_realtime_request(effective_text, route):
            for item in context["evidence_to_knowledge_items"](research_packet):
                remembered = context["remember_knowledge_item"](item)
                if remembered:
                    execution_context.memory_writeback.setdefault("knowledgeItems", []).append(remembered)
    if knowledge_hits:
        execution_context.add_tool_result({"tool": "knowledge_lookup", "ok": True, "count": len(knowledge_hits), "query": effective_text})
    execution_context.artifacts = artifacts if isinstance(artifacts, list) else []
    execution_context.add_conclusion(reply)

    context["clear_pending_voice_clarification"]()
    recorder = context.get("record_route_semantic_example")
    if callable(recorder):
        source_text = (
            str((clarification_context or {}).get("originalRequest", "")).strip()
            if clarification_context
            else str(original_text or "").strip()
        )
        if source_text:
            recorder(source_text, locale, route)
    return {
        "reply": normalize_resolution_reply(reply, fallback_reply),
        "route": context["serialize_voice_route"](route),
        "pendingClarification": None,
        "uiAction": ui_action,
        "lookupResult": lookup_result,
        "artifacts": artifacts,
        "executionContext": execution_context.to_dict(),
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
