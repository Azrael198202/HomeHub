from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable


ApiResponse = dict[str, Any]


@dataclass
class RuntimeBridge:
    root: Path
    get_setting: Callable[[str, Any], Any]
    get_secret: Callable[[str, Any], Any]
    openai_json: Callable[[str, str, str], dict[str, Any] | None]
    analyze_image: Callable[[str, str, str, str], dict[str, Any] | None] | None = None
    network_lookup: Callable[[str, str, str, list[str] | None, list[str] | None], dict[str, Any]] | None = None
    invoke_feature: Callable[[str, dict[str, Any], str], dict[str, Any] | None] | None = None
    log: Callable[[str], None] | None = None
    state: dict[str, Any] = field(default_factory=dict)

    def now_iso(self) -> str:
        from datetime import datetime

        return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")

    def emit_log(self, message: str) -> None:
        if self.log:
            self.log(message)

    def call_feature(self, feature_id: str, payload: dict[str, Any], locale: str) -> dict[str, Any] | None:
        if not self.invoke_feature:
            return None
        return self.invoke_feature(feature_id, payload, locale)


class HomeHubFeature:
    feature_id = "base"
    feature_name = "Base Feature"
    version = "1.0.0"

    def descriptor(self) -> dict[str, Any]:
        return {
            "id": self.feature_id,
            "name": self.feature_name,
            "version": self.version,
        }

    def voice_intents(self) -> list[dict[str, Any]]:
        return []

    def match_voice_intent(self, message: str, locale: str, runtime: RuntimeBridge) -> dict[str, Any] | None:
        return None

    def on_refresh(self, runtime: RuntimeBridge) -> None:
        return None

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict[str, Any] | None:
        return None

    def enhance_household_modules(
        self,
        modules: list[dict[str, Any]],
        locale: str,
        runtime: RuntimeBridge,
    ) -> list[dict[str, Any]]:
        return modules

    def dashboard_payload(self, locale: str, runtime: RuntimeBridge) -> dict[str, Any]:
        return {}

    def list_agent_types(self, locale: str, runtime: RuntimeBridge) -> list[dict[str, Any]]:
        return []

    def handle_api(
        self,
        method: str,
        path: str,
        query: dict[str, Any],
        body: dict[str, Any] | None,
        runtime: RuntimeBridge,
    ) -> ApiResponse | None:
        return None

    def reset(self, runtime: RuntimeBridge) -> None:
        return None
