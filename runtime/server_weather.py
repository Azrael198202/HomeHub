from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


WEATHER_CODE_LABELS = {
    0: "Clear",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Cloudy",
    45: "Fog",
    48: "Rime Fog",
    51: "Light Drizzle",
    53: "Drizzle",
    55: "Dense Drizzle",
    61: "Light Rain",
    63: "Rain",
    65: "Heavy Rain",
    66: "Light Freezing Rain",
    67: "Freezing Rain",
    71: "Light Snow",
    73: "Snow",
    75: "Heavy Snow",
    77: "Snow Grains",
    80: "Rain Showers",
    81: "Heavy Showers",
    82: "Violent Showers",
    85: "Snow Showers",
    86: "Heavy Snow Showers",
    95: "Thunderstorm",
    96: "Thunderstorm Hail",
    99: "Severe Thunderstorm",
}


def default_weather_state():
    return {
        "location": "",
        "condition": "",
        "temperatureC": None,
        "highC": None,
        "lowC": None,
        "latitude": None,
        "longitude": None,
        "source": "pending-gps",
        "updatedAt": "",
        "locationLabel": "",
        "gpsEnabled": False,
        "gpsPermission": "prompt",
    }


def load_weather_state(weather_file: Path):
    if not weather_file.exists():
        state = default_weather_state()
        save_weather_state(weather_file, state)
        return state
    try:
        data = json.loads(weather_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        state = default_weather_state()
        save_weather_state(weather_file, state)
        return state
    state = default_weather_state()
    if isinstance(data, dict):
        state.update({key: value for key, value in data.items() if key in state})
    return state


def save_weather_state(weather_file: Path, state: dict):
    weather_file.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def _json_get(url: str):
    request = urllib.request.Request(url, headers={"User-Agent": "HomeHub/0.1"})
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def _weather_label(code: int | None):
    return WEATHER_CODE_LABELS.get(int(code or 0), "Unknown")


def _normalize_place_query(query_text: str):
    text = str(query_text or "").strip()
    if not text:
        return ""
    replacements = [
        "今天",
        "今日",
        "今天的",
        "现在",
        "目前",
        "请问",
        "一下",
        "天气怎么样",
        "天气情况",
        "天气",
        "气温",
        "温度",
        "多少度",
        "几度",
        "多少",
        "预报",
        "天気",
        "天気予報",
        "weather",
        "forecast",
        "temperature",
        "how is",
        "what is",
        "today",
        "now",
    ]
    normalized = text
    for token in replacements:
        normalized = normalized.replace(token, " ")
    normalized = normalized.replace("？", " ").replace("?", " ").replace("，", " ").replace(",", " ")
    normalized = normalized.replace("的", " ").replace("の", " ")
    normalized = re.sub(r"\b\d{1,2}\s*度\b", " ", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    normalized = " ".join(part for part in normalized.split() if part)
    return normalized.strip()


def _candidate_place_queries(query_text: str):
    normalized = _normalize_place_query(query_text)
    candidates = []
    for item in [
        normalized,
        normalized.removeprefix("日本").strip(),
        normalized.removeprefix("中国").strip(),
        normalized.removeprefix("美国").strip(),
    ]:
        if item and item not in candidates:
            candidates.append(item)
    cjk_parts = [part for part in re.findall(r"[\u4e00-\u9fff]{2,}", normalized) if part]
    if cjk_parts:
        tail = cjk_parts[-1].strip()
        if tail and tail not in candidates:
            candidates.append(tail)
    return candidates


def _fetch_forecast(latitude: float, longitude: float):
    forecast_params = urllib.parse.urlencode(
        {
            "latitude": f"{latitude:.6f}",
            "longitude": f"{longitude:.6f}",
            "current": "temperature_2m,weather_code",
            "daily": "weather_code,temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
            "forecast_days": 1,
        }
    )
    return _json_get(f"https://api.open-meteo.com/v1/forecast?{forecast_params}")


def _build_weather_state(location_name: str, latitude: float, longitude: float, forecast: dict, *, source: str, gps_enabled: bool, location_label: str = ""):
    daily = forecast.get("daily", {}) if isinstance(forecast, dict) else {}
    current = forecast.get("current", {}) if isinstance(forecast, dict) else {}
    return {
        "location": location_name,
        "condition": _weather_label(current.get("weather_code")),
        "temperatureC": round(float(current.get("temperature_2m", 0))),
        "highC": round(float((daily.get("temperature_2m_max") or [0])[0] or 0)),
        "lowC": round(float((daily.get("temperature_2m_min") or [0])[0] or 0)),
        "latitude": latitude,
        "longitude": longitude,
        "source": source,
        "updatedAt": datetime.now(timezone.utc).isoformat(timespec="minutes"),
        "locationLabel": location_label or location_name,
        "gpsEnabled": gps_enabled,
        "gpsPermission": "granted" if gps_enabled else "prompt",
    }


def lookup_weather_from_query(current_state: dict, query_text: str):
    for place_query in _candidate_place_queries(query_text):
        geocode_params = urllib.parse.urlencode(
            {
                "name": place_query,
                "count": 1,
                "language": "zh",
                "format": "json",
            }
        )
        try:
            geocode = _json_get(f"https://geocoding-api.open-meteo.com/v1/search?{geocode_params}")
        except Exception:
            continue
        results = geocode.get("results", []) if isinstance(geocode, dict) else []
        result = results[0] if results else {}
        if not result:
            continue
        latitude = float(result.get("latitude", 0.0) or 0.0)
        longitude = float(result.get("longitude", 0.0) or 0.0)
        forecast = _fetch_forecast(latitude, longitude)
        location_name = ", ".join(
            [item for item in [result.get("name", ""), result.get("admin1", ""), result.get("country", "")] if item]
        ).strip(", ") or place_query
        return _build_weather_state(
            location_name,
            latitude,
            longitude,
            forecast,
            source="open-meteo-search",
            gps_enabled=False,
            location_label=place_query,
        )
    return None


def refresh_weather_from_coordinates(weather_file: Path, latitude: float, longitude: float, label: str = ""):
    forecast = _fetch_forecast(latitude, longitude)
    reverse_params = urllib.parse.urlencode(
        {
            "latitude": f"{latitude:.6f}",
            "longitude": f"{longitude:.6f}",
            "language": "en",
            "format": "json",
        }
    )
    reverse = _json_get(f"https://geocoding-api.open-meteo.com/v1/reverse?{reverse_params}")
    results = reverse.get("results", []) if isinstance(reverse, dict) else []
    result = results[0] if results else {}
    location_name = label or ", ".join(
        [item for item in [result.get("name", ""), result.get("admin1", ""), result.get("country", "")] if item]
    ).strip(", ") or f"{latitude:.3f}, {longitude:.3f}"
    state = _build_weather_state(
        location_name,
        latitude,
        longitude,
        forecast,
        source="open-meteo",
        gps_enabled=True,
        location_label=label or location_name,
    )
    save_weather_state(weather_file, state)
    return state
