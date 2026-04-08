from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass


VECTOR_DIMENSION = 256


@dataclass
class BackendStatus:
    backend: str
    available: bool
    detail: str = ""


def make_dense_vector(tokens: list[str], dimension: int = VECTOR_DIMENSION) -> list[float]:
    if not tokens:
        return [0.0] * dimension
    bucket = [0.0] * dimension
    for token in tokens:
        token_text = str(token or "").strip()
        if not token_text:
            continue
        index = hash(token_text) % dimension
        sign = -1.0 if (hash(f"sign:{token_text}") % 2) else 1.0
        bucket[index] += sign
    norm = sum(value * value for value in bucket) ** 0.5
    if norm <= 0:
        return bucket
    return [round(value / norm, 6) for value in bucket]


def _json_headers(api_key: str = "") -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["api-key"] = api_key
    return headers


class QdrantBackend:
    name = "qdrant"

    def __init__(self, config: dict):
        self.url = str(config.get("url", "")).rstrip("/")
        self.collection = str(config.get("collection", "homehub_semantic_memory")).strip() or "homehub_semantic_memory"
        self.api_key = str(config.get("apiKey", "")).strip()
        self.timeout = float(config.get("timeoutSeconds", 3) or 3)

    def _request(self, method: str, path: str, payload: dict | None = None) -> dict:
        if not self.url:
            raise RuntimeError("Missing Qdrant URL")
        data = None
        if payload is not None:
            data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            f"{self.url}{path}",
            data=data,
            headers=_json_headers(self.api_key),
            method=method,
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            body = response.read().decode("utf-8")
        return json.loads(body) if body else {}

    def status(self) -> BackendStatus:
        if not self.url:
            return BackendStatus(self.name, False, "missing-url")
        try:
            self._request("GET", "/collections")
            return BackendStatus(self.name, True, "connected")
        except Exception as exc:
            return BackendStatus(self.name, False, str(exc))

    def ensure_collection(self) -> None:
        self._request(
            "PUT",
            f"/collections/{self.collection}",
            {
                "vectors": {
                    "size": VECTOR_DIMENSION,
                    "distance": "Cosine",
                }
            },
        )

    def upsert(self, item: dict, vector: list[float], search_text: str) -> None:
        self.ensure_collection()
        self._request(
            "PUT",
            f"/collections/{self.collection}/points?wait=true",
            {
                "points": [
                    {
                        "id": str(item.get("id", "")),
                        "vector": vector,
                        "payload": {
                            "locale": str(item.get("locale", "")).strip(),
                            "accepted": bool(item.get("accepted", True)),
                            "searchText": search_text,
                            "item": item,
                        },
                    }
                ]
            },
        )

    def query(self, vector: list[float], locale: str, limit: int) -> list[dict]:
        self.ensure_collection()
        payload = {
            "vector": vector,
            "limit": max(1, limit),
            "with_payload": True,
        }
        if locale:
            payload["filter"] = {
                "must": [
                    {"key": "locale", "match": {"value": locale}},
                    {"key": "accepted", "match": {"value": True}},
                ]
            }
        result = self._request("POST", f"/collections/{self.collection}/points/search", payload)
        points = result.get("result", []) if isinstance(result, dict) else []
        matches = []
        for point in points:
            payload_data = point.get("payload", {}) if isinstance(point, dict) else {}
            item = payload_data.get("item", {}) if isinstance(payload_data, dict) else {}
            matches.append({"score": round(float(point.get("score", 0.0) or 0.0), 3), "item": item})
        return matches

    def delete_for_agent(self, agent_id: str) -> int:
        if not agent_id:
            return 0
        self.ensure_collection()
        self._request(
            "POST",
            f"/collections/{self.collection}/points/delete?wait=true",
            {
                "filter": {
                    "must": [
                        {"key": "item.agentId", "match": {"value": agent_id}},
                    ]
                }
            },
        )
        return 0


class PgVectorBackend:
    name = "pgvector"

    def __init__(self, config: dict):
        self.dsn = str(config.get("dsn", "")).strip()
        self.table = str(config.get("table", "homehub_semantic_memory")).strip() or "homehub_semantic_memory"

    def _connect(self):
        try:
            import psycopg
        except ModuleNotFoundError as exc:
            raise RuntimeError("psycopg-not-installed") from exc
        if not self.dsn:
            raise RuntimeError("missing-dsn")
        return psycopg.connect(self.dsn)

    def status(self) -> BackendStatus:
        try:
            with self._connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("select 1")
                    cursor.fetchone()
            return BackendStatus(self.name, True, "connected")
        except Exception as exc:
            return BackendStatus(self.name, False, str(exc))

    def ensure_table(self) -> None:
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("create extension if not exists vector")
                cursor.execute(
                    f"""
                    create table if not exists {self.table} (
                        id text primary key,
                        locale text not null,
                        accepted boolean not null default true,
                        agent_id text not null default '',
                        search_text text not null,
                        payload jsonb not null,
                        embedding vector({VECTOR_DIMENSION}) not null,
                        updated_at timestamptz not null default now()
                    )
                    """
                )
            connection.commit()

    def upsert(self, item: dict, vector: list[float], search_text: str) -> None:
        self.ensure_table()
        vector_literal = "[" + ",".join(str(value) for value in vector) + "]"
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"""
                    insert into {self.table} (id, locale, accepted, agent_id, search_text, payload, embedding, updated_at)
                    values (%s, %s, %s, %s, %s, %s::jsonb, %s::vector, now())
                    on conflict (id) do update set
                        locale = excluded.locale,
                        accepted = excluded.accepted,
                        agent_id = excluded.agent_id,
                        search_text = excluded.search_text,
                        payload = excluded.payload,
                        embedding = excluded.embedding,
                        updated_at = now()
                    """,
                    (
                        str(item.get("id", "")),
                        str(item.get("locale", "")).strip(),
                        bool(item.get("accepted", True)),
                        str(item.get("agentId", "")).strip(),
                        search_text,
                        json.dumps(item, ensure_ascii=False),
                        vector_literal,
                    ),
                )
            connection.commit()

    def query(self, vector: list[float], locale: str, limit: int) -> list[dict]:
        self.ensure_table()
        vector_literal = "[" + ",".join(str(value) for value in vector) + "]"
        sql = f"""
            select payload, 1 - (embedding <=> %s::vector) as score
            from {self.table}
            where accepted = true
        """
        params: list[object] = [vector_literal]
        if locale:
            sql += " and locale = %s"
            params.append(locale)
        sql += " order by embedding <=> %s::vector asc limit %s"
        params.extend([vector_literal, max(1, limit)])
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, params)
                rows = cursor.fetchall()
        return [{"score": round(float(score or 0.0), 3), "item": payload if isinstance(payload, dict) else json.loads(payload)} for payload, score in rows]

    def delete_for_agent(self, agent_id: str) -> int:
        if not agent_id:
            return 0
        self.ensure_table()
        with self._connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"delete from {self.table} where agent_id = %s", (agent_id,))
                removed = cursor.rowcount or 0
            connection.commit()
        return int(removed)


class MilvusBackend:
    name = "milvus"

    def __init__(self, config: dict):
        self.uri = str(config.get("uri", "")).strip()
        self.token = str(config.get("token", "")).strip()
        self.collection = str(config.get("collection", "homehub_semantic_memory")).strip() or "homehub_semantic_memory"

    def _client(self):
        try:
            from pymilvus import Collection, CollectionSchema, DataType, FieldSchema, connections, utility
        except ModuleNotFoundError as exc:
            raise RuntimeError("pymilvus-not-installed") from exc
        if not self.uri:
            raise RuntimeError("missing-uri")
        connections.connect(alias="homehub_semantic_memory", uri=self.uri, token=self.token or None)
        return Collection, CollectionSchema, DataType, FieldSchema, utility

    def status(self) -> BackendStatus:
        try:
            _, _, _, _, utility = self._client()
            utility.list_collections(using="homehub_semantic_memory")
            return BackendStatus(self.name, True, "connected")
        except Exception as exc:
            return BackendStatus(self.name, False, str(exc))

    def ensure_collection(self):
        Collection, CollectionSchema, DataType, FieldSchema, utility = self._client()
        if not utility.has_collection(self.collection, using="homehub_semantic_memory"):
            schema = CollectionSchema(
                [
                    FieldSchema(name="id", dtype=DataType.VARCHAR, max_length=128, is_primary=True, auto_id=False),
                    FieldSchema(name="locale", dtype=DataType.VARCHAR, max_length=32),
                    FieldSchema(name="accepted", dtype=DataType.BOOL),
                    FieldSchema(name="agent_id", dtype=DataType.VARCHAR, max_length=128),
                    FieldSchema(name="search_text", dtype=DataType.VARCHAR, max_length=4096),
                    FieldSchema(name="payload_json", dtype=DataType.VARCHAR, max_length=32768),
                    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=VECTOR_DIMENSION),
                ]
            )
            collection = Collection(self.collection, schema=schema, using="homehub_semantic_memory")
            collection.create_index("embedding", {"index_type": "AUTOINDEX", "metric_type": "COSINE"})
        collection = Collection(self.collection, using="homehub_semantic_memory")
        collection.load()
        return collection

    def upsert(self, item: dict, vector: list[float], search_text: str) -> None:
        collection = self.ensure_collection()
        collection.upsert(
            [
                [str(item.get("id", ""))],
                [str(item.get("locale", "")).strip()],
                [bool(item.get("accepted", True))],
                [str(item.get("agentId", "")).strip()],
                [search_text[:4096]],
                [json.dumps(item, ensure_ascii=False)[:32768]],
                [vector],
            ]
        )

    def query(self, vector: list[float], locale: str, limit: int) -> list[dict]:
        collection = self.ensure_collection()
        expr = "accepted == true"
        if locale:
            expr += f' && locale == "{locale}"'
        result = collection.search(
            data=[vector],
            anns_field="embedding",
            param={"metric_type": "COSINE"},
            limit=max(1, limit),
            expr=expr,
            output_fields=["payload_json"],
        )
        matches = []
        for hit in result[0] if result else []:
            payload_json = hit.entity.get("payload_json") if hasattr(hit, "entity") else ""
            item = json.loads(payload_json) if payload_json else {}
            matches.append({"score": round(float(hit.score or 0.0), 3), "item": item})
        return matches

    def delete_for_agent(self, agent_id: str) -> int:
        if not agent_id:
            return 0
        collection = self.ensure_collection()
        collection.delete(expr=f'agent_id == "{agent_id}"')
        return 0


def build_backend(config: dict):
    backend_type = str(config.get("backend", "json")).strip().lower()
    if backend_type == "qdrant":
        return QdrantBackend(config.get("qdrant", {}) if isinstance(config.get("qdrant", {}), dict) else {})
    if backend_type == "pgvector":
        return PgVectorBackend(config.get("pgvector", {}) if isinstance(config.get("pgvector", {}), dict) else {})
    if backend_type == "milvus":
        return MilvusBackend(config.get("milvus", {}) if isinstance(config.get("milvus", {}), dict) else {})
    return None

