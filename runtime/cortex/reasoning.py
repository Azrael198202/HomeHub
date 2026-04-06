from __future__ import annotations

import re


TOPIC_HINTS = {
    "weather": ["天气", "weather", "rain", "forecast", "气温"],
    "travel": ["公园", "路上", "出行", "交通", "walk", "bike", "bus", "taxi"],
    "finance": ["账单", "消费", "扣费", "invoice", "receipt", "expense", "bill"],
    "schedule": ["日程", "提醒", "calendar", "schedule", "meeting", "todo"],
    "research": ["搜索", "联网", "official", "latest", "查一下", "lookup"],
}


def tokenize_topics(*parts: str) -> dict[str, int]:
    joined = " ".join(str(part or "").lower() for part in parts if part)
    scores: dict[str, int] = {}
    for topic, hints in TOPIC_HINTS.items():
        count = sum(1 for hint in hints if hint.lower() in joined)
        if count:
            scores[topic] = count
    return scores


def blueprint_digest(agent: dict) -> dict:
    profile = agent.get("profile", {}) if isinstance(agent.get("profile", {}), dict) else {}
    return {
        "mission": str(profile.get("goal", "")).strip(),
        "primaryUser": str(profile.get("primaryUser", "")).strip(),
        "trigger": str(profile.get("trigger", "")).strip(),
        "inputs": str(profile.get("inputs", "")).strip(),
        "output": str(profile.get("output", "")).strip(),
        "constraints": str(profile.get("constraints", "")).strip(),
        "networkEnabled": str(profile.get("allowNetworkLookup", "")).strip().lower() in {"yes", "true", "1", "on", "allow", "allowed"},
        "generatedFeatureId": str(agent.get("generatedFeatureId", "")).strip(),
    }


def apply_blueprint_signals(state: dict, agent: dict) -> None:
    digest = blueprint_digest(agent)
    state["agentName"] = str(agent.get("name", "")).strip() or state.get("agentName", "")
    state["blueprint"] = digest
    styles = state.setdefault("signals", {}).setdefault("workingStyle", {})
    if digest.get("trigger"):
        styles["proactive"] = int(styles.get("proactive", 0) or 0) + 1
    if digest.get("output"):
        styles["structured"] = int(styles.get("structured", 0) or 0) + 1
    if re.search(r"不要|必须|确认|禁止|do not|must|confirm", digest.get("constraints", ""), re.IGNORECASE):
        styles["cautious"] = int(styles.get("cautious", 0) or 0) + 1
    topics = tokenize_topics(
        digest.get("mission", ""),
        digest.get("inputs", ""),
        digest.get("output", ""),
        digest.get("trigger", ""),
    )
    topic_bucket = state.setdefault("signals", {}).setdefault("topics", {})
    for topic, count in topics.items():
        topic_bucket[topic] = max(int(topic_bucket.get(topic, 0) or 0), count)


def record_event_signals(state: dict, event_type: str, payload: dict) -> None:
    stats = state.setdefault("stats", {})
    stats["totalEvents"] = int(stats.get("totalEvents", 0) or 0) + 1
    if event_type in {"has_input", "no_input", "attachment_input", "network_lookup", "confirmed_run"}:
        stats["usageEvents"] = int(stats.get("usageEvents", 0) or 0) + 1
    if event_type in {"confirmed", "confirmed_run"}:
        stats["confirmations"] = int(stats.get("confirmations", 0) or 0) + 1
    if event_type == "network_lookup":
        stats["networkLookups"] = int(stats.get("networkLookups", 0) or 0) + 1
    if event_type == "attachment_input":
        stats["attachmentInputs"] = int(stats.get("attachmentInputs", 0) or 0) + 1
    message = str(payload.get("message", "")).strip()
    attachments = payload.get("attachments", []) if isinstance(payload.get("attachments", []), list) else []
    if message:
        stats["textInputs"] = int(stats.get("textInputs", 0) or 0) + 1
    if payload.get("ok") is True or event_type in {"has_input", "attachment_input", "confirmed_run"}:
        stats["successfulRuns"] = int(stats.get("successfulRuns", 0) or 0) + 1

    signals = state.setdefault("signals", {})
    input_modes = signals.setdefault("inputModes", {})
    tool_dependence = signals.setdefault("toolDependence", {})
    if message:
        input_modes["text"] = int(input_modes.get("text", 0) or 0) + 1
    if attachments:
        input_modes["image"] = int(input_modes.get("image", 0) or 0) + 1
    if event_type == "network_lookup":
        tool_dependence["network"] = int(tool_dependence.get("network", 0) or 0) + 1
    else:
        tool_dependence["local"] = int(tool_dependence.get("local", 0) or 0) + 1

    topics = tokenize_topics(message, str(payload.get("query", "")).strip(), str(payload.get("summary", "")).strip())
    topic_bucket = signals.setdefault("topics", {})
    for topic, count in topics.items():
        topic_bucket[topic] = int(topic_bucket.get(topic, 0) or 0) + count


def evolution_snapshot(state: dict) -> dict:
    stats = state.get("stats", {}) if isinstance(state.get("stats", {}), dict) else {}
    total_events = int(stats.get("totalEvents", 0) or 0)
    usage_events = int(stats.get("usageEvents", 0) or 0)
    confirmations = int(stats.get("confirmations", 0) or 0)
    network_lookups = int(stats.get("networkLookups", 0) or 0)
    attachment_inputs = int(stats.get("attachmentInputs", 0) or 0)
    successful_runs = int(stats.get("successfulRuns", 0) or 0)
    personalization = min(
        1.0,
        (
            total_events * 0.08
            + usage_events * 0.12
            + confirmations * 0.18
            + attachment_inputs * 0.08
            + successful_runs * 0.1
        ),
    )
    if usage_events >= 12 and confirmations >= 3 and successful_runs >= 8:
        stage = "specialized"
        readiness = "high"
        recommended = "personalized-routing"
        upgrade = "This agent has enough repeated behavior to justify a dedicated routing profile or distilled local policy."
    elif usage_events >= 6 and confirmations >= 2:
        stage = "adapting"
        readiness = "medium"
        recommended = "shared+memory"
        upgrade = "Keep accumulating traces and start routing this agent through its own memory profile before training anything."
    elif total_events >= 3:
        stage = "learning"
        readiness = "low"
        recommended = "shared"
        upgrade = "The agent is learning patterns, but it still needs more confirmed interactions before getting its own model path."
    else:
        stage = "seed"
        readiness = "low"
        recommended = "shared"
        upgrade = "Collect more confirmed interactions before specializing this agent."
    if network_lookups >= 4 and recommended != "personalized-routing":
        upgrade += " Network dependence is rising, so its source policy should be personalized next."
    return {
        "stageLabel": stage,
        "personalizationScore": round(personalization, 2),
        "ownModelReadiness": readiness,
        "recommendedBrain": recommended,
        "nextUpgrade": upgrade,
    }
