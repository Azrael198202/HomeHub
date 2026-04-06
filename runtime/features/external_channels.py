from __future__ import annotations

import base64
import hashlib
import hmac
import html
import imaplib
import json
import mimetypes
import re
import smtplib
import urllib.error
import urllib.request
from copy import deepcopy
from datetime import datetime
from email import message_from_bytes
from email.message import EmailMessage
from email.utils import parsedate_to_datetime
from pathlib import Path
from xml.etree import ElementTree as ET

from .base import HomeHubFeature, RuntimeBridge
try:
    from server_components.language_detector import detect_text_locale, normalize_locale
except ModuleNotFoundError:
    from runtime.server_components.language_detector import detect_text_locale, normalize_locale


API_ROOT = "/api/external-channels"
API_WECHAT_WEBHOOK = "/api/external-channels/wechat/webhook"
API_WECHAT_SEND = "/api/external-channels/wechat/send"
API_LINE_WEBHOOK = "/api/external-channels/line/webhook"
API_LINE_SEND = "/api/external-channels/line/send"
API_EMAIL_INTAKE = "/api/external-channels/email/intake"
API_EMAIL_SEND = "/api/external-channels/email/send"
API_EMAIL_SYNC = "/api/external-channels/email/sync"
API_BRIDGE_INBOUND = "/api/external-channels/bridge/inbound"
API_BRIDGE_PULL = "/api/external-channels/bridge/pull"
API_BRIDGE_RESULT = "/api/external-channels/bridge/result"


class Feature(HomeHubFeature):
    feature_id = "external-channels"
    feature_name = "External Channels Hub"
    version = "1.0.0"

    def descriptor(self) -> dict:
        data = super().descriptor()
        data["summary"] = "Connects external apps and email so HomeHub can receive inbound messages and route them for processing."
        data["api"] = [
            API_ROOT,
            API_WECHAT_WEBHOOK,
            API_WECHAT_SEND,
            API_LINE_WEBHOOK,
            API_LINE_SEND,
            API_EMAIL_INTAKE,
            API_EMAIL_SEND,
            API_EMAIL_SYNC,
            API_BRIDGE_INBOUND,
            API_BRIDGE_PULL,
            API_BRIDGE_RESULT,
        ]
        return data

    def storage_path(self, runtime: RuntimeBridge) -> Path:
        data_dir = runtime.root / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir / "external_channels.json"

    def debug_log_path(self, runtime: RuntimeBridge) -> Path:
        logs_dir = runtime.root / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)
        return logs_dir / "external_channels_debug.jsonl"

    def processing_log_path(self, runtime: RuntimeBridge) -> Path:
        logs_dir = runtime.root / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)
        return logs_dir / "external_channels_processing.jsonl"

    def now_iso(self) -> str:
        return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")

    def default_store(self) -> dict:
        now = self.now_iso()
        return {
            "apps": {
                "wechatOfficial": {
                    "enabled": True,
                    "status": "ready-for-webhook",
                    "summary": "Supports WeChat Official Account developer mode with signature verification and passive XML replies.",
                    "users": [],
                    "inbox": [],
                    "outbox": [],
                    "pending": [],
                },
                "line": {
                    "enabled": False,
                    "status": "ready-for-webhook",
                    "summary": "Supports LINE Messaging API webhook, bridge handoff, and outbound push replies.",
                    "users": [],
                    "inbox": [],
                    "outbox": [],
                    "pending": [],
                },
            },
            "mail": {
                "enabled": True,
                "status": "ready-for-smtp-imap",
                "summary": "Send mail through SMTP, pull inbound mail through IMAP, and route both directions through HomeHub.",
                "inbox": [],
                "outbox": [],
                "lastSyncAt": "",
            },
            "recentActions": [
                {
                    "id": "external-channels-ready",
                    "summary": "External channels hub is ready.",
                    "createdAt": now,
                }
            ],
            "lastRun": "",
        }

    def load_store(self, runtime: RuntimeBridge) -> dict:
        path = self.storage_path(runtime)
        if not path.exists():
            store = self.default_store()
            self.save_store(store, runtime)
            return store
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            store = self.default_store()
            self.save_store(store, runtime)
            return store
        if not isinstance(data, dict):
            return self.default_store()
        default = self.default_store()
        apps = data.get("apps", {}) if isinstance(data.get("apps"), dict) else {}
        mail = data.get("mail", {}) if isinstance(data.get("mail"), dict) else {}
        recent = data.get("recentActions", []) if isinstance(data.get("recentActions"), list) else []
        return {
            "apps": {
                "wechatOfficial": {**default["apps"]["wechatOfficial"], **(apps.get("wechatOfficial", {}) if isinstance(apps.get("wechatOfficial"), dict) else {})},
                "line": {**default["apps"]["line"], **(apps.get("line", {}) if isinstance(apps.get("line"), dict) else {})},
            },
            "mail": {**default["mail"], **mail},
            "recentActions": recent,
            "lastRun": str(data.get("lastRun", "")),
        }

    def save_store(self, store: dict, runtime: RuntimeBridge) -> None:
        self.storage_path(runtime).write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")

    def write_debug_log(self, runtime: RuntimeBridge, event_type: str, payload: dict) -> None:
        entry = {
            "timestamp": self.now_iso(),
            "eventType": event_type,
            **payload,
        }
        try:
            with self.debug_log_path(runtime).open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except OSError:
            return

    def write_processing_log(self, runtime: RuntimeBridge, channel: str, payload: dict) -> None:
        entry = {
            "timestamp": self.now_iso(),
            "channel": channel,
            **payload,
        }
        try:
            with self.processing_log_path(runtime).open("a", encoding="utf-8") as handle:
                handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except OSError:
            return

    def on_refresh(self, runtime: RuntimeBridge) -> None:
        runtime.state[self.feature_id] = self.load_store(runtime)

    def reset(self, runtime: RuntimeBridge) -> None:
        store = self.default_store()
        runtime.state[self.feature_id] = store
        self.save_store(store, runtime)

    def get_store(self, runtime: RuntimeBridge) -> dict:
        store = runtime.state.get(self.feature_id)
        if not isinstance(store, dict):
            store = self.load_store(runtime)
            runtime.state[self.feature_id] = store
        return store

    def append_action(self, runtime: RuntimeBridge, summary: str) -> None:
        store = self.get_store(runtime)
        store.setdefault("recentActions", []).insert(0, {"id": f"external-{self.now_iso()}", "summary": summary, "createdAt": self.now_iso()})
        del store["recentActions"][15:]
        store["lastRun"] = self.now_iso()
        self.save_store(store, runtime)

    def build_inbound_payload(self, channel: str, sender: dict, content: str, locale: str, subject: str = "") -> str:
        if channel == "email":
            return f"[email]\nfrom: {sender.get('address') or sender.get('id')}\nsubject: {subject}\ncontent: {content}"
        return f"[{channel}]\nuser: {sender.get('displayName') or sender.get('id')}\ncontent: {content}"

    def looks_like_generic_resolution(self, resolution: dict | None) -> bool:
        if not isinstance(resolution, dict) or not resolution:
            return True
        route = resolution.get("route")
        if not isinstance(route, dict):
            return True
        selected = route.get("selected")
        if not isinstance(selected, dict):
            return True
        kind = str(route.get("kind", "")).strip()
        feature_id = str(selected.get("featureId", "")).strip()
        action = str(selected.get("action", "")).strip()
        if kind == "general":
            return True
        return feature_id == "homehub-core" and action == "reply_directly"

    def build_email_resolution_candidates(self, sender: dict, content: str, subject: str, attachments: list[dict] | None = None) -> list[tuple[str, str]]:
        candidates: list[tuple[str, str]] = []
        body = str(content or "").strip()
        title = str(subject or "").strip()
        attachment_lines: list[str] = []
        for item in attachments or []:
            name = str(item.get("name", "")).strip()
            mime_type = str(item.get("mimeType", "")).strip()
            preview = str(item.get("preview", "")).strip()
            line = f"- {name or 'unnamed'}"
            if mime_type:
                line += f" ({mime_type})"
            if preview:
                line += f": {preview[:200]}"
            attachment_lines.append(line)
        attachment_summary = "\n".join(attachment_lines).strip()
        if body:
            candidates.append(("email_body_only", body))
        if body and attachment_summary:
            candidates.append(("email_body_plus_attachments", f"{body}\n\n附件：\n{attachment_summary}"))
        elif attachment_summary:
            candidates.append(("email_attachments_only", f"附件：\n{attachment_summary}"))
        metadata_payload = self.build_inbound_payload("email", sender, body, "", "").strip()
        if metadata_payload and all(item[1] != metadata_payload for item in candidates):
            candidates.append(("email_metadata_fallback", metadata_payload))
        if title and body:
            candidates.append(("email_subject_plus_body_fallback", f"{title}\n{body}"))
        elif title:
            candidates.append(("email_subject_only_fallback", title))
        return candidates

    def email_attachment_record_view(self, attachments: list[dict] | None) -> list[dict]:
        visible: list[dict] = []
        for item in attachments or []:
            if not isinstance(item, dict):
                continue
            visible.append(
                {
                    "name": str(item.get("name", "")).strip(),
                    "mimeType": str(item.get("mimeType", "")).strip(),
                    "extension": str(item.get("extension", "")).strip(),
                    "routeKind": str(item.get("routeKind", "")).strip(),
                    "sizeBytes": int(item.get("sizeBytes", 0) or 0),
                    "preview": str(item.get("preview", "")).strip(),
                }
            )
        return visible

    def classify_email_attachment(self, attachment: dict) -> dict:
        name = str(attachment.get("name", "")).strip()
        mime_type = str(attachment.get("mimeType", "")).strip().lower()
        extension = Path(name).suffix.lower()
        image_exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tif", ".tiff", ".heic"}
        text_exts = {".txt", ".md", ".csv", ".json", ".log"}
        document_exts = {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx"}
        route_kind = "metadata"
        if mime_type.startswith("image/") or extension in image_exts:
            route_kind = "image_ocr"
        elif mime_type.startswith("text/") or extension in text_exts:
            route_kind = "text_context"
        elif extension in document_exts:
            route_kind = "document_context"
        return {
            "name": name,
            "mimeType": mime_type,
            "extension": extension,
            "routeKind": route_kind,
            "sizeBytes": int(attachment.get("sizeBytes", 0) or 0),
            "preview": str(attachment.get("preview", "")).strip(),
            "imageBase64": str(attachment.get("imageBase64", "")).strip(),
        }

    def classify_email_attachments(self, attachments: list[dict] | None) -> list[dict]:
        return [self.classify_email_attachment(item) for item in (attachments or []) if isinstance(item, dict)]

    def should_route_email_attachments_to_agent(self, content: str, attachments: list[dict] | None, resolution: dict | None) -> bool:
        classified = self.classify_email_attachments(attachments)
        if not classified:
            return False
        if not any(item.get("routeKind") == "image_ocr" for item in classified):
            return False
        lowered = str(content or "").lower()
        text = str(content or "")
        image_bill_tokens = ["附件", "照片", "图片", "收据", "账单", "金额", "ocr", "电费", "发票"]
        if any(token in text for token in image_bill_tokens):
            return True
        if any(token in lowered for token in ["attachment", "photo", "image", "receipt", "bill", "amount", "invoice", "ocr"]):
            return True
        route = resolution.get("route", {}) if isinstance(resolution, dict) else {}
        task_spec = route.get("taskSpec", {}) if isinstance(route, dict) else {}
        if bool(task_spec.get("requiresImage")):
            return True
        selected = route.get("selected", {}) if isinstance(route, dict) else {}
        return str(selected.get("featureId", "")).strip() == "custom-agents"

    def resolve_email_with_attachments(
        self,
        runtime: RuntimeBridge,
        sender: dict,
        content: str,
        locale: str,
        subject: str,
        attachments: list[dict],
        initial_resolution: dict,
    ) -> dict:
        def merge_resolution_text(primary: str, secondary: str) -> str:
            first = str(primary or "").strip()
            second = str(secondary or "").strip()
            if not first:
                return second
            if not second or second == first:
                return first
            return f"{first}\n{second}"

        classified_attachments = self.classify_email_attachments(attachments)
        if not self.should_route_email_attachments_to_agent(content, classified_attachments, initial_resolution):
            return initial_resolution
        forwarded_attachments = [
            {
                "name": str(item.get("name", "")).strip(),
                "mimeType": str(item.get("mimeType", "")).strip(),
                "extension": str(item.get("extension", "")).strip(),
                "routeKind": str(item.get("routeKind", "")).strip(),
                "sizeBytes": int(item.get("sizeBytes", 0) or 0),
                "imageBase64": str(item.get("imageBase64", "")).strip(),
            }
            for item in classified_attachments
            if item.get("routeKind") == "image_ocr" and str(item.get("imageBase64", "")).strip()
        ]
        if not forwarded_attachments:
            return initial_resolution
        agent_result = runtime.call_feature(
            "custom-agents",
            {
                "mode": "api",
                "method": "POST",
                "path": "/api/custom-agents/intake",
                "body": {
                    "message": content,
                    "locale": locale,
                    "attachments": forwarded_attachments,
                },
            },
            locale,
        )
        if not isinstance(agent_result, dict):
            return initial_resolution
        body = agent_result.get("body", {}) if isinstance(agent_result.get("body"), dict) else {}
        if not bool(body.get("ok")):
            return initial_resolution
        agent_item = body.get("item", {}) if isinstance(body.get("item"), dict) else {}
        generated_feature_id = str(body.get("featureId", "")).strip() or str(agent_item.get("generatedFeatureId", "")).strip()
        executed_tasks = [
            {
                "kind": "attachment_intake",
                "featureId": "custom-agents",
                "reply": str(body.get("reply", "")).strip(),
            }
        ]
        merged_reply = str(body.get("reply", "")).strip() or str(initial_resolution.get("reply", "")).strip()
        merged_artifacts = body.get("artifacts", []) if isinstance(body.get("artifacts"), list) else []
        followup_needed = any(
            token in content.lower() or token in content
            for token in [
                "表格", "excel", "xlsx", "导出", "下载", "文件", "文档", "sheet", "spreadsheet",
                "总额", "总金额", "总的消费金额", "到目前为止", "目前为止", "累计", "明细",
                "report", "summary", "total amount", "total", "details",
            ]
        )
        if generated_feature_id and followup_needed:
            followup = runtime.call_feature(
                generated_feature_id,
                {
                    "mode": "voice",
                    "message": content,
                    "locale": locale,
                },
                locale,
            )
            if isinstance(followup, dict):
                merged_reply = merge_resolution_text(merged_reply, followup.get("reply", ""))
                if isinstance(followup.get("artifacts"), list):
                    merged_artifacts = merged_artifacts + followup.get("artifacts", [])
                executed_tasks.append(
                    {
                        "kind": "followup_feature",
                        "featureId": generated_feature_id,
                        "reply": str(followup.get("reply", "")).strip(),
                        "artifacts": [str(item.get("fileName", "")).strip() for item in followup.get("artifacts", []) if isinstance(item, dict)],
                    }
                )
        merged = {
            "reply": merged_reply,
            "artifacts": merged_artifacts,
            "route": {
                "kind": "feature",
                "selected": {
                    "featureId": "custom-agents",
                    "featureName": "Custom Agents Studio",
                    "action": "operational_agent",
                    "score": 0.99,
                },
                "candidates": [initial_resolution.get("route", {}).get("selected", {})] if isinstance(initial_resolution.get("route", {}), dict) and initial_resolution.get("route", {}).get("selected") else [],
                "reasoning": "Email attachments were forwarded into the custom agent intake path for OCR and operational handling.",
                "taskSpec": {
                    "taskType": "bill_intake",
                    "intent": "attachment-bill-intake",
                    "requiresImage": True,
                    "inputModes": ["image", "text"],
                },
            },
            "resolutionStrategy": "email_body_plus_attachment_agent",
            "attachmentAgentResult": body,
            "attachmentRouting": classified_attachments,
            "executedTasks": executed_tasks,
        }
        return merged

    def get_wechat_official_config(self, runtime: RuntimeBridge) -> dict:
        token = str(runtime.get_secret("wechatOfficialToken", "")).strip()
        app_id = str(runtime.get_secret("wechatOfficialAppId", "")).strip()
        app_secret = str(runtime.get_secret("wechatOfficialAppSecret", "")).strip()
        encoding_aes_key = str(runtime.get_secret("wechatOfficialEncodingAesKey", "")).strip()
        return {
            "token": token,
            "appId": app_id,
            "appSecret": app_secret,
            "encodingAesKey": encoding_aes_key,
            "configured": bool(token and app_id),
        }

    def get_line_config(self, runtime: RuntimeBridge) -> dict:
        channel_secret = str(runtime.get_secret("lineChannelSecret", "")).strip()
        channel_access_token = str(runtime.get_secret("lineChannelAccessToken", "")).strip()
        return {
            "channelSecret": channel_secret,
            "channelAccessToken": channel_access_token,
            "configured": bool(channel_secret and channel_access_token),
        }

    def get_bridge_config(self, runtime: RuntimeBridge) -> dict:
        target_url = str(runtime.get_secret("externalBridgeUrl", "")).strip()
        shared_token = str(runtime.get_secret("externalBridgeToken", "")).strip()
        return {
            "targetUrl": target_url.rstrip("/"),
            "sharedToken": shared_token,
            "configured": bool(target_url and shared_token),
        }

    def resolve_bridge_request(
        self,
        runtime: RuntimeBridge,
        channel: str,
        sender: dict,
        content: str,
        locale: str,
        subject: str = "",
        attachments: list[dict] | None = None,
    ) -> dict:
        resolution = self.resolve_inbound(runtime, channel, sender, content, locale, subject, attachments)
        if channel == "email":
            resolution = self.resolve_email_with_attachments(runtime, sender, content, locale, subject, attachments or [], resolution)
        return resolution

    def forward_bridge_request(
        self,
        runtime: RuntimeBridge,
        *,
        channel: str,
        sender: dict,
        content: str,
        locale: str,
        subject: str = "",
        attachments: list[dict] | None = None,
        message_type: str = "text",
        metadata: dict | None = None,
    ) -> dict:
        config = self.get_bridge_config(runtime)
        if not config["configured"]:
            return {"ok": False, "error": "bridge_not_configured"}
        target_url = f"{config['targetUrl']}{API_BRIDGE_INBOUND}"
        payload = {
            "channel": channel,
            "sender": sender,
            "content": content,
            "locale": locale,
            "subject": subject,
            "attachments": attachments or [],
            "messageType": message_type,
            "metadata": metadata or {},
            "bridgeToken": config["sharedToken"],
        }
        request = urllib.request.Request(
            target_url,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        self.write_debug_log(
            runtime,
            "bridge_forward_attempt",
            {
                "channel": channel,
                "targetUrl": target_url,
                "sender": sender,
                "subject": subject,
                "contentPreview": content[:240],
                "messageType": message_type,
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw_body = response.read().decode("utf-8", errors="replace")
            bridge_body = json.loads(raw_body)
            if not isinstance(bridge_body, dict):
                raise ValueError("Bridge response was not a JSON object.")
            self.write_debug_log(
                runtime,
                "bridge_forward_success",
                {
                    "channel": channel,
                    "targetUrl": target_url,
                    "replyPreview": str(bridge_body.get("reply", ""))[:240],
                },
            )
            return {"ok": True, "body": bridge_body}
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
            self.write_debug_log(
                runtime,
                "bridge_forward_failed",
                {
                    "channel": channel,
                    "targetUrl": target_url,
                    "error": str(exc),
                    "errorType": exc.__class__.__name__,
                },
            )
            return {"ok": False, "error": str(exc), "errorType": exc.__class__.__name__}

    def verify_wechat_signature(self, token: str, query: dict) -> bool:
        signature = str((query.get("signature") or [""])[0]).strip()
        timestamp = str((query.get("timestamp") or [""])[0]).strip()
        nonce = str((query.get("nonce") or [""])[0]).strip()
        if not token or not signature or not timestamp or not nonce:
            return False
        joined = "".join(sorted([token, timestamp, nonce]))
        expected = hashlib.sha1(joined.encode("utf-8")).hexdigest()
        return expected == signature

    def parse_wechat_xml(self, raw_text: str) -> dict:
        root = ET.fromstring(raw_text)
        payload: dict[str, str] = {}
        for child in list(root):
            payload[child.tag] = (child.text or "").strip()
        return payload

    def build_wechat_passive_reply(self, incoming: dict, reply_text: str) -> str:
        to_user = incoming.get("FromUserName", "")
        from_user = incoming.get("ToUserName", "")
        timestamp = str(int(datetime.now().timestamp()))
        safe_reply = (reply_text or "HomeHub received your message.").strip()
        return (
            "<xml>"
            f"<ToUserName><![CDATA[{to_user}]]></ToUserName>"
            f"<FromUserName><![CDATA[{from_user}]]></FromUserName>"
            f"<CreateTime>{timestamp}</CreateTime>"
            "<MsgType><![CDATA[text]]></MsgType>"
            f"<Content><![CDATA[{safe_reply}]]></Content>"
            "</xml>"
        )

    def create_bridge_queue_item(
        self,
        channel: str,
        sender: dict,
        content: str,
        locale: str,
        *,
        subject: str = "",
        message_type: str = "text",
        attachments: list[dict] | None = None,
        metadata: dict | None = None,
    ) -> dict:
        return {
            "id": f"bridge-{datetime.now().strftime('%Y%m%d%H%M%S%f')}",
            "channel": channel,
            "sender": sender,
            "content": content,
            "locale": locale,
            "subject": subject,
            "messageType": message_type,
            "attachments": attachments or [],
            "metadata": metadata or {},
            "status": "pending",
            "attempts": 0,
            "createdAt": self.now_iso(),
            "claimedAt": "",
            "completedAt": "",
        }

    def claim_pending_bridge_item(self, bucket: dict) -> dict | None:
        pending = bucket.setdefault("pending", [])
        for item in pending:
            if not isinstance(item, dict):
                continue
            if str(item.get("status", "pending")).strip() != "pending":
                continue
            item["status"] = "processing"
            item["attempts"] = int(item.get("attempts", 0) or 0) + 1
            item["claimedAt"] = self.now_iso()
            return deepcopy(item)
        return None

    def claim_pending_bridge_item_from_apps(self, apps: dict) -> dict | None:
        for app_key in ["wechatOfficial", "line"]:
            bucket = apps.get(app_key, {})
            if not isinstance(bucket, dict):
                continue
            item = self.claim_pending_bridge_item(bucket)
            if item:
                return item
        return None

    def complete_bridge_item(self, bucket: dict, message_id: str, reply: str, resolution: dict | None) -> dict | None:
        pending = bucket.setdefault("pending", [])
        for index, item in enumerate(pending):
            if not isinstance(item, dict):
                continue
            if str(item.get("id", "")).strip() != message_id:
                continue
            item["status"] = "completed"
            item["completedAt"] = self.now_iso()
            item["reply"] = reply
            if isinstance(resolution, dict):
                item["resolution"] = resolution
            return pending.pop(index)
        return None

    def complete_bridge_item_from_apps(self, apps: dict, message_id: str, reply: str, resolution: dict | None) -> dict | None:
        for app_key in ["wechatOfficial", "line"]:
            bucket = apps.get(app_key, {})
            if not isinstance(bucket, dict):
                continue
            completed = self.complete_bridge_item(bucket, message_id, reply, resolution)
            if completed:
                return completed
        return None

    def get_wechat_access_token(self, runtime: RuntimeBridge) -> tuple[str, str]:
        config = self.get_wechat_official_config(runtime)
        if not config["appId"] or not config["appSecret"]:
            return "", "wechat_app_credentials_missing"
        cache = runtime.state.setdefault("_wechatAccessToken", {"token": "", "expiresAt": 0.0})
        now_ts = datetime.now().timestamp()
        cached_token = str(cache.get("token", "")).strip()
        expires_at = float(cache.get("expiresAt", 0.0) or 0.0)
        if cached_token and expires_at > (now_ts + 60):
            return cached_token, ""
        token_url = (
            "https://api.weixin.qq.com/cgi-bin/token"
            f"?grant_type=client_credential&appid={config['appId']}&secret={config['appSecret']}"
        )
        request = urllib.request.Request(token_url, method="GET")
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                payload = json.loads(response.read().decode("utf-8", errors="replace"))
        except Exception as exc:
            return "", str(exc)
        access_token = str(payload.get("access_token", "")).strip()
        if not access_token:
            return "", str(payload.get("errmsg", "")).strip() or "wechat_access_token_failed"
        expires_in = int(payload.get("expires_in", 7200) or 7200)
        cache["token"] = access_token
        cache["expiresAt"] = now_ts + max(300, expires_in - 120)
        return access_token, ""

    def send_wechat_official_text(self, runtime: RuntimeBridge, user_id: str, content: str) -> tuple[bool, str]:
        access_token, token_error = self.get_wechat_access_token(runtime)
        if not access_token:
            self.write_debug_log(runtime, "wechat_send_failed", {"target": user_id, "error": token_error or "missing_access_token"})
            return False, token_error or "missing_access_token"
        payload = {
            "touser": user_id,
            "msgtype": "text",
            "text": {"content": content},
        }
        request = urllib.request.Request(
            f"https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={access_token}",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                result = json.loads(response.read().decode("utf-8", errors="replace"))
        except Exception as exc:
            self.write_debug_log(runtime, "wechat_send_failed", {"target": user_id, "error": str(exc), "errorType": exc.__class__.__name__})
            return False, str(exc)
        if int(result.get("errcode", 0) or 0) != 0:
            error_text = str(result.get("errmsg", "")).strip() or f"errcode={result.get('errcode')}"
            self.write_debug_log(runtime, "wechat_send_failed", {"target": user_id, "error": error_text, "response": result})
            return False, error_text
        self.write_debug_log(runtime, "wechat_send_success", {"target": user_id, "contentPreview": content[:240]})
        return True, ""

    def verify_line_signature(self, channel_secret: str, signature: str, raw_text: str) -> bool:
        if not channel_secret or not signature:
            return False
        digest = hmac.new(channel_secret.encode("utf-8"), raw_text.encode("utf-8"), hashlib.sha256).digest()
        expected = base64.b64encode(digest).decode("utf-8")
        return hmac.compare_digest(expected, signature.strip())

    def parse_line_payload(self, raw_text: str) -> dict:
        payload = json.loads(raw_text)
        return payload if isinstance(payload, dict) else {}

    def normalize_line_event(self, event: dict) -> tuple[dict, str, str, str, dict]:
        source = event.get("source", {}) if isinstance(event.get("source"), dict) else {}
        source_type = str(source.get("type", "")).strip().lower()
        sender_id = (
            str(source.get("userId", "")).strip()
            or str(source.get("groupId", "")).strip()
            or str(source.get("roomId", "")).strip()
        )
        sender = {
            "id": sender_id,
            "displayName": sender_id or source_type or "line-user",
            "remark": source_type,
        }
        reply_token = str(event.get("replyToken", "")).strip()
        event_type = str(event.get("type", "")).strip().lower() or "message"
        message = event.get("message", {}) if isinstance(event.get("message"), dict) else {}
        message_type = str(message.get("type", "")).strip().lower() or event_type
        content = ""
        if event_type == "message":
            if message_type == "text":
                content = str(message.get("text", "")).strip()
            elif message_type == "image":
                content = f"[line image]\nmessageId: {str(message.get('id', '')).strip()}".strip()
            elif message_type == "audio":
                duration = str(message.get("duration", "")).strip()
                content = f"[line audio]\nmessageId: {str(message.get('id', '')).strip()}\nduration: {duration}".strip()
            elif message_type == "video":
                content = f"[line video]\nmessageId: {str(message.get('id', '')).strip()}".strip()
            elif message_type == "file":
                content = f"[line file]\nfileName: {str(message.get('fileName', '')).strip()}\nmessageId: {str(message.get('id', '')).strip()}".strip()
            elif message_type == "location":
                content = f"[line location]\ntitle: {str(message.get('title', '')).strip()}\naddress: {str(message.get('address', '')).strip()}".strip()
            elif message_type == "sticker":
                content = f"[line sticker]\npackageId: {str(message.get('packageId', '')).strip()}\nstickerId: {str(message.get('stickerId', '')).strip()}".strip()
        elif event_type == "follow":
            message_type = "event"
            content = "用户刚刚添加了 LINE 官方账号，希望开始与 HomeHub 对话。"
        elif event_type == "join":
            message_type = "event"
            content = "LINE 官方账号被加入了群组或房间。"
        elif event_type == "postback":
            message_type = "event"
            postback = event.get("postback", {}) if isinstance(event.get("postback"), dict) else {}
            content = f"[line postback] {str(postback.get('data', '')).strip()}".strip()
        else:
            message_type = "event"
            content = f"[line event] {event_type}".strip()
        metadata = {
            "replyToken": reply_token,
            "eventType": event_type,
            "source": source,
            "messageId": str(message.get("id", "")).strip(),
        }
        return sender, message_type, content, reply_token, metadata

    def send_line_api(self, runtime: RuntimeBridge, endpoint: str, payload: dict, *, debug_prefix: str, target: str) -> tuple[bool, str]:
        config = self.get_line_config(runtime)
        if not config["configured"]:
            self.write_debug_log(runtime, f"{debug_prefix}_failed", {"target": target, "error": "line_not_configured"})
            return False, "line_not_configured"
        request = urllib.request.Request(
            f"https://api.line.me{endpoint}",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {config['channelAccessToken']}",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                raw = response.read().decode("utf-8", errors="replace").strip()
                result = json.loads(raw) if raw else {}
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            error_text = body or str(exc)
            self.write_debug_log(runtime, f"{debug_prefix}_failed", {"target": target, "error": error_text, "status": exc.code})
            return False, error_text
        except Exception as exc:
            self.write_debug_log(runtime, f"{debug_prefix}_failed", {"target": target, "error": str(exc), "errorType": exc.__class__.__name__})
            return False, str(exc)
        self.write_debug_log(runtime, f"{debug_prefix}_success", {"target": target, "response": result})
        return True, ""

    def send_line_reply_text(self, runtime: RuntimeBridge, reply_token: str, content: str) -> tuple[bool, str]:
        if not reply_token:
            return False, "missing_reply_token"
        payload = {"replyToken": reply_token, "messages": [{"type": "text", "text": content}]}
        return self.send_line_api(runtime, "/v2/bot/message/reply", payload, debug_prefix="line_reply", target=reply_token)

    def send_line_push_text(self, runtime: RuntimeBridge, user_id: str, content: str) -> tuple[bool, str]:
        if not user_id:
            return False, "missing_user_id"
        payload = {"to": user_id, "messages": [{"type": "text", "text": content}]}
        return self.send_line_api(runtime, "/v2/bot/message/push", payload, debug_prefix="line_push", target=user_id)

    def normalize_wechat_message(self, payload: dict) -> tuple[str, str]:
        message_type = str(payload.get("MsgType", "text")).strip().lower() or "text"
        event = str(payload.get("Event", "")).strip().lower()
        if message_type == "text":
            return message_type, str(payload.get("Content", "")).strip()
        if message_type == "image":
            pic_url = str(payload.get("PicUrl", "")).strip()
            media_id = str(payload.get("MediaId", "")).strip()
            return message_type, f"[wechat image]\npicUrl: {pic_url}\nmediaId: {media_id}".strip()
        if message_type == "voice":
            recognition = str(payload.get("Recognition", "")).strip()
            media_id = str(payload.get("MediaId", "")).strip()
            if recognition:
                return message_type, recognition
            return message_type, f"[wechat voice]\nmediaId: {media_id}".strip()
        if message_type == "event":
            if event == "subscribe":
                return "event", "用户刚刚关注了公众号，希望开始与 HomeHub 对话。"
            if event == "click":
                return "event", f"[wechat event click] {str(payload.get('EventKey', '')).strip()}".strip()
            if event == "view":
                return "event", f"[wechat event view] {str(payload.get('EventKey', '')).strip()}".strip()
            return "event", f"[wechat event] {event}".strip()
        return message_type, str(payload.get("Content", "")).strip()

    def resolve_inbound(self, runtime: RuntimeBridge, channel: str, sender: dict, content: str, locale: str, subject: str = "", attachments: list[dict] | None = None) -> dict:
        attachment_text = "\n".join(
            filter(
                None,
                [
                    f"{str(item.get('name', '')).strip()}\n{str(item.get('preview', '')).strip()}".strip()
                    for item in (attachments or [])
                    if isinstance(item, dict)
                ],
            )
        ).strip()
        effective_locale = detect_text_locale(
            "\n".join(filter(None, [content, attachment_text])),
            normalize_locale(locale, str(runtime.get_setting("language", "zh-CN"))),
        )
        if runtime.resolve_message:
            try:
                if channel == "email":
                    attempts: list[dict] = []
                    for strategy, candidate in self.build_email_resolution_candidates(sender, content, subject, attachments):
                        resolution = runtime.resolve_message(candidate, effective_locale) or {}
                        attempts.append(
                            {
                                "strategy": strategy,
                                "locale": effective_locale,
                                "inputPreview": candidate[:240],
                                "route": resolution.get("route"),
                                "replyPreview": str(resolution.get("reply", ""))[:240],
                            }
                        )
                        if strategy == "email_metadata_fallback" or not self.looks_like_generic_resolution(resolution):
                            resolution["effectiveLocale"] = effective_locale
                            resolution["resolutionStrategy"] = strategy
                            resolution["resolutionAttempts"] = attempts
                            return resolution
                    fallback = {"reply": ""}
                    fallback["effectiveLocale"] = effective_locale
                    fallback["resolutionStrategy"] = "email_none"
                    fallback["resolutionAttempts"] = attempts
                    return fallback
                payload = str(content or "").strip() if channel.startswith("wechat") and str(content or "").strip() else self.build_inbound_payload(channel, sender, content, locale, subject)
                resolution = runtime.resolve_message(payload, effective_locale) or {}
                if isinstance(resolution, dict):
                    resolution["effectiveLocale"] = effective_locale
                return resolution
            except Exception as exc:
                return {"reply": f"HomeHub could not process the inbound {channel} message: {exc}"}
        return {"reply": f"HomeHub received the inbound {channel} message, but the message resolver is not available."}

    def upsert_channel_user(self, users: list[dict], user: dict) -> None:
        user_id = str(user.get("id", "")).strip()
        if not user_id:
            return
        for current in users:
            if str(current.get("id", "")).strip() == user_id:
                current.update(user)
                return
        users.insert(0, user)

    def record_inbound_message(
        self,
        bucket: dict,
        sender: dict,
        content: str,
        locale: str,
        *,
        message_type: str = "text",
        subject: str = "",
        homehub_result: dict | None = None,
    ) -> dict:
        item = {
            "id": f"inbound-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "sender": sender,
            "subject": subject,
            "content": content.strip(),
            "messageType": message_type,
            "locale": locale,
            "createdAt": self.now_iso(),
            "homehubReply": str((homehub_result or {}).get("reply", "")).strip(),
            "homehubRoute": (homehub_result or {}).get("route", {}),
            "homehubResolutionStrategy": str((homehub_result or {}).get("resolutionStrategy", "")).strip(),
        }
        bucket.setdefault("inbox", []).insert(0, item)
        del bucket["inbox"][50:]
        return item

    def queue_outbound(self, bucket: dict, target: dict, content: str, kind: str, subject: str = "") -> dict:
        item = {
            "id": f"outbound-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "target": target,
            "subject": subject,
            "content": content.strip(),
            "kind": kind,
            "status": "queued",
            "createdAt": self.now_iso(),
        }
        bucket.setdefault("outbox", []).insert(0, item)
        del bucket["outbox"][50:]
        return item

    def get_mail_config(self, runtime: RuntimeBridge) -> dict:
        address = str(runtime.get_secret("mailAddress", "")).strip()
        password = str(runtime.get_secret("mailPassword", "")).strip()
        smtp_host = str(runtime.get_secret("mailSmtpHost", "")).strip() or "smtp.gmail.com"
        smtp_port = int(str(runtime.get_secret("mailSmtpPort", "")).strip() or "587")
        imap_host = str(runtime.get_secret("mailImapHost", "")).strip() or "imap.gmail.com"
        imap_port = int(str(runtime.get_secret("mailImapPort", "")).strip() or "993")
        return {
            "address": address,
            "password": password,
            "smtpHost": smtp_host,
            "smtpPort": smtp_port,
            "imapHost": imap_host,
            "imapPort": imap_port,
            "configured": bool(address and password),
        }

    def resolve_artifact_attachments(self, runtime: RuntimeBridge, artifacts: list[dict] | None) -> list[dict]:
        resolved: list[dict] = []
        for artifact in artifacts or []:
            if not isinstance(artifact, dict):
                continue
            relative_path = str(artifact.get("path", "")).strip()
            if not relative_path:
                continue
            path = runtime.root / relative_path
            if not path.exists() or not path.is_file():
                continue
            mime_type, _encoding = mimetypes.guess_type(path.name)
            maintype, subtype = (mime_type or "application/octet-stream").split("/", 1)
            resolved.append(
                {
                    "path": path,
                    "fileName": str(artifact.get("fileName", "")).strip() or path.name,
                    "maintype": maintype,
                    "subtype": subtype,
                    "kind": str(artifact.get("kind", "")).strip(),
                    "label": str(artifact.get("label", "")).strip(),
                }
            )
        return resolved

    def send_email_via_smtp(
        self,
        runtime: RuntimeBridge,
        to_address: str,
        subject: str,
        content: str,
        artifacts: list[dict] | None = None,
    ) -> tuple[bool, str]:
        config = self.get_mail_config(runtime)
        if not config["configured"]:
            self.write_debug_log(
                runtime,
                "email_send_skipped",
                {
                    "reason": "mail_not_configured",
                    "target": to_address,
                    "subject": subject,
                },
            )
            return False, "Mail channel is not configured."
        message = EmailMessage()
        message["From"] = config["address"]
        message["To"] = to_address
        message["Subject"] = subject or "HomeHub"
        message.set_content(content)
        attachment_files = self.resolve_artifact_attachments(runtime, artifacts)
        for item in attachment_files:
            message.add_attachment(
                item["path"].read_bytes(),
                maintype=item["maintype"],
                subtype=item["subtype"],
                filename=item["fileName"],
            )
        self.write_debug_log(
            runtime,
            "email_send_attempt",
            {
                "target": to_address,
                "subject": subject,
                "smtpHost": config["smtpHost"],
                "smtpPort": config["smtpPort"],
                "from": config["address"],
                "bodyPreview": content[:240],
                "attachments": [item["fileName"] for item in attachment_files],
            },
        )
        try:
            with smtplib.SMTP(config["smtpHost"], config["smtpPort"], timeout=30) as client:
                client.starttls()
                client.login(config["address"], config["password"])
                client.send_message(message)
            self.write_debug_log(
                runtime,
                "email_send_success",
                {
                    "target": to_address,
                    "subject": subject,
                    "smtpHost": config["smtpHost"],
                    "smtpPort": config["smtpPort"],
                    "attachments": [item["fileName"] for item in attachment_files],
                },
            )
            return True, ""
        except Exception as exc:
            self.write_debug_log(
                runtime,
                "email_send_failed",
                {
                    "target": to_address,
                    "subject": subject,
                    "smtpHost": config["smtpHost"],
                    "smtpPort": config["smtpPort"],
                    "error": str(exc),
                    "errorType": exc.__class__.__name__,
                    "attachments": [item["fileName"] for item in attachment_files],
                },
            )
            return False, str(exc)

    def build_reply_subject(self, subject: str) -> str:
        clean = str(subject or "").strip()
        if not clean:
            return "Re: HomeHub"
        lowered = clean.lower()
        if lowered.startswith("re:"):
            return clean
        return f"Re: {clean}"

    def should_auto_reply_email(self, content: str, attachments: list[dict] | None = None) -> bool:
        attachment_text = "\n".join(
            filter(
                None,
                [
                    str(item.get("name", "")).strip() + ("\n" + str(item.get("preview", "")).strip() if str(item.get("preview", "")).strip() else "")
                    for item in (attachments or [])
                ],
            )
        ).strip()
        combined = f"{content}\n{attachment_text}".strip()
        lowered = combined.lower()
        return ("小栖" in combined) or ("homehub" in lowered)

    def send_inbound_email_reply(
        self,
        runtime: RuntimeBridge,
        sender: dict,
        subject: str,
        reply_text: str,
        artifacts: list[dict] | None = None,
    ) -> tuple[bool, str]:
        config = self.get_mail_config(runtime)
        target = str(sender.get("address") or sender.get("id") or "").strip()
        if not target:
            return False, "Missing sender address."
        if target.lower() == str(config.get("address", "")).strip().lower():
            self.write_debug_log(
                runtime,
                "email_auto_reply_skipped",
                {
                    "reason": "same_as_sender_account",
                    "target": target,
                    "subject": subject,
                },
            )
            return False, "Skipped self-reply."
        reply_subject = self.build_reply_subject(subject)
        self.write_debug_log(
            runtime,
            "email_auto_reply_attempt",
            {
                "target": target,
                "subject": reply_subject,
                "bodyPreview": str(reply_text or "")[:240],
                "attachments": [str(item.get("fileName", "")).strip() for item in (artifacts or []) if isinstance(item, dict)],
            },
        )
        ok, error = self.send_email_via_smtp(runtime, target, reply_subject, reply_text, artifacts)
        self.write_debug_log(
            runtime,
            "email_auto_reply_success" if ok else "email_auto_reply_failed",
            {
                "target": target,
                "subject": reply_subject,
                "error": error,
                "attachments": [str(item.get("fileName", "")).strip() for item in (artifacts or []) if isinstance(item, dict)],
            },
        )
        return ok, error

    def extract_email_text(self, message) -> str:
        if message.is_multipart():
            html_candidate = ""
            for part in message.walk():
                content_type = str(part.get_content_type() or "").lower()
                disposition = str(part.get("Content-Disposition", "")).lower()
                if "attachment" in disposition:
                    continue
                payload = part.get_payload(decode=True) or b""
                charset = part.get_content_charset() or "utf-8"
                if content_type == "text/plain":
                    return payload.decode(charset, errors="ignore").strip()
                if content_type == "text/html" and not html_candidate:
                    html_candidate = payload.decode(charset, errors="ignore").strip()
            return self.extract_text_from_html(html_candidate) if html_candidate else ""
        payload = message.get_payload(decode=True) or b""
        charset = message.get_content_charset() or "utf-8"
        raw = payload.decode(charset, errors="ignore").strip()
        if str(message.get_content_type() or "").lower() == "text/html":
            return self.extract_text_from_html(raw)
        return raw

    def extract_text_from_html(self, html_text: str) -> str:
        raw = str(html_text or "").strip()
        if not raw:
            return ""
        text = re.sub(r"(?is)<(script|style).*?>.*?</\\1>", " ", raw)
        text = re.sub(r"(?i)<br\\s*/?>", "\n", text)
        text = re.sub(r"(?i)</p\\s*>", "\n", text)
        text = re.sub(r"(?s)<[^>]+>", " ", text)
        text = html.unescape(text)
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    def extract_email_attachments(self, message) -> list[dict]:
        attachments: list[dict] = []
        if not message.is_multipart():
            return attachments
        for part in message.walk():
            disposition = str(part.get("Content-Disposition", "")).lower()
            name = str(part.get_filename() or "").strip()
            mime_type = str(part.get_content_type() or "").strip().lower()
            is_attachment = "attachment" in disposition or bool(name)
            if not is_attachment:
                continue
            payload = part.get_payload(decode=True) or b""
            preview = ""
            if mime_type.startswith("text/"):
                charset = part.get_content_charset() or "utf-8"
                preview = payload.decode(charset, errors="ignore").strip()[:500]
            attachments.append(
                {
                    "name": name,
                    "mimeType": mime_type,
                    "sizeBytes": len(payload),
                    "preview": preview,
                    "imageBase64": base64.b64encode(payload).decode("utf-8") if mime_type.startswith("image/") and payload else "",
                }
            )
        return attachments

    def list_imap_mailboxes(self, client) -> list[str]:
        names: list[str] = []
        try:
            status, payload = client.list()
        except Exception:
            return names
        if status != "OK" or not payload:
            return names
        for raw in payload:
            line = raw.decode("utf-8", errors="ignore") if isinstance(raw, (bytes, bytearray)) else str(raw)
            parts = line.rsplit(' "', 1)
            if len(parts) == 2:
                mailbox = parts[1].rstrip('"').strip()
                if mailbox:
                    names.append(mailbox)
        return names

    def candidate_imap_mailboxes(self, client) -> list[str]:
        listed = self.list_imap_mailboxes(client)
        candidates: list[str] = []
        seen: set[str] = set()

        def add(name: str) -> None:
            value = str(name or "").strip()
            if value and value not in seen:
                seen.add(value)
                candidates.append(value)

        add("INBOX")
        for mailbox in listed:
            lowered = mailbox.lower()
            if "all mail" in lowered or "allmail" in lowered or "すべて" in mailbox or "所有邮件" in mailbox or "全部邮件" in mailbox:
                add(mailbox)
        return candidates

    def build_email_record_id(self, uid: str, email_message) -> str:
        header_id = str(email_message.get("Message-ID", "")).strip()
        if header_id:
            return f"imap-msgid-{header_id}"
        return f"imap-uid-{uid}"

    def sync_mailbox(self, runtime: RuntimeBridge, limit: int = 10) -> dict:
        config = self.get_mail_config(runtime)
        if not config["configured"]:
            self.write_debug_log(runtime, "email_sync_skipped", {"reason": "mail_not_configured"})
            return {"ok": False, "error": "Mail channel is not configured."}
        store = self.get_store(runtime)
        mail = store.setdefault("mail", self.default_store()["mail"])
        known_ids = {str(item.get("id", "")).strip() for item in mail.get("inbox", []) if isinstance(item, dict)}
        imported = 0
        self.write_debug_log(
            runtime,
            "email_sync_attempt",
            {
                "imapHost": config["imapHost"],
                "imapPort": config["imapPort"],
                "address": config["address"],
                "limit": limit,
                "knownInboxCount": len(known_ids),
            },
        )
        try:
            with imaplib.IMAP4_SSL(config["imapHost"], config["imapPort"]) as client:
                client.login(config["address"], config["password"])
                for mailbox in self.candidate_imap_mailboxes(client):
                    try:
                        select_status, _ = client.select(mailbox, readonly=True)
                    except Exception:
                        continue
                    if select_status != "OK":
                        continue
                    status, payload = client.uid("search", None, "ALL")
                    if status != "OK":
                        continue
                    message_uids = [item for item in (payload[0].split() if payload and payload[0] else []) if item]
                    recent_uids = message_uids[-max(limit * 5, 25):]
                    for message_uid in reversed(recent_uids):
                        fetch_status, fetched = client.uid("fetch", message_uid, "(RFC822)")
                        if fetch_status != "OK" or not fetched:
                            self.write_debug_log(
                                runtime,
                                "email_sync_skipped_message",
                                {
                                    "messageUid": message_uid.decode("utf-8", errors="ignore"),
                                    "mailbox": mailbox,
                                    "reason": "fetch_failed",
                                },
                            )
                            continue
                        raw_message = fetched[0][1]
                        email_message = message_from_bytes(raw_message)
                        inbox_id = self.build_email_record_id(message_uid.decode("utf-8", errors="ignore"), email_message)
                        if inbox_id in known_ids:
                            self.write_debug_log(
                                runtime,
                                "email_sync_skipped_message",
                                {
                                    "messageId": inbox_id,
                                    "messageUid": message_uid.decode("utf-8", errors="ignore"),
                                    "mailbox": mailbox,
                                    "reason": "already_known",
                                },
                            )
                            continue
                        from_address = str(email_message.get("From", "")).strip()
                        subject = str(email_message.get("Subject", "")).strip()
                        content = self.extract_email_text(email_message)
                        attachments = self.extract_email_attachments(email_message)
                        if not from_address or (not content and not attachments):
                            self.write_debug_log(
                                runtime,
                                "email_sync_skipped_message",
                                {
                                    "messageId": inbox_id,
                                    "messageUid": message_uid.decode("utf-8", errors="ignore"),
                                    "mailbox": mailbox,
                                    "from": from_address,
                                    "subject": subject,
                                    "reason": "empty_content_and_no_attachments" if from_address else "missing_from_address",
                                    "contentType": str(email_message.get_content_type() or "").strip().lower(),
                                    "isMultipart": bool(email_message.is_multipart()),
                                },
                            )
                            continue
                        sender = {
                            "id": from_address,
                            "address": from_address,
                            "displayName": from_address,
                        }
                        locale = str(runtime.get_setting("language", "zh-CN")).strip() or "zh-CN"
                        resolution = self.resolve_inbound(runtime, "email", sender, content, locale, subject, attachments)
                        resolution = self.resolve_email_with_attachments(runtime, sender, content, locale, subject, attachments, resolution)
                        item = self.record_inbound_message(mail, sender, content, locale, message_type="email", subject=subject, homehub_result=resolution)
                        item["id"] = inbox_id
                        item["mailbox"] = mailbox
                        item["imapUid"] = message_uid.decode("utf-8", errors="ignore")
                        if attachments:
                            item["attachments"] = self.email_attachment_record_view(self.classify_email_attachments(attachments))
                        reply_text = str(resolution.get("reply", "")).strip()
                        reply_artifacts = resolution.get("artifacts", []) if isinstance(resolution.get("artifacts"), list) else []
                        if reply_text and self.should_auto_reply_email(content, attachments):
                            reply_ok, reply_error = self.send_inbound_email_reply(runtime, sender, subject, reply_text, reply_artifacts)
                            item["autoReply"] = {
                                "ok": reply_ok,
                                "error": reply_error,
                                "subject": self.build_reply_subject(subject),
                                "attachments": [str(artifact.get("fileName", "")).strip() for artifact in reply_artifacts if isinstance(artifact, dict)],
                            }
                        elif reply_text:
                            item["autoReply"] = {
                                "ok": False,
                                "error": "Skipped because the email did not mention 小栖 or homehub.",
                                "subject": self.build_reply_subject(subject),
                                "attachments": [str(artifact.get("fileName", "")).strip() for artifact in reply_artifacts if isinstance(artifact, dict)],
                            }
                            self.write_debug_log(
                                runtime,
                                "email_auto_reply_skipped",
                                {
                                    "reason": "missing_reply_keyword",
                                    "target": sender["address"],
                                    "subject": subject,
                                    "contentPreview": content[:240],
                                    "attachmentNames": [str(item.get("name", "")).strip() for item in attachments],
                                },
                            )
                        date_header = str(email_message.get("Date", "")).strip()
                        if date_header:
                            try:
                                item["sourceDate"] = parsedate_to_datetime(date_header).isoformat()
                            except Exception:
                                item["sourceDate"] = date_header
                        self.write_processing_log(
                            runtime,
                            "email",
                            {
                                "eventType": "inbound_processed",
                                "messageId": inbox_id,
                                "sender": sender,
                                "subject": subject,
                                "content": content[:4000],
                                "attachments": item.get("attachments", []),
                                "mailbox": mailbox,
                                "imapUid": item["imapUid"],
                                "route": resolution.get("route", {}),
                                "effectiveLocale": resolution.get("effectiveLocale", locale),
                                "resolutionStrategy": resolution.get("resolutionStrategy", ""),
                                "attachmentRouting": resolution.get("attachmentRouting", []),
                                "executedTasks": resolution.get("executedTasks", []),
                                "reply": reply_text,
                                "artifacts": reply_artifacts,
                                "autoReply": item.get("autoReply", {}),
                            },
                        )
                        known_ids.add(inbox_id)
                        imported += 1
                mail["lastSyncAt"] = self.now_iso()
                self.save_store(store, runtime)
                self.append_action(runtime, f"Synchronized {imported} inbound email message(s).")
                self.write_debug_log(
                    runtime,
                    "email_sync_success",
                    {
                        "imapHost": config["imapHost"],
                        "imapPort": config["imapPort"],
                        "address": config["address"],
                        "imported": imported,
                        "lastSyncAt": mail["lastSyncAt"],
                    },
                )
                return {"ok": True, "imported": imported, "lastSyncAt": mail["lastSyncAt"]}
        except Exception as exc:
            self.write_debug_log(
                runtime,
                "email_sync_failed",
                {
                    "imapHost": config["imapHost"],
                    "imapPort": config["imapPort"],
                    "address": config["address"],
                    "error": str(exc),
                    "errorType": exc.__class__.__name__,
                },
            )
            return {"ok": False, "error": str(exc)}

    def enhance_household_modules(self, modules: list[dict], locale: str, runtime: RuntimeBridge) -> list[dict]:
        current = deepcopy(modules)
        store = self.get_store(runtime)
        apps = store.get("apps", {})
        wechat = apps.get("wechatOfficial", {}) if isinstance(apps.get("wechatOfficial"), dict) else {}
        mail = store.get("mail", {}) if isinstance(store.get("mail"), dict) else {}
        if locale == "zh-CN":
            apps_summary = f"外接应用已准备好，公众号收件 {len(wechat.get('inbox', []))} 条，LINE 收件 {len(line.get('inbox', []))} 条。"
            mail_summary = f"邮件模块已准备好，当前收件 {len(mail.get('inbox', []))} 条，发件队列 {len(mail.get('outbox', []))} 条。"
            apps_name = "外部应用连接"
            mail_name = "邮件收发"
        else:
            apps_summary = f"External app bridge ready. WeChat inbox: {len(wechat.get('inbox', []))}, LINE inbox: {len(line.get('inbox', []))}."
            mail_summary = f"Mail bridge ready. Inbox: {len(mail.get('inbox', []))}, outbox: {len(mail.get('outbox', []))}."
            apps_name = "External Apps"
            mail_name = "Mail Hub"
        current.append({"id": "external-apps", "name": apps_name, "summary": apps_summary, "state": "active", "actionLabel": "Open"})
        current.append({"id": "external-mail", "name": mail_name, "summary": mail_summary, "state": "active", "actionLabel": "Open"})
        return current

    def dashboard_payload(self, locale: str, runtime: RuntimeBridge) -> dict:
        store = self.get_store(runtime)
        wechat_config = self.get_wechat_official_config(runtime)
        line_config = self.get_line_config(runtime)
        mail_config = self.get_mail_config(runtime)
        return {
            "externalChannels": {
                "apps": store.get("apps", {}),
                "mail": store.get("mail", {}),
                "recentActions": store.get("recentActions", [])[:8],
                "wechatOfficialConfig": {
                    "configured": wechat_config["configured"],
                    "appId": wechat_config["appId"],
                    "tokenConfigured": bool(wechat_config["token"]),
                    "appSecretConfigured": bool(wechat_config["appSecret"]),
                    "encodingAesKeyConfigured": bool(wechat_config["encodingAesKey"]),
                    "webhookUrl": API_WECHAT_WEBHOOK,
                },
                "lineConfig": {
                    "configured": line_config["configured"],
                    "channelSecretConfigured": bool(line_config["channelSecret"]),
                    "channelAccessTokenConfigured": bool(line_config["channelAccessToken"]),
                    "webhookUrl": API_LINE_WEBHOOK,
                },
                "mailConfig": {
                    "configured": mail_config["configured"],
                    "address": mail_config["address"],
                    "smtpHost": mail_config["smtpHost"],
                    "smtpPort": mail_config["smtpPort"],
                    "imapHost": mail_config["imapHost"],
                    "imapPort": mail_config["imapPort"],
                },
                "bridgeConfig": self.get_bridge_config(runtime),
            }
        }

    def handle_api(self, method: str, path: str, query: dict, body: dict | None, runtime: RuntimeBridge) -> dict | None:
        store = self.get_store(runtime)
        apps = store.setdefault("apps", {})
        wechat = apps.setdefault("wechatOfficial", self.default_store()["apps"]["wechatOfficial"])
        line = apps.setdefault("line", self.default_store()["apps"]["line"])
        mail = store.setdefault("mail", self.default_store()["mail"])

        if method == "GET" and path == API_ROOT:
            return {
                "status": 200,
                "body": {
                    "apps": apps,
                    "mail": mail,
                    "recentActions": store.get("recentActions", [])[:10],
                    "wechatOfficialConfig": self.get_wechat_official_config(runtime),
                    "lineConfig": self.get_line_config(runtime),
                    "mailConfig": self.get_mail_config(runtime),
                    "bridgeConfig": self.get_bridge_config(runtime),
                },
            }

        if method == "POST" and path == API_BRIDGE_PULL:
            payload = body or {}
            bridge_config = self.get_bridge_config(runtime)
            shared_token = str(payload.get("bridgeToken", "")).strip()
            if not bridge_config["sharedToken"] or shared_token != bridge_config["sharedToken"]:
                self.write_debug_log(runtime, "bridge_pull_rejected", {"reason": "invalid_bridge_token"})
                return {"status": 403, "body": {"ok": False, "error": "invalid_bridge_token"}}
            item = self.claim_pending_bridge_item_from_apps(apps)
            self.save_store(store, runtime)
            if not item:
                return {"status": 200, "body": {"ok": True, "item": None}}
            self.write_debug_log(
                runtime,
                "bridge_pull_success",
                {
                    "messageId": item["id"],
                    "channel": item["channel"],
                    "sender": item.get("sender", {}),
                    "messageType": item.get("messageType", "text"),
                },
            )
            return {"status": 200, "body": {"ok": True, "item": item}}

        if method == "POST" and path == API_BRIDGE_INBOUND:
            payload = body or {}
            bridge_config = self.get_bridge_config(runtime)
            shared_token = str(payload.get("bridgeToken", "")).strip()
            if bridge_config["sharedToken"] and shared_token != bridge_config["sharedToken"]:
                self.write_debug_log(runtime, "bridge_inbound_rejected", {"reason": "invalid_bridge_token"})
                return {"status": 403, "body": {"ok": False, "error": "invalid_bridge_token"}}
            channel = str(payload.get("channel", "")).strip() or "bridge"
            sender = payload.get("sender", {}) if isinstance(payload.get("sender"), dict) else {}
            content = str(payload.get("content", "")).strip()
            locale = str(payload.get("locale", runtime.get_setting("language", "zh-CN"))).strip() or "zh-CN"
            subject = str(payload.get("subject", "")).strip()
            attachments = payload.get("attachments", []) if isinstance(payload.get("attachments"), list) else []
            message_type = str(payload.get("messageType", "text")).strip() or "text"
            if not content and not attachments:
                return {"status": 400, "body": {"ok": False, "error": "content or attachments are required"}}
            resolution = self.resolve_bridge_request(runtime, channel, sender, content, locale, subject, attachments)
            reply_text = str(resolution.get("reply", "")).strip()
            self.write_processing_log(
                runtime,
                f"{channel}-bridge",
                {
                    "eventType": "bridge_inbound_processed",
                    "sender": sender,
                    "messageType": message_type,
                    "subject": subject,
                    "content": content[:4000],
                    "attachments": self.email_attachment_record_view(self.classify_email_attachments(attachments)) if attachments else [],
                    "route": resolution.get("route", {}),
                    "effectiveLocale": resolution.get("effectiveLocale", locale),
                    "resolutionStrategy": resolution.get("resolutionStrategy", ""),
                    "attachmentRouting": resolution.get("attachmentRouting", []),
                    "executedTasks": resolution.get("executedTasks", []),
                    "reply": reply_text,
                    "artifacts": resolution.get("artifacts", []) if isinstance(resolution.get("artifacts"), list) else [],
                },
            )
            return {
                "status": 200,
                "body": {
                    "ok": True,
                    "reply": reply_text,
                    "resolution": resolution,
                },
            }

        if method == "POST" and path == API_BRIDGE_RESULT:
            payload = body or {}
            bridge_config = self.get_bridge_config(runtime)
            shared_token = str(payload.get("bridgeToken", "")).strip()
            if not bridge_config["sharedToken"] or shared_token != bridge_config["sharedToken"]:
                self.write_debug_log(runtime, "bridge_result_rejected", {"reason": "invalid_bridge_token"})
                return {"status": 403, "body": {"ok": False, "error": "invalid_bridge_token"}}
            message_id = str(payload.get("messageId", "")).strip()
            reply = str(payload.get("reply", "")).strip()
            resolution = payload.get("resolution", {}) if isinstance(payload.get("resolution"), dict) else {}
            if not message_id:
                return {"status": 400, "body": {"ok": False, "error": "messageId is required"}}
            completed = self.complete_bridge_item_from_apps(apps, message_id, reply, resolution)
            if not completed:
                return {"status": 404, "body": {"ok": False, "error": "message_not_found"}}
            target_user = str((completed.get("sender") or {}).get("id", "")).strip()
            channel = str(completed.get("channel", "")).strip()
            send_ok = False
            send_error = ""
            if channel == "wechat-official" and target_user and reply:
                send_ok, send_error = self.send_wechat_official_text(runtime, target_user, reply)
                out_item = self.queue_outbound(
                    wechat,
                    {"id": target_user, "displayName": target_user},
                    reply,
                    "wechat-official",
                )
                out_item["status"] = "sent" if send_ok else "failed"
                if send_error:
                    out_item["error"] = send_error
            elif channel == "line" and target_user and reply:
                send_ok, send_error = self.send_line_push_text(runtime, target_user, reply)
                out_item = self.queue_outbound(
                    line,
                    {"id": target_user, "displayName": target_user},
                    reply,
                    "line",
                )
                out_item["status"] = "sent" if send_ok else "failed"
                if send_error:
                    out_item["error"] = send_error
            self.save_store(store, runtime)
            self.write_debug_log(
                runtime,
                "bridge_result_processed",
                {
                    "messageId": message_id,
                    "channel": channel,
                    "targetUser": target_user,
                    "replyPreview": reply[:240],
                    "sendOk": send_ok,
                    "sendError": send_error,
                },
            )
            self.write_processing_log(
                runtime,
                channel or "external-bridge",
                {
                    "eventType": "bridge_result_processed",
                    "messageId": message_id,
                    "sender": completed.get("sender", {}),
                    "content": str(completed.get("content", ""))[:4000],
                    "reply": reply,
                    "sendOk": send_ok,
                    "sendError": send_error,
                    "route": resolution.get("route", {}),
                    "effectiveLocale": resolution.get("effectiveLocale", completed.get("locale", "")),
                    "resolutionStrategy": resolution.get("resolutionStrategy", ""),
                },
            )
            return {"status": 200, "body": {"ok": True, "sendOk": send_ok, "sendError": send_error}}

        if method == "GET" and path == API_WECHAT_WEBHOOK:
            config = self.get_wechat_official_config(runtime)
            if not config["configured"]:
                self.write_debug_log(runtime, "wechat_verify_failed", {"reason": "wechat_not_configured"})
                return {
                    "status": 503,
                    "rawBody": "wechat official account is not configured",
                    "contentType": "text/plain; charset=utf-8",
                }
            if not self.verify_wechat_signature(config["token"], query):
                self.write_debug_log(
                    runtime,
                    "wechat_verify_failed",
                    {
                        "reason": "invalid_signature",
                        "timestamp": str((query.get("timestamp") or [""])[0]),
                        "nonce": str((query.get("nonce") or [""])[0]),
                    },
                )
                return {
                    "status": 403,
                    "rawBody": "invalid signature",
                    "contentType": "text/plain; charset=utf-8",
                }
            echostr = str((query.get("echostr") or [""])[0])
            self.write_debug_log(runtime, "wechat_verify_success", {"echostr": echostr})
            self.append_action(runtime, "Verified WeChat Official Account webhook challenge.")
            return {
                "status": 200,
                "rawBody": echostr,
                "contentType": "text/plain; charset=utf-8",
            }

        if method == "POST" and path == API_WECHAT_WEBHOOK:
            config = self.get_wechat_official_config(runtime)
            if not config["configured"]:
                self.write_debug_log(runtime, "wechat_inbound_failed", {"reason": "wechat_not_configured"})
                return {"status": 503, "body": {"error": "WeChat Official Account is not configured."}}
            if not self.verify_wechat_signature(config["token"], query):
                self.write_debug_log(runtime, "wechat_inbound_failed", {"reason": "invalid_signature"})
                return {
                    "status": 403,
                    "rawBody": "invalid signature",
                    "contentType": "text/plain; charset=utf-8",
                }
            payload = body or {}
            raw_text = str(payload.get("_raw", "")).strip()
            if not raw_text:
                self.write_debug_log(runtime, "wechat_inbound_failed", {"reason": "missing_xml_body"})
                return {"status": 400, "body": {"error": "WeChat webhook requires XML body."}}
            try:
                xml_payload = self.parse_wechat_xml(raw_text)
            except ET.ParseError:
                self.write_debug_log(runtime, "wechat_inbound_failed", {"reason": "invalid_xml", "rawPreview": raw_text[:240]})
                return {"status": 400, "body": {"error": "Invalid WeChat XML payload."}}

            message_type, content = self.normalize_wechat_message(xml_payload)
            event = str(xml_payload.get("Event", "")).strip().lower()
            locale = str(runtime.get_setting("language", "zh-CN")).strip() or "zh-CN"
            sender = {
                "id": str(xml_payload.get("FromUserName", "")).strip(),
                "displayName": str(xml_payload.get("FromUserName", "")).strip(),
                "remark": "",
            }
            bridge_config = self.get_bridge_config(runtime)
            self.write_debug_log(
                runtime,
                "wechat_inbound_received",
                {
                    "senderId": sender["id"],
                    "messageType": message_type,
                    "event": event,
                    "contentPreview": content[:240],
                },
            )
            if not sender["id"] or not content:
                return {
                    "status": 200,
                    "rawBody": "success",
                    "contentType": "text/plain; charset=utf-8",
                }
            self.upsert_channel_user(wechat.setdefault("users", []), sender)
            if bridge_config["configured"] and bridge_config.get("targetUrl"):
                bridge_result = self.forward_bridge_request(
                    runtime,
                    channel="wechat-official",
                    sender=sender,
                    content=content,
                    locale=locale,
                    subject="",
                    attachments=[],
                    message_type=message_type,
                    metadata={"event": event},
                )
                if bridge_result.get("ok"):
                    bridge_body = bridge_result.get("body", {}) if isinstance(bridge_result.get("body"), dict) else {}
                    resolution = bridge_body.get("resolution", {}) if isinstance(bridge_body.get("resolution"), dict) else {}
                    if not resolution:
                        resolution = {"reply": str(bridge_body.get("reply", "")).strip()}
                    resolution["resolutionStrategy"] = str(resolution.get("resolutionStrategy", "")).strip() or "wechat_bridge_forward"
                else:
                    error_text = str(bridge_result.get("error", "")).strip() or "bridge_unavailable"
                    resolution = {
                        "reply": "本地 HomeHub 当前不可达，请稍后再试。",
                        "route": {
                            "kind": "bridge",
                            "selected": {"featureId": "external-channels", "action": "wechat_bridge_unavailable", "score": 1.0},
                        },
                        "resolutionStrategy": "wechat_bridge_failed",
                        "bridgeError": error_text,
                    }
            else:
                if bridge_config.get("sharedToken"):
                    queue_item = self.create_bridge_queue_item(
                        "wechat-official",
                        sender,
                        content,
                        locale,
                        message_type=message_type,
                        metadata={"event": event},
                    )
                    wechat.setdefault("pending", []).insert(0, queue_item)
                    del wechat["pending"][100:]
                    self.save_store(store, runtime)
                    self.write_debug_log(
                        runtime,
                        "wechat_bridge_queued",
                        {
                            "messageId": queue_item["id"],
                            "senderId": sender["id"],
                            "messageType": message_type,
                            "contentPreview": content[:240],
                        },
                    )
                    return {
                        "status": 200,
                        "rawBody": self.build_wechat_passive_reply(xml_payload, "消息已收到，正在交给本地 HomeHub 处理。"),
                        "contentType": "application/xml; charset=utf-8",
                    }
                resolution = self.resolve_inbound(runtime, "wechat-official", sender, content, locale)
            item = self.record_inbound_message(wechat, sender, content, locale, message_type=message_type, homehub_result=resolution)
            reply_text = str(resolution.get("reply", "")).strip() or "HomeHub 已收到你的消息。"
            if message_type == "event" and event == "unsubscribe":
                self.append_action(runtime, f"WeChat follower {sender['id']} unsubscribed.")
                return {
                    "status": 200,
                    "rawBody": "success",
                    "contentType": "text/plain; charset=utf-8",
                }
            self.append_action(runtime, f"Processed inbound WeChat Official Account message from {sender.get('displayName') or sender['id']}.")
            self.write_debug_log(
                runtime,
                "wechat_inbound_replied",
                {
                    "senderId": sender["id"],
                    "messageType": message_type,
                    "replyPreview": reply_text[:240],
                },
            )
            self.write_processing_log(
                runtime,
                "wechat-official",
                {
                    "eventType": "inbound_processed",
                    "sender": sender,
                    "messageType": message_type,
                    "event": event,
                    "content": content[:4000],
                    "route": resolution.get("route", {}),
                    "effectiveLocale": resolution.get("effectiveLocale", locale),
                    "resolutionStrategy": resolution.get("resolutionStrategy", ""),
                    "reply": reply_text,
                    "artifacts": resolution.get("artifacts", []) if isinstance(resolution.get("artifacts"), list) else [],
                },
            )
            return {
                "status": 200,
                "rawBody": self.build_wechat_passive_reply(xml_payload, reply_text),
                "contentType": "application/xml; charset=utf-8",
            }

        if method == "POST" and path == API_WECHAT_SEND:
            payload = body or {}
            target = {"id": str(payload.get("userId", "")).strip(), "displayName": str(payload.get("displayName", "")).strip()}
            content = str(payload.get("content", "")).strip()
            if not target["id"] or not content:
                return {"status": 400, "body": {"error": "userId and content are required"}}
            item = self.queue_outbound(wechat, target, content, "wechat-official")
            send_ok, send_error = self.send_wechat_official_text(runtime, target["id"], content)
            item["status"] = "sent" if send_ok else "failed"
            if send_error:
                item["error"] = send_error
            self.save_store(store, runtime)
            self.append_action(runtime, f"Sent outbound WeChat message for {target.get('displayName') or target['id']}." if send_ok else f"Failed outbound WeChat message for {target.get('displayName') or target['id']}.")
            return {"status": 200 if send_ok else 502, "body": {"ok": send_ok, "item": item, "error": send_error}}

        if method == "POST" and path == API_LINE_WEBHOOK:
            config = self.get_line_config(runtime)
            payload = body or {}
            raw_text = str(payload.get("_raw", "")).strip()
            headers = payload.get("_headers", {}) if isinstance(payload.get("_headers"), dict) else {}
            signature = str(headers.get("x-line-signature", "")).strip()
            if not config["configured"]:
                self.write_debug_log(runtime, "line_inbound_failed", {"reason": "line_not_configured"})
                return {"status": 503, "body": {"error": "LINE is not configured."}}
            if not raw_text:
                self.write_debug_log(runtime, "line_inbound_failed", {"reason": "missing_json_body"})
                return {"status": 400, "body": {"error": "LINE webhook requires JSON body."}}
            if not self.verify_line_signature(config["channelSecret"], signature, raw_text):
                self.write_debug_log(runtime, "line_inbound_failed", {"reason": "invalid_signature"})
                return {"status": 403, "body": {"error": "invalid signature"}}
            try:
                line_payload = self.parse_line_payload(raw_text)
            except (json.JSONDecodeError, ValueError):
                self.write_debug_log(runtime, "line_inbound_failed", {"reason": "invalid_json", "rawPreview": raw_text[:240]})
                return {"status": 400, "body": {"error": "Invalid LINE JSON payload."}}
            events = line_payload.get("events", []) if isinstance(line_payload.get("events"), list) else []
            bridge_config = self.get_bridge_config(runtime)
            processed = 0
            for event in events:
                if not isinstance(event, dict):
                    continue
                sender, message_type, content, reply_token, metadata = self.normalize_line_event(event)
                event_type = str(metadata.get("eventType", "")).strip()
                locale = str(runtime.get_setting("language", "zh-CN")).strip() or "zh-CN"
                self.write_debug_log(
                    runtime,
                    "line_inbound_received",
                    {
                        "senderId": sender["id"],
                        "messageType": message_type,
                        "eventType": event_type,
                        "contentPreview": content[:240],
                    },
                )
                if not sender["id"] or not content:
                    continue
                self.upsert_channel_user(line.setdefault("users", []), sender)
                if bridge_config["configured"] and bridge_config.get("targetUrl"):
                    bridge_result = self.forward_bridge_request(
                        runtime,
                        channel="line",
                        sender=sender,
                        content=content,
                        locale=locale,
                        subject="",
                        attachments=[],
                        message_type=message_type,
                        metadata=metadata,
                    )
                    if bridge_result.get("ok"):
                        bridge_body = bridge_result.get("body", {}) if isinstance(bridge_result.get("body"), dict) else {}
                        resolution = bridge_body.get("resolution", {}) if isinstance(bridge_body.get("resolution"), dict) else {}
                        if not resolution:
                            resolution = {"reply": str(bridge_body.get("reply", "")).strip()}
                        resolution["resolutionStrategy"] = str(resolution.get("resolutionStrategy", "")).strip() or "line_bridge_forward"
                    else:
                        error_text = str(bridge_result.get("error", "")).strip() or "bridge_unavailable"
                        resolution = {
                            "reply": "本地 HomeHub 当前不可达，请稍后再试。",
                            "route": {
                                "kind": "bridge",
                                "selected": {"featureId": "external-channels", "action": "line_bridge_unavailable", "score": 1.0},
                            },
                            "resolutionStrategy": "line_bridge_failed",
                            "bridgeError": error_text,
                        }
                    reply_text = str(resolution.get("reply", "")).strip() or "HomeHub 已收到你的消息。"
                    if reply_token:
                        self.send_line_reply_text(runtime, reply_token, reply_text)
                else:
                    if bridge_config.get("sharedToken"):
                        queue_item = self.create_bridge_queue_item(
                            "line",
                            sender,
                            content,
                            locale,
                            message_type=message_type,
                            metadata=metadata,
                        )
                        line.setdefault("pending", []).insert(0, queue_item)
                        del line["pending"][100:]
                        self.save_store(store, runtime)
                        self.write_debug_log(
                            runtime,
                            "line_bridge_queued",
                            {
                                "messageId": queue_item["id"],
                                "senderId": sender["id"],
                                "messageType": message_type,
                                "contentPreview": content[:240],
                            },
                        )
                        if reply_token:
                            self.send_line_reply_text(runtime, reply_token, "消息已收到，正在交给本地 HomeHub 处理。")
                        processed += 1
                        continue
                    resolution = self.resolve_inbound(runtime, "line", sender, content, locale)
                    reply_text = str(resolution.get("reply", "")).strip() or "HomeHub 已收到你的消息。"
                    if reply_token:
                        self.send_line_reply_text(runtime, reply_token, reply_text)
                item = self.record_inbound_message(line, sender, content, locale, message_type=message_type, homehub_result=resolution)
                self.append_action(runtime, f"Processed inbound LINE message from {sender.get('displayName') or sender['id']}.")
                self.write_debug_log(
                    runtime,
                    "line_inbound_replied",
                    {
                        "senderId": sender["id"],
                        "messageType": message_type,
                        "replyPreview": reply_text[:240],
                    },
                )
                self.write_processing_log(
                    runtime,
                    "line",
                    {
                        "eventType": "inbound_processed",
                        "sender": sender,
                        "messageType": message_type,
                        "event": event_type,
                        "content": content[:4000],
                        "route": resolution.get("route", {}),
                        "effectiveLocale": resolution.get("effectiveLocale", locale),
                        "resolutionStrategy": resolution.get("resolutionStrategy", ""),
                        "reply": reply_text,
                        "artifacts": resolution.get("artifacts", []) if isinstance(resolution.get("artifacts"), list) else [],
                    },
                )
                processed += 1
            self.save_store(store, runtime)
            return {"status": 200, "body": {"ok": True, "processed": processed}}

        if method == "POST" and path == API_LINE_SEND:
            payload = body or {}
            target = {"id": str(payload.get("userId", "")).strip(), "displayName": str(payload.get("displayName", "")).strip()}
            content = str(payload.get("content", "")).strip()
            if not target["id"] or not content:
                return {"status": 400, "body": {"error": "userId and content are required"}}
            item = self.queue_outbound(line, target, content, "line")
            send_ok, send_error = self.send_line_push_text(runtime, target["id"], content)
            item["status"] = "sent" if send_ok else "failed"
            if send_error:
                item["error"] = send_error
            self.save_store(store, runtime)
            self.append_action(runtime, f"Sent outbound LINE message for {target.get('displayName') or target['id']}." if send_ok else f"Failed outbound LINE message for {target.get('displayName') or target['id']}.")
            return {"status": 200 if send_ok else 502, "body": {"ok": send_ok, "item": item, "error": send_error}}

        if method == "POST" and path == API_EMAIL_INTAKE:
            payload = body or {}
            locale = str(payload.get("locale", runtime.get_setting("language", "zh-CN"))).strip() or "zh-CN"
            sender = {
                "id": str(payload.get("from", "")).strip() or str(payload.get("sender", "")).strip(),
                "address": str(payload.get("from", "")).strip() or str(payload.get("sender", "")).strip(),
                "displayName": str(payload.get("displayName", "")).strip(),
            }
            subject = str(payload.get("subject", "")).strip()
            content = str(payload.get("content", "")).strip() or str(payload.get("body", "")).strip()
            attachments = payload.get("attachments", []) if isinstance(payload.get("attachments", []), list) else []
            if not sender["id"] or (not content and not attachments):
                return {"status": 400, "body": {"error": "from and content or attachments are required"}}
            resolution = self.resolve_inbound(runtime, "email", sender, content, locale, subject, attachments)
            resolution = self.resolve_email_with_attachments(runtime, sender, content, locale, subject, attachments, resolution)
            item = self.record_inbound_message(mail, sender, content, locale, message_type="email", subject=subject, homehub_result=resolution)
            if attachments:
                item["attachments"] = self.email_attachment_record_view(self.classify_email_attachments(attachments))
            reply_text = str(resolution.get("reply", "")).strip()
            reply_artifacts = resolution.get("artifacts", []) if isinstance(resolution.get("artifacts"), list) else []
            if reply_text and self.should_auto_reply_email(content, attachments):
                reply_ok, reply_error = self.send_inbound_email_reply(runtime, sender, subject, reply_text, reply_artifacts)
                item["autoReply"] = {
                    "ok": reply_ok,
                    "error": reply_error,
                    "subject": self.build_reply_subject(subject),
                    "attachments": [str(artifact.get("fileName", "")).strip() for artifact in reply_artifacts if isinstance(artifact, dict)],
                }
                self.save_store(store, runtime)
            elif reply_text:
                item["autoReply"] = {
                    "ok": False,
                    "error": "Skipped because the email did not mention 小栖 or homehub.",
                    "subject": self.build_reply_subject(subject),
                    "attachments": [str(artifact.get("fileName", "")).strip() for artifact in reply_artifacts if isinstance(artifact, dict)],
                }
                self.write_debug_log(
                    runtime,
                    "email_auto_reply_skipped",
                    {
                        "reason": "missing_reply_keyword",
                        "target": sender["address"],
                        "subject": subject,
                        "contentPreview": content[:240],
                        "attachmentNames": [str(item.get("name", "")).strip() for item in attachments],
                    },
                )
                self.save_store(store, runtime)
            self.write_processing_log(
                runtime,
                "email",
                {
                    "eventType": "manual_intake_processed",
                    "sender": sender,
                    "subject": subject,
                    "content": content[:4000],
                    "attachments": item.get("attachments", []),
                    "route": resolution.get("route", {}),
                    "effectiveLocale": resolution.get("effectiveLocale", locale),
                    "resolutionStrategy": resolution.get("resolutionStrategy", ""),
                    "attachmentRouting": resolution.get("attachmentRouting", []),
                    "executedTasks": resolution.get("executedTasks", []),
                    "reply": reply_text,
                    "artifacts": reply_artifacts,
                    "autoReply": item.get("autoReply", {}),
                },
            )
            self.append_action(runtime, f"Processed inbound email from {sender['address']}.")
            return {"status": 200, "body": {"ok": True, "item": item, "reply": resolution.get("reply", ""), "route": resolution.get("route", {})}}

        if method == "POST" and path == API_EMAIL_SEND:
            payload = body or {}
            target = {"address": str(payload.get("to", "")).strip(), "displayName": str(payload.get("displayName", "")).strip()}
            subject = str(payload.get("subject", "")).strip()
            content = str(payload.get("content", "")).strip() or str(payload.get("body", "")).strip()
            outbound_artifacts = payload.get("artifacts", []) if isinstance(payload.get("artifacts", []), list) else []
            if not target["address"] or not content:
                return {"status": 400, "body": {"error": "to and content are required"}}
            item = self.queue_outbound(mail, target, content, "email", subject=subject)
            if outbound_artifacts:
                item["attachments"] = [str(artifact.get("fileName", "")).strip() for artifact in outbound_artifacts if isinstance(artifact, dict)]
            ok, error = self.send_email_via_smtp(runtime, target["address"], subject, content, outbound_artifacts)
            item["status"] = "sent" if ok else "failed"
            if error:
                item["error"] = error
            self.save_store(store, runtime)
            self.append_action(runtime, f"{'Sent' if ok else 'Failed to send'} outbound email for {target['address']}.")
            return {"status": 200 if ok else 502, "body": {"ok": ok, "item": item, "error": error}}

        if method == "POST" and path == API_EMAIL_SYNC:
            payload = body or {}
            limit = int(payload.get("limit", 10) or 10)
            result = self.sync_mailbox(runtime, limit=max(1, min(limit, 50)))
            status = 200 if result.get("ok") else 502
            return {"status": status, "body": result}

        return None


def load_feature() -> HomeHubFeature:
    return Feature()
