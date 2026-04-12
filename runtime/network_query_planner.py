from __future__ import annotations

import json
import re
from typing import Any, Callable, Optional


def score_lookup_result(result: dict[str, Any]) -> int:
    if not isinstance(result, dict):
        return -1
    sources = result.get("sources", []) if isinstance(result.get("sources", []), list) else []
    answer = str(result.get("answer", "")).strip()
    source_bonus = len(sources) * 12
    answer_bonus = min(220, len(answer))
    source_diversity = len({str(item.get("url", "")).split("/")[2] for item in sources if isinstance(item, dict) and "://" in str(item.get("url", ""))}) * 8
    penalty = 0
    weak_markers = [
        "没有返回可用结果",
        "请稍后重试",
        "did not return usable results",
        "try again",
    ]
    lowered = answer.lower()
    if any(marker in answer or marker in lowered for marker in weak_markers):
        penalty -= 80
    return source_bonus + answer_bonus + source_diversity + penalty


def derive_refined_queries(
    original_query: str,
    locale: str,
    route_hints: Optional[dict[str, Any]] = None,
    ai_rewrites: Optional[list[str]] = None,
) -> list[str]:
    query = str(original_query or "").strip()
    if not query:
        return []
    hints = route_hints if isinstance(route_hints, dict) else {}
    preferred_sources = hints.get("preferredSources", []) if isinstance(hints.get("preferredSources", []), list) else []
    route_summary = str(hints.get("summary", "")).strip()
    route_key = str(hints.get("routeKey", "")).strip()
    candidates: list[str] = []
    if isinstance(ai_rewrites, list):
        candidates.extend(str(item or "").strip() for item in ai_rewrites if str(item or "").strip())
    if route_summary:
        candidates.append(f"{query} {route_summary}")
    if route_key:
        if locale == "zh-CN":
            candidates.append(f"{query} 关键信息 官方来源")
        else:
            candidates.append(f"{query} key facts official source")
    for source in preferred_sources[:3]:
        candidates.append(f"{query} site:{source}")
    unique: list[str] = []
    seen = set()
    for item in candidates:
        normalized = re.sub(r"\s+", " ", str(item or "").strip())
        if not normalized or normalized in seen or normalized == query:
            continue
        seen.add(normalized)
        unique.append(normalized)
    return unique


def suggest_ai_rewrites(
    query_text: str,
    locale: str,
    route_hints: Optional[dict[str, Any]],
    openai_chat_json: Optional[Callable[[str, str, str], Optional[dict[str, Any]]]],
) -> list[str]:
    if not callable(openai_chat_json):
        return []
    hints = route_hints if isinstance(route_hints, dict) else {}
    payload = openai_chat_json(
        (
            "You rewrite search queries for HomeHub web research. "
            "Return JSON only with one key: rewrites. "
            "Provide up to 4 concise search queries that improve retrieval quality. "
            "Prefer official, primary, or well-known authoritative sources. "
            "Do not explain."
        ),
        json.dumps(
            {
                "locale": locale,
                "query": str(query_text or "").strip(),
                "routeHints": {
                    "routeKey": str(hints.get("routeKey", "")).strip(),
                    "summary": str(hints.get("summary", "")).strip(),
                    "preferredSources": hints.get("preferredSources", []),
                },
            },
            ensure_ascii=False,
        ),
        "gpt-4o-mini",
    )
    rewrites = payload.get("rewrites", []) if isinstance(payload, dict) else []
    if not isinstance(rewrites, list):
        return []
    return [str(item or "").strip() for item in rewrites if str(item or "").strip()]


def run_iterative_network_lookup(
    query_text: str,
    locale: str,
    policy_id: str,
    preferred_sources: Optional[list[str]],
    allowed_domains: Optional[list[str]],
    route_hints: Optional[dict[str, Any]],
    build_query_candidates: Callable[[str, str, Optional[list[str]]], list[str]],
    perform_network_lookup: Callable[[str, str, str, Optional[list[str]], Optional[list[str]]], dict[str, Any]],
    build_grounded_reply: Callable[[str, dict[str, Any], str], str],
    is_weak_grounded_reply: Callable[[str], bool],
    openai_chat_json: Optional[Callable[[str, str, str], Optional[dict[str, Any]]]] = None,
) -> dict[str, Any]:
    query = str(query_text or "").strip()
    if not query:
        return {"ok": False, "error": "no_query"}
    base_candidates = build_query_candidates(query, locale, preferred_sources)
    ai_rewrites = suggest_ai_rewrites(query, locale, route_hints, openai_chat_json)
    refined_candidates = derive_refined_queries(query, locale, route_hints, ai_rewrites)
    all_candidates: list[str] = []
    seen = set()
    for item in base_candidates + refined_candidates:
        normalized = str(item or "").strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        all_candidates.append(normalized)
    best_result: dict[str, Any] = {"ok": False, "error": "no_query"}
    best_score = -1
    attempted: list[str] = []
    for candidate in all_candidates:
        attempted.append(candidate)
        result = perform_network_lookup(candidate, locale, policy_id, preferred_sources, allowed_domains)
        if not isinstance(result, dict):
            continue
        score = score_lookup_result(result)
        if score > best_score:
            best_score = score
            best_result = dict(result)
            best_result["autonomousQuery"] = candidate
        sources = result.get("sources", []) if isinstance(result.get("sources", []), list) else []
        if result.get("ok") and sources:
            reply = build_grounded_reply(candidate, result, locale)
            if not is_weak_grounded_reply(reply):
                result["autonomousQuery"] = candidate
                result["attemptedQueries"] = attempted
                return result
    if isinstance(best_result, dict):
        best_result["attemptedQueries"] = attempted
    return best_result
