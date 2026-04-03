from __future__ import annotations

import json
import re
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from ..base import HomeHubFeature, RuntimeBridge


BLUEPRINT = {
    "name": "家庭账单",
    "goal": "记录用户的消费并提供每周的消费总结和提醒",
}
API_ROOT = "/api/u5bb6_u5ead_u8d26_u5355"
API_ITEMS = "/api/u5bb6_u5ead_u8d26_u5355/items"
API_RUN = "/api/u5bb6_u5ead_u8d26_u5355/run"


class Feature(HomeHubFeature):
    feature_id = "u5bb6_u5ead_u8d26_u5355"
    feature_name = "家庭账单"
    version = "1.1.0"

    def descriptor(self) -> dict:
        data = super().descriptor()
        data["summary"] = BLUEPRINT["goal"]
        data["blueprint"] = BLUEPRINT
        data["api"] = [API_ROOT, API_ITEMS, API_RUN]
        data["voiceIntents"] = self.voice_intents()
        return data

    def voice_intents(self) -> list[dict]:
        return [{
            "id": f"{self.feature_id}-intent",
            "name": self.feature_name,
            "summary": "记录消费、统计今日或本周总额，并根据阈值给出预警。",
        }]

    def storage_path(self, runtime: RuntimeBridge) -> Path:
        data_dir = runtime.root / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir / f"{self.feature_id}.json"

    def now_local(self) -> datetime:
        return datetime.now().replace(second=0, microsecond=0)

    def now_iso(self) -> str:
        return self.now_local().isoformat(timespec="minutes")

    def default_store(self) -> dict:
        now = self.now_iso()
        return {
            "settings": {"enabled": True, "warningThreshold": 2000},
            "items": [],
            "recentActions": [{
                "id": f"{self.feature_id}-ready",
                "summary": f"{self.feature_name} is ready.",
                "createdAt": now,
            }],
            "lastRun": "",
            "lastSummary": {},
        }

    def load_store(self, runtime: RuntimeBridge) -> dict:
        path = self.storage_path(runtime)
        if not path.exists():
            store = self.default_store()
            self.save_store(store, runtime)
            return store
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            store = self.default_store()
            self.save_store(store, runtime)
            return store
        if not isinstance(data, dict):
            return self.default_store()
        return {
            "settings": data.get("settings", {}) if isinstance(data.get("settings"), dict) else {},
            "items": data.get("items", []) if isinstance(data.get("items"), list) else [],
            "recentActions": data.get("recentActions", []) if isinstance(data.get("recentActions"), list) else [],
            "lastRun": str(data.get("lastRun", "")),
            "lastSummary": data.get("lastSummary", {}) if isinstance(data.get("lastSummary"), dict) else {},
        }

    def save_store(self, store: dict, runtime: RuntimeBridge) -> None:
        self.storage_path(runtime).write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")

    def on_refresh(self, runtime: RuntimeBridge) -> None:
        runtime.state[self.feature_id] = self.load_store(runtime)

    def reset(self, runtime: RuntimeBridge) -> None:
        store = self.default_store()
        runtime.state[self.feature_id] = store
        self.save_store(store, runtime)

    def get_store(self, runtime: RuntimeBridge) -> dict:
        store = runtime.state.get(self.feature_id)
        if not isinstance(store, dict):
            store = self.load_store(runtime)
            runtime.state[self.feature_id] = store
        return store

    def append_action(self, runtime: RuntimeBridge, summary: str) -> None:
        store = self.get_store(runtime)
        stamp = self.now_iso()
        store.setdefault("recentActions", []).insert(0, {
            "id": f"{self.feature_id}-{stamp.replace(':', '').replace('-', '')}",
            "summary": summary,
            "createdAt": stamp,
        })
        del store["recentActions"][12:]
        self.save_store(store, runtime)

    def detect_amount(self, text: str) -> int | None:
        match = re.search(r"(\d+(?:\.\d+)?)\s*(?:日元|円|yen|jpy)", text.lower())
        if not match:
            match = re.search(r"(\d+(?:\.\d+)?)", text)
        if not match:
            return None
        try:
            return int(float(match.group(1)))
        except (TypeError, ValueError):
            return None

    def detect_category(self, text: str) -> str:
        category_map = {
            "买菜": "买菜",
            "超市": "买菜",
            "餐": "餐饮",
            "吃饭": "餐饮",
            "咖啡": "咖啡",
            "地铁": "交通",
            "电车": "交通",
            "交通": "交通",
            "账单": "账单",
            "水电": "账单",
        }
        for token, category in category_map.items():
            if token in text:
                return category
        return "其他"

    def should_record_expense(self, text: str) -> bool:
        return self.detect_amount(text) is not None and any(
            token in text for token in ["花了", "消费", "支出", "记账", "记到", "账单", "买了"]
        )

    def should_summarize(self, text: str) -> bool:
        return any(token in text for token in ["总消费", "总额", "花了多少钱", "花费多少", "消费多少", "超出", "预警"])

    def parse_threshold(self, text: str, store: dict) -> int:
        match = re.search(r"(\d{3,6})\s*(?:日元|円|yen|jpy)?", text.lower())
        if match and any(token in text for token in ["超过", "超出", "预警", "threshold"]):
            try:
                return int(match.group(1))
            except ValueError:
                pass
        return int(store.get("settings", {}).get("warningThreshold", 2000) or 2000)

    def add_expense_item(self, runtime: RuntimeBridge, amount: int, category: str, source_text: str) -> dict:
        store = self.get_store(runtime)
        item = {
            "id": f"{self.feature_id}-item-{self.now_iso().replace(':', '').replace('-', '')}",
            "amount": amount,
            "category": category,
            "currency": "JPY",
            "sourceText": source_text.strip(),
            "createdAt": self.now_iso(),
        }
        store.setdefault("items", []).insert(0, item)
        self.append_action(runtime, f"Recorded {amount} JPY for {category}.")
        self.save_store(store, runtime)
        return item

    def summarize_items(self, runtime: RuntimeBridge, period: str, threshold: int | None = None) -> dict:
        store = self.get_store(runtime)
        now = self.now_local()
        total = 0
        matched: list[dict] = []
        for item in store.get("items", []):
            try:
                created_at = datetime.fromisoformat(str(item.get("createdAt", "")))
            except ValueError:
                continue
            same_day = created_at.date() == now.date()
            same_week = created_at.isocalendar()[:2] == now.isocalendar()[:2]
            if (period == "today" and same_day) or (period == "week" and same_week):
                matched.append(item)
                total += int(item.get("amount", 0) or 0)
        effective_threshold = threshold if threshold is not None else int(store.get("settings", {}).get("warningThreshold", 2000) or 2000)
        summary = {
            "period": period,
            "total": total,
            "count": len(matched),
            "threshold": effective_threshold,
            "overThreshold": total > effective_threshold,
            "items": matched,
            "generatedAt": self.now_iso(),
        }
        store["lastSummary"] = summary
        store["lastRun"] = summary["generatedAt"]
        self.append_action(runtime, f"Calculated {period} total: {total} JPY.")
        self.save_store(store, runtime)
        return summary

    def build_summary_reply(self, summary: dict, locale: str, include_total_always: bool = True) -> str:
        total = int(summary.get("total", 0) or 0)
        threshold = int(summary.get("threshold", 2000) or 2000)
        over = bool(summary.get("overThreshold"))
        label = "今天" if summary.get("period") == "today" else "本周"
        if locale != "zh-CN":
            base = f"Your {summary.get('period', 'current')} total is {total} JPY."
            return base + (f" Warning: this is over the {threshold} JPY threshold." if over else "")
        base = f"{label}截至目前总消费是 {total} 日元。"
        if over:
            return base + f" 已超过 {threshold} 日元预警额度。"
        return base if include_total_always else ""

    def run_feature(self, runtime: RuntimeBridge, source: str, payload: dict | None = None) -> dict:
        request = dict(payload or {})
        store = self.get_store(runtime)
        store["lastRun"] = self.now_iso()
        action = str(request.get("action", "")).strip() or ("record_expense" if self.should_record_expense(str(request.get("message", ""))) else "report_today_total")
        if action == "record_expense":
            message = str(request.get("message", "")).strip()
            amount = int(request.get("amount", 0) or self.detect_amount(message) or 0)
            category = str(request.get("category", "")).strip() or self.detect_category(message)
            if amount <= 0:
                return {"ok": False, "error": "amount_required", "message": "No expense amount detected."}
            item = self.add_expense_item(runtime, amount, category, message)
            return {
                "ok": True,
                "action": action,
                "item": item,
                "reply": f"已记录您的消费：{category} {amount} 日元。",
            }
        period = str(request.get("period", "today")).strip().lower() or "today"
        threshold = request.get("threshold")
        try:
            threshold_value = int(threshold) if threshold is not None else None
        except (TypeError, ValueError):
            threshold_value = None
        summary = self.summarize_items(runtime, period, threshold_value)
        reply = self.build_summary_reply(summary, str(request.get("locale", "zh-CN")), bool(request.get("includeTotalAlways", True)))
        return {
            "ok": True,
            "action": action,
            "summary": summary,
            "reply": reply,
            "lastRun": store.get("lastRun", ""),
            "blueprint": BLUEPRINT,
        }

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        if self.should_record_expense(message):
            result = self.run_feature(runtime, "voice", {"action": "record_expense", "message": message, "locale": locale})
            return {"reply": result.get("reply", ""), "result": result}
        if self.should_summarize(message):
            period = "today" if "今天" in message else "week"
            result = self.run_feature(
                runtime,
                "voice",
                {
                    "action": "report_today_total" if period == "today" else "report_week_total",
                    "period": period,
                    "threshold": self.parse_threshold(message, self.get_store(runtime)),
                    "includeTotalAlways": True,
                    "locale": locale,
                },
            )
            return {"reply": result.get("reply", ""), "result": result}
        return None

    def enhance_household_modules(self, modules: list[dict], locale: str, runtime: RuntimeBridge) -> list[dict]:
        current = deepcopy(modules)
        store = self.get_store(runtime)
        current.append({
            "id": self.feature_id,
            "name": self.feature_name,
            "summary": BLUEPRINT["goal"],
            "state": "active" if store.get("items") else "ready",
            "actionLabel": "Open",
        })
        return current

    def dashboard_payload(self, locale: str, runtime: RuntimeBridge) -> dict:
        store = self.get_store(runtime)
        return {
            self.feature_id: {
                "blueprint": BLUEPRINT,
                "status": "active",
                "storagePath": str(self.storage_path(runtime)),
                "itemCount": len(store.get("items", [])),
                "lastRun": store.get("lastRun", ""),
                "lastSummary": store.get("lastSummary", {}),
                "recentActions": store.get("recentActions", [])[:4],
            }
        }

    def handle_api(self, method: str, path: str, query: dict, body: dict | None, runtime: RuntimeBridge) -> dict | None:
        store = self.get_store(runtime)
        if method == "GET" and path == API_ROOT:
            return {"status": 200, "body": {"featureId": self.feature_id, "featureName": self.feature_name, "blueprint": BLUEPRINT, "store": store}}
        if method == "GET" and path == API_ITEMS:
            return {"status": 200, "body": {"items": store.get("items", []), "recentActions": store.get("recentActions", [])[:10]}}
        if method == "POST" and path == API_ITEMS:
            payload = body or {}
            amount = int(payload.get("amount", 0) or 0)
            category = str(payload.get("category", "")).strip() or "其他"
            source_text = str(payload.get("message", "")).strip() or f"{category} {amount}"
            if amount <= 0:
                return {"status": 400, "body": {"error": "amount is required"}}
            item = self.add_expense_item(runtime, amount, category, source_text)
            return {"status": 201, "body": {"ok": True, "item": item, "items": store.get("items", [])}}
        if method == "POST" and path == API_RUN:
            result = self.run_feature(runtime, "api", body or {})
            return {"status": 200 if result.get("ok") else 400, "body": result}
        return None


def load_feature() -> HomeHubFeature:
    return Feature()
