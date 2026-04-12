from __future__ import annotations

import json
import math
import re
from datetime import datetime
from pathlib import Path
from typing import Any


MEMORY_FILE = Path(__file__).resolve().parent / "data" / "knowledge_memory.json"
MAX_ITEMS = 600


def _now_iso() -> str:
    return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")


def _default_payload() -> dict[str, Any]:
    return {
        "meta": {
            "schemaVersion": "1.0",
            "brainFamily": "homehub-knowledge-memory",
            "updatedAt": _now_iso(),
        },
        "items": [],
    }


def _ensure_parent() -> None:
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)


def _load_payload() -> dict[str, Any]:
    if not MEMORY_FILE.exists():
        return _default_payload()
    try:
        data = json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return _default_payload()
    if not isinstance(data, dict):
        return _default_payload()
    items = data.get("items", [])
    return {
        "meta": data.get("meta", {}) if isinstance(data.get("meta", {}), dict) else _default_payload()["meta"],
        "items": items if isinstance(items, list) else [],
    }


def _save_payload(payload: dict[str, Any]) -> None:
    _ensure_parent()
    body = {
        "meta": payload.get("meta", {}) if isinstance(payload, dict) else {},
        "items": payload.get("items", []) if isinstance(payload, dict) else [],
    }
    body["meta"]["updatedAt"] = _now_iso()
    MEMORY_FILE.write_text(json.dumps(body, ensure_ascii=False, indent=2), encoding="utf-8")


def _tokenize(text: str) -> list[str]:
    raw = str(text or "").strip().lower()
    if not raw:
        return []
    ascii_tokens = re.findall(r"[a-z0-9]{2,}", raw)
    cjk_chunks = re.findall(r"[\u4e00-\u9fff]{1,4}", raw)
    return ascii_tokens + cjk_chunks


def _score(query_tokens: set[str], search_text: str) -> float:
    haystack_tokens = set(_tokenize(search_text))
    if not query_tokens or not haystack_tokens:
        return 0.0
    overlap = len(query_tokens & haystack_tokens)
    if overlap <= 0:
        return 0.0
    return overlap / math.sqrt(max(1, len(query_tokens)) * max(1, len(haystack_tokens)))


def query_knowledge_memory(query_text: str, limit: int = 3, min_score: float = 0.18) -> list[dict[str, Any]]:
    payload = _load_payload()
    query_tokens = set(_tokenize(query_text))
    scored: list[tuple[float, dict[str, Any]]] = []
    for item in payload.get("items", []):
        if not isinstance(item, dict):
            continue
        search_text = " ".join(
            part
            for part in [
                str(item.get("title", "")).strip(),
                str(item.get("summary", "")).strip(),
                str(item.get("searchText", "")).strip(),
                str(item.get("source", "")).strip(),
            ]
            if part
        )
        score = _score(query_tokens, search_text)
        if score >= min_score:
            scored.append((score, item))
    scored.sort(key=lambda entry: (entry[0], str(entry[1].get("updatedAt", ""))), reverse=True)
    return [{**item, "score": score} for score, item in scored[: max(1, limit)]]


def remember_knowledge_item(item: dict[str, Any]) -> dict[str, Any] | None:
    if not isinstance(item, dict):
        return None
    title = str(item.get("title", "")).strip()
    summary = str(item.get("summary", "")).strip()
    url = str(item.get("url", "")).strip()
    if not summary:
        return None
    payload = _load_payload()
    normalized = {
        "id": str(item.get("id", "")).strip() or f"knowledge-{_now_iso().replace(':', '').replace('-', '')}",
        "title": title,
        "summary": summary,
        "url": url,
        "source": str(item.get("source", "")).strip(),
        "publishedAt": str(item.get("publishedAt", "")).strip(),
        "searchText": str(item.get("searchText", "")).strip() or " ".join(part for part in [title, summary, url] if part),
        "category": str(item.get("category", "")).strip() or "general",
        "createdAt": str(item.get("createdAt", "")).strip() or _now_iso(),
        "updatedAt": _now_iso(),
    }
    items = payload.get("items", [])
    dedup_key = normalized["url"] or normalized["title"] or normalized["summary"][:80]
    kept: list[dict[str, Any]] = []
    replaced = False
    for current in items:
        if not isinstance(current, dict):
            continue
        current_key = str(current.get("url", "")).strip() or str(current.get("title", "")).strip() or str(current.get("summary", "")).strip()[:80]
        if dedup_key and current_key == dedup_key:
            kept.append({**current, **normalized})
            replaced = True
        else:
            kept.append(current)
    if not replaced:
        kept.insert(0, normalized)
    payload["items"] = kept[:MAX_ITEMS]
    _save_payload(payload)
    return normalized
