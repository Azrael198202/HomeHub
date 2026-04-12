from __future__ import annotations

from typing import Any, Callable, Optional

try:
    from server_network import normalize_domain
except ModuleNotFoundError:
    from runtime.server_network import normalize_domain


ResearchLookup = Callable[[str, str, str, Optional[list[str]], Optional[list[str]]], dict[str, Any]]


def _clean_summary(text: str, limit: int = 280) -> str:
    value = " ".join(str(text or "").strip().split())
    if len(value) <= limit:
        return value
    return value[:limit].rstrip(" ,;:") + "..."


def build_research_packet(
    query_text: str,
    locale: str,
    lookup: ResearchLookup,
    policy_id: str = "official-only",
    preferred_sources: Optional[list[str]] = None,
    allowed_domains: Optional[list[str]] = None,
) -> dict[str, Any]:
    result = lookup(query_text, locale, policy_id, preferred_sources, allowed_domains)
    sources = result.get("sources", []) if isinstance(result.get("sources", []), list) else []
    evidence: list[dict[str, Any]] = []
    for item in sources:
        if not isinstance(item, dict):
            continue
        url = str(item.get("url", "")).strip()
        title = str(item.get("title", "")).strip()
        summary = _clean_summary(str(item.get("excerpt", "")).strip())
        evidence.append(
            {
                "title": title,
                "url": url,
                "source": normalize_domain(url),
                "publishedAt": str(item.get("publishedAt", "")).strip(),
                "cleanText": str(item.get("excerpt", "")).strip(),
                "summary": summary,
                "score": 1.0 if summary else 0.0,
            }
        )
    return {
        "ok": bool(result.get("ok")),
        "query": str(query_text or "").strip(),
        "locale": str(locale or "").strip(),
        "policy": str(result.get("policy", policy_id)).strip() or policy_id,
        "answer": str(result.get("answer", "")).strip(),
        "sources": sources,
        "evidence": evidence,
        "error": str(result.get("error", "")).strip(),
    }


def evidence_to_knowledge_items(packet: dict[str, Any], category: str = "general") -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    if not isinstance(packet, dict):
        return items
    query = str(packet.get("query", "")).strip()
    for evidence in packet.get("evidence", []):
        if not isinstance(evidence, dict):
            continue
        summary = str(evidence.get("summary", "")).strip()
        if not summary:
            continue
        items.append(
            {
                "title": str(evidence.get("title", "")).strip(),
                "summary": summary,
                "url": str(evidence.get("url", "")).strip(),
                "source": str(evidence.get("source", "")).strip(),
                "publishedAt": str(evidence.get("publishedAt", "")).strip(),
                "searchText": " ".join(
                    part
                    for part in [
                        query,
                        str(evidence.get("title", "")).strip(),
                        summary,
                        str(evidence.get("source", "")).strip(),
                    ]
                    if part
                ),
                "category": category,
            }
        )
    return items
