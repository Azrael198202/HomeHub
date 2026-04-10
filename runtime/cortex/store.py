from __future__ import annotations

import json
import tempfile
import threading
import time
from pathlib import Path


class CortexStore:
    _path_locks: dict[str, threading.RLock] = {}
    _path_locks_guard = threading.Lock()

    def __init__(self, runtime_root: Path):
        self.runtime_root = runtime_root

    @property
    def storage_path(self) -> Path:
        agents_dir = self.runtime_root / "agents"
        agents_dir.mkdir(parents=True, exist_ok=True)
        return agents_dir / "cortex_profiles.json"

    def load(self) -> dict:
        path = self.storage_path
        with self._lock_for(path):
            if not path.exists():
                return {"meta": self.default_meta(), "items": {}}
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError):
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
        target = self.storage_path
        target.parent.mkdir(parents=True, exist_ok=True)
        with self._lock_for(target):
            temp_path: Path | None = None
            try:
                with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=target.parent, prefix=f"{target.stem}-", suffix=".tmp", delete=False) as handle:
                    handle.write(json.dumps(body, ensure_ascii=False, indent=2))
                    handle.flush()
                    temp_path = Path(handle.name)
                self._replace_with_retry(temp_path, target)
            finally:
                if temp_path and temp_path.exists():
                    temp_path.unlink(missing_ok=True)

    def default_meta(self) -> dict:
        return {
            "schemaVersion": "2.0",
            "brainFamily": "homehub-exec-brain",
        }

    @classmethod
    def _lock_for(cls, path: Path) -> threading.RLock:
        key = str(path.resolve())
        with cls._path_locks_guard:
            lock = cls._path_locks.get(key)
            if lock is None:
                lock = threading.RLock()
                cls._path_locks[key] = lock
            return lock

    def _replace_with_retry(self, source: Path, target: Path) -> None:
        delays = (0.05, 0.1, 0.2, 0.35, 0.5, 0.75)
        last_error: PermissionError | None = None
        for delay in (*delays, 0.0):
            try:
                source.replace(target)
                return
            except PermissionError as exc:
                last_error = exc
                if delay <= 0:
                    break
                time.sleep(delay)
        if last_error is not None:
            raise last_error
