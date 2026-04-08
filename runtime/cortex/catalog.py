from __future__ import annotations

from copy import deepcopy


MODEL_CATALOG = {
    "local": [
        {
            "id": "ollama:qwen2.5:1.5b-instruct",
            "label": "Qwen 2.5 1.5B Instruct",
            "provider": "ollama",
            "family": "local",
            "roles": ["router", "intent-triage", "guardrail-fallback"],
            "inputModes": ["text"],
            "strengths": ["low-latency routing", "cheap local fallback", "structured intent hints"],
            "bestFor": ["pre-brain command triage", "agent existence checks", "lightweight guardrails"],
        },
        {
            "id": "ollama:qwen2.5:3b-instruct",
            "label": "Qwen 2.5 3B Instruct",
            "provider": "ollama",
            "family": "local",
            "roles": ["semantic-understanding", "task-compiler", "response-drafter"],
            "inputModes": ["text"],
            "strengths": ["strong local semantics", "multilingual household dialogue", "JSON shaping"],
            "bestFor": ["semantic parsing", "taskflow drafting", "fallback response generation"],
        },
        {
            "id": "ollama:qwen2.5:7b-instruct",
            "label": "Qwen 2.5 7B Instruct",
            "provider": "ollama",
            "family": "local",
            "roles": ["planner", "executor", "controller"],
            "inputModes": ["text"],
            "strengths": ["deeper planning", "tool sequencing", "multi-step execution"],
            "bestFor": ["exec-brain control loop", "taskflow planning", "offline reasoning"],
        },
        {
            "id": "ollama:qwen2.5-coder:7b",
            "label": "Qwen 2.5 Coder 7B",
            "provider": "ollama",
            "family": "local",
            "roles": ["workflow-compiler", "artifact-builder", "code-generator"],
            "inputModes": ["text"],
            "strengths": ["file-safe generation", "automation", "format-aware artifact assembly"],
            "bestFor": ["Word/Excel/PPT task plans", "workflow templates", "tool-call JSON schemas"],
        },
        {
            "id": "ollama:qwen2.5vl:7b",
            "label": "Qwen 2.5 VL 7B",
            "provider": "ollama",
            "family": "local",
            "roles": ["vision", "ocr-fallback", "document-understanding"],
            "inputModes": ["image", "text"],
            "strengths": ["receipt understanding", "screenshot reasoning", "multimodal extraction"],
            "bestFor": ["pre-brain image normalization", "document OCR fallback", "multimodal workbench"],
        },
    ],
    "cloud": [
        {
            "id": "openai:gpt-5.4",
            "label": "GPT-5.4",
            "provider": "openai",
            "family": "cloud",
            "roles": ["deep-planner", "brain-architect", "complex-controller"],
            "inputModes": ["text", "image"],
            "strengths": ["high-end planning", "structured reasoning", "complex task decomposition"],
            "bestFor": ["exec-brain escalation", "new agent blueprinting", "cross-domain orchestration"],
        },
        {
            "id": "openai:gpt-5.4-mini",
            "label": "GPT-5.4 Mini",
            "provider": "openai",
            "family": "cloud",
            "roles": ["fast-controller", "response-polisher", "tool-router"],
            "inputModes": ["text", "image"],
            "strengths": ["fast cloud routing", "high-quality rewrite", "low-latency synthesis"],
            "bestFor": ["repo-brain rendering", "controller fallback", "response normalization"],
        },
        {
            "id": "google:gemini-multimodal",
            "label": "Gemini Multimodal",
            "provider": "google",
            "family": "cloud",
            "roles": ["multimodal-reasoner", "doc-vision", "ocr-enhancer"],
            "inputModes": ["image", "text", "audio"],
            "strengths": ["multimodal grounding", "document interpretation", "vision-heavy requests"],
            "bestFor": ["image-heavy exec paths", "OCR escalation", "document reasoning"],
        },
        {
            "id": "anthropic:long-context-reasoner",
            "label": "Anthropic Long Context Reasoner",
            "provider": "anthropic",
            "family": "cloud",
            "roles": ["long-context", "policy-review", "document-drafting"],
            "inputModes": ["text", "image"],
            "strengths": ["long context synthesis", "policy-aware drafting", "document review"],
            "bestFor": ["repo-brain document synthesis", "constraint-heavy planning", "policy review"],
        },
    ],
    "huggingface": [
        {
            "id": "hf:BAAI/bge-m3",
            "label": "BAAI/bge-m3",
            "provider": "huggingface",
            "family": "huggingface",
            "roles": ["embedding", "multilingual-memory"],
            "inputModes": ["text"],
            "strengths": ["multilingual embeddings", "dense retrieval", "memory indexing"],
            "bestFor": ["repo-brain memory vectors", "cross-lingual retrieval", "semantic lookup"],
            "reference": "https://huggingface.co/models?library=sentence-transformers",
        },
        {
            "id": "hf:BAAI/bge-reranker-v2-m3",
            "label": "BAAI/bge-reranker-v2-m3",
            "provider": "huggingface",
            "family": "huggingface",
            "roles": ["reranker", "evidence-ranking"],
            "inputModes": ["text"],
            "strengths": ["reranking", "evidence compression", "retrieval precision"],
            "bestFor": ["repo-brain evidence ordering", "RAG post-filter", "tool-result rerank"],
            "reference": "https://huggingface.co/models?library=sentence-transformers",
        },
        {
            "id": "hf:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            "label": "Paraphrase Multilingual MiniLM L12 v2",
            "provider": "huggingface",
            "family": "huggingface",
            "roles": ["semantic-match", "similarity", "intent-clustering"],
            "inputModes": ["text"],
            "strengths": ["multilingual matching", "intent grouping", "duplicate collapse"],
            "bestFor": ["pre-brain similarity search", "agent lookup", "memory deduplication"],
            "reference": "https://huggingface.co/models?library=sentence-transformers",
        },
        {
            "id": "hf:jinaai/jina-embeddings-v4",
            "label": "jina-embeddings-v4",
            "provider": "huggingface",
            "family": "huggingface",
            "roles": ["visual-document-retrieval", "doc-memory"],
            "inputModes": ["image", "text"],
            "strengths": ["visual document retrieval", "mixed text-image retrieval", "document grounding"],
            "bestFor": ["repo-brain multimodal memory", "document retrieval", "image-linked recall"],
            "reference": "https://huggingface.co/models?other=sentence-transformers",
        },
        {
            "id": "hf:nvidia/audio-flamingo-3-hf",
            "label": "Audio Flamingo 3",
            "provider": "huggingface",
            "family": "huggingface",
            "roles": ["audio-text-to-text", "audio-reasoning"],
            "inputModes": ["audio", "text"],
            "strengths": ["audio reasoning", "speech-aware answering", "instruction-following on audio"],
            "bestFor": ["future pre-brain voice reasoning", "audio QA", "audio-grounded planning"],
            "reference": "https://huggingface.co/docs/transformers/en/tasks/audio_text_to_text",
        },
    ],
}


def build_model_catalog() -> dict:
    return deepcopy(MODEL_CATALOG)


def build_model_plan(state: dict, request: dict | None = None) -> dict:
    request = request if isinstance(request, dict) else {}
    blueprint = state.get("blueprint", {}) if isinstance(state.get("blueprint", {}), dict) else {}
    evolution = state.get("evolution", {}) if isinstance(state.get("evolution", {}), dict) else {}
    input_modes = request.get("inputModes", ["text"])
    if not isinstance(input_modes, list) or not input_modes:
        input_modes = ["text"]

    need_image = "image" in input_modes
    need_voice = "voice" in input_modes or "audio" in input_modes
    need_network = bool(blueprint.get("networkEnabled")) or bool(request.get("requiresNetwork"))
    readiness = str(evolution.get("ownModelReadiness", "low")).strip() or "low"
    task_type = str(request.get("taskType", "")).strip()

    planner_id = "openai:gpt-5.4" if need_network or readiness == "high" else "ollama:qwen2.5:7b-instruct"
    response_id = "openai:gpt-5.4-mini" if need_network else "ollama:qwen2.5:3b-instruct"
    vision_id = "google:gemini-multimodal" if need_network and need_image else "ollama:qwen2.5vl:7b"
    artifact_id = "openai:gpt-5.4" if task_type in {"document_workflow", "agent_creation"} and need_network else "ollama:qwen2.5-coder:7b"
    audio_reasoner_id = "hf:nvidia/audio-flamingo-3-hf" if need_voice else ""

    assignments = {
        "router": "ollama:qwen2.5:1.5b-instruct",
        "semantic": "ollama:qwen2.5:3b-instruct",
        "planner": planner_id,
        "executor": "ollama:qwen2.5:7b-instruct",
        "vision": vision_id if need_image else "",
        "artifact": artifact_id,
        "response": response_id,
        "embedding": "hf:BAAI/bge-m3",
        "reranker": "hf:BAAI/bge-reranker-v2-m3",
        "similarity": "hf:sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        "docMemory": "hf:jinaai/jina-embeddings-v4" if need_image else "hf:BAAI/bge-m3",
        "audioReasoner": audio_reasoner_id,
    }

    explanations = {
        "router": "Use the lightest local model for always-on intent triage.",
        "semantic": "Keep semantic normalization local to reduce latency and preserve privacy.",
        "planner": "Promote to a cloud planner only when the task needs network-backed deep planning or the cortex is highly specialized.",
        "executor": "Keep the main execution loop local-first so HomeHub behaves like a persistent box brain.",
        "vision": "Use local VL for default document/image understanding, and cloud multimodal only when richer network inference is allowed.",
        "artifact": "Route artifact and workflow generation to the coder model unless the task explicitly benefits from stronger cloud synthesis.",
        "response": "Use a smaller cloud model for polished responses only when the task already depends on the network.",
        "embedding": "Prefer multilingual embeddings for repo-brain memory and cross-lingual retrieval.",
        "reranker": "Rerank retrieved evidence before the exec-brain consumes it.",
        "similarity": "Use a compact multilingual similarity model to find matching brains, commands, and memory shards.",
        "docMemory": "Use multimodal memory indexing when the request contains images or document evidence.",
        "audioReasoner": "Reserve audio-text-to-text models for future richer voice reasoning instead of plain STT.",
    }

    return {
        "assignments": assignments,
        "explanations": explanations,
        "inputModes": input_modes,
        "networkEnabled": need_network,
    }
