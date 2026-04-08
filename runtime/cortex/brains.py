from __future__ import annotations


def _request_value(request: dict, key: str, default):
    value = request.get(key, default)
    return value if value not in (None, "") else default


def build_pre_brain(request: dict, model_plan: dict) -> dict:
    input_modes = model_plan.get("inputModes", ["text"])
    steps = [
        {
            "id": "language-classifier",
            "label": "Language Classifier",
            "purpose": "Normalize zh/en/ja input and decide the semantic lane.",
            "modelRole": "router",
        },
        {
            "id": "semantic-normalizer",
            "label": "Semantic Normalizer",
            "purpose": "Unify text, STT text, and OCR text into one command object.",
            "modelRole": "semantic",
        },
    ]
    if "voice" in input_modes or "audio" in input_modes:
        steps.insert(
            0,
            {
                "id": "voice-stt",
                "label": "Voice STT",
                "purpose": "Convert microphone audio into text before semantic normalization.",
                "runtimeInterface": "transcribe_audio",
            },
        )
    if "image" in input_modes:
        steps.insert(
            0,
            {
                "id": "image-ocr",
                "label": "Image OCR / Vision",
                "purpose": "Extract text, structure, and visual cues from screenshots, receipts, and documents.",
                "modelRole": "vision",
                "runtimeInterface": "analyze_image_with_homehub",
            },
        )
    return {
        "name": "pre-brain",
        "goal": "Convert raw command, voice, and image signals into one semantic command packet.",
        "inputModes": input_modes,
        "stages": steps,
        "outputContract": {
            "normalizedCommand": {
                "text": _request_value(request, "command", ""),
                "locale": _request_value(request, "locale", "zh-CN"),
                "taskType": _request_value(request, "taskType", "general_chat"),
                "inputModes": input_modes,
            }
        },
    }


def build_exec_brain(state: dict, request: dict, model_plan: dict, model_catalog: dict) -> dict:
    blueprint = state.get("blueprint", {}) if isinstance(state.get("blueprint", {}), dict) else {}
    feature_id = str(blueprint.get("generatedFeatureId", "")).strip()
    agent_library = [
        {
            "id": state.get("agentId", ""),
            "name": state.get("agentName", ""),
            "mission": blueprint.get("mission", ""),
            "featureId": feature_id,
            "status": state.get("stage", "seed"),
        }
    ]
    execution_units = [
        {
            "id": "brain-registry-check",
            "label": "Brain Registry Check",
            "purpose": "Check whether a matching smart unit already exists before considering a new one.",
            "modelRole": "similarity",
        },
        {
            "id": "capability-gap-analysis",
            "label": "Capability Gap Analysis",
            "purpose": "Infer whether the user demand exceeds the capability coverage of existing smart units.",
            "modelRole": "planner",
        },
        {
            "id": "taskflow-compiler",
            "label": "Taskflow Compiler",
            "purpose": "Assemble N execution units into a taskflow that matches the inferred requirement and capability gap result.",
            "modelRole": "planner",
        },
        {
            "id": "execution-loop",
            "label": "Execution Loop",
            "purpose": "Run the taskflow, call features/tools, and collect artifacts/results.",
            "modelRole": "executor",
        },
    ]
    if feature_id:
        execution_units.insert(
            1,
            {
                "id": "feature-bridge",
                "label": "Generated Feature Bridge",
                "purpose": "Route execution into the generated HomeHub feature when this brain has one.",
                "runtimeInterface": "RuntimeBridge.call_feature",
                "featureId": feature_id,
            },
        )
    return {
        "name": "exec-brain",
        "goal": "Judge demand fit, reuse or create the right smart units autonomously, compile a taskflow, and execute it.",
        "agentLibrary": agent_library,
        "modelLibrary": {
            "local": model_catalog.get("local", []),
            "cloud": model_catalog.get("cloud", []),
            "huggingface": model_catalog.get("huggingface", []),
        },
        "executionUnits": execution_units,
        "taskflow": compile_taskflow(state, request, model_plan),
    }


def build_repo_brain(request: dict, model_plan: dict) -> dict:
    output_modes = ["text"]
    if request.get("speakReply"):
        output_modes.append("voice")
    if request.get("requireArtifacts"):
        output_modes.append("artifact")
    return {
        "name": "repo-brain",
        "goal": "Package execution results back into text, voice, and multimodal artifacts.",
        "outputModes": output_modes,
        "stages": [
            {
                "id": "text-renderer",
                "label": "Text Renderer",
                "purpose": "Convert execution state into a user-facing text answer.",
                "modelRole": "response",
            },
            {
                "id": "voice-renderer",
                "label": "TTS Renderer",
                "purpose": "Turn the final text answer into voice when voice output is requested.",
                "runtimeInterface": "synthesize_speech",
            },
            {
                "id": "artifact-renderer",
                "label": "Artifact Renderer",
                "purpose": "Generate Excel, Word, PPT, image, or mixed multimodal output packages.",
                "modelRole": "artifact",
            },
        ],
    }


def build_repo_memory_contracts(state: dict) -> dict:
    return {
        "eventLedger": {
            "purpose": "Keep event-sourced brain activity and execution traces.",
            "backingStore": "runtime/agents/cortex_profiles.json",
        },
        "profileMemory": {
            "purpose": "Persistent agent cortex profile for mission, behavior, and specialization.",
            "backingStore": "runtime/agents/cortex_profiles.json",
        },
        "homeMemory": {
            "purpose": "Household schedule/reminder/event memory reused by brains.",
            "backingStore": "runtime/home_memory.json",
        },
        "artifactStore": {
            "purpose": "Persist generated documents, images, and exports.",
            "backingStore": "runtime/generated/",
        },
        "retrievalInterfaces": [
            "vector-memory adapter",
            "reranker adapter",
            "document-memory adapter",
            "policy/search adapter",
        ],
    }


def build_interface_contracts(state: dict) -> dict:
    blueprint = state.get("blueprint", {}) if isinstance(state.get("blueprint", {}), dict) else {}
    return {
        "runtimeBridge": {
            "openaiJson": "RuntimeBridge.openai_json",
            "analyzeImage": "RuntimeBridge.analyze_image",
            "networkLookup": "RuntimeBridge.network_lookup",
            "invokeFeature": "RuntimeBridge.call_feature",
        },
        "currentRuntimeEntrypoints": [
            "/api/voice/chat",
            "/api/audio/transcribe",
            "/api/audio/synthesize",
            "/api/network/query",
            "/api/custom-agents",
        ],
        "featureHooks": {
            "generatedFeatureId": blueprint.get("generatedFeatureId", ""),
            "required": [
                "FeatureManager.list_features",
                "FeatureManager.invoke_feature",
                "FeatureManager.route_voice_intent",
            ],
        },
    }


def build_support_stack() -> list[dict]:
    return [
        {"id": "event-sourcing", "label": "Event Sourcing", "purpose": "Replayable brain state and specialization traces."},
        {"id": "model-router", "label": "Functional Model Router", "purpose": "Assign models by role instead of by vendor."},
        {"id": "policy-engine", "label": "Policy Engine", "purpose": "Guard network, artifact, and tool execution boundaries."},
        {"id": "artifact-compiler", "label": "Artifact Compiler", "purpose": "Render text, voice, Excel, Word, and PPT outputs."},
        {"id": "memory-adapters", "label": "Memory Adapters", "purpose": "Leave clean interfaces for vector DB, RAG, reranking, and search layers."},
    ]


def compile_taskflow(state: dict, request: dict, model_plan: dict) -> dict:
    command = str(request.get("command", "")).strip()
    task_type = str(request.get("taskType", "general_chat")).strip() or "general_chat"
    blueprint = state.get("blueprint", {}) if isinstance(state.get("blueprint", {}), dict) else {}
    return {
        "command": command,
        "taskType": task_type,
        "missionFit": blueprint.get("mission", ""),
        "stages": [
            {"id": "ingest", "brain": "pre-brain", "selectedModelRole": "router"},
            {"id": "understand", "brain": "pre-brain", "selectedModelRole": "semantic"},
            {"id": "gap-analysis", "brain": "exec-brain", "selectedModelRole": "planner"},
            {"id": "plan", "brain": "exec-brain", "selectedModelRole": "planner"},
            {"id": "execute", "brain": "exec-brain", "selectedModelRole": "executor"},
            {"id": "package", "brain": "repo-brain", "selectedModelRole": "response"},
        ],
        "selectedModels": model_plan.get("assignments", {}),
    }
