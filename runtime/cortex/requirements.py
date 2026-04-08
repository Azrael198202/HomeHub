from __future__ import annotations


def infer_requirement_spec(request: dict | None = None) -> dict:
    request = request if isinstance(request, dict) else {}
    command = str(request.get("command", "")).strip()
    command_lower = command.lower()
    input_modes = request.get("inputModes", ["text"])
    if not isinstance(input_modes, list) or not input_modes:
        input_modes = ["text"]

    require_search = any(token in command_lower for token in ["search", "latest", "official", "lookup", "research"])
    require_archive = any(token in command for token in ["记录", "归档", "档案", "历史", "长期"]) or any(
        token in command_lower for token in ["record", "archive", "history", "long-term", "track"]
    )
    require_follow_up = any(token in command for token in ["建议", "分析", "规划", "总结"]) or any(
        token in command_lower for token in ["advice", "analyze", "plan", "summary", "suggest"]
    )
    require_artifact = bool(request.get("requireArtifacts", False)) or any(
        token in command_lower for token in ["excel", "word", "ppt", "report", "document"]
    )

    return {
        "command": command,
        "taskType": str(request.get("taskType", "general_chat")).strip() or "general_chat",
        "inputModes": sorted(set(str(item).strip() for item in input_modes if str(item).strip())) or ["text"],
        "requiredCapabilities": [
            capability
            for capability, enabled in [
                ("semantic-understanding", True),
                ("voice-intake", "voice" in input_modes or "audio" in input_modes),
                ("ocr-intake", "image" in input_modes),
                ("network-research", bool(request.get("requiresNetwork", False)) or require_search),
                ("archive-writing", require_archive),
                ("follow-up-questioning", require_follow_up),
                ("artifact-generation", require_artifact),
            ]
            if enabled
        ],
        "decisionHints": {
            "requireSearch": bool(request.get("requiresNetwork", False)) or require_search,
            "requireArchive": require_archive,
            "requireFollowUp": require_follow_up,
            "requireArtifact": require_artifact,
        },
    }


def build_autonomous_creation_plan(state: dict, request: dict | None = None) -> dict:
    request = request if isinstance(request, dict) else {}
    requirement = infer_requirement_spec(request)
    blueprint = state.get("blueprint", {}) if isinstance(state.get("blueprint", {}), dict) else {}
    mission = str(blueprint.get("mission", "")).strip()
    mission_lower = mission.lower()
    capabilities = requirement.get("requiredCapabilities", [])
    fit_signals = []
    for capability in capabilities:
        keyword = capability.replace("-", " ")
        if keyword in mission_lower:
            fit_signals.append(capability)
    capability_fit = 0.0 if not capabilities else round(len(fit_signals) / len(capabilities), 2)
    should_create = capability_fit < 0.55

    return {
        "requirement": requirement,
        "existingBrainFit": {
            "agentId": state.get("agentId", ""),
            "agentName": state.get("agentName", ""),
            "mission": mission,
            "matchedCapabilities": fit_signals,
            "capabilityFitScore": capability_fit,
        },
        "decision": {
            "shouldCreateNewBrain": should_create,
            "reason": (
                "Existing smart unit does not cover enough of the inferred requirement capabilities."
                if should_create
                else "Existing smart unit covers the inferred requirement sufficiently."
            ),
        },
        "proposedBrain": {
            "agentType": requirement.get("taskType", "general-purpose-smart-unit"),
            "mission": f"Handle demand: {requirement.get('command', '')}".strip(),
            "inputModes": requirement.get("inputModes", ["text"]),
            "requiredCapabilities": capabilities,
            "featureHooks": [
                hook
                for hook, enabled in [
                    ("document OCR", "ocr-intake" in capabilities),
                    ("controlled network lookup", "network-research" in capabilities),
                    ("archive writer", "archive-writing" in capabilities),
                    ("follow-up interviewer", "follow-up-questioning" in capabilities),
                    ("artifact builder", "artifact-generation" in capabilities),
                ]
                if enabled
            ],
        },
    }
