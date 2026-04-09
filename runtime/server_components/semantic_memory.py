from __future__ import annotations

import json
import math
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

try:
    from server_components.semantic_vector_backends import VECTOR_DIMENSION, build_backend, make_dense_vector
except ModuleNotFoundError:
    from runtime.server_components.semantic_vector_backends import VECTOR_DIMENSION, build_backend, make_dense_vector


MEMORY_FILE = Path(__file__).resolve().parent.parent / "data" / "task_semantic_memory.json"
EXPORT_DIR = Path(__file__).resolve().parent.parent / "generated" / "training"
CONFIG_FILE = Path(__file__).resolve().parent.parent / "semantic_memory.local.json"
MAX_ITEMS = 500
DEFAULT_THRESHOLD = 0.33
DEFAULT_RECALL_THRESHOLD = 0.18
EMBEDDING_SCHEMA_VERSION = 1
NOISY_TEXT_MARKERS = [
    "line公式アカウント",
    "運用事務局",
    "送信専用",
    "配信停止",
    "お問い合わせフォーム",
    "starter kit",
    "unsubscribe",
    "the weather channel",
]


def now_iso() -> str:
    return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")


def _ensure_parent() -> None:
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)


def _ensure_export_dir() -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def _ensure_config_file() -> None:
    if CONFIG_FILE.exists():
        return
    CONFIG_FILE.write_text(json.dumps(default_backend_config(), ensure_ascii=False, indent=2), encoding="utf-8")


def _tokenize(text: str) -> list[str]:
    raw = str(text or "").strip().lower()
    if not raw:
        return []
    ascii_parts = re.findall(r"[a-z0-9]{2,}", raw)
    ascii_ngrams: list[str] = []
    for chunk in ascii_parts:
        if len(chunk) < 4:
            continue
        for width in (3, 4):
            if len(chunk) < width:
                continue
            for index in range(0, len(chunk) - width + 1):
                ascii_ngrams.append(chunk[index:index + width])
    cjk_unigrams = re.findall(r"[\u4e00-\u9fff]", raw)
    cjk_parts = re.findall(r"[\u4e00-\u9fff]{2,}", raw)
    ngrams: list[str] = []
    for chunk in cjk_parts:
        ngrams.append(chunk)
        length = len(chunk)
        for width in (2, 3):
            if length < width:
                continue
            for index in range(0, length - width + 1):
                ngrams.append(chunk[index:index + width])
    return ascii_parts + ascii_ngrams + cjk_unigrams + ngrams


def _vectorize(text: str) -> Counter:
    return Counter(_tokenize(text))


def _embedding(text: str) -> list[float]:
    return make_dense_vector(_tokenize(text), dimension=VECTOR_DIMENSION)


def _dense_cosine(left: list[float], right: list[float]) -> float:
    if not left or not right or len(left) != len(right):
        return 0.0
    dot = 0.0
    left_norm = 0.0
    right_norm = 0.0
    for left_value, right_value in zip(left, right):
        dot += left_value * right_value
        left_norm += left_value * left_value
        right_norm += right_value * right_value
    if left_norm <= 0 or right_norm <= 0:
        return 0.0
    return dot / math.sqrt(left_norm * right_norm)


def _item_search_text(item: dict) -> str:
    task_spec = item.get("taskSpec", {}) if isinstance(item.get("taskSpec", {}), dict) else {}
    parts = [
        str(item.get("sourceText", "")).strip(),
        str(item.get("correctionText", "")).strip(),
        str(item.get("agentName", "")).strip(),
        str(task_spec.get("summary", "")).strip(),
        str(task_spec.get("intent", "")).strip(),
        str(task_spec.get("taskType", "")).strip(),
    ]
    return " ".join(part for part in parts if part)


def _normalize_item_index_fields(item: dict) -> tuple[dict, bool]:
    if not isinstance(item, dict):
        return {}, False
    normalized = dict(item)
    changed = False
    search_text = str(normalized.get("searchText", "")).strip()
    if not search_text:
        search_text = _item_search_text(normalized)
        normalized["searchText"] = search_text
        changed = True
    embedding = normalized.get("embedding")
    if not isinstance(embedding, list) or len(embedding) != VECTOR_DIMENSION or not all(isinstance(value, (int, float)) for value in embedding):
        normalized["embedding"] = _embedding(search_text)
        changed = True
    schema_version = int(normalized.get("embeddingSchemaVersion", 0) or 0)
    if schema_version != EMBEDDING_SCHEMA_VERSION:
        normalized["embedding"] = _embedding(search_text)
        normalized["embeddingSchemaVersion"] = EMBEDDING_SCHEMA_VERSION
        changed = True
    return normalized, changed


def _looks_like_noisy_training_text(text: str) -> bool:
    value = str(text or "").strip()
    if not value:
        return False
    lowered = value.lower()
    url_count = len(re.findall(r"https?://", value))
    if value.startswith("Original request:"):
        return True
    if len(value) > 500:
        return True
    if url_count >= 3:
        return True
    return any(marker in lowered for marker in NOISY_TEXT_MARKERS)


def _is_usable_memory_item(item: dict) -> bool:
    if not isinstance(item, dict):
        return False
    if not bool(item.get("accepted", True)):
        return False
    source_text = str(item.get("sourceText", "")).strip()
    correction_text = str(item.get("correctionText", "")).strip()
    if not source_text:
        return False
    if _looks_like_noisy_training_text(source_text):
        return False
    if correction_text and _looks_like_noisy_training_text(correction_text):
        return False
    return True


def _cosine(left: Counter, right: Counter) -> float:
    if not left or not right:
        return 0.0
    dot = sum(left[key] * right.get(key, 0) for key in left)
    left_norm = math.sqrt(sum(value * value for value in left.values()))
    right_norm = math.sqrt(sum(value * value for value in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def _recall_similarity(left: Counter, right: Counter) -> float:
    left_keys = set(left)
    right_keys = set(right)
    if not left_keys or not right_keys:
        return 0.0
    return len(left_keys & right_keys) / max(1, min(len(left_keys), len(right_keys)))


def _similarity(left: Counter, right: Counter) -> float:
    cosine = _cosine(left, right)
    recall = _recall_similarity(left, right)
    return max(cosine, recall)


def default_payload() -> dict:
    return {
        "meta": {
            "schemaVersion": "1.0",
            "backend": "json-hybrid-indexed",
            "brainFamily": "homehub-semantic-memory",
            "updatedAt": now_iso(),
        },
        "items": [],
    }


def default_backend_config() -> dict:
    return {
        "backend": "qdrant",
        "mirrorToJson": True,
        "qdrant": {
            "url": "",
            "apiKey": "",
            "collection": "homehub_semantic_memory",
            "timeoutSeconds": 3,
        },
        "pgvector": {
            "dsn": "",
            "table": "homehub_semantic_memory",
        },
        "milvus": {
            "uri": "",
            "token": "",
            "collection": "homehub_semantic_memory",
        },
    }


def load_backend_config() -> dict:
    _ensure_config_file()
    try:
        raw = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        raw = {}
    config = default_backend_config()
    if not isinstance(raw, dict):
        return config
    for key in ("backend", "mirrorToJson"):
        if key in raw:
            config[key] = raw[key]
    for key in ("qdrant", "pgvector", "milvus"):
        if isinstance(raw.get(key), dict):
            config[key] = {**config[key], **raw[key]}
    return config


def get_active_backend() -> tuple[object | None, dict]:
    config = load_backend_config()
    backend = build_backend(config)
    return backend, config


def load_memory() -> dict:
    if not MEMORY_FILE.exists():
        return default_payload()
    try:
        data = json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default_payload()
    if not isinstance(data, dict):
        return default_payload()
    meta = data.get("meta", {})
    items = data.get("items", [])
    merged_meta = {**default_payload()["meta"], **(meta if isinstance(meta, dict) else {})}
    if str(merged_meta.get("backend", "")).strip() in {"json-cosine", "json-hybrid-similarity"}:
        merged_meta["backend"] = "json-hybrid-indexed"
    normalized_items: list[dict] = []
    changed = False
    for item in items if isinstance(items, list) else []:
        if not isinstance(item, dict):
            changed = True
            continue
        normalized_item, item_changed = _normalize_item_index_fields(item)
        normalized_items.append(normalized_item)
        changed = changed or item_changed
    payload = {
        "meta": merged_meta,
        "items": normalized_items,
    }
    if changed:
        save_memory(payload)
    return {
        "meta": merged_meta,
        "items": normalized_items,
    }


def save_memory(payload: dict) -> None:
    _ensure_parent()
    meta = payload.get("meta", {}) if isinstance(payload, dict) else {}
    items = payload.get("items", []) if isinstance(payload, dict) else []
    body = {
        "meta": {
            **default_payload()["meta"],
            **(meta if isinstance(meta, dict) else {}),
            "updatedAt": now_iso(),
        },
        "items": items if isinstance(items, list) else [],
    }
    MEMORY_FILE.write_text(json.dumps(body, ensure_ascii=False, indent=2), encoding="utf-8")


def semantic_backend_snapshot() -> dict:
    payload = load_memory()
    backend, config = get_active_backend()
    status = backend.status() if backend is not None else None
    configured_backend = str(config.get("backend", "json")).strip() or "json"
    active_backend = configured_backend
    detail = "json-local-active"
    fallback_used = False
    if backend is not None:
        if status and status.available:
            active_backend = status.backend
            detail = status.detail
        else:
            active_backend = "json"
            detail = status.detail if status else "fallback-to-json"
            fallback_used = configured_backend != "json"
    return {
        "backend": str(payload.get("meta", {}).get("backend", "json-hybrid-similarity")).strip() or "json-hybrid-similarity",
        "configuredBackend": configured_backend,
        "activeBackend": active_backend,
        "fallbackUsed": fallback_used,
        "detail": detail,
        "items": len(payload.get("items", [])) if isinstance(payload.get("items", []), list) else 0,
        "storagePath": str(MEMORY_FILE),
        "configPath": str(CONFIG_FILE),
    }


def query_semantic_memory(text: str, locale: str, limit: int = 5, threshold: float = DEFAULT_RECALL_THRESHOLD) -> list[dict]:
    query_text = str(text or "").strip()
    if not query_text:
        return []
    backend, config = get_active_backend()
    if backend is not None:
        status = backend.status()
        if status.available:
            try:
                remote_matches = backend.query(_embedding(query_text), locale, limit)
                filtered = []
                for entry in remote_matches:
                    score = float(entry.get("score", 0.0) or 0.0)
                    if score < threshold:
                        continue
                    item = entry.get("item", {}) if isinstance(entry.get("item", {}), dict) else {}
                    if not isinstance(item, dict):
                        continue
                    filtered.append({"score": round(score, 3), "item": item})
                if filtered:
                    return filtered[: max(1, limit)]
            except Exception:
                if not bool(config.get("mirrorToJson", True)):
                    return []
    query_vector = _vectorize(query_text)
    query_dense = _embedding(query_text)
    if not query_vector:
        return []
    scored: list[dict] = []
    for item in load_memory().get("items", []):
        if not _is_usable_memory_item(item):
            continue
        item_locale = str(item.get("locale", "")).strip()
        if item_locale and locale and item_locale != locale:
            continue
        normalized_item, _ = _normalize_item_index_fields(item)
        search_text = str(normalized_item.get("searchText", "")).strip() or _item_search_text(normalized_item)
        lexical_score = _similarity(query_vector, _vectorize(search_text))
        dense_score = _dense_cosine(query_dense, normalized_item.get("embedding", []))
        prefix_bonus = 0.02 if query_text.lower() in search_text.lower() else 0.0
        score = max(lexical_score, dense_score, (lexical_score * 0.55) + (dense_score * 0.45) + prefix_bonus)
        if score < threshold:
            continue
        scored.append(
            {
                "score": round(score, 3),
                "item": normalized_item,
            }
        )
    scored.sort(key=lambda entry: (entry["score"], str(entry["item"].get("updatedAt", ""))), reverse=True)
    return scored[: max(1, limit)]


def infer_from_semantic_memory(text: str, locale: str, threshold: float = DEFAULT_THRESHOLD) -> dict | None:
    matches = query_semantic_memory(text, locale, limit=1, threshold=threshold)
    if not matches:
        return None
    best_item = matches[0]["item"]
    task_spec = best_item.get("taskSpec", {})
    if not isinstance(task_spec, dict):
        return None
    inferred = dict(task_spec)
    inferred["confidence"] = max(float(inferred.get("confidence", 0.0) or 0.0), float(matches[0]["score"]))
    inferred["reasoning"] = "semantic-memory-match"
    inferred["memoryId"] = str(best_item.get("id", "")).strip()
    return inferred


def upsert_semantic_memory_item(
    source_text: str,
    locale: str,
    task_spec: dict,
    correction_text: str = "",
    *,
    agent_id: str = "",
    agent_name: str = "",
    accepted: bool = True,
) -> dict | None:
    normalized_text = str(source_text or "").strip()
    if not normalized_text or not isinstance(task_spec, dict):
        return None
    normalized_correction = str(correction_text or "").strip()
    if _looks_like_noisy_training_text(normalized_text):
        return None
    if normalized_correction and _looks_like_noisy_training_text(normalized_correction):
        return None
    payload = load_memory()
    items = payload.get("items", [])
    if not isinstance(items, list):
        items = []
    normalized_locale = str(locale or "").strip()
    updated = []
    for item in items:
        if not isinstance(item, dict):
            continue
        same_text = str(item.get("sourceText", "")).strip() == normalized_text
        same_locale = str(item.get("locale", "")).strip() == normalized_locale
        same_agent = str(item.get("agentId", "")).strip() == str(agent_id or "").strip()
        if same_text and same_locale and same_agent:
            continue
        updated.append(item)
    item = {
        "id": f"sem-{datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        "sourceText": normalized_text,
        "locale": normalized_locale,
        "taskSpec": dict(task_spec),
        "correctionText": normalized_correction,
        "agentId": str(agent_id or "").strip(),
        "agentName": str(agent_name or "").strip(),
        "accepted": bool(accepted),
        "createdAt": now_iso(),
        "updatedAt": now_iso(),
    }
    search_text = _item_search_text(item)
    item["searchText"] = search_text
    item["embedding"] = _embedding(search_text)
    item["embeddingSchemaVersion"] = EMBEDDING_SCHEMA_VERSION
    updated.insert(0, item)
    backend, config = get_active_backend()
    if bool(config.get("mirrorToJson", True)) or backend is None:
        payload["items"] = updated[:MAX_ITEMS]
        save_memory(payload)
    if backend is not None:
        status = backend.status()
        if status.available:
            try:
                backend.upsert(item, _embedding(search_text), search_text)
            except Exception:
                if not bool(config.get("mirrorToJson", True)):
                    payload["items"] = updated[:MAX_ITEMS]
                    save_memory(payload)
    return item


def record_semantic_example(
    source_text: str,
    locale: str,
    task_spec: dict,
    correction_text: str = "",
    *,
    agent_id: str = "",
    agent_name: str = "",
    accepted: bool = True,
) -> dict | None:
    return upsert_semantic_memory_item(
        source_text,
        locale,
        task_spec,
        correction_text=correction_text,
        agent_id=agent_id,
        agent_name=agent_name,
        accepted=accepted,
    )


def delete_semantic_examples_for_agent(agent_id: str) -> int:
    normalized_id = str(agent_id or "").strip()
    if not normalized_id:
        return 0
    payload = load_memory()
    items = payload.get("items", [])
    if not isinstance(items, list):
        return 0
    filtered = [item for item in items if str(item.get("agentId", "")).strip() != normalized_id]
    removed = len(items) - len(filtered)
    backend, config = get_active_backend()
    if removed or bool(config.get("mirrorToJson", True)):
        payload["items"] = filtered
        save_memory(payload)
    if backend is not None:
        status = backend.status()
        if status.available:
            try:
                backend.delete_for_agent(normalized_id)
            except Exception:
                pass
    return removed


def export_training_pairs(agent_id: str = "", task_type: str = "", limit: int = 100) -> dict:
    normalized_agent_id = str(agent_id or "").strip()
    normalized_task_type = str(task_type or "").strip()
    _ensure_export_dir()
    items = []
    for item in load_memory().get("items", []):
        if not isinstance(item, dict):
            continue
        if normalized_agent_id and str(item.get("agentId", "")).strip() != normalized_agent_id:
            continue
        item_task_type = str((item.get("taskSpec", {}) if isinstance(item.get("taskSpec", {}), dict) else {}).get("taskType", "")).strip()
        if normalized_task_type and item_task_type != normalized_task_type:
            continue
        items.append(item)
    items = items[: max(1, limit)]
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    slug = normalized_agent_id or normalized_task_type or "general"
    jsonl_path = EXPORT_DIR / f"{slug}-semantic-training-{stamp}.jsonl"
    summary_path = EXPORT_DIR / f"{slug}-semantic-training-{stamp}.md"
    lines = []
    summary_lines = [
        f"# Training Export: {slug}",
        "",
        f"- Created At: {now_iso()}",
        f"- Agent ID: {normalized_agent_id or '-'}",
        f"- Task Type: {normalized_task_type or '-'}",
        f"- Sample Count: {len(items)}",
        "",
    ]
    for item in items:
        task_spec = item.get("taskSpec", {}) if isinstance(item.get("taskSpec", {}), dict) else {}
        prompt = str(item.get("sourceText", "")).strip()
        completion = json.dumps(task_spec, ensure_ascii=False)
        lines.append(json.dumps({"prompt": prompt, "completion": completion}, ensure_ascii=False))
        summary_lines.extend(
            [
                f"## {str(item.get('id', '')).strip() or 'sample'}",
                "",
                f"- Source: {prompt or '-'}",
                f"- Correction: {str(item.get('correctionText', '')).strip() or '-'}",
                f"- Task Type: {str(task_spec.get('taskType', '')).strip() or '-'}",
                f"- Agent ID: {str(item.get('agentId', '')).strip() or '-'}",
                f"- Agent Name: {str(item.get('agentName', '')).strip() or '-'}",
                "",
                "```json",
                completion,
                "```",
                "",
            ]
        )
    jsonl_path.write_text("\n".join(lines), encoding="utf-8")
    summary_path.write_text("\n".join(summary_lines), encoding="utf-8")
    return {
        "ok": True,
        "count": len(items),
        "jsonlPath": str(jsonl_path),
        "summaryPath": str(summary_path),
    }
