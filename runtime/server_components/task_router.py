from __future__ import annotations

import json
import re
from typing import Any, Callable

try:
    from server_components.semantic_memory import infer_from_semantic_memory, query_semantic_memory
except ModuleNotFoundError:
    from runtime.server_components.semantic_memory import infer_from_semantic_memory, query_semantic_memory

try:
    from network_lookup_extensions import infer_network_task_spec
except ModuleNotFoundError:
    from runtime.network_lookup_extensions import infer_network_task_spec

try:
    from local_request_guard import looks_like_explicit_local_path_request
except ModuleNotFoundError:
    from runtime.local_request_guard import looks_like_explicit_local_path_request


TaskSpec = dict[str, Any]

ZH_NETWORK_TOKENS = [
    "\u67e5\u8be2",
    "\u641c\u7d22",
    "\u4e0a\u7f51",
    "\u8054\u7f51",
    "\u5b98\u7f51",
    "\u6700\u65b0",
    "\u65b0\u95fb",
    "\u4ef7\u683c",
]
ZH_AGENT_TOKENS = [
    "\u667a\u80fd\u4f53",
    "\u52a9\u624b",
    "\u673a\u5668\u4eba",
    "\u5de5\u4f5c\u6d41",
]
ZH_REMINDER_TOKENS = ["\u63d0\u9192", "\u95f9\u949f"]
ZH_SCHEDULE_TOKENS = ["\u65e5\u7a0b", "\u5b89\u6392", "\u4f1a\u8bae", "\u884c\u7a0b", "\u8ba1\u5212"]
ZH_BILL_TOKENS = ["\u8d26\u5355", "\u6536\u636e", "\u53d1\u7968", "\u6263\u8d39", "\u652f\u51fa", "\u8d39\u7528"]
ZH_DOCUMENT_TOKENS = [
    "OCR",
    "\u626b\u63cf",
    "\u8bc6\u522b\u6587\u5b57",
    "\u6587\u6863",
    "\u8868\u683c",
    "PPT",
    "Excel",
    "Word",
    "\u622a\u56fe",
    "\u56fe\u7247",
    "\u7167\u7247",
]
ZH_STUDY_TOKENS = ["\u5b66\u4e60\u8ba1\u5212", "\u4f5c\u4e1a", "\u590d\u4e60", "\u5b66\u4e60"]
ZH_TRAVEL_LOOKUP_TOKENS = ["\u673a\u7968", "\u822a\u73ed", "\u65b0\u5e72\u7ebf", "\u706b\u8f66\u7968", "\u9ad8\u94c1", "\u5217\u8f66", "\u7968\u4ef7", "\u8d39\u7528"]
ZH_GREETING_TOKENS = ["你好", "您好", "早上好", "晚上好", "嗨", "哈喽"]


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", str(text or "")))


def is_brief_greeting(user_text: str) -> bool:
    text = str(user_text or "").strip()
    lowered = text.lower()
    if not text:
        return False
    english = {"hi", "hello", "hey", "good morning", "good evening", "good afternoon"}
    if lowered in english or lowered.startswith("hello homehub") or lowered.startswith("hi homehub"):
        return True
    if len(text) <= 20 and any(token in text for token in ZH_GREETING_TOKENS):
        return True
    for separator in [":", "：", "\n"]:
        if separator in text:
            tail = text.split(separator, 1)[-1].strip()
            if tail and tail != text and is_brief_greeting(tail):
                return True
    return False


def detect_input_modes(user_text: str) -> list[str]:
    lowered = str(user_text or "").lower()
    raw = str(user_text or "")
    modes = ["text"]
    if any(token in lowered for token in ["image", "photo", "screenshot", "receipt", "invoice", "picture", "scan", "ocr", "document"]):
        modes.append("image")
    if any(token in raw for token in ["\u56fe\u7247", "\u7167\u7247", "\u622a\u56fe", "\u626b\u63cf", "\u53d1\u7968", "\u6536\u636e", "\u6587\u6863"]):
        modes.append("image")
    if any(token in lowered for token in ["say", "voice", "speak", "audio"]):
        modes.append("voice")
    if any(token in raw for token in ["\u8bed\u97f3", "\u97f3\u9891", "\u8bf4\u8bdd"]):
        modes.append("voice")
    return sorted(set(modes))


def infer_task_spec_with_openai(
    user_text: str,
    locale: str,
    semantic_examples: list[dict[str, Any]] | None = None,
    *,
    ai_available: bool,
    openai_chat_json: Callable[[str, str, str], dict[str, Any] | None],
) -> dict[str, Any] | None:
    if not ai_available:
        return None
    examples = semantic_examples if isinstance(semantic_examples, list) else []
    payload = openai_chat_json(
        (
            "You are HomeHub's task-spec parser. Return JSON only with keys: "
            "taskType, intent, urgency, requiresImage, requiresGeneration, requiresScheduling, "
            "requiresLongRunningAgent, preferredExecution, missingInfo, summary, confidence. "
            "Valid taskType values: agent_creation, reminder, schedule, bill_intake, general_chat, "
            "study_plan, ui_navigation, network_lookup, document_workflow, weather, time_query. "
            "Valid urgency values: low, normal, high. "
            "Valid preferredExecution values: local, cloud, hybrid. "
            "Set confidence between 0 and 1. "
            "You may receive similar resolved examples. Use them as semantic routing hints, not as rigid templates."
        ),
        json.dumps({"locale": locale, "message": user_text, "similarExamples": examples[:3]}, ensure_ascii=False),
        "gpt-4o-mini",
    )
    return payload if isinstance(payload, dict) else None


def build_semantic_route_examples(user_text: str, locale: str, limit: int = 3) -> list[dict[str, Any]]:
    examples: list[dict[str, Any]] = []
    for entry in query_semantic_memory(user_text, locale, limit=limit, threshold=0.12):
        item = entry.get("item", {}) if isinstance(entry.get("item", {}), dict) else {}
        task_spec = item.get("taskSpec", {}) if isinstance(item.get("taskSpec", {}), dict) else {}
        if not task_spec:
            continue
        examples.append(
            {
                "sourceText": str(item.get("sourceText", "")).strip(),
                "correctionText": str(item.get("correctionText", "")).strip(),
                "taskType": str(task_spec.get("taskType", "")).strip(),
                "intent": str(task_spec.get("intent", "")).strip(),
                "summary": str(task_spec.get("summary", "")).strip(),
                "preferredExecution": str(task_spec.get("preferredExecution", "")).strip(),
                "score": float(entry.get("score", 0.0) or 0.0),
            }
        )
    return examples


def apply_rule_based_task_hints(spec: TaskSpec, user_text: str) -> TaskSpec:
    lowered = str(user_text or "").lower()
    raw = str(user_text or "")
    travel_lookup = any(token in raw for token in ZH_TRAVEL_LOOKUP_TOKENS) or any(
        token in lowered for token in ["flight", "airfare", "ticket", "plane", "shinkansen", "train", "rail fare"]
    )

    if any(token in lowered for token in ["weather", "forecast", "temperature", "rain"]) or any(
        token in raw for token in ["\u5929\u6c14", "\u6c14\u6e29", "\u964d\u96e8", "\u4e0b\u96e8", "\u9884\u62a5", "\u5929\u6c17"]
    ):
        spec.update(
            {
                "taskType": "weather",
                "intent": "weather-query",
                "summary": "Get the latest local weather from the current device location or saved location.",
                "preferredExecution": "local",
            }
        )

    if spec["taskType"] != "weather" and (
        travel_lookup
        or
        any(token in lowered for token in ["search", "lookup", "look up", "web", "online", "official", "latest", "news", "price"]) or any(
        token in raw for token in ZH_NETWORK_TOKENS
        )
    ):
        spec.update(
            {
                "taskType": "network_lookup",
                "intent": "network-lookup",
                "summary": "Query approved external sources and return a sourced summary.",
                "preferredExecution": "hybrid",
            }
        )

    if any(token in lowered for token in ["agent", "assistant", "workflow", "bot"]) or any(token in raw for token in ZH_AGENT_TOKENS):
        spec.update(
            {
                "taskType": "agent_creation",
                "intent": "custom-agent-builder",
                "summary": "Create, refine, or activate a long-running HomeHub agent.",
                "requiresGeneration": True,
                "requiresLongRunningAgent": True,
                "preferredExecution": "hybrid",
            }
        )

    if "remind me" in lowered or any(token in lowered for token in ["reminder", "remind", "alarm"]) or any(token in raw for token in ZH_REMINDER_TOKENS):
        spec.update(
            {
                "taskType": "reminder",
                "intent": "local-schedule",
                "summary": "Create or manage a reminder.",
                "requiresScheduling": True,
                "preferredExecution": "local",
            }
        )

    if not travel_lookup and (any(token in lowered for token in ["schedule", "calendar", "meeting", "event"]) or any(token in raw for token in ZH_SCHEDULE_TOKENS)):
        spec.update(
            {
                "taskType": "schedule",
                "intent": "local-schedule",
                "summary": "Create or query an event or schedule.",
                "requiresScheduling": True,
                "preferredExecution": "local",
            }
        )

    if spec["taskType"] != "agent_creation" and (
        any(token in lowered for token in ["bill", "receipt", "invoice", "charge", "expense"]) or any(token in raw for token in ZH_BILL_TOKENS)
    ):
        spec.update(
            {
                "taskType": "bill_intake" if "image" in spec["inputModes"] else spec["taskType"],
                "summary": "Understand or track bills, receipts, or charge records.",
                "requiresImage": "image" in spec["inputModes"] or spec["requiresImage"],
                "preferredExecution": "hybrid",
            }
        )

    if spec["taskType"] != "agent_creation" and (
        any(token in lowered for token in ["ocr", "extract text", "document", "table", "ppt", "powerpoint", "slides", "excel", "spreadsheet", "xlsx", "word", "docx"]) or any(
            token in raw for token in ZH_DOCUMENT_TOKENS
        )
    ):
        spec.update(
            {
                "taskType": "document_workflow",
                "intent": "document-workflow",
                "summary": "Read, extract, or generate office-style documents such as OCR results, PowerPoint, Excel, or Word files.",
                "requiresImage": spec["requiresImage"] or any(token in lowered for token in ["ocr", "scan", "screenshot", "image", "photo"]) or any(
                    token in raw for token in ["\u56fe\u7247", "\u7167\u7247", "\u622a\u56fe", "\u626b\u63cf"]
                ),
                "requiresGeneration": True,
                "preferredExecution": "hybrid",
            }
        )

    if spec["taskType"] == "agent_creation":
        missing = []
        if not any(token in lowered for token in ["daily", "weekly", "monthly", "when", "trigger", "schedule"]) and not any(
            token in raw for token in ["\u6bcf\u5929", "\u6bcf\u5468", "\u6bcf\u6708", "\u4ec0\u4e48\u65f6\u5019", "\u89e6\u53d1", "\u5b9a\u65f6"]
        ):
            missing.append("trigger")
        if not any(token in lowered for token in ["output", "result", "summary", "record", "alert"]) and not any(
            token in raw for token in ["\u8f93\u51fa", "\u7ed3\u679c", "\u603b\u7ed3", "\u8bb0\u5f55", "\u63d0\u9192"]
        ):
            missing.append("output")
        spec["missingInfo"] = missing
    return spec


def build_task_spec(
    user_text: str,
    locale: str,
    *,
    detect_ui_action: Callable[[str, str], dict[str, Any] | None],
    infer_task_spec: Callable[[str, str, list[dict[str, Any]]], dict[str, Any] | None],
) -> TaskSpec:
    spec: TaskSpec = {
        "taskType": "general_chat",
        "intent": "general-chat",
        "summary": "General household conversation or Q&A.",
        "urgency": "normal",
        "inputModes": detect_input_modes(user_text),
        "requiresImage": False,
        "requiresGeneration": False,
        "requiresScheduling": False,
        "requiresLongRunningAgent": False,
        "preferredExecution": "hybrid",
        "missingInfo": [],
    }
    if detect_ui_action(user_text, locale):
        spec.update(
            {
                "taskType": "ui_navigation",
                "intent": "ui-action",
                "summary": "Navigate the TV shell UI directly.",
                "preferredExecution": "local",
            }
        )
        return spec

    if is_brief_greeting(user_text):
        spec.update(
            {
                "taskType": "general_chat",
                "intent": "general-chat",
                "summary": "Short greeting or casual household conversation.",
                "preferredExecution": "local",
                "reasoning": "greeting-guard",
            }
        )
        return spec

    if looks_like_explicit_local_path_request(user_text):
        spec.update(
            {
                "taskType": "document_workflow",
                "intent": "local-file-request",
                "summary": "Inspect, read, classify, or manage local files and folders on this device.",
                "preferredExecution": "local",
                "reasoning": "local-request-guard",
            }
        )
        return spec

    direct_spec = apply_rule_based_task_hints(dict(spec), user_text)
    if direct_spec.get("taskType") in {"weather", "time_query", "reminder", "schedule"}:
        return direct_spec

    semantic_network_spec = infer_network_task_spec(user_text)
    if isinstance(semantic_network_spec, dict):
        spec["taskType"] = str(semantic_network_spec.get("taskType", spec["taskType"])).strip() or spec["taskType"]
        spec["intent"] = str(semantic_network_spec.get("intent", spec["intent"])).strip() or spec["intent"]
        spec["summary"] = str(semantic_network_spec.get("summary", spec["summary"])).strip() or spec["summary"]
        preferred = str(semantic_network_spec.get("preferredExecution", spec["preferredExecution"])).strip()
        if preferred in {"local", "cloud", "hybrid"}:
            spec["preferredExecution"] = preferred
        spec["reasoning"] = "semantic-network-route-memory"
        return spec

    memory_spec = infer_from_semantic_memory(user_text, locale)
    if memory_spec:
        spec["taskType"] = str(memory_spec.get("taskType", spec["taskType"])).strip() or spec["taskType"]
        spec["intent"] = str(memory_spec.get("intent", spec["intent"])).strip() or spec["intent"]
        spec["summary"] = str(memory_spec.get("summary", spec["summary"])).strip() or spec["summary"]
        spec["requiresImage"] = bool(memory_spec.get("requiresImage", spec["requiresImage"]))
        spec["requiresGeneration"] = bool(memory_spec.get("requiresGeneration", spec["requiresGeneration"]))
        spec["requiresScheduling"] = bool(memory_spec.get("requiresScheduling", spec["requiresScheduling"]))
        spec["requiresLongRunningAgent"] = bool(memory_spec.get("requiresLongRunningAgent", spec["requiresLongRunningAgent"]))
        preferred = str(memory_spec.get("preferredExecution", spec["preferredExecution"])).strip()
        if preferred in {"local", "cloud", "hybrid"}:
            spec["preferredExecution"] = preferred
        if isinstance(memory_spec.get("missingInfo"), list):
            spec["missingInfo"] = [str(item).strip() for item in memory_spec.get("missingInfo", []) if str(item).strip()]
        spec["reasoning"] = str(memory_spec.get("reasoning", "semantic-memory-match")).strip() or "semantic-memory-match"
        return spec

    semantic_examples = build_semantic_route_examples(user_text, locale)
    ai_spec = infer_task_spec(user_text, locale, semantic_examples)
    ai_used = False
    if ai_spec:
        task_type = str(ai_spec.get("taskType", "")).strip()
        try:
            confidence = float(ai_spec.get("confidence", 0.0) or 0.0)
        except (TypeError, ValueError):
            confidence = 0.0
        if task_type in {"agent_creation", "reminder", "schedule", "bill_intake", "general_chat", "study_plan", "ui_navigation", "network_lookup", "document_workflow", "weather", "time_query"} and confidence >= 0.55:
            spec["taskType"] = task_type
            spec["intent"] = str(ai_spec.get("intent", spec["intent"])).strip() or spec["intent"]
            spec["summary"] = str(ai_spec.get("summary", spec["summary"])).strip() or spec["summary"]
            if str(ai_spec.get("urgency", "")).strip() in {"low", "normal", "high"}:
                spec["urgency"] = str(ai_spec.get("urgency")).strip()
            spec["requiresImage"] = bool(ai_spec.get("requiresImage", spec["requiresImage"]))
            spec["requiresGeneration"] = bool(ai_spec.get("requiresGeneration", spec["requiresGeneration"]))
            spec["requiresScheduling"] = bool(ai_spec.get("requiresScheduling", spec["requiresScheduling"]))
            spec["requiresLongRunningAgent"] = bool(ai_spec.get("requiresLongRunningAgent", spec["requiresLongRunningAgent"]))
            preferred = str(ai_spec.get("preferredExecution", spec["preferredExecution"])).strip()
            if preferred in {"local", "cloud", "hybrid"}:
                spec["preferredExecution"] = preferred
            if isinstance(ai_spec.get("missingInfo"), list):
                spec["missingInfo"] = [str(item).strip() for item in ai_spec.get("missingInfo", []) if str(item).strip()]
            ai_used = True
    if not ai_used:
        spec = apply_rule_based_task_hints(spec, user_text)
        if semantic_examples:
            spec["reasoning"] = "semantic-example-assisted-rules"
    elif semantic_examples:
        spec["reasoning"] = "semantic-example-assisted-ai"
    return spec
