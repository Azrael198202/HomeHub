from __future__ import annotations

import re


SUPPORTED_LOCALES = {"zh-CN", "en-US", "ja-JP"}


def normalize_locale(locale: str | None, fallback: str = "en-US") -> str:
    value = str(locale or "").strip()
    if value in SUPPORTED_LOCALES:
        return value
    lowered = value.lower()
    if lowered.startswith("zh"):
        return "zh-CN"
    if lowered.startswith("ja"):
        return "ja-JP"
    if lowered.startswith("en"):
        return "en-US"
    return fallback


def contains_hiragana_or_katakana(text: str) -> bool:
    return bool(re.search(r"[\u3040-\u30ff]", text))


def contains_cjk_ideographs(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text))


def detect_text_locale(text: str, fallback: str = "en-US") -> str:
    raw = str(text or "").strip()
    if not raw:
        return normalize_locale(fallback, "en-US")
    lowered = raw.lower()
    if contains_hiragana_or_katakana(raw):
        return "ja-JP"
    if re.search(r"[a-zA-Z]", raw) and not contains_cjk_ideographs(raw):
        return "en-US"
    if any(token in lowered for token in ["receipt", "invoice", "schedule", "voice", "weather", "ocr"]):
        return normalize_locale(fallback, "en-US") if not contains_cjk_ideographs(raw) else "zh-CN"
    if contains_cjk_ideographs(raw):
        return "zh-CN"
    return normalize_locale(fallback, "en-US")


def detect_document_locale(text: str, fallback: str = "en-US") -> str:
    raw = str(text or "").strip()
    if not raw:
        return normalize_locale(fallback, "en-US")
    if contains_hiragana_or_katakana(raw):
        return "ja-JP"
    if re.search(r"[a-zA-Z]", raw) and not contains_cjk_ideographs(raw):
        return "en-US"
    if contains_cjk_ideographs(raw):
        return "zh-CN"
    return normalize_locale(fallback, "en-US")
