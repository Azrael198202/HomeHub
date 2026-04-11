from __future__ import annotations

import json
import math
import re
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from server_components.semantic_vector_backends import VECTOR_DIMENSION, make_dense_vector
except ModuleNotFoundError:
    from runtime.server_components.semantic_vector_backends import VECTOR_DIMENSION, make_dense_vector


MEMORY_FILE = Path(__file__).resolve().parent / "data" / "network_route_memory.json"
MAX_ITEMS = 800
SCHEMA_VERSION = 1


def _now_iso() -> str:
    return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")


def _tokenize(text: str) -> list[str]:
    raw = str(text or "").strip().lower()
    if not raw:
        return []
    ascii_parts = re.findall(r"[a-z0-9]{2,}", raw)
    cjk_parts = re.findall(r"[\u4e00-\u9fff]{1,6}", raw)
    return ascii_parts + cjk_parts


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


def _default_routes() -> list[dict[str, Any]]:
    seeds = [
        {
            "routeKey": "weather",
            "summary": "Live weather, rain, temperature, forecast, daily conditions.",
            "examples": [
                "东京今天的天气怎么样",
                "今天会下雨吗",
                "what is the weather today",
            ],
            "preferredSources": ["weathernews.jp", "weather.com", "weather.gov"],
            "allowedDomains": ["weathernews.jp", "weather.com", "weather.gov"],
            "queryPatterns": [
                "{query}",
                "{query} 实时天气 气温",
                "{query} 今日天气 最高 最低 气温",
                "{query} weather today forecast",
            ],
        },
        {
            "routeKey": "flight",
            "summary": "Flights, airfare, airline schedules, route timing, ticket price lookups.",
            "examples": [
                "东京到旧金山的机票时间和票价",
                "flight time and fare from Tokyo to San Francisco",
                "航班票价和起飞时间",
            ],
            "preferredSources": ["flightconnections.com", "trip.com", "skyscanner.net", "kayak.com", "expedia.com", "jal.co.jp", "ana.co.jp"],
            "allowedDomains": ["flightconnections.com", "trip.com", "skyscanner.net", "kayak.com", "expedia.com", "jal.co.jp", "ana.co.jp"],
            "queryPatterns": [
                "{query}",
                "{query} 起飞 时间 票价",
                "{query} 航班 时间 价格",
                "{query} flight time fare",
            ],
        },
        {
            "routeKey": "train",
            "summary": "Trains, railways, shinkansen, timetables, rail fares and ticket costs.",
            "examples": [
                "福冈到大阪的新干线时间和费用",
                "东京到大阪火车票时间和票价",
                "shinkansen timetable and fare",
            ],
            "preferredSources": ["navitime.co.jp", "smart-ex.jp", "jr-central.co.jp", "jr-odekake.net"],
            "allowedDomains": ["navitime.co.jp", "smart-ex.jp", "jr-central.co.jp", "jr-odekake.net"],
            "queryPatterns": [
                "{query}",
                "{query} 新干线 时间 费用",
                "{query} 列车 时间 票价",
                "{query} train timetable price",
            ],
        },
        {
            "routeKey": "apple-purchase",
            "summary": "Apple device recommendations, Mac purchase advice, official product pricing.",
            "examples": [
                "MacBook Air 和 MacBook Pro 怎么选",
                "Apple 官网 MacBook Air 起售价",
                "which MacBook should I buy",
            ],
            "preferredSources": ["apple.com", "support.apple.com"],
            "allowedDomains": ["apple.com", "support.apple.com"],
            "queryPatterns": [
                "{query}",
                "{query} 推荐 型号 价格",
                "{query} Apple 官网 价格",
                "{query} Apple official price",
            ],
        },
        {
            "routeKey": "recipe",
            "summary": "Recipe lookup, ingredients, cooking steps, family meal ideas.",
            "examples": [
                "给我一个鸡肉咖喱菜谱",
                "早餐菜谱和做法",
                "recipe ingredients and steps",
            ],
            "preferredSources": ["cookpad.com", "allrecipes.com", "delish.com", "kurashiru.com"],
            "allowedDomains": ["cookpad.com", "allrecipes.com", "delish.com", "kurashiru.com"],
            "queryPatterns": [
                "{query}",
                "{query} 菜谱 配料 做法",
                "{query} 做法 食材 步骤",
                "{query} recipe ingredients steps",
            ],
        },
        {
            "routeKey": "news",
            "summary": "Latest news, hot topics, headline summaries, current events.",
            "examples": [
                "今天日本有什么热点新闻",
                "latest headline news summary",
                "热点新闻摘要",
            ],
            "preferredSources": ["reuters.com", "apnews.com", "nhk.or.jp", "bbc.com"],
            "allowedDomains": ["reuters.com", "apnews.com", "nhk.or.jp", "bbc.com"],
            "queryPatterns": [
                "{query}",
                "{query} 最新 新闻 摘要",
                "{query} 热点 新闻 来源",
                "{query} latest news summary",
            ],
        },
        {
            "routeKey": "stocks",
            "summary": "Stock price, market quotes, daily movement, live equity information.",
            "examples": [
                "英伟达今天的股价是多少",
                "苹果公司股票价格",
                "stock price today",
            ],
            "preferredSources": ["finance.yahoo.com", "marketwatch.com", "nasdaq.com", "nikkei.com"],
            "allowedDomains": ["finance.yahoo.com", "marketwatch.com", "nasdaq.com", "nikkei.com"],
            "queryPatterns": [
                "{query}",
                "{query} 今日 股价 涨跌",
                "{query} 最新 股票 价格",
                "{query} stock price today",
            ],
        },
        {
            "routeKey": "knowledge",
            "summary": "Factual explanations, educational concepts, definitions, evergreen knowledge.",
            "examples": [
                "光合作用是什么",
                "为什么要通分",
                "what is Time Machine",
            ],
            "preferredSources": ["wikipedia.org", "britannica.com", "support.apple.com"],
            "allowedDomains": [],
            "queryPatterns": [
                "{query}",
                "{query} 是什么",
                "{query} 原理 解释",
                "{query} explanation",
            ],
        },
    ]
    items: list[dict[str, Any]] = []
    for route in seeds:
        for example in route["examples"]:
            search_text = " ".join(
                part
                for part in [
                    route["routeKey"],
                    route["summary"],
                    example,
                    " ".join(route.get("preferredSources", [])),
                ]
                if part
            )
            items.append(
                {
                    "id": f"network-route-seed-{route['routeKey']}-{abs(hash(example))}",
                    "routeKey": route["routeKey"],
                    "summary": route["summary"],
                    "sourceText": example,
                    "searchText": search_text,
                    "preferredSources": list(route.get("preferredSources", [])),
                    "allowedDomains": list(route.get("allowedDomains", [])),
                    "queryPatterns": list(route.get("queryPatterns", [])),
                    "accepted": True,
                    "seed": True,
                    "createdAt": _now_iso(),
                    "updatedAt": _now_iso(),
                    "embedding": _embedding(search_text),
                    "embeddingSchemaVersion": SCHEMA_VERSION,
                }
            )
    return items


def _default_payload() -> dict[str, Any]:
    return {
        "meta": {
            "schemaVersion": "1.0",
            "brainFamily": "homehub-network-route-memory",
            "updatedAt": _now_iso(),
        },
        "items": _default_routes(),
    }


def _ensure_parent() -> None:
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)


def load_network_route_memory() -> dict[str, Any]:
    if not MEMORY_FILE.exists():
        payload = _default_payload()
        save_network_route_memory(payload)
        return payload
    try:
        payload = json.loads(MEMORY_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        payload = _default_payload()
    if not isinstance(payload, dict):
        payload = _default_payload()
    items = payload.get("items", [])
    if not isinstance(items, list) or not items:
        payload = _default_payload()
    return payload


def save_network_route_memory(payload: dict[str, Any]) -> None:
    _ensure_parent()
    body = {
        "meta": payload.get("meta", {}) if isinstance(payload, dict) else {},
        "items": payload.get("items", []) if isinstance(payload, dict) else [],
    }
    body["meta"]["updatedAt"] = _now_iso()
    MEMORY_FILE.write_text(json.dumps(body, ensure_ascii=False, indent=2), encoding="utf-8")


def classify_network_route(query_text: str, limit: int = 3, threshold: float = 0.16) -> list[dict[str, Any]]:
    query = str(query_text or "").strip()
    if not query:
        return []
    query_embedding = _embedding(query)
    scored: list[dict[str, Any]] = []
    for item in load_network_route_memory().get("items", []):
        if not isinstance(item, dict) or not item.get("accepted", True):
            continue
        score = _dense_cosine(query_embedding, item.get("embedding", []))
        if score < threshold:
            continue
        scored.append({"score": round(score, 3), "item": item})
    scored.sort(key=lambda entry: (entry["score"], str(entry["item"].get("updatedAt", ""))), reverse=True)
    return scored[: max(1, limit)]


def best_network_route(query_text: str) -> dict[str, Any]:
    matches = classify_network_route(query_text, limit=1)
    if matches:
        item = matches[0]["item"]
        return {
            "routeKey": str(item.get("routeKey", "")).strip(),
            "score": float(matches[0].get("score", 0.0) or 0.0),
            "preferredSources": list(item.get("preferredSources", [])) if isinstance(item.get("preferredSources", []), list) else [],
            "allowedDomains": list(item.get("allowedDomains", [])) if isinstance(item.get("allowedDomains", []), list) else [],
            "queryPatterns": list(item.get("queryPatterns", [])) if isinstance(item.get("queryPatterns", []), list) else [],
            "summary": str(item.get("summary", "")).strip(),
        }
    return {
        "routeKey": "knowledge",
        "score": 0.0,
        "preferredSources": [],
        "allowedDomains": [],
        "queryPatterns": ["{query}", "{query} 是什么", "{query} explanation"],
        "summary": "Fallback semantic route for general web research.",
    }


def remember_network_route_example(
    query_text: str,
    route_key: str,
    preferred_sources: list[str] | None = None,
    allowed_domains: list[str] | None = None,
    query_patterns: list[str] | None = None,
    summary: str = "",
) -> dict[str, Any] | None:
    query = str(query_text or "").strip()
    route = str(route_key or "").strip()
    if not query or not route:
        return None
    payload = load_network_route_memory()
    items = payload.get("items", [])
    if not isinstance(items, list):
        items = []
    normalized_patterns = [str(item).strip() for item in (query_patterns or []) if str(item).strip()]
    normalized_sources = [str(item).strip() for item in (preferred_sources or []) if str(item).strip()]
    normalized_domains = [str(item).strip() for item in (allowed_domains or []) if str(item).strip()]
    search_text = " ".join(
        part
        for part in [
            route,
            str(summary or "").strip(),
            query,
            " ".join(normalized_sources),
        ]
        if part
    )
    normalized = {
        "id": f"network-route-{datetime.now().strftime('%Y%m%d%H%M%S%f')}",
        "routeKey": route,
        "summary": str(summary or "").strip(),
        "sourceText": query,
        "searchText": search_text,
        "preferredSources": normalized_sources,
        "allowedDomains": normalized_domains,
        "queryPatterns": normalized_patterns or ["{query}"],
        "accepted": True,
        "seed": False,
        "createdAt": _now_iso(),
        "updatedAt": _now_iso(),
        "embedding": _embedding(search_text),
        "embeddingSchemaVersion": SCHEMA_VERSION,
    }
    dedup_key = f"{route}::{query.lower()}"
    kept: list[dict[str, Any]] = []
    replaced = False
    for current in items:
        if not isinstance(current, dict):
            continue
        current_key = f"{str(current.get('routeKey', '')).strip()}::{str(current.get('sourceText', '')).strip().lower()}"
        if current_key == dedup_key:
            kept.append({**current, **normalized})
            replaced = True
        else:
            kept.append(current)
    if not replaced:
        kept.insert(0, normalized)
    payload["items"] = kept[:MAX_ITEMS]
    save_network_route_memory(payload)
    return normalized


def build_semantic_route_query_candidates(query_text: str, locale: str, route: dict[str, Any]) -> list[str]:
    query = str(query_text or "").strip()
    if not query:
        return []
    patterns = route.get("queryPatterns", []) if isinstance(route.get("queryPatterns", []), list) else []
    candidates = [query]
    for pattern in patterns:
        value = str(pattern or "").strip()
        if not value:
            continue
        candidates.append(value.replace("{query}", query).replace("{locale}", str(locale or "").strip()))
    unique: list[str] = []
    seen = set()
    for item in candidates:
        normalized = str(item or "").strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        unique.append(normalized)
    return unique
