from __future__ import annotations

from datetime import datetime


def build_welcome_message(locale: str | None = None, now: datetime | None = None) -> str:
    language = str(locale or "en-US")
    current = now or datetime.now()
    hour = current.hour
    if language == "zh-CN":
        if 5 <= hour < 11:
            return "早上好，HomeHub 已准备好。你今天想先处理什么？"
        if 11 <= hour < 18:
            return "下午好，HomeHub 已准备好。你现在想让我帮你做什么？"
        if 18 <= hour < 23:
            return "晚上好，HomeHub 已准备好。今晚你想先处理什么？"
        return "夜深了，HomeHub 还在。你要我先帮你处理什么？"
    if language == "ja-JP":
        if 5 <= hour < 11:
            return "おはようございます。HomeHub の準備ができました。まず何を進めますか。"
        if 11 <= hour < 18:
            return "こんにちは。HomeHub の準備ができました。何から始めましょうか。"
        if 18 <= hour < 23:
            return "こんばんは。HomeHub の準備ができました。今夜は何を手伝いましょうか。"
        return "遅い時間ですが、HomeHub は待機しています。何を進めましょうか。"
    if 5 <= hour < 11:
        return "Good morning. HomeHub is ready. What should we start with?"
    if 11 <= hour < 18:
        return "Good afternoon. HomeHub is ready. What do you want to do next?"
    if 18 <= hour < 23:
        return "Good evening. HomeHub is ready. What would you like help with tonight?"
    return "It's late, but HomeHub is still ready. What do you want to do?"


def build_initial_conversation(locale: str | None = None, now: datetime | None = None) -> list[dict[str, str]]:
    current = now or datetime.now()
    return [
        {
            "speaker": "HomeHub",
            "text": build_welcome_message(locale, current),
            "time": current.strftime("%H:%M"),
        }
    ]

