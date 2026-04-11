from __future__ import annotations

from typing import Any, Callable


def should_block_network_for_local_request(
    user_text: str,
    route: dict[str, Any],
    looks_like_local_file_request_fn: Callable[[str], bool],
) -> bool:
    if not callable(looks_like_local_file_request_fn):
        return False
    if looks_like_local_file_request_fn(user_text):
        return True
    task_spec = route.get("taskSpec", {}) if isinstance(route.get("taskSpec", {}), dict) else {}
    task_type = str(task_spec.get("taskType", "")).strip()
    return task_type == "document_workflow" and looks_like_local_file_request_fn(user_text)
