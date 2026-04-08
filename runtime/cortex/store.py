from __future__ import annotations

import json
from pathlib import Path


class CortexStore:
    def __init__(self, runtime_root: Path):
        self.runtime_root = runtime_root

    @property
    def storage_path(self) -> Path:
        agents_dir = self.runtime_root / "agents"
        agents_dir.mkdir(parents=True, exist_ok=True)
        return agents_dir / "cortex_profiles.json"

    def load(self) -> dict:
        path = self.storage_path
        if not path.exists():
            return {"meta": self.default_meta(), "items": {}}
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {"meta": self.default_meta(), "items": {}}
        if not isinstance(data, dict):
            return {"meta": self.default_meta(), "items": {}}
        meta = data.get("meta", {})
        items = data.get("items", {})
        return {
            "meta": meta if isinstance(meta, dict) else self.default_meta(),
            "items": items if isinstance(items, dict) else {},
        }

    def save(self, payload: dict) -> None:
        body = {
            "meta": payload.get("meta", self.default_meta()) if isinstance(payload, dict) else self.default_meta(),
            "items": payload.get("items", {}) if isinstance(payload, dict) else {},
        }
        self.storage_path.write_text(json.dumps(body, ensure_ascii=False, indent=2), encoding="utf-8")

    def default_meta(self) -> dict:
        return {
            "schemaVersion": "2.0",
            "brainFamily": "homehub-exec-brain",
        }
