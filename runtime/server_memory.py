from __future__ import annotations

import json
import random
import re
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path


def default_home_memory():
    now_value = datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")
    return {
        "events": [],
        "reminders": [],
        "recentActions": [
            {
                "id": "act-local-memory-ready",
                "kind": "init",
                "summary": "HomeHub local memory is ready for schedule and reminder requests.",
                "createdAt": now_value,
            }
        ],
    }


def load_home_memory(memory_file: Path):
    if not memory_file.exists():
        memory = default_home_memory()
        save_home_memory(memory_file, memory)
        return memory
    try:
        data = json.loads(memory_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        memory = default_home_memory()
        save_home_memory(memory_file, memory)
        return memory
    if not isinstance(data, dict):
        return default_home_memory()
    return {
        "events": data.get("events", []) if isinstance(data.get("events", []), list) else [],
        "reminders": data.get("reminders", []) if isinstance(data.get("reminders", []), list) else [],
        "recentActions": data.get("recentActions", []) if isinstance(data.get("recentActions", []), list) else [],
    }


def save_home_memory(memory_file: Path, memory: dict):
    memory_file.write_text(json.dumps(memory, ensure_ascii=False, indent=2), encoding="utf-8")


def now_local():
    return datetime.now().replace(second=0, microsecond=0)


def now_hhmm():
    return datetime.now().strftime("%H:%M")


def parse_iso_datetime(value):
    try:
        return datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def make_memory_id(prefix):
    return f"{prefix}-{datetime.now().strftime('%Y%m%d%H%M%S')}-{random.randint(100, 999)}"


def format_datetime_local(value, locale):
    dt = parse_iso_datetime(value)
    if not dt:
        return str(value)
    if locale == "zh-CN":
        return dt.strftime("%m月%d日 %H:%M")
    if locale == "ja-JP":
        return dt.strftime("%m月%d日 %H:%M")
    return dt.strftime("%b %d %H:%M")


def sort_records_by_datetime(items, key_name):
    return sorted(items, key=lambda item: parse_iso_datetime(item.get(key_name)) or datetime.max)


def get_upcoming_events(home_memory: dict, limit=5):
    now_value = now_local()
    events = []
    for event in home_memory.get("events", []):
        start_at = parse_iso_datetime(event.get("startAt"))
        if start_at and start_at >= now_value - timedelta(hours=1):
            events.append(event)
    return sort_records_by_datetime(events, "startAt")[:limit]


def get_pending_reminders(home_memory: dict, limit=5):
    now_value = now_local()
    reminders = []
    for reminder in home_memory.get("reminders", []):
        trigger_at = parse_iso_datetime(reminder.get("triggerAt"))
        if reminder.get("status", "pending") != "done" and trigger_at and trigger_at >= now_value - timedelta(hours=12):
            reminders.append(reminder)
    return sort_records_by_datetime(reminders, "triggerAt")[:limit]


def get_due_reminders(home_memory: dict, limit=3):
    now_value = now_local()
    due = []
    for reminder in home_memory.get("reminders", []):
        trigger_at = parse_iso_datetime(reminder.get("triggerAt"))
        if reminder.get("status", "pending") != "done" and trigger_at and trigger_at <= now_value:
            due.append(reminder)
    return sort_records_by_datetime(due, "triggerAt")[:limit]


def record_memory_action(home_memory: dict, kind, summary):
    home_memory.setdefault("recentActions", []).insert(
        0,
        {
            "id": make_memory_id("act"),
            "kind": kind,
            "summary": summary,
            "createdAt": now_local().isoformat(timespec="minutes"),
        },
    )
    del home_memory["recentActions"][12:]


def create_local_event(
    home_memory: dict,
    memory_file: Path,
    title,
    start_at,
    end_at,
    participants=None,
    location="",
    reminder_offset_minutes=None,
    notes="",
):
    event_id = make_memory_id("evt")
    reminder_ids = []
    event = {
        "id": event_id,
        "title": title,
        "startAt": start_at.isoformat(timespec="minutes"),
        "endAt": end_at.isoformat(timespec="minutes"),
        "participants": participants or [],
        "location": location,
        "source": "homehub-local",
        "createdAt": now_local().isoformat(timespec="minutes"),
        "notes": notes,
        "linkedReminderIds": reminder_ids,
    }
    home_memory.setdefault("events", []).append(event)
    created_reminder = None
    if reminder_offset_minutes is not None:
        reminder_time = start_at - timedelta(minutes=reminder_offset_minutes)
        reminder_id = make_memory_id("rem")
        created_reminder = {
            "id": reminder_id,
            "title": f"Reminder: {title}",
            "triggerAt": reminder_time.isoformat(timespec="minutes"),
            "eventId": event_id,
            "status": "pending",
            "channels": ["voice", "tv", "mobile"],
            "createdAt": now_local().isoformat(timespec="minutes"),
        }
        home_memory.setdefault("reminders", []).append(created_reminder)
        reminder_ids.append(reminder_id)
    record_memory_action(home_memory, "create-event", f"Created schedule '{title}' for {start_at.isoformat(timespec='minutes')}.")
    save_home_memory(memory_file, home_memory)
    return event, created_reminder


def create_local_reminder(home_memory: dict, memory_file: Path, title, trigger_at, notes=""):
    reminder = {
        "id": make_memory_id("rem"),
        "title": title,
        "triggerAt": trigger_at.isoformat(timespec="minutes"),
        "eventId": "",
        "status": "pending",
        "channels": ["voice", "tv", "mobile"],
        "createdAt": now_local().isoformat(timespec="minutes"),
        "notes": notes,
    }
    home_memory.setdefault("reminders", []).append(reminder)
    record_memory_action(home_memory, "create-reminder", f"Created reminder '{title}' for {trigger_at.isoformat(timespec='minutes')}.")
    save_home_memory(memory_file, home_memory)
    return reminder


def detect_day_offset(text_value):
    lowered = text_value.lower()
    if "后天" in text_value:
        return 2
    if "明天" in text_value or "明早" in text_value or "明晚" in text_value or "tomorrow" in lowered:
        return 1
    return 0


def parse_zh_number(text_value):
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


def detect_time_from_text(text_value):
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
            hour = parse_zh_number(zh_match.group(1))
            if zh_match.group(2) == "半":
                minute = 30
            else:
                minute = parse_zh_number(zh_match.group(3) or "") or 0
    if hour is None:
        return None
    if any(token in text_value for token in ["下午", "晚上", "今晚", "傍晚"]) and hour < 12:
        hour += 12
    if any(token in text_value for token in ["中午"]) and hour < 11:
        hour += 12
    if any(token in lowered for token in ["afternoon", "evening", "tonight"]) and hour < 12:
        hour += 12
    return hour, minute


def detect_reminder_offset_minutes(text_value):
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


def infer_title_from_text(text_value):
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
        core = generic.group(2).strip("，。 ")
        suffix = generic.group(3).strip()
        return f"{core}{suffix}"
    return "家庭日程"


def build_datetime_from_text(text_value):
    time_parts = detect_time_from_text(text_value)
    if not time_parts:
        return None
    hour, minute = time_parts
    base = now_local() + timedelta(days=detect_day_offset(text_value))
    candidate = base.replace(hour=hour, minute=minute)
    if detect_day_offset(text_value) == 0 and candidate < now_local() - timedelta(minutes=5):
        candidate += timedelta(days=1)
    return candidate


def summarize_schedule(home_memory: dict, locale):
    events = get_upcoming_events(home_memory, limit=3)
    reminders = get_pending_reminders(home_memory, limit=3)
    if locale == "zh-CN":
        if not events and not reminders:
            return "本地日程里暂时没有新的安排或提醒。"
        lines = []
        if events:
            lines.append("接下来日程有：" + "；".join(f"{event['title']}（{format_datetime_local(event['startAt'], locale)}）" for event in events))
        if reminders:
            lines.append("提醒有：" + "；".join(f"{item['title']}（{format_datetime_local(item['triggerAt'], locale)}）" for item in reminders))
        return " ".join(lines)
    if locale == "ja-JP":
        return "ローカル予定とリマインダーを表示しました。"
    return "I pulled the upcoming local schedule and reminders."


def try_extract_schedule_with_openai(user_text, locale, context: dict):
    api_key = context["secrets"].get("openaiApiKey", "")
    if not api_key:
        return None
    schema_prompt = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You extract household scheduling intent. "
                    "Return JSON only with keys: action, title, startAt, endAt, reminderOffsetMinutes, location, participants, confidence. "
                    "Valid action values: create_event, create_reminder, show_schedule, none. "
                    f"Current local time is {now_local().isoformat(timespec='minutes')}."
                ),
            },
            {"role": "user", "content": f"Locale={locale}\nUser message: {user_text}"},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.2,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(schema_prompt).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = json.loads(response.read().decode("utf-8"))
        content = payload["choices"][0]["message"]["content"]
        if isinstance(content, list):
            content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
        data = json.loads(content)
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def detect_local_assistant_action(user_text, locale, context: dict):
    lowered = user_text.lower()
    ai_result = try_extract_schedule_with_openai(user_text, locale, context)
    if isinstance(ai_result, dict) and ai_result.get("action") in {"create_event", "create_reminder", "show_schedule"}:
        return ai_result
    if any(token in user_text for token in ["查看日程", "看看日程", "我的日程", "有什么安排", "提醒列表"]) or "show my schedule" in lowered:
        return {"action": "show_schedule"}
    if any(token in user_text for token in ["提醒", "日程", "会议", "安排", "行程", "闹钟"]) or "remind me" in lowered or "schedule" in lowered:
        start_at = build_datetime_from_text(user_text)
        offset = detect_reminder_offset_minutes(user_text)
        title = infer_title_from_text(user_text)
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
        if start_at and (any(token in user_text for token in ["提醒", "闹钟"]) or "remind me" in lowered):
            return {
                "action": "create_reminder",
                "title": title if title != "家庭日程" else "HomeHub reminder",
                "startAt": start_at.isoformat(timespec="minutes"),
            }
    return {"action": "none"}


def build_household_modules(base_modules: list[dict], home_memory: dict, locale):
    modules = json.loads(json.dumps(base_modules, ensure_ascii=False))
    upcoming_events = get_upcoming_events(home_memory, limit=3)
    pending_reminders = get_pending_reminders(home_memory, limit=3)
    due_reminders = get_due_reminders(home_memory, limit=2)
    for module in modules:
        if module["id"] == "schedule":
            if upcoming_events:
                next_event = upcoming_events[0]
                if locale == "zh-CN":
                    module["summary"] = f"已记录 {len(upcoming_events)} 个本地日程。下一个是 {next_event['title']}，时间 {format_datetime_local(next_event['startAt'], locale)}。"
                    module["actionLabel"] = "查看日程"
                elif locale == "ja-JP":
                    module["summary"] = f"ローカル予定 {len(upcoming_events)} 件。次は {next_event['title']}、{format_datetime_local(next_event['startAt'], locale)}。"
                    module["actionLabel"] = "予定を見る"
                else:
                    module["summary"] = f"{len(upcoming_events)} local events tracked. Next: {next_event['title']} at {format_datetime_local(next_event['startAt'], locale)}."
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
                module["summary"] = f"已有 {len(pending_reminders)} 条提醒。下一条是 {next_reminder['title']}，将在 {format_datetime_local(next_reminder['triggerAt'], locale)} 触发。"
                module["actionLabel"] = "查看提醒"
            elif locale == "ja-JP":
                module["summary"] = f"リマインダー {len(pending_reminders)} 件。次は {next_reminder['title']}、{format_datetime_local(next_reminder['triggerAt'], locale)}。"
                module["actionLabel"] = "通知を見る"
            else:
                module["summary"] = f"{len(pending_reminders)} reminders queued. Next: {next_reminder['title']} at {format_datetime_local(next_reminder['triggerAt'], locale)}."
                module["actionLabel"] = "View Reminders"
            module["state"] = "attention" if due_reminders else "active"
    return modules
