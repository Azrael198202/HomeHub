from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


def get_secrets_file(runtime_env: str, local_file: Path, prod_file: Path) -> Path:
    if runtime_env == "prod":
        return prod_file
    return local_file


def load_secrets_file(secrets_file: Path, default_secrets):
    if not secrets_file.exists():
        return default_secrets()
    try:
        data = json.loads(secrets_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default_secrets()
    return {
        "googleApiKey": data.get("googleApiKey", ""),
        "googleAccessToken": data.get("googleAccessToken", ""),
        "openaiApiKey": data.get("openaiApiKey", ""),
        "mailAddress": data.get("mailAddress", ""),
        "mailPassword": data.get("mailPassword", ""),
        "mailSmtpHost": data.get("mailSmtpHost", ""),
        "mailSmtpPort": data.get("mailSmtpPort", ""),
        "mailImapHost": data.get("mailImapHost", ""),
        "mailImapPort": data.get("mailImapPort", ""),
        "wechatOfficialToken": data.get("wechatOfficialToken", ""),
        "wechatOfficialAppId": data.get("wechatOfficialAppId", ""),
        "wechatOfficialAppSecret": data.get("wechatOfficialAppSecret", ""),
        "wechatOfficialEncodingAesKey": data.get("wechatOfficialEncodingAesKey", ""),
        "lineChannelSecret": data.get("lineChannelSecret", ""),
        "lineChannelAccessToken": data.get("lineChannelAccessToken", ""),
        "externalBridgeUrl": data.get("externalBridgeUrl", ""),
        "externalBridgeToken": data.get("externalBridgeToken", ""),
    }


def get_effective_secrets(file_secrets: dict):
    return {
        "googleApiKey": os.environ.get("HOMEHUB_GOOGLE_API_KEY") or os.environ.get("GOOGLE_API_KEY") or file_secrets.get("googleApiKey", ""),
        "googleAccessToken": os.environ.get("HOMEHUB_GOOGLE_ACCESS_TOKEN") or os.environ.get("GOOGLE_ACCESS_TOKEN") or file_secrets.get("googleAccessToken", ""),
        "openaiApiKey": os.environ.get("HOMEHUB_OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY") or file_secrets.get("openaiApiKey", ""),
        "mailAddress": os.environ.get("HOMEHUB_MAIL_ADDRESS") or file_secrets.get("mailAddress", ""),
        "mailPassword": os.environ.get("HOMEHUB_MAIL_PASSWORD") or file_secrets.get("mailPassword", ""),
        "mailSmtpHost": os.environ.get("HOMEHUB_MAIL_SMTP_HOST") or file_secrets.get("mailSmtpHost", ""),
        "mailSmtpPort": os.environ.get("HOMEHUB_MAIL_SMTP_PORT") or file_secrets.get("mailSmtpPort", ""),
        "mailImapHost": os.environ.get("HOMEHUB_MAIL_IMAP_HOST") or file_secrets.get("mailImapHost", ""),
        "mailImapPort": os.environ.get("HOMEHUB_MAIL_IMAP_PORT") or file_secrets.get("mailImapPort", ""),
        "wechatOfficialToken": os.environ.get("HOMEHUB_WECHAT_OFFICIAL_TOKEN") or file_secrets.get("wechatOfficialToken", ""),
        "wechatOfficialAppId": os.environ.get("HOMEHUB_WECHAT_OFFICIAL_APP_ID") or file_secrets.get("wechatOfficialAppId", ""),
        "wechatOfficialAppSecret": os.environ.get("HOMEHUB_WECHAT_OFFICIAL_APP_SECRET") or file_secrets.get("wechatOfficialAppSecret", ""),
        "wechatOfficialEncodingAesKey": os.environ.get("HOMEHUB_WECHAT_OFFICIAL_ENCODING_AES_KEY") or file_secrets.get("wechatOfficialEncodingAesKey", ""),
        "lineChannelSecret": os.environ.get("HOMEHUB_LINE_CHANNEL_SECRET") or file_secrets.get("lineChannelSecret", ""),
        "lineChannelAccessToken": os.environ.get("HOMEHUB_LINE_CHANNEL_ACCESS_TOKEN") or file_secrets.get("lineChannelAccessToken", ""),
        "externalBridgeUrl": os.environ.get("HOMEHUB_EXTERNAL_BRIDGE_URL") or file_secrets.get("externalBridgeUrl", ""),
        "externalBridgeToken": os.environ.get("HOMEHUB_EXTERNAL_BRIDGE_TOKEN") or file_secrets.get("externalBridgeToken", ""),
    }


def get_secret_sources(file_secrets: dict):
    return {
        "googleApiKey": "env" if (os.environ.get("HOMEHUB_GOOGLE_API_KEY") or os.environ.get("GOOGLE_API_KEY")) else ("file" if file_secrets.get("googleApiKey") else "missing"),
        "googleAccessToken": "env" if (os.environ.get("HOMEHUB_GOOGLE_ACCESS_TOKEN") or os.environ.get("GOOGLE_ACCESS_TOKEN")) else ("file" if file_secrets.get("googleAccessToken") else "missing"),
        "openaiApiKey": "env" if (os.environ.get("HOMEHUB_OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")) else ("file" if file_secrets.get("openaiApiKey") else "missing"),
        "mailAddress": "env" if os.environ.get("HOMEHUB_MAIL_ADDRESS") else ("file" if file_secrets.get("mailAddress") else "missing"),
        "mailPassword": "env" if os.environ.get("HOMEHUB_MAIL_PASSWORD") else ("file" if file_secrets.get("mailPassword") else "missing"),
        "mailSmtpHost": "env" if os.environ.get("HOMEHUB_MAIL_SMTP_HOST") else ("file" if file_secrets.get("mailSmtpHost") else "missing"),
        "mailSmtpPort": "env" if os.environ.get("HOMEHUB_MAIL_SMTP_PORT") else ("file" if file_secrets.get("mailSmtpPort") else "missing"),
        "mailImapHost": "env" if os.environ.get("HOMEHUB_MAIL_IMAP_HOST") else ("file" if file_secrets.get("mailImapHost") else "missing"),
        "mailImapPort": "env" if os.environ.get("HOMEHUB_MAIL_IMAP_PORT") else ("file" if file_secrets.get("mailImapPort") else "missing"),
        "wechatOfficialToken": "env" if os.environ.get("HOMEHUB_WECHAT_OFFICIAL_TOKEN") else ("file" if file_secrets.get("wechatOfficialToken") else "missing"),
        "wechatOfficialAppId": "env" if os.environ.get("HOMEHUB_WECHAT_OFFICIAL_APP_ID") else ("file" if file_secrets.get("wechatOfficialAppId") else "missing"),
        "wechatOfficialAppSecret": "env" if os.environ.get("HOMEHUB_WECHAT_OFFICIAL_APP_SECRET") else ("file" if file_secrets.get("wechatOfficialAppSecret") else "missing"),
        "wechatOfficialEncodingAesKey": "env" if os.environ.get("HOMEHUB_WECHAT_OFFICIAL_ENCODING_AES_KEY") else ("file" if file_secrets.get("wechatOfficialEncodingAesKey") else "missing"),
        "lineChannelSecret": "env" if os.environ.get("HOMEHUB_LINE_CHANNEL_SECRET") else ("file" if file_secrets.get("lineChannelSecret") else "missing"),
        "lineChannelAccessToken": "env" if os.environ.get("HOMEHUB_LINE_CHANNEL_ACCESS_TOKEN") else ("file" if file_secrets.get("lineChannelAccessToken") else "missing"),
        "externalBridgeUrl": "env" if os.environ.get("HOMEHUB_EXTERNAL_BRIDGE_URL") else ("file" if file_secrets.get("externalBridgeUrl") else "missing"),
        "externalBridgeToken": "env" if os.environ.get("HOMEHUB_EXTERNAL_BRIDGE_TOKEN") else ("file" if file_secrets.get("externalBridgeToken") else "missing"),
    }


def save_secrets(secrets_file: Path, secrets: dict):
    secrets_file.write_text(json.dumps(secrets, ensure_ascii=False, indent=2), encoding="utf-8")


def get_google_service_account_file(default_file: Path) -> Path:
    path_value = os.environ.get("HOMEHUB_GOOGLE_SERVICE_ACCOUNT_JSON") or os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if path_value:
        return Path(path_value)
    return default_file


def mint_google_access_token_from_service_account(service_account_path: Path, token_cache: dict):
    script = f"""
$svc = Get-Content -LiteralPath '{str(service_account_path)}' -Raw | ConvertFrom-Json
function B64Url([byte[]]$bytes) {{
  [Convert]::ToBase64String($bytes).TrimEnd('=') -replace '\\+','-' -replace '/','_'
}}
$now = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$headerJson = '{{"alg":"RS256","typ":"JWT"}}'
$claimJson = (@{{
  iss = $svc.client_email
  scope = 'https://www.googleapis.com/auth/cloud-platform'
  aud = 'https://oauth2.googleapis.com/token'
  exp = $now + 3600
  iat = $now
}} | ConvertTo-Json -Compress)
$unsigned = (B64Url ([Text.Encoding]::UTF8.GetBytes($headerJson))) + '.' + (B64Url ([Text.Encoding]::UTF8.GetBytes($claimJson)))
$pkcs8 = [Convert]::FromBase64String(($svc.private_key -replace '-----BEGIN PRIVATE KEY-----','' -replace '-----END PRIVATE KEY-----','' -replace '\\s',''))
$key = [System.Security.Cryptography.CngKey]::Import($pkcs8, [System.Security.Cryptography.CngKeyBlobFormat]::Pkcs8PrivateBlob)
$rsa = New-Object System.Security.Cryptography.RSACng($key)
$sig = $rsa.SignData([Text.Encoding]::UTF8.GetBytes($unsigned), [System.Security.Cryptography.HashAlgorithmName]::SHA256, [System.Security.Cryptography.RSASignaturePadding]::Pkcs1)
$jwt = $unsigned + '.' + (B64Url $sig)
$body = 'grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=' + $jwt
$resp = Invoke-RestMethod -Method Post -Uri 'https://oauth2.googleapis.com/token' -ContentType 'application/x-www-form-urlencoded' -Body $body
$resp | ConvertTo-Json -Compress
"""
    result = subprocess.run(["powershell", "-NoProfile", "-Command", script], capture_output=True, text=True, check=False, timeout=30)
    if result.returncode != 0:
        raise RuntimeError(f"Failed to mint Google access token from service account. {result.stderr.strip()}")
    payload = json.loads(result.stdout.strip())
    token_cache["access_token"] = payload.get("access_token", "")
    token_cache["expires_at"] = int(datetime.now().timestamp()) + int(payload.get("expires_in", 3600)) - 60
    return token_cache["access_token"]


def get_google_cloud_headers(secrets: dict, token_cache: dict, service_account_file: Path):
    access_token = secrets.get("googleAccessToken", "")
    api_key = secrets.get("googleApiKey", "")
    if not access_token and service_account_file.exists():
        if token_cache["access_token"] and token_cache["expires_at"] > int(datetime.now().timestamp()):
            access_token = token_cache["access_token"]
        else:
            access_token = mint_google_access_token_from_service_account(service_account_file, token_cache)
    if not access_token:
        if api_key:
            return {"x-goog-api-key": api_key}
        raise RuntimeError(
            "Google Cloud credentials are not configured. "
            "Set HOMEHUB_GOOGLE_ACCESS_TOKEN / GOOGLE_ACCESS_TOKEN, "
            "or provide HOMEHUB_GOOGLE_API_KEY / GOOGLE_API_KEY, "
            "or place a service account JSON at runtime/google-cloud-service-account.json."
        )
    return {"Authorization": f"Bearer {access_token}"}


def load_persisted_settings(settings_file: Path, language_settings: dict, provider_catalog: dict, runtime_profiles: list[dict]):
    default_settings = {
        "language": language_settings["current"],
        "sttProvider": "google",
        "ttsProvider": "google",
        "runtimeProfile": "low-memory",
        "machineAccessMode": "full-access",
        "bootstrapConsent": False,
        "bootstrapCompleted": False,
        "assistantAvatarMode": "custom",
        "assistantAvatarCustomModelUrl": "/generated/avatar/pixellabs-glb-3347.glb",
    }
    if not settings_file.exists():
        return default_settings
    try:
        data = json.loads(settings_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default_settings
    supported_codes = {item["code"] for item in language_settings["supported"]}
    language = data.get("language", language_settings["current"])
    if language not in supported_codes:
        language = language_settings["current"]
    supported_providers = set(provider_catalog.keys())
    stt_provider = data.get("sttProvider", "google")
    tts_provider = data.get("ttsProvider", "google")
    if stt_provider not in supported_providers:
        stt_provider = "google"
    if tts_provider not in supported_providers:
        tts_provider = "google"
    supported_profiles = {item["id"] for item in runtime_profiles}
    runtime_profile = data.get("runtimeProfile", "low-memory")
    if runtime_profile not in supported_profiles:
        runtime_profile = "low-memory"
    machine_access_mode = str(data.get("machineAccessMode", "full-access")).strip().lower()
    if machine_access_mode not in {"full-access", "guarded"}:
        machine_access_mode = "full-access"
    assistant_avatar_mode = str(data.get("assistantAvatarMode", "custom")).strip().lower()
    if assistant_avatar_mode not in {"house", "custom"}:
        assistant_avatar_mode = "house"
    assistant_avatar_custom_model_url = str(
        data.get("assistantAvatarCustomModelUrl", "/generated/avatar/pixellabs-glb-3347.glb")
    ).strip() or "/generated/avatar/pixellabs-glb-3347.glb"
    return {
        "language": language,
        "sttProvider": stt_provider,
        "ttsProvider": tts_provider,
        "runtimeProfile": runtime_profile,
        "machineAccessMode": machine_access_mode,
        "bootstrapConsent": bool(data.get("bootstrapConsent", False)),
        "bootstrapCompleted": bool(data.get("bootstrapCompleted", False)),
        "assistantAvatarMode": assistant_avatar_mode,
        "assistantAvatarCustomModelUrl": assistant_avatar_custom_model_url,
    }


def save_persisted_settings(settings_file: Path, settings: dict):
    settings_file.write_text(json.dumps(settings, ensure_ascii=False, indent=2), encoding="utf-8")


def load_bootstrap_status(status_file: Path):
    if not status_file.exists():
        return {"stage": "idle", "message": "", "completed": False}
    try:
        data = json.loads(status_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"stage": "idle", "message": "", "completed": False}
    if not isinstance(data, dict):
        return {"stage": "idle", "message": "", "completed": False}
    return data


def save_bootstrap_status(status_file: Path, payload: dict):
    status_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def refresh_bootstrap_process_state(current_process, load_status, persisted_settings: dict, save_settings):
    if current_process is None:
        return None, persisted_settings
    code = current_process.poll()
    if code is None:
        return current_process, persisted_settings
    current_process = None
    status = load_status()
    if status.get("completed"):
        persisted_settings["bootstrapCompleted"] = True
        save_settings(persisted_settings)
    return current_process, persisted_settings


def bootstrap_snapshot(current_process, stale_seconds: int, status_file: Path, persisted_settings: dict, load_status, refresh_state):
    current_process, persisted_settings = refresh_state(current_process, load_status, persisted_settings)
    status = load_status()
    stage = status.get("stage", "idle")
    stale = False
    if stage in {"starting", "installing-tools", "installing-python", "installing-models"} and current_process is None:
        try:
            age_seconds = max(0.0, time.time() - status_file.stat().st_mtime)
        except OSError:
            age_seconds = 0.0
        stale = age_seconds > stale_seconds
        if stale:
            stage = "stalled"
            status["message"] = "Bootstrap appears to be stuck. You can continue using HomeHub and install the remaining dependencies manually."
    return {
        "approved": bool(persisted_settings.get("bootstrapConsent", False)),
        "completed": bool(persisted_settings.get("bootstrapCompleted", False)),
        "inProgress": bool(stage in {"starting", "installing-tools", "installing-python", "installing-models"}),
        "blocking": bool(stage in {"starting", "installing-tools", "installing-python"}),
        "stage": stage,
        "stale": stale,
        "message": status.get("message", ""),
        "missingCommands": status.get("missingCommands", []),
        "missingPythonModules": status.get("missingPythonModules", []),
        "installedPythonModules": status.get("installedPythonModules", []),
        "failedPythonModules": status.get("failedPythonModules", []),
        "installingPythonPackage": status.get("installingPythonPackage", ""),
        "missingOllamaModels": status.get("missingOllamaModels", []),
        "restartRequired": bool(status.get("restartRequired", False)),
    }, current_process, persisted_settings


def start_bootstrap_install(current_process, project_root: Path, bootstrap_script: Path, status_file: Path):
    if current_process is not None and current_process.poll() is None:
        return current_process, False
    save_bootstrap_status(status_file, {"stage": "starting", "message": "Preparing first-run bootstrap.", "completed": False})
    current_process = subprocess.Popen(
        [sys.executable, str(bootstrap_script), "--apply", "--quiet", "--status-file", str(status_file)],
        cwd=str(project_root),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return current_process, True
