from __future__ import annotations


def build_requirement_validation(state: dict, request: dict | None = None) -> dict:
    request = request if isinstance(request, dict) else {}
    command = str(request.get("command", "")).strip()
    task_type = str(request.get("taskType", "general_chat")).strip() or "general_chat"
    input_modes = request.get("inputModes", ["text"])
    if not isinstance(input_modes, list) or not input_modes:
        input_modes = ["text"]
    blueprint = state.get("blueprint", {}) if isinstance(state.get("blueprint", {}), dict) else {}
    feature_id = str(blueprint.get("generatedFeatureId", "")).strip()
    has_existing_brain = bool(state.get("agentId"))

    autonomous_creation = {
        "owner": "homehub-brain",
        "principle": "HomeHub decides by itself whether an existing smart unit is enough or whether a new one must be created.",
        "decisionFlow": [
            "normalize the user's requirement",
            "infer capability requirements from the demand instead of from a fixed template",
            "search existing smart units by semantic similarity and capability tags",
            "reuse an existing unit if capability fit is high enough",
            "create a new smart unit if capability fit is insufficient",
            "expand the taskflow with retrieval, questioning, archive writing, and artifact generation only when the demand needs them",
        ],
    }

    return {
        "validationMode": "requirement-driven-autonomous-creation",
        "goal": "Validate that HomeHub reacts to a user demand, judges capability gaps on its own, and creates or reuses the right smart unit without relying on a fixed scenario template.",
        "request": {
            "command": command,
            "taskType": task_type,
            "inputModes": input_modes,
        },
        "autonomousCreation": autonomous_creation,
        "existingBrainCheck": {
            "hasCurrentBrainState": has_existing_brain,
            "generatedFeatureId": feature_id,
            "expectedBehavior": "HomeHub should check fit first, not assume that a new brain must always be created.",
        },
        "validationChain": [
            {
                "step": 1,
                "name": "Requirement Understanding",
                "whatHappens": "The pre-brain converts the user demand into a normalized requirement packet with task type, input modes, desired outputs, and implied constraints.",
            },
            {
                "step": 2,
                "name": "Capability Gap Analysis",
                "whatHappens": "The exec-brain determines whether the current smart-unit library already covers the requirement well enough.",
            },
            {
                "step": 3,
                "name": "Autonomous Smart-Unit Decision",
                "whatHappens": "If fit is high, reuse an existing smart unit. If fit is low, HomeHub designs and creates a new one by itself.",
            },
            {
                "step": 4,
                "name": "Taskflow Expansion",
                "whatHappens": "HomeHub decides whether OCR, search, RAG, archive writing, follow-up questioning, and artifact generation are needed for this requirement.",
            },
            {
                "step": 5,
                "name": "Execution and Packaging",
                "whatHappens": "The selected or newly created unit executes the taskflow and the repo-brain packages the result into text, voice, and/or artifacts.",
            },
        ],
        "successCriteria": [
            "HomeHub does not depend on a hardcoded vertical scenario to decide what to build",
            "the brain can infer capability requirements from the user's demand",
            "existing smart units are searched before creation",
            "new smart units are created only when the capability gap is real",
            "optional behaviors such as search, archive building, and follow-up questioning are activated only when the requirement needs them",
        ],
        "demoExamples": [
            "hospital report analysis",
            "weekly family bill review",
            "trip plan organizer",
            "study-plan assistant",
            "device setup and maintenance assistant",
        ],
    }
