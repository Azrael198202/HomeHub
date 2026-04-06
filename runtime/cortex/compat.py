from __future__ import annotations


def truthy(value: object) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "on", "allow", "allowed"}
