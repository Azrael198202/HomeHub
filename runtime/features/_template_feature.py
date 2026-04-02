from __future__ import annotations

from copy import deepcopy

from .base import HomeHubFeature, RuntimeBridge


class Feature(HomeHubFeature):
    feature_id = "template-feature"
    feature_name = "Template Feature"
    version = "1.0.0"

    def descriptor(self) -> dict:
        data = super().descriptor()
        data["summary"] = "Use this file as the template for future HomeHub feature modules."
        return data

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        return None

    def enhance_household_modules(self, modules: list[dict], locale: str, runtime: RuntimeBridge) -> list[dict]:
        return deepcopy(modules)

    def dashboard_payload(self, locale: str, runtime: RuntimeBridge) -> dict:
        return {}

    def handle_api(self, method: str, path: str, query: dict, body: dict | None, runtime: RuntimeBridge) -> dict | None:
        return None

    def reset(self, runtime: RuntimeBridge) -> None:
        return None


def load_feature() -> HomeHubFeature:
    return Feature()
