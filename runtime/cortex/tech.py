from __future__ import annotations


def build_technology_stack(request: dict | None = None) -> list[dict]:
    request = request if isinstance(request, dict) else {}
    task_type = str(request.get("taskType", "")).strip()
    need_network = bool(request.get("requiresNetwork", False))
    need_image = "image" in request.get("inputModes", [])

    return [
        {
            "id": "vector-db",
            "label": "Vector Database",
            "used": True,
            "phase": "repo-brain memory",
            "purpose": "Store semantic health records, report chunks, medicine history, hospital visits, and personal habits.",
            "minimumInterface": ["upsert_embeddings", "query_similar", "delete_namespace"],
            "recommendedBackends": ["Qdrant", "Milvus", "pgvector"],
        },
        {
            "id": "langgraph",
            "label": "LangChain / LangGraph",
            "used": True,
            "phase": "exec-brain orchestration",
            "purpose": "Represent the taskflow as a graph with retries, checkpoints, and human follow-up nodes.",
            "minimumInterface": ["compile_graph", "resume_graph", "checkpoint_state"],
            "recommendedWhen": "Use when execution units grow beyond a linear 5-stage taskflow.",
        },
        {
            "id": "rag",
            "label": "RAG",
            "used": True,
            "phase": "analysis and advice",
            "purpose": "Ground analysis on prior reports, medicine records, local notes, and retrieved medical references.",
            "minimumInterface": ["retrieve_context", "rerank_context", "compose_evidence_bundle"],
        },
        {
            "id": "elasticsearch",
            "label": "Elasticsearch",
            "used": need_network or task_type in {"medical_result_analysis", "research", "document_workflow"},
            "phase": "search and indexing",
            "purpose": "Index report text, OCR text, visit history, medicines, and external medical references for keyword + hybrid search.",
            "minimumInterface": ["index_document", "keyword_search", "hybrid_search"],
        },
        {
            "id": "fine-tuning",
            "label": "Fine-Tuning",
            "used": False,
            "phase": "future specialization",
            "purpose": "Only after enough confirmed report-analysis traces exist; not needed for the first working brain.",
            "minimumInterface": ["export_training_pairs", "evaluate_specialized_model"],
        },
        {
            "id": "agents",
            "label": "Agents",
            "used": True,
            "phase": "exec-brain",
            "purpose": "Treat each smart unit as the smallest execution cell: OCR agent, medical analyzer agent, follow-up interviewer agent, health archive agent.",
            "minimumInterface": ["lookup_agent", "create_agent", "run_agent", "handoff_agent"],
        },
        {
            "id": "lora",
            "label": "LoRA",
            "used": False,
            "phase": "future local specialization",
            "purpose": "Optional later path to specialize a local medical analyzer without full fine-tuning.",
            "minimumInterface": ["adapter_registry", "attach_adapter", "evaluate_adapter"],
        },
        {
            "id": "event-sourcing",
            "label": "Event Sourcing",
            "used": True,
            "phase": "cortex core",
            "purpose": "Track every intake, analysis, follow-up, and advice event so the brain can evolve safely.",
            "minimumInterface": ["append_event", "replay_events", "snapshot_state"],
        },
        {
            "id": "schema-extraction",
            "label": "Structured Extraction",
            "used": True,
            "phase": "pre-brain and repo-brain",
            "purpose": "Turn messy hospital reports into structured fields such as hospital, date, department, metrics, medicine, next visit.",
            "minimumInterface": ["extract_schema", "validate_schema", "merge_schema"],
        },
        {
            "id": "policy-engine",
            "label": "Policy Engine",
            "used": True,
            "phase": "exec-brain control",
            "purpose": "Prevent unsafe medical claims, require disclaimers, and separate analysis from diagnosis.",
            "minimumInterface": ["check_medical_policy", "require_disclaimer", "mark_human_review"],
        },
        {
            "id": "multimodal-index",
            "label": "Multimodal Index",
            "used": need_image,
            "phase": "medical evidence memory",
            "purpose": "Store OCR text plus report image linkage so future queries can trace back to the original scan.",
            "minimumInterface": ["link_image_to_record", "retrieve_image_evidence"],
        },
    ]
