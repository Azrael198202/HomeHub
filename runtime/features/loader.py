from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any

from .base import HomeHubFeature, RuntimeBridge


class FeatureManager:
    def __init__(self, features_dir: Path):
        self.features_dir = features_dir
        self._signature: tuple[tuple[str, int], ...] = ()
        self._features: list[HomeHubFeature] = []

    def _compute_signature(self) -> tuple[tuple[str, int], ...]:
        items: list[tuple[str, int]] = []
        if not self.features_dir.exists():
            return ()
        for path in sorted(self.features_dir.glob("*.py")):
            if path.name.startswith("_") or path.name in {"__init__.py", "base.py", "loader.py"}:
                continue
            items.append((path.name, path.stat().st_mtime_ns))
        return tuple(items)

    def _load_feature_from_path(self, path: Path) -> HomeHubFeature:
        package_name = __package__ or "features"
        module_name = f"{package_name}.{path.stem}__dynamic_{path.stat().st_mtime_ns}"
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"Unable to load feature spec for {path.name}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)

        factory = getattr(module, "load_feature", None)
        if callable(factory):
            feature = factory()
        else:
            feature_cls = getattr(module, "Feature", None)
            if feature_cls is None:
                raise RuntimeError(f"Feature file {path.name} must expose load_feature() or Feature.")
            feature = feature_cls()

        if not isinstance(feature, HomeHubFeature):
            raise RuntimeError(f"Feature file {path.name} did not return a HomeHubFeature instance.")
        return feature

    def refresh(self, runtime: RuntimeBridge) -> None:
        signature = self._compute_signature()
        if signature == self._signature:
            for feature in self._features:
                feature.on_refresh(runtime)
            return

        loaded: list[HomeHubFeature] = []
        for filename, _ in signature:
            path = self.features_dir / filename
            feature = self._load_feature_from_path(path)
            feature.on_refresh(runtime)
            loaded.append(feature)

        self._features = loaded
        self._signature = signature
        runtime.emit_log(f"Feature scan loaded {len(self._features)} module(s).")

    def list_features(self, runtime: RuntimeBridge) -> list[dict[str, Any]]:
        self.refresh(runtime)
        return [feature.descriptor() for feature in self._features]

    def route_voice_intent(self, message: str, locale: str, runtime: RuntimeBridge) -> dict[str, Any]:
        self.refresh(runtime)
        matches: list[dict[str, Any]] = []
        for feature in self._features:
            match = feature.match_voice_intent(message, locale, runtime)
            if not match:
                continue
            item = dict(match)
            item.setdefault("featureId", feature.feature_id)
            item.setdefault("featureName", feature.feature_name)
            item.setdefault("score", 0.5)
            matches.append(item)
        matches.sort(key=lambda item: item.get("score", 0.0), reverse=True)
        return {
            "selected": matches[0] if matches else None,
            "candidates": matches,
        }

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict[str, Any] | None:
        self.refresh(runtime)
        for feature in self._features:
            result = feature.handle_voice_chat(message, locale, runtime)
            if result:
                return result
        return None

    def dispatch_voice_intent(self, route: dict[str, Any] | None, message: str, locale: str, runtime: RuntimeBridge) -> dict[str, Any] | None:
        self.refresh(runtime)
        selected = (route or {}).get("selected")
        if not selected:
            return None
        feature_id = selected.get("featureId")
        for feature in self._features:
            if feature.feature_id != feature_id:
                continue
            result = feature.handle_voice_chat(message, locale, runtime)
            if result:
                result.setdefault("route", selected)
                return result
        return None

    def enhance_household_modules(
        self,
        modules: list[dict[str, Any]],
        locale: str,
        runtime: RuntimeBridge,
    ) -> list[dict[str, Any]]:
        self.refresh(runtime)
        current = modules
        for feature in self._features:
            current = feature.enhance_household_modules(current, locale, runtime)
        return current

    def dashboard_payload(self, locale: str, runtime: RuntimeBridge) -> dict[str, Any]:
        self.refresh(runtime)
        payload: dict[str, Any] = {}
        for feature in self._features:
            payload.update(feature.dashboard_payload(locale, runtime))
        return payload

    def list_agent_types(self, locale: str, runtime: RuntimeBridge) -> list[dict[str, Any]]:
        self.refresh(runtime)
        items: list[dict[str, Any]] = []
        for feature in self._features:
            items.extend(feature.list_agent_types(locale, runtime))
        return items

    def handle_api(
        self,
        method: str,
        path: str,
        query: dict[str, Any],
        body: dict[str, Any] | None,
        runtime: RuntimeBridge,
    ) -> dict[str, Any] | None:
        self.refresh(runtime)
        for feature in self._features:
            response = feature.handle_api(method, path, query, body, runtime)
            if response:
                return response
        return None

    def reset(self, runtime: RuntimeBridge) -> None:
        self.refresh(runtime)
        for feature in self._features:
            feature.reset(runtime)
