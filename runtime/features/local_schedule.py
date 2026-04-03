from __future__ import annotations

import json
import re
from copy import deepcopy
from datetime import datetime, timedelta
from pathlib import Path

from .base import HomeHubFeature, RuntimeBridge


class Feature(HomeHubFeature):
    feature_id = "local-schedule"
    feature_name = "Local Schedule and Reminder"
    version = "1.0.0"

    def descriptor(self) -> dict:
        data = super().descriptor()
        data["summary"] = "Stores local schedule items and reminders, and responds to unified voice requests."
        data["api"] = ["/api/memory"]
        data["voiceIntents"] = self.voice_intents()
        return data

    def voice_intents(self) -> list[dict]:
        return [
            {
                "id": "schedule-reminder",
                "name": "Schedule and Reminder",
                "summary": "Creates, lists, and completes local schedule items and reminders.",
            }
        ]

    def memory_path(self, runtime: RuntimeBridge) -> Path:
        return runtime.root / "home_memory.json"

    def default_memory(self) -> dict:
        now = datetime.now().replace(second=0, microsecond=0)
        return {
            "events": [],
            "reminders": [],
            "recentActions": [
                {
                    "id": "act-local-memory-ready",
                    "kind": "init",
                    "summary": "HomeHub local memory is ready for schedule and reminder requests.",
                    "createdAt": now.isoformat(timespec="minutes"),
                }
            ],
        }

    def load_memory(self, runtime: RuntimeBridge) -> dict:
        path = self.memory_path(runtime)
        if not path.exists():
            memory = self.default_memory()
            self.save_memory(memory, runtime)
            return memory
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            memory = self.default_memory()
            self.save_memory(memory, runtime)
            return memory
        if not isinstance(data, dict):
            return self.default_memory()
        return {
            "events": data.get("events", []) if isinstance(data.get("events", []), list) else [],
            "reminders": data.get("reminders", []) if isinstance(data.get("reminders", []), list) else [],
            "recentActions": data.get("recentActions", []) if isinstance(data.get("recentActions", []), list) else [],
        }

    def save_memory(self, memory: dict, runtime: RuntimeBridge) -> None:
        self.memory_path(runtime).write_text(
            json.dumps(memory, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def on_refresh(self, runtime: RuntimeBridge) -> None:
        runtime.state[self.feature_id] = self.load_memory(runtime)

    def reset(self, runtime: RuntimeBridge) -> None:
        memory = self.default_memory()
        runtime.state[self.feature_id] = memory
        self.save_memory(memory, runtime)

    def get_memory(self, runtime: RuntimeBridge) -> dict:
        memory = runtime.state.get(self.feature_id)
        if not isinstance(memory, dict):
            memory = self.load_memory(runtime)
            runtime.state[self.feature_id] = memory
        return memory

    def now_local(self) -> datetime:
        return datetime.now().replace(second=0, microsecond=0)

    def has_active_agent_builder_session(self, runtime: RuntimeBridge) -> bool:
        store = runtime.state.get("custom-agents")
        if not isinstance(store, dict):
            return False
        for item in store.get("items", []):
            if item.get("status") in {"collecting", "review"}:
                return True
        return False

    def normalize_datetime(self, dt: datetime) -> datetime:
        if dt.tzinfo is None:
            return dt.replace(second=0, microsecond=0)
        return dt.astimezone().replace(tzinfo=None, second=0, microsecond=0)

    def parse_iso_datetime(self, value, runtime: RuntimeBridge | None = None, field_name: str = "") -> datetime | None:
        try:
            return self.normalize_datetime(datetime.fromisoformat(str(value)))
        except (TypeError, ValueError):
            if runtime and value not in (None, ""):
                label = f" for {field_name}" if field_name else ""
                runtime.emit_log(f"[local-schedule] Ignored invalid datetime{label}: {value}")
            return None

    def make_memory_id(self, prefix: str) -> str:
        from random import randint

        return f"{prefix}-{datetime.now().strftime('%Y%m%d%H%M%S')}-{randint(100, 999)}"

    def format_datetime_local(self, value, locale: str) -> str:
        dt = self.parse_iso_datetime(value)
        if not dt:
            return str(value)
        if locale in {"zh-CN", "ja-JP"}:
            return dt.strftime("%m月%d日 %H:%M")
        return dt.strftime("%b %d %H:%M")

    def sort_records_by_datetime(self, items: list[dict], key_name: str) -> list[dict]:
        return sorted(items, key=lambda item: self.parse_iso_datetime(item.get(key_name)) or datetime.max)

    def get_upcoming_events(self, runtime: RuntimeBridge, limit: int = 5) -> list[dict]:
        memory = self.get_memory(runtime)
        now_value = self.now_local()
        events = []
        for event in memory.get("events", []):
            start_at = self.parse_iso_datetime(event.get("startAt"), runtime, "event.startAt")
            if start_at and start_at >= now_value - timedelta(hours=1):
                events.append(event)
        return self.sort_records_by_datetime(events, "startAt")[:limit]

    def get_pending_reminders(self, runtime: RuntimeBridge, limit: int = 5) -> list[dict]:
        memory = self.get_memory(runtime)
        now_value = self.now_local()
        reminders = []
        for reminder in memory.get("reminders", []):
            trigger_at = self.parse_iso_datetime(reminder.get("triggerAt"), runtime, "reminder.triggerAt")
            if reminder.get("status", "pending") != "done" and trigger_at and trigger_at >= now_value - timedelta(hours=12):
                reminders.append(reminder)
        return self.sort_records_by_datetime(reminders, "triggerAt")[:limit]

    def get_due_reminders(self, runtime: RuntimeBridge, limit: int = 3) -> list[dict]:
        memory = self.get_memory(runtime)
        now_value = self.now_local()
        due = []
        for reminder in memory.get("reminders", []):
            trigger_at = self.parse_iso_datetime(reminder.get("triggerAt"), runtime, "reminder.triggerAt")
            if reminder.get("status", "pending") != "done" and trigger_at and trigger_at <= now_value:
                due.append(reminder)
        return self.sort_records_by_datetime(due, "triggerAt")[:limit]

    def record_memory_action(self, runtime: RuntimeBridge, kind: str, summary: str) -> None:
        memory = self.get_memory(runtime)
        memory.setdefault("recentActions", []).insert(
            0,
            {
                "id": self.make_memory_id("act"),
                "kind": kind,
                "summary": summary,
                "createdAt": self.now_local().isoformat(timespec="minutes"),
            },
        )
        del memory["recentActions"][12:]

    def create_local_event(
        self,
        runtime: RuntimeBridge,
        title: str,
        start_at: datetime,
        end_at: datetime,
        participants=None,
        location: str = "",
        reminder_offset_minutes: int | None = None,
        notes: str = "",
    ) -> tuple[dict, dict | None]:
        memory = self.get_memory(runtime)
        event_id = self.make_memory_id("evt")
        reminder_ids: list[str] = []
        event = {
            "id": event_id,
            "title": title,
            "startAt": start_at.isoformat(timespec="minutes"),
            "endAt": end_at.isoformat(timespec="minutes"),
            "participants": participants or [],
            "location": location,
            "source": "homehub-local",
            "createdAt": self.now_local().isoformat(timespec="minutes"),
            "notes": notes,
            "linkedReminderIds": reminder_ids,
        }
        memory.setdefault("events", []).append(event)
        created_reminder = None
        if reminder_offset_minutes is not None:
            reminder_id = self.make_memory_id("rem")
            created_reminder = {
                "id": reminder_id,
                "title": f"Reminder: {title}",
                "triggerAt": (start_at - timedelta(minutes=reminder_offset_minutes)).isoformat(timespec="minutes"),
                "eventId": event_id,
                "status": "pending",
                "channels": ["voice", "tv", "mobile"],
                "createdAt": self.now_local().isoformat(timespec="minutes"),
            }
            memory.setdefault("reminders", []).append(created_reminder)
            reminder_ids.append(reminder_id)
        self.record_memory_action(runtime, "create-event", f"Created schedule '{title}' for {start_at.isoformat(timespec='minutes')}.")
        self.save_memory(memory, runtime)
        return event, created_reminder

    def create_local_reminder(self, runtime: RuntimeBridge, title: str, trigger_at: datetime, notes: str = "") -> dict:
        memory = self.get_memory(runtime)
        reminder = {
            "id": self.make_memory_id("rem"),
            "title": title,
            "triggerAt": trigger_at.isoformat(timespec="minutes"),
            "eventId": "",
            "status": "pending",
            "channels": ["voice", "tv", "mobile"],
            "createdAt": self.now_local().isoformat(timespec="minutes"),
            "notes": notes,
        }
        memory.setdefault("reminders", []).append(reminder)
        self.record_memory_action(runtime, "create-reminder", f"Created reminder '{title}' for {trigger_at.isoformat(timespec='minutes')}.")
        self.save_memory(memory, runtime)
        return reminder

    def complete_reminder(self, runtime: RuntimeBridge, reminder_id: str) -> dict | None:
        memory = self.get_memory(runtime)
        for reminder in memory.get("reminders", []):
            if reminder.get("id") != reminder_id:
                continue
            if reminder.get("status", "pending") == "done":
                return reminder
            reminder["status"] = "done"
            reminder["completedAt"] = self.now_local().isoformat(timespec="minutes")
            self.record_memory_action(runtime, "complete-reminder", f"Completed reminder '{reminder.get('title', 'Reminder')}'.")
            self.save_memory(memory, runtime)
            return reminder
        return None

    def detect_day_offset(self, text_value: str) -> int:
        lowered = text_value.lower()
        if "后天" in text_value:
            return 2
        if "明天" in text_value or "明早" in text_value or "明晚" in text_value or "tomorrow" in lowered:
            return 1
        return 0

    def parse_zh_number(self, text_value: str) -> int | None:
        digits = {"零": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
        if not text_value:
            return None
        if text_value == "十":
            return 10
        if "十" in text_value:
            left, _, right = text_value.partition("十")
            tens = 1 if left == "" else digits.get(left)
            ones = 0 if right == "" else digits.get(right)
            if tens is None or ones is None:
                return None
            return tens * 10 + ones
        if len(text_value) == 1:
            return digits.get(text_value)
        return None

    def detect_time_from_text(self, text_value: str) -> tuple[int, int] | None:
        lowered = text_value.lower()
        hour = None
        minute = 0
        match = re.search(r"(\d{1,2})[:：](\d{2})", text_value)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2))
        else:
            match = re.search(r"(\d{1,2})点半", text_value)
            if match:
                hour = int(match.group(1))
                minute = 30
            else:
                match = re.search(r"(\d{1,2})点(?:(\d{1,2})分?)?", text_value)
                if match:
                    hour = int(match.group(1))
                    minute = int(match.group(2) or 0)
                else:
                    match = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b", lowered)
                    if match:
                        hour = int(match.group(1))
                        minute = int(match.group(2) or 0)
                        if match.group(3) == "pm" and hour < 12:
                            hour += 12
                        if match.group(3) == "am" and hour == 12:
                            hour = 0
                    else:
                        match = re.search(r"\b(\d{1,2})\b", text_value)
                        if match and any(token in text_value for token in ["点", "时", "hour", "pm", "am"]):
                            hour = int(match.group(1))
        if hour is None:
            zh_match = re.search(r"([零一二两三四五六七八九十]{1,3})点(半|([零一二两三四五六七八九十]{1,3})分?)?", text_value)
            if zh_match:
                hour = self.parse_zh_number(zh_match.group(1))
                if zh_match.group(2) == "半":
                    minute = 30
                else:
                    minute = self.parse_zh_number(zh_match.group(3) or "") or 0

        if hour is None:
            return None
        if any(token in text_value for token in ["下午", "晚上", "今晚", "傍晚"]) and hour < 12:
            hour += 12
        if "中午" in text_value and hour < 11:
            hour += 12
        if any(token in lowered for token in ["afternoon", "evening", "tonight"]) and hour < 12:
            hour += 12
        return hour, minute

    def detect_reminder_offset_minutes(self, text_value: str) -> int | None:
        if "提前半小时" in text_value or "提前半個小時" in text_value:
            return 30
        match = re.search(r"提前(\d{1,3})\s*分钟", text_value)
        if match:
            return int(match.group(1))
        match = re.search(r"提前(\d{1,2})\s*小时", text_value)
        if match:
            return int(match.group(1)) * 60
        match = re.search(r"(\d{1,3})\s*minutes?\s+before", text_value.lower())
        if match:
            return int(match.group(1))
        match = re.search(r"(\d{1,2})\s*hours?\s+before", text_value.lower())
        if match:
            return int(match.group(1)) * 60
        return 30 if "提前提醒" in text_value or "remind me ahead" in text_value.lower() else None

    def infer_title_from_text(self, text_value: str) -> str:
        quoted = re.search(r"[\"“](.+?)[\"”]", text_value)
        if quoted:
            return quoted.group(1).strip()
        person_meeting = re.search(r"和(.+?)的(会议|会面|聚餐|通话|视频|课程)", text_value)
        if person_meeting:
            return f"和{person_meeting.group(1).strip()}的{person_meeting.group(2).strip()}"
        remind_match = re.search(r"提醒我(.+)", text_value)
        if remind_match:
            return remind_match.group(1).strip("，。 ")
        generic = re.search(r"(创建|添加|安排|设定|新建)(.+?)(日程|会议|提醒|行程)", text_value)
        if generic:
            return f"{generic.group(2).strip('，。 ')}{generic.group(3).strip()}"
        return "家庭日程"

    def build_datetime_from_text(self, text_value: str) -> datetime | None:
        time_parts = self.detect_time_from_text(text_value)
        if not time_parts:
            return None
        hour, minute = time_parts
        base = self.now_local() + timedelta(days=self.detect_day_offset(text_value))
        candidate = base.replace(hour=hour, minute=minute)
        if self.detect_day_offset(text_value) == 0 and candidate < self.now_local() - timedelta(minutes=5):
            candidate += timedelta(days=1)
        return candidate

    def detect_day_offset(self, text_value: str) -> int:
        lowered = text_value.lower()
        if "大后天" in text_value:
            return 3
        if "后天" in text_value:
            return 2
        if any(token in text_value for token in ["明天", "明早", "明晚"]) or "tomorrow" in lowered:
            return 1
        if "昨天" in text_value or "yesterday" in lowered:
            return -1
        return 0

    def parse_zh_number(self, text_value: str) -> int | None:
        normalized = str(text_value or "").strip()
        if not normalized:
            return None
        if normalized.isdigit():
            return int(normalized)
        digits = {
            "零": 0,
            "〇": 0,
            "一": 1,
            "二": 2,
            "两": 2,
            "三": 3,
            "四": 4,
            "五": 5,
            "六": 6,
            "七": 7,
            "八": 8,
            "九": 9,
        }
        if normalized == "十":
            return 10
        if "十" in normalized:
            left, _, right = normalized.partition("十")
            tens = 1 if left == "" else digits.get(left)
            ones = 0 if right == "" else digits.get(right)
            if tens is None or ones is None:
                return None
            return tens * 10 + ones
        if len(normalized) == 1:
            return digits.get(normalized)
        return None

    def detect_time_from_text(self, text_value: str) -> tuple[int, int] | None:
        lowered = text_value.lower()
        hour = None
        minute = 0
        match = re.search(r"(\d{1,2})[:：](\d{1,2})", text_value)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2))
        else:
            match = re.search(r"(\d{1,2})点半", text_value)
            if match:
                hour = int(match.group(1))
                minute = 30
            else:
                match = re.search(r"(\d{1,2})点(?:(\d{1,2})分?)?", text_value)
                if match:
                    hour = int(match.group(1))
                    minute = int(match.group(2) or 0)
                else:
                    match = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b", lowered)
                    if match:
                        hour = int(match.group(1))
                        minute = int(match.group(2) or 0)
                        if match.group(3) == "pm" and hour < 12:
                            hour += 12
                        if match.group(3) == "am" and hour == 12:
                            hour = 0
                    else:
                        zh_match = re.search(r"([零〇一二两三四五六七八九十]{1,3})点(半|([零〇一二两三四五六七八九十]{1,3})分?)?", text_value)
                        if zh_match:
                            hour = self.parse_zh_number(zh_match.group(1))
                            if zh_match.group(2) == "半":
                                minute = 30
                            else:
                                minute = self.parse_zh_number(zh_match.group(3) or "") or 0
        if hour is None:
            return None
        if any(token in text_value for token in ["下午", "傍晚", "晚上", "今晚"]) and hour < 12:
            hour += 12
        if "中午" in text_value and hour < 11:
            hour += 12
        if any(token in lowered for token in ["afternoon", "evening", "tonight"]) and hour < 12:
            hour += 12
        return hour, minute

    def detect_reminder_offset_minutes(self, text_value: str) -> int | None:
        lowered = text_value.lower()
        if "提前半小时" in text_value or "提前半个小时" in text_value:
            return 30
        match = re.search(r"提前(\d{1,3})\s*分钟", text_value)
        if match:
            return int(match.group(1))
        match = re.search(r"提前(\d{1,2})\s*小时", text_value)
        if match:
            return int(match.group(1)) * 60
        match = re.search(r"(\d{1,3})\s*minutes?\s+before", lowered)
        if match:
            return int(match.group(1))
        match = re.search(r"(\d{1,2})\s*hours?\s+before", lowered)
        if match:
            return int(match.group(1)) * 60
        return 30 if "提前提醒" in text_value or "remind me ahead" in lowered else None

    def has_explicit_datetime_reference(self, text_value: str) -> bool:
        return bool(
            re.search(r"(\d{1,2})[:：](\d{1,2})", text_value)
            or re.search(r"(\d{1,2}|[零〇一二两三四五六七八九十]{1,3})点", text_value)
            or any(token in text_value for token in ["今天", "明天", "后天", "今晚", "下午", "上午", "中午"])
        )

    def infer_title_from_text(self, text_value: str) -> str:
        normalized = str(text_value or "").strip()
        quoted = re.search(r"[\"“](.+?)[\"”]", normalized)
        if quoted:
            return quoted.group(1).strip()
        if any(token in normalized for token in ["消费", "花费", "支出", "账单"]):
            if any(token in normalized for token in ["本周", "这周"]):
                return "本周消费总额提醒"
            return "消费提醒"
        if any(token in normalized for token in ["会议", "开会", "日程", "安排", "行程"]):
            return "家庭日程"
        remind_match = re.search(r"提醒我(.+)", normalized)
        if remind_match:
            candidate = remind_match.group(1).strip("，。,. ")
            candidate = re.sub(r"^(在|于)?(今天|明天|后天)?的?", "", candidate).strip()
            if candidate:
                return candidate[:40]
        return "家庭提醒"

    def build_datetime_from_text(self, text_value: str) -> datetime | None:
        time_parts = self.detect_time_from_text(text_value)
        if not time_parts:
            return None
        hour, minute = time_parts
        now_value = self.now_local()
        day_offset = self.detect_day_offset(text_value)
        base = now_value + timedelta(days=day_offset)
        candidate = base.replace(hour=hour, minute=minute)
        if day_offset == 0 and candidate < now_value - timedelta(minutes=5):
            candidate += timedelta(days=1)
        return candidate

    def normalize_ai_schedule_action(self, action: dict, user_text: str) -> dict:
        normalized = dict(action)
        if not self.has_explicit_datetime_reference(user_text):
            return normalized
        local_start = self.build_datetime_from_text(user_text)
        if not local_start:
            return normalized
        normalized["startAt"] = local_start.isoformat(timespec="minutes")
        if normalized.get("action") == "create_event":
            source_start = self.parse_iso_datetime(action.get("startAt"))
            source_end = self.parse_iso_datetime(action.get("endAt"))
            if source_start and source_end and source_end > source_start:
                normalized["endAt"] = (local_start + (source_end - source_start)).isoformat(timespec="minutes")
            else:
                normalized["endAt"] = (local_start + timedelta(minutes=60)).isoformat(timespec="minutes")
        return normalized

    def summarize_schedule(self, locale: str, runtime: RuntimeBridge) -> str:
        events = self.get_upcoming_events(runtime, limit=3)
        reminders = self.get_pending_reminders(runtime, limit=3)
        if locale == "zh-CN":
            if not events and not reminders:
                return "本地日程里暂时没有新的安排或提醒。"
            lines = []
            if events:
                lines.append("接下来日程有：" + "；".join(f"{event['title']}（{self.format_datetime_local(event['startAt'], locale)}）" for event in events))
            if reminders:
                lines.append("提醒有：" + "；".join(f"{item['title']}（{self.format_datetime_local(item['triggerAt'], locale)}）" for item in reminders))
            return " ".join(lines)
        if locale == "ja-JP":
            return "ローカル予定とリマインダーを表示しました。"
        return "I pulled the upcoming local schedule and reminders."

    def try_extract_schedule_with_openai(self, user_text: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        payload = runtime.openai_json(
            (
                "You extract household scheduling intent. "
                "Return JSON only with keys: action, title, startAt, endAt, reminderOffsetMinutes, location, participants, confidence. "
                f"Valid action values: create_event, create_reminder, show_schedule, none. Current local time is {self.now_local().isoformat(timespec='minutes')}."
            ),
            f"Locale={locale}\nUser message: {user_text}",
            "gpt-4o-mini",
        )
        return payload if isinstance(payload, dict) else None

    def format_datetime_local(self, value, locale: str) -> str:
        dt = self.parse_iso_datetime(value)
        if not dt:
            return str(value)
        if locale in {"zh-CN", "ja-JP"}:
            return dt.strftime("%m\u6708%d\u65e5 %H:%M")
        return dt.strftime("%b %d %H:%M")

    def detect_day_offset(self, text_value: str) -> int:
        lowered = text_value.lower()
        if "\u5927\u540e\u5929" in text_value:
            return 3
        if "\u540e\u5929" in text_value:
            return 2
        if any(token in text_value for token in ["\u660e\u5929", "\u660e\u65e9", "\u660e\u665a"]) or "tomorrow" in lowered:
            return 1
        if "\u6628\u5929" in text_value or "yesterday" in lowered:
            return -1
        return 0

    def parse_zh_number(self, text_value: str) -> int | None:
        normalized = str(text_value or "").strip()
        if not normalized:
            return None
        if normalized.isdigit():
            return int(normalized)
        digits = {
            "\u96f6": 0,
            "\u3007": 0,
            "\u4e00": 1,
            "\u4e8c": 2,
            "\u4e24": 2,
            "\u4e09": 3,
            "\u56db": 4,
            "\u4e94": 5,
            "\u516d": 6,
            "\u4e03": 7,
            "\u516b": 8,
            "\u4e5d": 9,
        }
        if normalized == "\u5341":
            return 10
        if "\u5341" in normalized:
            left, _, right = normalized.partition("\u5341")
            tens = 1 if left == "" else digits.get(left)
            ones = 0 if right == "" else digits.get(right)
            if tens is None or ones is None:
                return None
            return tens * 10 + ones
        if len(normalized) == 1:
            return digits.get(normalized)
        return None

    def detect_time_from_text(self, text_value: str) -> tuple[int, int] | None:
        lowered = text_value.lower()
        hour = None
        minute = 0
        match = re.search(r"(\d{1,2})[:：](\d{1,2})", text_value)
        if match:
            hour = int(match.group(1))
            minute = int(match.group(2))
        else:
            match = re.search(r"(\d{1,2})\u70b9\u534a", text_value)
            if match:
                hour = int(match.group(1))
                minute = 30
            else:
                match = re.search(r"(\d{1,2})\u70b9(?:(\d{1,2})\u5206?)?", text_value)
                if match:
                    hour = int(match.group(1))
                    minute = int(match.group(2) or 0)
                else:
                    match = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b", lowered)
                    if match:
                        hour = int(match.group(1))
                        minute = int(match.group(2) or 0)
                        if match.group(3) == "pm" and hour < 12:
                            hour += 12
                        if match.group(3) == "am" and hour == 12:
                            hour = 0
                    else:
                        zh_match = re.search(
                            r"([\u96f6\u3007\u4e00\u4e8c\u4e24\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]{1,3})\u70b9(\u534a|([\u96f6\u3007\u4e00\u4e8c\u4e24\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]{1,3})\u5206?)?",
                            text_value,
                        )
                        if zh_match:
                            hour = self.parse_zh_number(zh_match.group(1))
                            if zh_match.group(2) == "\u534a":
                                minute = 30
                            else:
                                minute = self.parse_zh_number(zh_match.group(3) or "") or 0
        if hour is None:
            return None
        if any(token in text_value for token in ["\u4e0b\u5348", "\u508d\u665a", "\u665a\u4e0a", "\u4eca\u665a"]) and hour < 12:
            hour += 12
        if "\u4e2d\u5348" in text_value and hour < 11:
            hour += 12
        if any(token in lowered for token in ["afternoon", "evening", "tonight"]) and hour < 12:
            hour += 12
        return hour, minute

    def detect_reminder_offset_minutes(self, text_value: str) -> int | None:
        lowered = text_value.lower()
        if "\u63d0\u524d\u534a\u5c0f\u65f6" in text_value or "\u63d0\u524d\u534a\u4e2a\u5c0f\u65f6" in text_value:
            return 30
        match = re.search(r"\u63d0\u524d(\d{1,3})\s*\u5206\u949f", text_value)
        if match:
            return int(match.group(1))
        match = re.search(r"\u63d0\u524d(\d{1,2})\s*\u5c0f\u65f6", text_value)
        if match:
            return int(match.group(1)) * 60
        match = re.search(r"(\d{1,3})\s*minutes?\s+before", lowered)
        if match:
            return int(match.group(1))
        match = re.search(r"(\d{1,2})\s*hours?\s+before", lowered)
        if match:
            return int(match.group(1)) * 60
        return 30 if "\u63d0\u524d\u63d0\u9192" in text_value or "remind me ahead" in lowered else None

    def has_explicit_datetime_reference(self, text_value: str) -> bool:
        return bool(
            re.search(r"(\d{1,2})[:：](\d{1,2})", text_value)
            or re.search(r"(\d{1,2}|[\u96f6\u3007\u4e00\u4e8c\u4e24\u4e09\u56db\u4e94\u516d\u4e03\u516b\u4e5d\u5341]{1,3})\u70b9", text_value)
            or any(
                token in text_value
                for token in ["\u4eca\u5929", "\u660e\u5929", "\u540e\u5929", "\u4eca\u665a", "\u4e0b\u5348", "\u4e0a\u5348", "\u4e2d\u5348"]
            )
        )

    def infer_title_from_text(self, text_value: str) -> str:
        normalized = str(text_value or "").strip()
        quoted = re.search(r"[\"“](.+?)[\"”]", normalized)
        if quoted:
            return quoted.group(1).strip()
        if any(token in normalized for token in ["\u6d88\u8d39", "\u82b1\u8d39", "\u652f\u51fa", "\u8d26\u5355"]):
            if any(token in normalized for token in ["\u672c\u5468", "\u8fd9\u5468"]):
                return "\u672c\u5468\u6d88\u8d39\u603b\u989d\u63d0\u9192"
            return "\u6d88\u8d39\u63d0\u9192"
        if any(token in normalized for token in ["\u4f1a\u8bae", "\u5f00\u4f1a", "\u65e5\u7a0b", "\u5b89\u6392", "\u884c\u7a0b"]):
            return "\u5bb6\u5ead\u65e5\u7a0b"
        remind_match = re.search(r"\u63d0\u9192\u6211(.+)", normalized)
        if remind_match:
            candidate = remind_match.group(1).strip("\uff0c\u3002,. ")
            candidate = re.sub(r"^(\u5728|\u4e8e)?(\u4eca\u5929|\u660e\u5929|\u540e\u5929)?\u7684?", "", candidate).strip()
            if candidate:
                return candidate[:40]
        return "\u5bb6\u5ead\u63d0\u9192"

    def build_datetime_from_text(self, text_value: str) -> datetime | None:
        time_parts = self.detect_time_from_text(text_value)
        if not time_parts:
            return None
        hour, minute = time_parts
        now_value = self.now_local()
        day_offset = self.detect_day_offset(text_value)
        base = now_value + timedelta(days=day_offset)
        candidate = base.replace(hour=hour, minute=minute)
        if day_offset == 0 and candidate < now_value - timedelta(minutes=5):
            candidate += timedelta(days=1)
        return candidate

    def normalize_ai_schedule_action(self, action: dict, user_text: str) -> dict:
        normalized = dict(action)
        if not self.has_explicit_datetime_reference(user_text):
            return normalized
        local_start = self.build_datetime_from_text(user_text)
        if not local_start:
            return normalized
        normalized["startAt"] = local_start.isoformat(timespec="minutes")
        if normalized.get("action") == "create_event":
            source_start = self.parse_iso_datetime(action.get("startAt"))
            source_end = self.parse_iso_datetime(action.get("endAt"))
            if source_start and source_end and source_end > source_start:
                normalized["endAt"] = (local_start + (source_end - source_start)).isoformat(timespec="minutes")
            else:
                normalized["endAt"] = (local_start + timedelta(minutes=60)).isoformat(timespec="minutes")
        return normalized

    def detect_local_assistant_action(self, user_text: str, locale: str, runtime: RuntimeBridge) -> dict:
        if self.has_active_agent_builder_session(runtime):
            return {"action": "none"}
        lowered = user_text.lower()
        ai_result = self.try_extract_schedule_with_openai(user_text, locale, runtime)
        if isinstance(ai_result, dict) and ai_result.get("action") in {"create_event", "create_reminder", "show_schedule"}:
            return ai_result
        if any(token in user_text for token in ["查看日程", "看看日程", "我的日程", "有什么安排", "提醒列表"]) or "show my schedule" in lowered:
            return {"action": "show_schedule"}
        if any(token in user_text for token in ["提醒", "日程", "会议", "安排", "行程", "闹钟"]) or "remind me" in lowered or "schedule" in lowered:
            start_at = self.build_datetime_from_text(user_text)
            offset = self.detect_reminder_offset_minutes(user_text)
            title = self.infer_title_from_text(user_text)
            if start_at and any(token in user_text for token in ["日程", "会议", "安排", "行程", "schedule", "meeting"]):
                return {
                    "action": "create_event",
                    "title": title,
                    "startAt": start_at.isoformat(timespec="minutes"),
                    "endAt": (start_at + timedelta(minutes=60)).isoformat(timespec="minutes"),
                    "reminderOffsetMinutes": offset,
                    "location": "",
                    "participants": [],
                }
            if (start_at and any(token in user_text for token in ["提醒", "闹钟"])) or ("remind me" in lowered and start_at):
                return {
                    "action": "create_reminder",
                    "title": title if title != "家庭日程" else "HomeHub reminder",
                    "startAt": start_at.isoformat(timespec="minutes"),
                }
        return {"action": "none"}

    def detect_local_assistant_action(self, user_text: str, locale: str, runtime: RuntimeBridge) -> dict:
        if self.has_active_agent_builder_session(runtime):
            return {"action": "none"}
        lowered = user_text.lower()
        if any(
            token in user_text
            for token in ["\u67e5\u770b\u65e5\u7a0b", "\u770b\u770b\u65e5\u7a0b", "\u544a\u8bc9\u6211\u65e5\u7a0b", "\u672c\u5468\u8fd8\u6709\u5b89\u6392", "\u63d0\u9192\u5217\u8868"]
        ) or "show my schedule" in lowered:
            return {"action": "show_schedule"}
        if any(
            token in user_text
            for token in ["\u63d0\u9192", "\u65e5\u7a0b", "\u4f1a\u8bae", "\u5b89\u6392", "\u884c\u7a0b", "\u95f9\u949f"]
        ) or "remind me" in lowered or "schedule" in lowered:
            start_at = self.build_datetime_from_text(user_text)
            offset = self.detect_reminder_offset_minutes(user_text)
            title = self.infer_title_from_text(user_text)
            if start_at and any(
                token in user_text
                for token in ["\u65e5\u7a0b", "\u4f1a\u8bae", "\u5b89\u6392", "\u884c\u7a0b", "schedule", "meeting"]
            ):
                return {
                    "action": "create_event",
                    "title": title,
                    "startAt": start_at.isoformat(timespec="minutes"),
                    "endAt": (start_at + timedelta(minutes=60)).isoformat(timespec="minutes"),
                    "reminderOffsetMinutes": offset,
                    "location": "",
                    "participants": [],
                }
            if (start_at and any(token in user_text for token in ["\u63d0\u9192", "\u95f9\u949f"])) or ("remind me" in lowered and start_at):
                return {
                    "action": "create_reminder",
                    "title": title if title != "\u5bb6\u5ead\u65e5\u7a0b" else "HomeHub reminder",
                    "startAt": start_at.isoformat(timespec="minutes"),
                }
        ai_result = self.try_extract_schedule_with_openai(user_text, locale, runtime)
        if isinstance(ai_result, dict) and ai_result.get("action") in {"create_event", "create_reminder", "show_schedule"}:
            return self.normalize_ai_schedule_action(ai_result, user_text)
        return {"action": "none"}

    def match_voice_intent(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        action = self.detect_local_assistant_action(message, locale, runtime)
        action_name = action.get("action", "none")
        if action_name == "none":
            return None
        score_map = {
            "create_event": 0.98,
            "create_reminder": 0.98,
            "show_schedule": 0.88,
        }
        return {
            "intent": "schedule-reminder",
            "action": action_name,
            "score": score_map.get(action_name, 0.8),
        }

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        action = self.detect_local_assistant_action(message, locale, runtime)
        action_name = action.get("action", "none")
        if action_name == "show_schedule":
            return {"reply": self.summarize_schedule(locale, runtime)}
        if action_name == "create_event":
            start_at = self.parse_iso_datetime(action.get("startAt"))
            end_at = self.parse_iso_datetime(action.get("endAt")) or (start_at + timedelta(minutes=60) if start_at else None)
            if not start_at or not end_at:
                reply = "我还没完全听清时间，你可以再说一次具体几点吗？" if locale == "zh-CN" else "I still need a specific time."
                return {"reply": reply}
            title = str(action.get("title", "")).strip() or self.infer_title_from_text(message)
            reminder_offset = action.get("reminderOffsetMinutes")
            if reminder_offset is not None:
                try:
                    reminder_offset = int(reminder_offset)
                except (TypeError, ValueError):
                    reminder_offset = None
            event, reminder = self.create_local_event(
                runtime,
                title,
                start_at,
                end_at,
                participants=action.get("participants") or [],
                location=str(action.get("location", "")).strip(),
                reminder_offset_minutes=reminder_offset,
                notes=f"Original request: {message}",
            )
            if locale == "zh-CN":
                if reminder:
                    reply = (
                        f"已经帮你把“{event['title']}”加入 HomeHub 本地日程，时间是 {self.format_datetime_local(event['startAt'], locale)}。"
                        f" 我也加了一个提前 {reminder_offset} 分钟的提醒，会在电视、语音和手机端一起显示。"
                    )
                else:
                    reply = f"已经帮你把“{event['title']}”加入 HomeHub 本地日程，时间是 {self.format_datetime_local(event['startAt'], locale)}。"
                return {"reply": reply, "assistantMemory": self.dashboard_payload(locale, runtime).get("assistantMemory", {})}
            if locale == "ja-JP":
                return {"reply": f"ローカル予定に「{event['title']}」を追加しました。"}
            return {"reply": f"I added '{event['title']}' to HomeHub local schedule for {self.format_datetime_local(event['startAt'], locale)}."}
        if action_name == "create_reminder":
            trigger_at = self.parse_iso_datetime(action.get("startAt"))
            if not trigger_at:
                reply = "我还需要一个更具体的提醒时间。" if locale == "zh-CN" else "I still need a reminder time."
                return {"reply": reply}
            title = str(action.get("title", "")).strip() or self.infer_title_from_text(message)
            reminder = self.create_local_reminder(runtime, title, trigger_at, notes=f"Original request: {message}")
            if locale == "zh-CN":
                return {"reply": f"已经创建提醒“{reminder['title']}”，触发时间是 {self.format_datetime_local(reminder['triggerAt'], locale)}。"}
            if locale == "ja-JP":
                return {"reply": f"リマインダー「{reminder['title']}」を追加しました。"}
            return {"reply": f"I created reminder '{reminder['title']}' for {self.format_datetime_local(reminder['triggerAt'], locale)}."}
        return None

    def enhance_household_modules(self, modules: list[dict], locale: str, runtime: RuntimeBridge) -> list[dict]:
        current = deepcopy(modules)
        upcoming_events = self.get_upcoming_events(runtime, limit=3)
        pending_reminders = self.get_pending_reminders(runtime, limit=3)
        due_reminders = self.get_due_reminders(runtime, limit=2)

        for module in current:
            if module["id"] == "schedule":
                if upcoming_events:
                    next_event = upcoming_events[0]
                    if locale == "zh-CN":
                        module["summary"] = f"已记录 {len(upcoming_events)} 个本地日程。下一个是 {next_event['title']}，时间 {self.format_datetime_local(next_event['startAt'], locale)}。"
                        module["actionLabel"] = "查看日程"
                    elif locale == "ja-JP":
                        module["summary"] = f"ローカル予定 {len(upcoming_events)} 件。次は {next_event['title']}、{self.format_datetime_local(next_event['startAt'], locale)}。"
                        module["actionLabel"] = "予定を見る"
                    else:
                        module["summary"] = f"{len(upcoming_events)} local events tracked. Next: {next_event['title']} at {self.format_datetime_local(next_event['startAt'], locale)}."
                        module["actionLabel"] = "Open Schedule"
                    module["state"] = "attention" if due_reminders else "active"
                else:
                    if locale == "zh-CN":
                        module["summary"] = "还没有本地日程。你可以直接对 HomeHub 说出要创建的安排。"
                        module["actionLabel"] = "语音创建"
                    elif locale == "ja-JP":
                        module["summary"] = "ローカル予定はまだありません。音声で追加できます。"
                        module["actionLabel"] = "音声で作成"
                    else:
                        module["summary"] = "No local schedule items yet. Ask HomeHub by voice to create one."
                        module["actionLabel"] = "Create by Voice"
                    module["state"] = "ready"
            if module["id"] == "messages" and pending_reminders:
                next_reminder = pending_reminders[0]
                if locale == "zh-CN":
                    module["summary"] = f"已有 {len(pending_reminders)} 条提醒。下一条是 {next_reminder['title']}，将在 {self.format_datetime_local(next_reminder['triggerAt'], locale)} 触发。"
                    module["actionLabel"] = "查看提醒"
                elif locale == "ja-JP":
                    module["summary"] = f"リマインダー {len(pending_reminders)} 件。次は {next_reminder['title']}、{self.format_datetime_local(next_reminder['triggerAt'], locale)}。"
                    module["actionLabel"] = "通知を見る"
                else:
                    module["summary"] = f"{len(pending_reminders)} reminders queued. Next: {next_reminder['title']} at {self.format_datetime_local(next_reminder['triggerAt'], locale)}."
                    module["actionLabel"] = "View Reminders"
                module["state"] = "attention" if due_reminders else "active"
        return current

    def dashboard_payload(self, locale: str, runtime: RuntimeBridge) -> dict:
        memory = self.get_memory(runtime)
        return {
            "assistantMemory": {
                "upcomingEvents": self.get_upcoming_events(runtime, limit=5),
                "pendingReminders": self.get_pending_reminders(runtime, limit=5),
                "dueReminders": self.get_due_reminders(runtime, limit=3),
                "recentActions": memory.get("recentActions", [])[:5],
            }
        }

    def detect_warning_threshold(self, text_value: str) -> int | None:
        match = re.search(r"(\d{3,6})\s*(?:日元|円|yen|jpy)?", str(text_value or "").lower())
        if not match:
            return None
        if any(token in text_value for token in ["超过", "超出", "预警", "threshold"]):
            try:
                return int(match.group(1))
            except (TypeError, ValueError):
                return None
        return None

    def find_workflow_feature_id(self, message: str, runtime: RuntimeBridge) -> str:
        store = runtime.state.get("custom-agents", {})
        if not isinstance(store, dict):
            return ""
        expense_tokens = ["消费", "花费", "支出", "账单", "扣费"]
        for agent in store.get("items", []):
            if agent.get("status") != "complete":
                continue
            feature_id = str(agent.get("generatedFeatureId", "")).strip()
            if not feature_id:
                continue
            profile = agent.get("profile", {})
            corpus = " ".join(
                str(profile.get(key, ""))
                for key in ["name", "goal", "trigger", "inputs", "output", "checkPrompt", "hasInputAction"]
            )
            if any(token in corpus for token in expense_tokens) and any(token in message for token in expense_tokens):
                return feature_id
        return ""

    def build_reminder_workflow_plan(self, message: str, runtime: RuntimeBridge) -> dict | None:
        message_text = str(message or "").strip()
        if not any(token in message_text for token in ["消费", "花费", "支出", "账单"]) or not any(
            token in message_text for token in ["总额", "总消费", "花了多少钱", "预警", "超过"]
        ):
            return None
        feature_id = self.find_workflow_feature_id(message_text, runtime)
        if not feature_id:
            return None
        threshold = self.detect_warning_threshold(message_text) or 2000
        api_run_path = f"/api/{feature_id}/run"
        return {
            "kind": "feature_api",
            "featureId": feature_id,
            "request": {
                "mode": "api",
                "method": "POST",
                "path": api_run_path,
                "body": {
                    "action": "report_today_total",
                    "period": "today",
                    "threshold": threshold,
                    "includeTotalAlways": True,
                },
            },
            "originalRequest": message_text,
        }

    def create_local_reminder(self, runtime: RuntimeBridge, title: str, trigger_at: datetime, notes: str = "", workflow: dict | None = None) -> dict:
        memory = self.get_memory(runtime)
        reminder = {
            "id": self.make_memory_id("rem"),
            "title": title,
            "triggerAt": trigger_at.isoformat(timespec="minutes"),
            "eventId": "",
            "status": "pending",
            "channels": ["voice", "tv", "mobile"],
            "createdAt": self.now_local().isoformat(timespec="minutes"),
            "notes": notes,
        }
        if workflow:
            reminder["workflow"] = workflow
        memory.setdefault("reminders", []).append(reminder)
        self.record_memory_action(runtime, "create-reminder", f"Created reminder '{title}' for {trigger_at.isoformat(timespec='minutes')}.")
        self.save_memory(memory, runtime)
        return reminder

    def execute_reminder_workflow(self, reminder: dict, runtime: RuntimeBridge, locale: str) -> dict | None:
        workflow = reminder.get("workflow")
        if not isinstance(workflow, dict):
            return None
        feature_id = str(workflow.get("featureId", "")).strip()
        request = workflow.get("request", {}) if isinstance(workflow.get("request", {}), dict) else {}
        if not feature_id or not request:
            return None
        result = runtime.call_feature(feature_id, request, locale)
        if not isinstance(result, dict):
            return {"ok": False, "reply": "Workflow execution returned no result."}
        body = result.get("body") if isinstance(result.get("body"), dict) else result
        reply = str(body.get("reply") or body.get("message") or "").strip()
        if not reply and isinstance(body.get("summary"), dict):
            summary = body["summary"]
            total = int(summary.get("total", 0) or 0)
            threshold = int(summary.get("threshold", 2000) or 2000)
            reply = f"今天截至目前总消费是 {total} 日元。"
            if total > threshold:
                reply += f" 已超过 {threshold} 日元预警额度。"
        outcome = {
            "ok": bool(body.get("ok", True)),
            "reply": reply or "Workflow finished.",
            "executedAt": self.now_local().isoformat(timespec="minutes"),
            "featureId": feature_id,
        }
        reminder["workflowResult"] = outcome
        reminder["executedAt"] = outcome["executedAt"]
        original_request = str(workflow.get("originalRequest", "")).strip()
        reminder["notes"] = outcome["reply"] + (f"\nOriginal request: {original_request}" if original_request else "")
        return outcome

    def resolve_due_reminder_workflows(self, runtime: RuntimeBridge, locale: str) -> None:
        memory = self.get_memory(runtime)
        changed = False
        now_value = self.now_local()
        for reminder in memory.get("reminders", []):
            if reminder.get("status", "pending") == "done":
                continue
            if reminder.get("executedAt"):
                continue
            trigger_at = self.parse_iso_datetime(reminder.get("triggerAt"), runtime, "reminder.triggerAt")
            if not trigger_at or trigger_at > now_value:
                continue
            if not reminder.get("workflow"):
                continue
            outcome = self.execute_reminder_workflow(reminder, runtime, locale)
            if outcome:
                changed = True
                self.record_memory_action(runtime, "execute-reminder-workflow", f"Executed reminder workflow for '{reminder.get('title', 'Reminder')}'.")
        if changed:
            self.save_memory(memory, runtime)

    def dashboard_payload(self, locale: str, runtime: RuntimeBridge) -> dict:
        self.resolve_due_reminder_workflows(runtime, locale)
        memory = self.get_memory(runtime)
        return {
            "assistantMemory": {
                "upcomingEvents": self.get_upcoming_events(runtime, limit=5),
                "pendingReminders": self.get_pending_reminders(runtime, limit=5),
                "dueReminders": self.get_due_reminders(runtime, limit=3),
                "recentActions": memory.get("recentActions", [])[:5],
            }
        }

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        action = self.detect_local_assistant_action(message, locale, runtime)
        action_name = action.get("action", "none")
        if action_name == "show_schedule":
            return {"reply": self.summarize_schedule(locale, runtime)}
        if action_name == "create_event":
            start_at = self.parse_iso_datetime(action.get("startAt"))
            end_at = self.parse_iso_datetime(action.get("endAt")) or (start_at + timedelta(minutes=60) if start_at else None)
            if not start_at or not end_at:
                return {"reply": "我还没完全听清时间，你可以再说一次具体几点吗？" if locale == "zh-CN" else "I still need a specific time."}
            title = str(action.get("title", "")).strip() or self.infer_title_from_text(message)
            reminder_offset = action.get("reminderOffsetMinutes")
            if reminder_offset is not None:
                try:
                    reminder_offset = int(reminder_offset)
                except (TypeError, ValueError):
                    reminder_offset = None
            event, reminder = self.create_local_event(
                runtime,
                title,
                start_at,
                end_at,
                participants=action.get("participants") or [],
                location=str(action.get("location", "")).strip(),
                reminder_offset_minutes=reminder_offset,
                notes=f"Original request: {message}",
            )
            if locale == "zh-CN":
                reply = f"已经帮你把“{event['title']}”加入 HomeHub 本地日程，时间是 {self.format_datetime_local(event['startAt'], locale)}。"
                if reminder:
                    reply += f" 我也加了一个提前 {reminder_offset} 分钟的提醒，会在电视、语音和手机端一起显示。"
                return {"reply": reply, "assistantMemory": self.dashboard_payload(locale, runtime).get("assistantMemory", {})}
            return {"reply": f"I added '{event['title']}' to HomeHub local schedule for {self.format_datetime_local(event['startAt'], locale)}."}
        if action_name == "create_reminder":
            trigger_at = self.parse_iso_datetime(action.get("startAt"))
            if not trigger_at:
                return {"reply": "我还需要一个更具体的提醒时间。" if locale == "zh-CN" else "I still need a reminder time."}
            title = str(action.get("title", "")).strip() or self.infer_title_from_text(message)
            workflow = self.build_reminder_workflow_plan(message, runtime)
            reminder = self.create_local_reminder(runtime, title, trigger_at, notes=f"Original request: {message}", workflow=workflow)
            if locale == "zh-CN":
                reply = f"已经创建提醒“{reminder['title']}”，触发时间是 {self.format_datetime_local(reminder['triggerAt'], locale)}。"
                if workflow:
                    reply += " 到时间后我会自动调用对应智能体执行并给出结果。"
                return {"reply": reply}
            return {"reply": f"I created reminder '{reminder['title']}' for {self.format_datetime_local(reminder['triggerAt'], locale)}."}
        return None

    def handle_api(self, method: str, path: str, query: dict, body: dict | None, runtime: RuntimeBridge) -> dict | None:
        if method == "GET" and path == "/api/memory":
            return {"status": 200, "body": self.dashboard_payload(runtime.get_setting("language", "en-US"), runtime)["assistantMemory"]}
        if method == "POST" and path == "/api/memory/reminders/complete":
            reminder_id = str((body or {}).get("id", "")).strip()
            if not reminder_id:
                return {"status": 400, "body": {"error": "Reminder id is required."}}
            reminder = self.complete_reminder(runtime, reminder_id)
            if not reminder:
                return {"status": 404, "body": {"error": "Reminder not found."}}
            locale = runtime.get_setting("language", "en-US")
            return {
                "status": 200,
                "body": {
                    "ok": True,
                    "reminder": reminder,
                    "assistantMemory": self.dashboard_payload(locale, runtime)["assistantMemory"],
                },
            }
        return None


def load_feature() -> HomeHubFeature:
    return Feature()
