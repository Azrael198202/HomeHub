from __future__ import annotations

import json
from typing import Any, Callable


TaskSpec = dict[str, Any]


def detect_input_modes(user_text: str) -> list[str]:
    lowered = str(user_text or "").lower()
    modes = ["text"]
    if any(token in lowered for token in ["image", "photo", "screenshot", "receipt", "invoice", "picture"]) or any(
        token in user_text for token in ["图片", "照片", "截图", "账单图", "小票", "发票"]
    ):
        modes.append("image")
    if any(token in lowered for token in ["say", "voice", "speak", "audio"]) or any(token in user_text for token in ["语音", "说话", "听我"]):
        modes.append("voice")
    return sorted(set(modes))


def infer_task_spec_with_openai(
    user_text: str,
    locale: str,
    *,
    ai_available: bool,
    openai_chat_json: Callable[[str, str, str], dict[str, Any] | None],
) -> dict[str, Any] | None:
    if not ai_available:
        return None
    payload = openai_chat_json(
        (
            "You are HomeHub's task-spec parser. Return JSON only with keys: "
            "taskType, intent, urgency, requiresImage, requiresGeneration, requiresScheduling, "
            "requiresLongRunningAgent, preferredExecution, missingInfo, summary, confidence. "
            "Valid taskType values: agent_creation, reminder, schedule, bill_intake, general_chat, study_plan, ui_navigation, network_lookup, document_workflow. "
            "Valid urgency values: low, normal, high. "
            "Valid preferredExecution values: local, cloud, hybrid. "
            "Set confidence between 0 and 1."
        ),
        json.dumps({"locale": locale, "message": user_text}, ensure_ascii=False),
        "gpt-4o-mini",
    )
    return payload if isinstance(payload, dict) else None


def apply_rule_based_task_hints(spec: TaskSpec, user_text: str) -> TaskSpec:
    lowered = str(user_text or "").lower()
    if any(token in user_text for token in ["查询", "搜索", "查一下", "上网查", "联网查", "官网", "官方", "最新"]) or any(
        token in lowered for token in ["search", "lookup", "look up", "web", "online", "official", "latest", "news", "weather", "price"]
    ):
        spec.update(
            {
                "taskType": "network_lookup",
                "intent": "network-lookup",
                "summary": "Query approved external sources and return a sourced summary.",
                "preferredExecution": "hybrid",
            }
        )
    if any(token in user_text for token in ["智能体", "助手", "代理", "机器人"]) or any(
        token in lowered for token in ["agent", "assistant", "workflow", "bot"]
    ):
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
    if any(token in user_text for token in ["提醒", "闹钟"]) or "remind me" in lowered:
        spec.update(
            {
                "taskType": "reminder",
                "intent": "local-schedule",
                "summary": "Create or manage a reminder.",
                "requiresScheduling": True,
                "preferredExecution": "local",
            }
        )
    elif any(token in user_text for token in ["日程", "会议", "安排", "行程"]) or any(
        token in lowered for token in ["schedule", "calendar", "meeting"]
    ):
        spec.update(
            {
                "taskType": "schedule",
                "intent": "local-schedule",
                "summary": "Create or query an event or schedule.",
                "requiresScheduling": True,
                "preferredExecution": "local",
            }
        )
    if any(token in user_text for token in ["账单", "扣费", "发票", "小票", "收据"]) or any(
        token in lowered for token in ["bill", "receipt", "invoice", "charge", "expense"]
    ):
        spec.update(
            {
                "taskType": "bill_intake" if "image" in spec["inputModes"] else spec["taskType"],
                "summary": "Understand or track bills, receipts, or charge records.",
                "requiresImage": "image" in spec["inputModes"] or spec["requiresImage"],
                "preferredExecution": "hybrid",
            }
        )
    if any(token in user_text for token in ["OCR", "识别文字", "提取文字", "文档", "表格", "PPT", "幻灯片", "Excel", "表格文件", "Word", "文稿"]) or any(
        token in lowered for token in ["ocr", "extract text", "document", "table", "ppt", "powerpoint", "slides", "excel", "spreadsheet", "xlsx", "word", "docx"]
    ):
        spec.update(
            {
                "taskType": "document_workflow",
                "intent": "document-workflow",
                "summary": "Read, extract, or generate office-style documents such as OCR results, PowerPoint, Excel, or Word files.",
                "requiresImage": spec["requiresImage"] or any(token in lowered for token in ["ocr", "scan", "screenshot", "image", "photo"]),
                "requiresGeneration": True,
                "preferredExecution": "hybrid",
            }
        )
    if any(token in user_text for token in ["学习计划", "复习", "作业"]) or any(
        token in lowered for token in ["study plan", "homework", "revision plan"]
    ):
        spec.update(
            {
                "taskType": "study_plan",
                "intent": "study-plan-agent",
                "summary": "Create or continue a study plan agent workflow.",
                "requiresLongRunningAgent": True,
                "preferredExecution": "hybrid",
            }
        )
    if spec["taskType"] == "agent_creation":
        missing = []
        if not any(token in user_text for token in ["每", "每天", "每周", "每月", "收到", "上传", "定时"]) and not any(
            token in lowered for token in ["daily", "weekly", "monthly", "when", "trigger", "schedule"]
        ):
            missing.append("trigger")
        if not any(token in user_text for token in ["输出", "结果", "记录", "汇总", "提醒"]) and not any(
            token in lowered for token in ["output", "result", "summary", "record", "alert"]
        ):
            missing.append("output")
        spec["missingInfo"] = missing
    return spec


def build_task_spec(
    user_text: str,
    locale: str,
    *,
    detect_ui_action: Callable[[str, str], dict[str, Any] | None],
    infer_task_spec: Callable[[str, str], dict[str, Any] | None],
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

    ai_spec = infer_task_spec(user_text, locale)
    ai_used = False
    if ai_spec:
        task_type = str(ai_spec.get("taskType", "")).strip()
        try:
            confidence = float(ai_spec.get("confidence", 0.0) or 0.0)
        except (TypeError, ValueError):
            confidence = 0.0
        if task_type in {"agent_creation", "reminder", "schedule", "bill_intake", "general_chat", "study_plan", "ui_navigation", "network_lookup", "document_workflow"} and confidence >= 0.55:
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
    return spec
