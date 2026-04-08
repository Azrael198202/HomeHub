from __future__ import annotations

import base64
import io
import json
import urllib.error
import urllib.request
import wave


def build_wav_from_pcm(pcm_bytes, channels=1, rate=24000, sample_width=2):
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(rate)
        wav_file.writeframes(pcm_bytes)
    return buffer.getvalue()


def build_google_stt_config(mime_type, locale):
    mime = (mime_type or "").lower()
    config = {"languageCode": locale, "enableAutomaticPunctuation": True}
    if locale.startswith("en"):
        config["model"] = "latest_long"
    if "webm" in mime:
        config["encoding"] = "WEBM_OPUS"
        config["sampleRateHertz"] = 48000
    elif "ogg" in mime or "opus" in mime:
        config["encoding"] = "OGG_OPUS"
        config["sampleRateHertz"] = 48000
    elif "wav" in mime or "wave" in mime:
        config["encoding"] = "LINEAR16"
        config["sampleRateHertz"] = 48000
    return config


def google_transcribe_audio(audio_base64, mime_type, locale, provider_catalog: dict, persisted_settings: dict, json_post, get_google_cloud_headers, log_external_usage):
    selected_provider = provider_catalog.get(persisted_settings.get("sttProvider", "google"), provider_catalog["google"])
    headers = get_google_cloud_headers()
    payload = {"config": build_google_stt_config(mime_type, locale), "audio": {"content": audio_base64}}
    response_json = json_post("https://speech.googleapis.com/v1/speech:recognize", payload, headers=headers)
    transcript = " ".join(result.get("alternatives", [{}])[0].get("transcript", "") for result in response_json.get("results", [])).strip()
    log_external_usage("google", selected_provider["stt"]["defaultModel"], "stt", locale, transcript=transcript, audio_base64=audio_base64)
    return {"provider": "google", "model": selected_provider["stt"]["defaultModel"], "transcript": transcript}


def google_synthesize_speech(text_value, locale, provider_catalog: dict, persisted_settings: dict, json_post, get_google_cloud_headers, log_external_usage, voice_name="Kore"):
    selected_provider = provider_catalog.get(persisted_settings.get("ttsProvider", "google"), provider_catalog["google"])
    headers = get_google_cloud_headers()
    payload = {
        "input": {"text": text_value},
        "voice": {"languageCode": locale, "name": voice_name if locale.startswith("en") else ""},
        "audioConfig": {"audioEncoding": "LINEAR16"},
    }
    response_json = json_post("https://texttospeech.googleapis.com/v1/text:synthesize", payload, headers=headers)
    audio_b64 = response_json.get("audioContent")
    if not audio_b64:
        raise RuntimeError("Google TTS did not return audio data.")
    log_external_usage("google", selected_provider["tts"]["defaultModel"], "tts", locale, text_value=text_value)
    return {"provider": "google", "model": selected_provider["tts"]["defaultModel"], "audioBase64": audio_b64, "mimeType": "audio/wav"}


def build_multipart_form(fields, file_field, filename, file_bytes, mime_type):
    boundary = "----HomeHubBoundary7MA4YWxkTrZu0gW"
    lines = []
    for key, value in fields.items():
        lines.append(f"--{boundary}\r\n".encode("utf-8"))
        lines.append(f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode("utf-8"))
        lines.append(f"{value}\r\n".encode("utf-8"))
    lines.append(f"--{boundary}\r\n".encode("utf-8"))
    lines.append(f'Content-Disposition: form-data; name="{file_field}"; filename="{filename}"\r\n'.encode("utf-8"))
    lines.append(f"Content-Type: {mime_type}\r\n\r\n".encode("utf-8"))
    lines.append(file_bytes)
    lines.append(b"\r\n")
    lines.append(f"--{boundary}--\r\n".encode("utf-8"))
    return boundary, b"".join(lines)


def openai_transcribe_audio(audio_base64, mime_type, locale, model_name, secrets: dict, log_external_usage):
    api_key = secrets.get("openaiApiKey", "")
    if not api_key:
        raise RuntimeError("OpenAI API key is not configured.")
    audio_bytes = base64.b64decode(audio_base64)
    boundary, body = build_multipart_form({"model": model_name}, "file", "input.wav", audio_bytes, mime_type)
    request = urllib.request.Request(
        "https://api.openai.com/v1/audio/transcriptions",
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error: {exc}") from exc
    transcript = payload.get("text", "")
    log_external_usage("openai", model_name, "stt", locale, transcript=transcript, audio_base64=audio_base64)
    return {"provider": "openai", "model": model_name, "transcript": transcript}


def openai_synthesize_speech(text_value, locale, model_name, secrets: dict, log_external_usage):
    api_key = secrets.get("openaiApiKey", "")
    if not api_key:
        raise RuntimeError("OpenAI API key is not configured.")
    payload = {
        "model": model_name,
        "input": text_value,
        "voice": "alloy",
        "response_format": "wav",
        "instructions": f"Speak naturally in locale {locale}.",
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            wav_bytes = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Network error: {exc}") from exc
    log_external_usage("openai", model_name, "tts", locale, text_value=text_value)
    return {
        "provider": "openai",
        "model": model_name,
        "audioBase64": base64.b64encode(wav_bytes).decode("utf-8"),
        "mimeType": "audio/wav",
    }


def audio_runtime_available(runtime_name, secrets: dict, get_google_service_account_file, mode):
    runtime_name = str(runtime_name or "").strip().lower()
    if runtime_name == "openai":
        return bool(secrets.get("openaiApiKey"))
    if runtime_name == "google":
        return bool(secrets.get("googleAccessToken") or secrets.get("googleApiKey") or get_google_service_account_file().exists())
    return False


def resolve_audio_provider(provider_id, mode, catalog: dict, persisted_settings: dict, secrets: dict, get_google_service_account_file):
    requested_id = str(provider_id or "").strip()
    requested = catalog.get(requested_id)
    if requested is not None:
        runtime_name = str(requested.get(mode, {}).get("runtime", "catalog")).strip().lower()
        if audio_runtime_available(runtime_name, secrets, get_google_service_account_file, mode):
            return requested_id, requested, False
    fallback_order = [str(persisted_settings.get("sttProvider" if mode == "stt" else "ttsProvider", "")).strip(), "openai", "google"]
    seen = {requested_id} if requested_id else set()
    for candidate_id in fallback_order:
        if not candidate_id or candidate_id in seen:
            continue
        seen.add(candidate_id)
        candidate = catalog.get(candidate_id)
        if candidate is None:
            continue
        runtime_name = str(candidate.get(mode, {}).get("runtime", "catalog")).strip().lower()
        if audio_runtime_available(runtime_name, secrets, get_google_service_account_file, mode):
            return candidate_id, candidate, candidate_id != requested_id
    return requested_id, requested, False


def transcribe_audio(provider_id, audio_base64, mime_type, locale, context: dict):
    resolved_id, provider, fell_back = resolve_audio_provider(
        provider_id,
        "stt",
        context["provider_catalog"],
        context["persisted_settings"],
        context["secrets"],
        context["get_google_service_account_file"],
    )
    if not provider:
        raise RuntimeError(f"Unsupported STT provider: {provider_id}")
    runtime = provider["stt"].get("runtime", "catalog")
    model_name = provider["stt"].get("defaultModel", "unknown")
    if runtime == "google":
        result = google_transcribe_audio(
            audio_base64,
            mime_type,
            locale,
            context["provider_catalog"],
            context["persisted_settings"],
            context["json_post"],
            context["get_google_cloud_headers"],
            context["log_external_usage"],
        )
    elif runtime == "openai":
        result = openai_transcribe_audio(audio_base64, mime_type, locale, model_name, context["secrets"], context["log_external_usage"])
    else:
        raise RuntimeError("No usable speech-to-text runtime is configured. Choose OpenAI/Google credentials or wire a local STT runtime.")
    if isinstance(result, dict):
        result["requestedProvider"] = provider_id
        result["providerResolved"] = resolved_id
        result["fallbackUsed"] = fell_back
    return result


def synthesize_speech(provider_id, text_value, locale, context: dict):
    resolved_id, provider, fell_back = resolve_audio_provider(
        provider_id,
        "tts",
        context["provider_catalog"],
        context["persisted_settings"],
        context["secrets"],
        context["get_google_service_account_file"],
    )
    if not provider:
        raise RuntimeError(f"Unsupported TTS provider: {provider_id}")
    runtime = provider["tts"].get("runtime", "catalog")
    model_name = provider["tts"].get("defaultModel", "unknown")
    if runtime == "google":
        result = google_synthesize_speech(
            text_value,
            locale,
            context["provider_catalog"],
            context["persisted_settings"],
            context["json_post"],
            context["get_google_cloud_headers"],
            context["log_external_usage"],
        )
    elif runtime == "openai":
        result = openai_synthesize_speech(text_value, locale, model_name, context["secrets"], context["log_external_usage"])
    else:
        raise RuntimeError("No usable text-to-speech runtime is configured. Choose OpenAI/Google credentials or wire a local TTS runtime.")
    if isinstance(result, dict):
        result["requestedProvider"] = provider_id
        result["providerResolved"] = resolved_id
        result["fallbackUsed"] = fell_back
    return result
