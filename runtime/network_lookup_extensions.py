from __future__ import annotations

from typing import Any, Callable

from runtime.network_route_memory import (
    best_network_route,
    build_semantic_route_query_candidates,
    remember_network_route_example,
)


def infer_research_hints(query_text: str) -> dict[str, Any]:
    route = best_network_route(query_text)
    remember_network_route_example(
        query_text,
        route.get("routeKey", ""),
        preferred_sources=route.get("preferredSources", []),
        allowed_domains=route.get("allowedDomains", []),
        query_patterns=route.get("queryPatterns", []),
        summary=route.get("summary", ""),
    )
    return {
        "routeKey": route.get("routeKey", ""),
        "routeScore": float(route.get("score", 0.0) or 0.0),
        "preferredSources": list(route.get("preferredSources", [])) if isinstance(route.get("preferredSources", []), list) else [],
        "allowedDomains": list(route.get("allowedDomains", [])) if isinstance(route.get("allowedDomains", []), list) else [],
        "queryPatterns": list(route.get("queryPatterns", [])) if isinstance(route.get("queryPatterns", []), list) else [],
        "summary": str(route.get("summary", "")).strip(),
    }


def append_topic_specific_query_candidates(candidates: list[str], query_text: str, locale: str, preferred_sources: list[str] | None = None) -> list[str]:
    route = best_network_route(query_text)
    route_sources = list(route.get("preferredSources", [])) if isinstance(route.get("preferredSources", []), list) else []
    if isinstance(preferred_sources, list):
        for item in preferred_sources:
            source = str(item or "").strip()
            if source and source not in route_sources:
                route_sources.append(source)
    route["preferredSources"] = route_sources
    semantic_candidates = build_semantic_route_query_candidates(query_text, locale, route)
    combined = list(candidates) + semantic_candidates
    unique: list[str] = []
    seen = set()
    for item in combined:
        normalized = str(item or "").strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        unique.append(normalized)
    return unique


def should_attempt_source_reference_lookup(
    user_text: str,
    route: dict[str, Any],
    knowledge_hits: list[dict[str, Any]],
    is_information_request_fn: Callable[[str], bool],
) -> bool:
    if knowledge_hits:
        return False
    task_spec = route.get("taskSpec", {}) if isinstance(route.get("taskSpec", {}), dict) else {}
    task_type = str(task_spec.get("taskType", "general_chat")).strip() or "general_chat"
    if task_type in {"time_query", "clock", "reminder", "schedule", "ui_navigation", "agent_creation"}:
        return False
    return is_information_request_fn(user_text) or task_type in {"weather", "network_lookup", "document_workflow", "general_chat"}


def lookup_from_source_references(user_text: str, context: dict[str, Any]) -> dict[str, Any] | None:
    references = context["query_source_reference_memory"](user_text, 3, 0.16)
    urls = [str(item.get("url", "")).strip() for item in references if isinstance(item, dict)]
    if not urls:
        return None
    result = context["perform_reference_url_lookup"](urls)
    if not isinstance(result, dict) or not result.get("ok"):
        return None
    result["sourceReferenceHits"] = references
    return result


def remember_lookup_sources(user_text: str, lookup_result: dict[str, Any] | None, context: dict[str, Any], execution_context: Any) -> None:
    if not isinstance(lookup_result, dict) or not lookup_result.get("ok"):
        return
    route = infer_research_hints(user_text)
    remember_network_route_example(
        user_text,
        route.get("routeKey", ""),
        preferred_sources=route.get("preferredSources", []),
        allowed_domains=route.get("allowedDomains", []),
        query_patterns=route.get("queryPatterns", []),
        summary=route.get("summary", ""),
    )
    sources = lookup_result.get("sources", []) if isinstance(lookup_result.get("sources", []), list) else []
    remembered_items = []
    for item in sources:
        if not isinstance(item, dict):
            continue
        remembered = context["remember_source_reference"](
            {
                "url": str(item.get("url", "")).strip(),
                "title": str(item.get("title", "")).strip(),
                "source": str(item.get("source", "")).strip(),
                "queryText": str(user_text or "").strip(),
                "searchText": " ".join(
                    part
                    for part in [
                        str(user_text or "").strip(),
                        str(item.get("title", "")).strip(),
                        str(item.get("excerpt", "")).strip(),
                        str(item.get("url", "")).strip(),
                    ]
                    if part
                ),
                "category": "network-source-reference",
            }
        )
        if remembered:
            remembered_items.append(remembered)
    if remembered_items:
        execution_context.memory_writeback.setdefault("sourceReferences", []).extend(remembered_items)
