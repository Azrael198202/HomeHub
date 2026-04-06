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
            return {"items": {}}
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {"items": {}}
        if not isinstance(data, dict):
            return {"items": {}}
        items = data.get("items", {})
        return {"items": items if isinstance(items, dict) else {}}

    def save(self, payload: dict) -> None:
        self.storage_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
