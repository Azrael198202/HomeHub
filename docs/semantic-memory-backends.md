# HomeHub Semantic Memory Backends

HomeHub now uses a pluggable semantic-memory backend with a safe local mirror.

## Default behavior

- Config file: `runtime/semantic_memory.local.json`
- Default backend: `qdrant`
- Local mirror: `true`
- Local training/sample store: `runtime/data/task_semantic_memory.json`

If Qdrant is not configured or not reachable yet, HomeHub automatically falls back to the local JSON mirror and keeps learning.

## Supported backends

### Qdrant

- Set `backend` to `qdrant`
- Fill `qdrant.url`
- Optional: `qdrant.apiKey`

Qdrant uses REST, so no extra Python package is required.

### pgvector

- Set `backend` to `pgvector`
- Fill `pgvector.dsn`
- Optional package file: `runtime/requirements.semantic-memory.txt`

HomeHub will try to create the `vector` extension and the storage table automatically.

### Milvus

- Set `backend` to `milvus`
- Fill `milvus.uri`
- Optional: `milvus.token`
- Optional package file: `runtime/requirements.semantic-memory.txt`

HomeHub will try to create and load the collection automatically.

## Safety model

- HomeHub always prefers the configured vector backend when it is reachable.
- If the backend is unavailable, HomeHub falls back to the local JSON mirror.
- This keeps the brain learnable, exportable, and resilient.

## Current runtime visibility

`/api/semantic-memory` now exposes:

- `configuredBackend`
- `activeBackend`
- `fallbackUsed`
- `detail`
- `storagePath`
- `configPath`
