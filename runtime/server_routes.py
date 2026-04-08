from __future__ import annotations

from copy import deepcopy
from urllib.parse import parse_qs


def _parse_bool(value) -> bool:
    return str(value or "").strip().lower() in {"1", "true", "yes", "on"}


def handle_get_route(handler, parsed, runtime, context: dict) -> bool:
    path = parsed.path
    feature_response = context["feature_manager"].handle_api("GET", path, parse_qs(parsed.query), None, runtime)
    if feature_response:
        handler._send_feature_response(feature_response)
        return True

    if path == "/api/health":
        handler._send_json({"ok": True, "service": "homehub-runtime"})
        return True

    if path == "/api/dashboard":
        handler._send_json(context["build_dashboard"]())
        return True

    if path == "/api/bootstrap/status":
        handler._send_json(context["bootstrap_snapshot"]())
        return True

    if path == "/api/cortex/unpacked":
        params = parse_qs(parsed.query)
        request = {
            "command": str(params.get("command", [""])[0]).strip(),
            "locale": context["normalize_locale"](params.get("locale", [context["persisted_settings"]["language"]])[0], context["persisted_settings"]["language"]),
            "taskType": str(params.get("taskType", ["general_chat"])[0]).strip() or "general_chat",
            "inputModes": context["normalize_string_list"](params.get("inputModes", ["text"])[0]) or ["text"],
            "requireArtifacts": _parse_bool(params.get("requireArtifacts", ["false"])[0]),
            "requiresNetwork": _parse_bool(params.get("requiresNetwork", ["true"])[0]),
            "speakReply": _parse_bool(params.get("speakReply", ["false"])[0]),
        }
        handler._send_json(context["build_cortex_unpacked"](request))
        return True

    if path == "/api/providers":
        handler._send_json(context["model_providers"])
        return True

    if path == "/api/network/policies":
        handler._send_json({"items": list(context["network_lookup_policies"].values())})
        return True

    if path == "/api/skills":
        handler._send_json(context["skills"])
        return True

    if path == "/api/features":
        handler._send_json(context["feature_manager"].list_features(runtime))
        return True

    if path == "/api/agent-types":
        handler._send_json(context["feature_manager"].list_agent_types(context["persisted_settings"]["language"], runtime))
        return True

    if path == "/api/pairing":
        handler._send_json(context["pairing"])
        return True

    if path == "/api/relay":
        handler._send_json(context["relay_messages"])
        return True

    if path == "/api/voice":
        handler._send_json(context["voice_profile"])
        return True

    if path == "/api/semantic-memory":
        params = parse_qs(parsed.query)
        query_text = str(params.get("q", [""])[0]).strip()
        locale = context["normalize_locale"](params.get("locale", [context["persisted_settings"]["language"]])[0], context["persisted_settings"]["language"])
        if query_text:
            handler._send_json(
                {
                    "ok": True,
                    "query": query_text,
                    "locale": locale,
                    "matches": context["query_semantic_memory"](query_text, locale),
                    "backend": context["semantic_backend_snapshot"](),
                }
            )
        else:
            handler._send_json({"ok": True, "backend": context["semantic_backend_snapshot"]()})
        return True

    if path == "/api/usage/logs":
        usage_log_file = context["usage_log_file"]
        if not usage_log_file.exists():
            handler._send_json({"items": []})
            return True
        lines = usage_log_file.read_text(encoding="utf-8").splitlines()[-200:]
        items = [context["json"].loads(line) for line in lines if line.strip()]
        handler._send_json({"items": items})
        return True

    if path == "/api/run":
        task = parse_qs(parsed.query).get("task", ["Plan a family trip and show progress on TV"])[0]
        handler._send_json(
            {
                "task": task,
                "fanout": 4,
                "strategy": "planner -> device | lifestyle | developer | voice",
                "status": "running",
            }
        )
        return True

    if path == "/" or path == "/index.html":
        handler._send_file(context["static_dir"] / "index.html", "text/html; charset=utf-8")
        return True

    if path == "/assets/app.css":
        handler._send_file(context["static_dir"] / "assets" / "app.css", "text/css; charset=utf-8")
        return True

    if path == "/assets/app.js":
        handler._send_file(context["static_dir"] / "assets" / "app.js", "application/javascript; charset=utf-8")
        return True

    if path.startswith("/generated/"):
        relative = path.removeprefix("/generated/").strip("/")
        generated_dir = context["generated_dir"]
        target = (generated_dir / relative).resolve()
        try:
            target.relative_to(generated_dir.resolve())
        except ValueError:
            handler.send_error(403)
            return True
        if not target.exists() or not target.is_file():
            handler.send_error(404)
            return True
        content_type = context["mimetypes"].guess_type(str(target))[0] or "application/octet-stream"
        handler._send_file(target, content_type)
        return True

    return False


def handle_post_route(handler, parsed, runtime, preview_body, raw_text: str, request_headers: dict, context: dict) -> bool:
    feature_response = context["feature_manager"].handle_api("POST", parsed.path, parse_qs(parsed.query), preview_body, runtime)
    if feature_response:
        handler._send_feature_response(feature_response)
        return True

    if parsed.path == "/api/settings/language":
        body = preview_body
        if not body or "language" not in body:
            handler._send_json({"error": "Invalid request body"}, status=400)
            return True
        supported_codes = {item["code"] for item in context["language_settings"]["supported"]}
        language = body["language"]
        if language not in supported_codes:
            handler._send_json({"error": "Unsupported language"}, status=400)
            return True
        context["persisted_settings"]["language"] = language
        context["save_persisted_settings"](context["persisted_settings"])
        handler._send_json({"ok": True, "language": language})
        return True

    if parsed.path == "/api/cortex/unpacked":
        body = preview_body if isinstance(preview_body, dict) else {}
        request = {
            "command": str(body.get("command", "")).strip(),
            "locale": context["normalize_locale"](body.get("locale", context["persisted_settings"]["language"]), context["persisted_settings"]["language"]),
            "taskType": str(body.get("taskType", "general_chat")).strip() or "general_chat",
            "inputModes": context["normalize_string_list"](body.get("inputModes", ["text"])) or ["text"],
            "requireArtifacts": bool(body.get("requireArtifacts", False)),
            "requiresNetwork": bool(body.get("requiresNetwork", False)),
            "speakReply": bool(body.get("speakReply", False)),
        }
        handler._send_json(context["build_cortex_unpacked"](request))
        return True

    if parsed.path == "/api/semantic-memory/record":
        body = preview_body if isinstance(preview_body, dict) else {}
        source_text = str(body.get("sourceText", "")).strip()
        locale = context["normalize_locale"](body.get("locale", context["persisted_settings"]["language"]), context["persisted_settings"]["language"])
        task_spec = body.get("taskSpec", {}) if isinstance(body.get("taskSpec", {}), dict) else {}
        if not source_text or not task_spec:
            handler._send_json({"error": "sourceText and taskSpec are required"}, status=400)
            return True
        item = context["record_semantic_example"](
            source_text,
            locale,
            task_spec,
            correction_text=str(body.get("correctionText", "")).strip(),
            agent_id=str(body.get("agentId", "")).strip(),
            agent_name=str(body.get("agentName", "")).strip(),
            accepted=bool(body.get("accepted", True)),
        )
        handler._send_json({"ok": True, "item": item, "backend": context["semantic_backend_snapshot"]()})
        return True

    if parsed.path == "/api/semantic-memory/export":
        body = preview_body if isinstance(preview_body, dict) else {}
        result = context["export_training_pairs"](
            agent_id=str(body.get("agentId", "")).strip(),
            task_type=str(body.get("taskType", "")).strip(),
            limit=int(body.get("limit", 100) or 100),
        )
        handler._send_json(result)
        return True

    if parsed.path == "/api/bootstrap/approve":
        context["persisted_settings"]["bootstrapConsent"] = True
        context["persisted_settings"]["bootstrapCompleted"] = False
        context["save_persisted_settings"](context["persisted_settings"])
        context["start_bootstrap_install"]()
        handler._send_json({"ok": True, "bootstrap": context["bootstrap_snapshot"]()})
        return True

    if parsed.path == "/api/settings/audio":
        body = preview_body
        if not body:
            handler._send_json({"error": "Invalid request body"}, status=400)
            return True
        provider_catalog = context["get_audio_provider_catalog"]()
        supported_providers = set(provider_catalog.keys())
        stt_provider = body.get("sttProvider", context["persisted_settings"]["sttProvider"])
        tts_provider = body.get("ttsProvider", context["persisted_settings"]["ttsProvider"])
        if stt_provider not in supported_providers or tts_provider not in supported_providers:
            handler._send_json({"error": "Unsupported provider"}, status=400)
            return True
        if provider_catalog[stt_provider]["stt"].get("runtime") == "catalog":
            handler._send_json({"error": "Selected STT provider is catalog-only."}, status=400)
            return True
        if provider_catalog[tts_provider]["tts"].get("runtime") == "catalog":
            handler._send_json({"error": "Selected TTS provider is catalog-only."}, status=400)
            return True
        context["persisted_settings"]["sttProvider"] = stt_provider
        context["persisted_settings"]["ttsProvider"] = tts_provider
        context["save_persisted_settings"](context["persisted_settings"])
        handler._send_json({"ok": True, "sttProvider": stt_provider, "ttsProvider": tts_provider})
        return True

    if parsed.path == "/api/settings/secrets":
        body = preview_body
        if not body:
            handler._send_json({"error": "Invalid request body"}, status=400)
            return True
        file_secrets = context["load_secrets_file"]()
        google_api_key = body.get("googleApiKey", file_secrets.get("googleApiKey", ""))
        openai_api_key = body.get("openaiApiKey", file_secrets.get("openaiApiKey", ""))
        context["save_secrets"](
            {
                "googleApiKey": google_api_key,
                "googleAccessToken": body.get("googleAccessToken", file_secrets.get("googleAccessToken", "")),
                "openaiApiKey": openai_api_key,
                "mailAddress": body.get("mailAddress", file_secrets.get("mailAddress", "")),
                "mailPassword": body.get("mailPassword", file_secrets.get("mailPassword", "")),
                "mailSmtpHost": body.get("mailSmtpHost", file_secrets.get("mailSmtpHost", "")),
                "mailSmtpPort": body.get("mailSmtpPort", file_secrets.get("mailSmtpPort", "")),
                "mailImapHost": body.get("mailImapHost", file_secrets.get("mailImapHost", "")),
                "mailImapPort": body.get("mailImapPort", file_secrets.get("mailImapPort", "")),
                "wechatOfficialToken": body.get("wechatOfficialToken", file_secrets.get("wechatOfficialToken", "")),
                "wechatOfficialAppId": body.get("wechatOfficialAppId", file_secrets.get("wechatOfficialAppId", "")),
                "wechatOfficialAppSecret": body.get("wechatOfficialAppSecret", file_secrets.get("wechatOfficialAppSecret", "")),
                "wechatOfficialEncodingAesKey": body.get("wechatOfficialEncodingAesKey", file_secrets.get("wechatOfficialEncodingAesKey", "")),
                "lineChannelSecret": body.get("lineChannelSecret", file_secrets.get("lineChannelSecret", "")),
                "lineChannelAccessToken": body.get("lineChannelAccessToken", file_secrets.get("lineChannelAccessToken", "")),
                "externalBridgeUrl": body.get("externalBridgeUrl", file_secrets.get("externalBridgeUrl", "")),
                "externalBridgeToken": body.get("externalBridgeToken", file_secrets.get("externalBridgeToken", "")),
            }
        )
        secrets = context["refresh_secrets_state"]()
        secret_sources = context["get_secret_sources"]()
        handler._send_json(
            {
                "ok": True,
                "googleConfigured": bool(secrets.get("googleAccessToken") or context["get_google_service_account_file"]().exists()),
                "openaiConfigured": bool(secrets.get("openaiApiKey")),
                "mailConfigured": bool(secrets.get("mailAddress") and secrets.get("mailPassword")),
                "wechatOfficialConfigured": bool(secrets.get("wechatOfficialToken") and secrets.get("wechatOfficialAppId")),
                "lineConfigured": bool(secrets.get("lineChannelSecret") and secrets.get("lineChannelAccessToken")),
                "googleSource": "service-account-file" if context["get_google_service_account_file"]().exists() else secret_sources.get("googleAccessToken", "missing"),
                "openaiSource": secret_sources.get("openaiApiKey", "missing"),
                "mailAddressSource": secret_sources.get("mailAddress", "missing"),
                "wechatOfficialTokenSource": secret_sources.get("wechatOfficialToken", "missing"),
                "wechatOfficialAppIdSource": secret_sources.get("wechatOfficialAppId", "missing"),
                "lineChannelSecretSource": secret_sources.get("lineChannelSecret", "missing"),
                "lineChannelAccessTokenSource": secret_sources.get("lineChannelAccessToken", "missing"),
                "externalBridgeConfigured": bool(secrets.get("externalBridgeUrl") and secrets.get("externalBridgeToken")),
                "externalBridgeUrlSource": secret_sources.get("externalBridgeUrl", "missing"),
            }
        )
        return True

    if parsed.path == "/api/audio/transcribe":
        body = preview_body
        if not body or "audioBase64" not in body:
            handler._send_json({"error": "audioBase64 is required"}, status=400)
            return True
        provider = body.get("provider", context["persisted_settings"]["sttProvider"])
        mime_type = body.get("mimeType", "audio/wav")
        locale = body.get("locale", context["persisted_settings"]["language"])
        try:
            result = context["transcribe_audio"](provider, body["audioBase64"], mime_type, locale)
        except RuntimeError as exc:
            handler._send_json({"error": str(exc)}, status=502)
            return True
        except Exception as exc:
            handler._send_json({"error": f"Unexpected transcription error: {exc}"}, status=500)
            return True
        transcript_text = str(result.get("transcript", "")).strip()
        detected_locale = context["detect_text_locale"](transcript_text, context["normalize_locale"](locale, context["persisted_settings"]["language"]))
        result["detectedLocale"] = detected_locale
        handler._send_json({"ok": True, **result})
        return True

    if parsed.path == "/api/audio/synthesize":
        body = preview_body
        if not body or "text" not in body:
            handler._send_json({"error": "text is required"}, status=400)
            return True
        provider = body.get("provider", context["persisted_settings"]["ttsProvider"])
        locale = body.get("locale", context["persisted_settings"]["language"])
        try:
            result = context["synthesize_speech"](provider, body["text"], locale)
        except RuntimeError as exc:
            handler._send_json({"error": str(exc)}, status=502)
            return True
        except Exception as exc:
            handler._send_json({"error": f"Unexpected synthesis error: {exc}"}, status=500)
            return True
        handler._send_json({"ok": True, **result})
        return True

    if parsed.path == "/api/network/query":
        body = preview_body
        if not body or "query" not in body:
            handler._send_json({"error": "query is required"}, status=400)
            return True
        locale = body.get("locale", context["persisted_settings"]["language"])
        policy_id = str(body.get("policyId", "safe-general")).strip() or "safe-general"
        preferred_sources = body.get("preferredSources", []) if isinstance(body.get("preferredSources", []), list) else []
        allowed_domains = body.get("allowedDomains", []) if isinstance(body.get("allowedDomains", []), list) else []
        result = context["perform_network_lookup"](str(body.get("query", "")).strip(), locale, policy_id, preferred_sources, allowed_domains)
        handler._send_json({"ok": result.get("ok", False), **result})
        return True

    if parsed.path == "/api/voice/chat":
        body = preview_body
        if not body or "message" not in body:
            handler._send_json({"error": "message is required"}, status=400)
            return True
        message = str(body["message"]).strip()
        if not message:
            handler._send_json({"error": "message is empty"}, status=400)
            return True
        requested_locale = context["normalize_locale"](body.get("locale", context["persisted_settings"]["language"]), context["persisted_settings"]["language"])
        locale = context["detect_text_locale"](message, requested_locale)
        context["append_conversation_turn"]("You", message)
        resolution = context["resolve_voice_request"](message, locale)
        voice_route = resolution["route"]
        context["set_last_voice_route"](voice_route)
        reply_text = resolution["reply"]
        context["append_conversation_turn"]("HomeHub", reply_text, resolution.get("artifacts", []))
        audio_payload = None
        if body.get("speakReply", True):
            try:
                audio_payload = context["synthesize_speech"](context["persisted_settings"]["ttsProvider"], reply_text, locale)
            except Exception as exc:
                audio_payload = {"error": str(exc)}
        handler._send_json(
            {
                "ok": True,
                "reply": reply_text,
                "detectedLocale": locale,
                "conversation": context["current_conversation"],
                "voiceRoute": voice_route,
                "pendingVoiceClarification": resolution.get("pendingClarification"),
                "uiAction": resolution.get("uiAction"),
                "lookupResult": resolution.get("lookupResult"),
                "artifacts": resolution.get("artifacts", []),
                "assistantMemory": context["build_assistant_memory_snapshot"](),
                "audio": audio_payload,
            }
        )
        return True

    if parsed.path == "/api/settings/audio-provider":
        body = preview_body
        if not body:
            handler._send_json({"error": "Invalid request body"}, status=400)
            return True
        try:
            entry_type = str(body.get("entryType", "capability")).strip().lower() or "capability"
            provider_id = str(body.get("id", "")).strip().lower()
            if not provider_id:
                raise ValueError("Entry id is required.")
            if provider_id in context["audio_provider_catalog"]:
                raise ValueError("This provider id is reserved by a built-in stack.")
            existing = context["load_custom_audio_providers"]()
            items = [item for item in existing.get("items", []) if item.get("id") != provider_id]
            if entry_type == "provider":
                items.append(
                    {
                        "entryType": "provider",
                        "id": provider_id,
                        "label": body.get("label", provider_id),
                        "sttRuntime": body.get("sttRuntime", "catalog"),
                        "ttsRuntime": body.get("ttsRuntime", "catalog"),
                        "sttDefaultModel": body.get("sttDefaultModel", "not-configured"),
                        "sttFallbackModel": body.get("sttFallbackModel", "not-configured"),
                        "ttsDefaultModel": body.get("ttsDefaultModel", "not-configured"),
                        "ttsFallbackModel": body.get("ttsFallbackModel", "not-configured"),
                        "supportedLanguages": context["normalize_supported_languages"](body.get("supportedLanguages")),
                    }
                )
            else:
                items.append(
                    {
                        "entryType": "capability",
                        "id": provider_id,
                        "label": body.get("label", provider_id),
                        "source": body.get("source", "Custom"),
                        "summary": body.get("summary", "Custom AI capability entry."),
                        "models": context["normalize_string_list"](body.get("models")),
                        "capabilities": context["normalize_string_list"](body.get("capabilities")),
                        "supportedLanguages": context["normalize_supported_languages"](body.get("supportedLanguages")),
                        "syncOpenclaw": body.get("syncOpenclaw", "manual"),
                        "syncWorkbuddy": body.get("syncWorkbuddy", "manual"),
                    }
                )
            context["save_custom_audio_providers"]({"items": items})
        except ValueError as exc:
            handler._send_json({"error": str(exc)}, status=400)
            return True
        handler._send_json({"ok": True, "providerId": provider_id, "catalog": context["get_audio_provider_catalog"]()})
        return True

    if parsed.path == "/api/voice/reset":
        welcome_seed = context["build_initial_conversation"](context["persisted_settings"]["language"])
        context["voice_conversation"].clear()
        context["voice_conversation"].extend(deepcopy(welcome_seed))
        context["current_conversation"].clear()
        context["current_conversation"].extend(deepcopy(welcome_seed))
        context["reset_last_voice_route"]()
        context["clear_pending_voice_clarification"]()
        context["feature_manager"].reset(runtime)
        handler._send_json({"ok": True, "conversation": context["current_conversation"]})
        return True

    return False
