from __future__ import annotations


def build_request_loop(state: dict, request: dict, model_plan: dict, autonomous_creation: dict) -> dict:
    assignments = model_plan.get("assignments", {}) if isinstance(model_plan.get("assignments", {}), dict) else {}
    creation_mode = str(autonomous_creation.get("decision", "")).strip() or "reuse_or_create"
    return {
        "title": "HomeHub Request Loop",
        "inspiredBy": "ccunpacked.dev agent loop",
        "steps": [
            {
                "id": "input",
                "label": "Input",
                "purpose": "Accept text, voice, image, or mixed multimodal requests.",
                "state": {"inputModes": request.get("inputModes", ["text"])},
            },
            {
                "id": "normalize",
                "label": "Normalize",
                "purpose": "Convert raw signals into one semantic command packet.",
                "modelRole": assignments.get("router", ""),
            },
            {
                "id": "retrieve",
                "label": "Retrieve",
                "purpose": "Check semantic memory, vector memory, JSON memory, and existing smart units.",
                "memoryOrder": ["json-memory", "vector-memory", "agent-library", "network-research"],
            },
            {
                "id": "decide",
                "label": "Decide",
                "purpose": "Judge whether to reuse, extend, or autonomously create a smart unit.",
                "decisionMode": creation_mode,
            },
            {
                "id": "plan",
                "label": "Plan",
                "purpose": "Compile an execution graph and assign the best models by function.",
                "modelRole": assignments.get("planner", ""),
            },
            {
                "id": "execute",
                "label": "Execute",
                "purpose": "Invoke features, tools, searches, and agents until the taskflow completes.",
                "modelRole": assignments.get("executor", ""),
            },
            {
                "id": "render",
                "label": "Render",
                "purpose": "Return text, voice, and artifact outputs back to the user.",
                "modelRole": assignments.get("response", ""),
            },
            {
                "id": "learn",
                "label": "Learn",
                "purpose": "Write corrected understanding and execution evidence back into memory.",
                "stores": ["semantic-memory", "event-ledger", "profile-memory"],
            },
        ],
    }


def build_architecture_explorer(state: dict) -> dict:
    blueprint = state.get("blueprint", {}) if isinstance(state.get("blueprint", {}), dict) else {}
    return {
        "title": "HomeHub Cortex Explorer",
        "inspiredBy": "ccunpacked.dev architecture explorer",
        "zones": [
            {
                "id": "runtime",
                "label": "Runtime",
                "purpose": "Entry server, HTTP routes, dashboard assembly, voice loop, and network bridge.",
                "modules": ["runtime/server.py", "runtime/server_routes.py", "runtime/server_voice.py"],
            },
            {
                "id": "cortex",
                "label": "Cortex",
                "purpose": "Brain design, taskflow compilation, requirement inference, and evolution memory.",
                "modules": ["runtime/cortex/architect.py", "runtime/cortex/brains.py", "runtime/cortex/core.py"],
            },
            {
                "id": "features",
                "label": "Features",
                "purpose": "Execution surface used by smart units and runtime routing.",
                "modules": ["runtime/features/custom_agents.py", "runtime/features/local_schedule.py", "runtime/features/external_channels.py"],
            },
            {
                "id": "memory",
                "label": "Memory",
                "purpose": "Persistent state, semantic examples, vector adapters, and household memory.",
                "modules": ["runtime/cortex/store.py", "runtime/server_components/semantic_memory.py", "runtime/home_memory.json"],
            },
            {
                "id": "services",
                "label": "Services",
                "purpose": "Node or sidecar services that expand execution outside the runtime process.",
                "modules": ["services/core-engine", "services/companion-api"],
            },
            {
                "id": "agent-blueprint",
                "label": "Current Smart Unit",
                "purpose": "Current agent mission, feature bridge, and specialization status.",
                "state": {
                    "agentId": state.get("agentId", ""),
                    "agentName": state.get("agentName", ""),
                    "featureId": blueprint.get("generatedFeatureId", ""),
                    "mission": blueprint.get("mission", ""),
                },
            },
        ],
    }


def build_capability_explorer(request: dict, technology_stack: list[dict]) -> dict:
    requires_network = bool(request.get("requiresNetwork", False))
    input_modes = request.get("inputModes", ["text"])
    return {
        "title": "HomeHub Capability Explorer",
        "inspiredBy": "ccunpacked.dev tool system",
        "groups": [
            {"id": "conversation", "label": "Conversation", "items": ["text intake", "voice intake", "semantic normalization"]},
            {"id": "perception", "label": "Perception", "items": ["OCR", "vision analysis", "language detection"]},
            {"id": "memory", "label": "Memory", "items": ["semantic memory", "vector backend", "event ledger", "profile memory"]},
            {"id": "research", "label": "Research", "items": ["network lookup", "official-source fetch", "RAG", "Elasticsearch hybrid search"]},
            {"id": "execution", "label": "Execution", "items": ["feature invocation", "custom agents", "schedule/reminder actions", "artifact compiler"]},
            {"id": "adaptation", "label": "Adaptation", "items": ["autonomous agent creation", "training-pair export", "fine-tuning prep", "LoRA prep"]},
        ],
        "requestFit": {
            "inputModes": input_modes,
            "networkLikely": requires_network,
            "technologyHints": [item.get("id", "") for item in technology_stack if isinstance(item, dict)],
        },
    }


def build_feature_status_matrix() -> dict:
    return {
        "title": "HomeHub Feature Status",
        "inspiredBy": "ccunpacked.dev hidden features",
        "items": [
            {"id": "voice-runtime", "label": "Voice Runtime", "status": "stable"},
            {"id": "ocr-fallback", "label": "OCR Fallback Layers", "status": "stable"},
            {"id": "semantic-memory", "label": "Semantic Memory Learning Loop", "status": "stable"},
            {"id": "qdrant-backend", "label": "Qdrant Vector Backend", "status": "experimental"},
            {"id": "autonomous-agent-creation", "label": "Autonomous Agent Creation", "status": "experimental"},
            {"id": "background-agents", "label": "Background Agents", "status": "planned"},
            {"id": "lora-export", "label": "LoRA Export Pipeline", "status": "planned"},
            {"id": "fine-tuning-pipeline", "label": "Fine-Tuning Pipeline", "status": "planned"},
        ],
    }

