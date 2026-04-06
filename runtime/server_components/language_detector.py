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


def detect_text_locale(text: str, fallback: str = "en-US") -> str:
    raw = str(text or "").strip()
    if not raw:
        return normalize_locale(fallback, "en-US")
    if re.search(r"[\u3040-\u30ff]", raw):
        return "ja-JP"
    if any(token in raw for token in ["合計", "現計", "お買上", "お買い上げ", "内消費税", "ご利用額", "税込", "税率", "レシート番号", "問い合わせ"]):
        return "ja-JP"
    if re.search(r"[\u4e00-\u9fff]", raw):
        if any(token in raw for token in ["消费", "账单", "金额", "提醒", "日程", "费用", "记录", "总额", "识别"]):
            return "zh-CN"
    return normalize_locale(fallback, "en-US")


def detect_document_locale(text: str, fallback: str = "en-US") -> str:
    raw = str(text or "").strip()
    if not raw:
        return normalize_locale(fallback, "en-US")
    if re.search(r"[\u3040-\u30ff]", raw):
        return "ja-JP"
    if any(token in raw for token in ["合計", "現計", "お買上", "お買い上げ", "内消費税", "ご利用額", "税込", "税率", "レシート番号", "店舗", "取引番号"]):
        return "ja-JP"
    if re.search(r"[\u4e00-\u9fff]", raw):
        if any(token in raw for token in ["消费", "账单", "金额", "收据", "发票", "总额"]):
            return "zh-CN"
    return normalize_locale(fallback, "en-US")
