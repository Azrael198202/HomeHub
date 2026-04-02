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

    def parse_iso_datetime(self, value) -> datetime | None:
        try:
            return datetime.fromisoformat(str(value))
        except (TypeError, ValueError):
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
            start_at = self.parse_iso_datetime(event.get("startAt"))
            if start_at and start_at >= now_value - timedelta(hours=1):
                events.append(event)
        return self.sort_records_by_datetime(events, "startAt")[:limit]

    def get_pending_reminders(self, runtime: RuntimeBridge, limit: int = 5) -> list[dict]:
        memory = self.get_memory(runtime)
        now_value = self.now_local()
        reminders = []
        for reminder in memory.get("reminders", []):
            trigger_at = self.parse_iso_datetime(reminder.get("triggerAt"))
            if reminder.get("status", "pending") != "done" and trigger_at and trigger_at >= now_value - timedelta(hours=12):
                reminders.append(reminder)
        return self.sort_records_by_datetime(reminders, "triggerAt")[:limit]

    def get_due_reminders(self, runtime: RuntimeBridge, limit: int = 3) -> list[dict]:
        memory = self.get_memory(runtime)
        now_value = self.now_local()
        due = []
        for reminder in memory.get("reminders", []):
            trigger_at = self.parse_iso_datetime(reminder.get("triggerAt"))
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

    def detect_local_assistant_action(self, user_text: str, locale: str, runtime: RuntimeBridge) -> dict:
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
