from __future__ import annotations

import json
import os
import re
import shutil
from datetime import datetime
from pathlib import Path

from .base import HomeHubFeature, RuntimeBridge


API_ROOT = "/api/local-files"
API_LIST = "/api/local-files/list"
API_SEARCH = "/api/local-files/search"
API_READ = "/api/local-files/read"
API_WRITE = "/api/local-files/write"
API_MOVE = "/api/local-files/move"
API_DELETE = "/api/local-files/delete"
API_CONFIRM = "/api/local-files/confirm-delete"
API_CLASSIFY = "/api/local-files/classify"


class Feature(HomeHubFeature):
    feature_id = "local-files"
    feature_name = "Local Files"
    version = "1.1.0"

    SEND_TOKENS = ("发给我", "发送", "附件", "下载", "share", "send me", "attachment", "download")
    LIST_TOKENS = ("查看", "列出", "显示", "看看", "下面有什么", "有哪些", "list", "show", "what files", "what is under")
    SEARCH_TOKENS = ("搜索", "查找", "寻找", "find", "search", "lookup")
    READ_TOKENS = ("读取", "打开", "阅读", "read", "open")
    CLASSIFY_TOKENS = ("分类", "整理", "归类", "按类型", "创建新的文件夹", "sort", "organize", "classify")
    FILE_HINT_TOKENS = ("文件", "文件夹", "目录", "路径", "附件", "file", "folder", "directory", "path", "attachment")
    TEXT_EXTENSIONS = {".txt", ".md", ".csv", ".json", ".log", ".ini"}
    CATEGORY_MAP = {
        "Documents": {".pdf", ".doc", ".docx", ".ppt", ".pptx"},
        "Finance": {".xls", ".xlsx", ".csv"},
        "Text": {".txt", ".md", ".json", ".ini", ".log"},
        "Media": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".mp4", ".mov", ".mp3", ".wav"},
        "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    }

    def descriptor(self) -> dict:
        data = super().descriptor()
        data["summary"] = "Browse, search, read, write, move, classify, share, and delete local files with guarded actions."
        data["api"] = [API_ROOT, API_LIST, API_SEARCH, API_READ, API_WRITE, API_MOVE, API_DELETE, API_CONFIRM, API_CLASSIFY]
        data["voiceIntents"] = [{"id": "local-files", "name": "Local Files", "summary": "Handle local file-system tasks."}]
        return data

    def storage_path(self, runtime: RuntimeBridge) -> Path:
        data_dir = runtime.root / "data"
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir / "local_files.json"

    def generated_root(self, runtime: RuntimeBridge) -> Path:
        path = runtime.root / "generated" / "local-files"
        path.mkdir(parents=True, exist_ok=True)
        return path

    def default_store(self) -> dict:
        return {"pendingDelete": None, "recentActions": [], "lastRun": ""}

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
        return {
            "pendingDelete": data.get("pendingDelete") if isinstance(data.get("pendingDelete"), dict) else None,
            "recentActions": data.get("recentActions", []) if isinstance(data.get("recentActions"), list) else [],
            "lastRun": str(data.get("lastRun", "")).strip(),
        }

    def save_store(self, store: dict, runtime: RuntimeBridge) -> None:
        self.storage_path(runtime).write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")

    def on_refresh(self, runtime: RuntimeBridge) -> None:
        runtime.state[self.feature_id] = self.load_store(runtime)

    def reset(self, runtime: RuntimeBridge) -> None:
        runtime.state[self.feature_id] = self.default_store()
        self.save_store(runtime.state[self.feature_id], runtime)

    def get_store(self, runtime: RuntimeBridge) -> dict:
        store = runtime.state.get(self.feature_id)
        if not isinstance(store, dict):
            store = self.load_store(runtime)
            runtime.state[self.feature_id] = store
        return store

    def now_iso(self) -> str:
        return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")

    def remember_action(self, runtime: RuntimeBridge, summary: str) -> None:
        store = self.get_store(runtime)
        stamp = self.now_iso()
        store["recentActions"] = [{"id": f"local-files-{stamp}", "summary": summary, "createdAt": stamp}] + list(store.get("recentActions", []))[:11]
        store["lastRun"] = stamp
        self.save_store(store, runtime)

    def protected_prefixes(self) -> list[Path]:
        home = Path.home()
        return [Path("/System"), Path("/Library/Keychains"), Path("/private/etc"), Path("/private/var/db"), home / ".ssh", home / ".gnupg", home / ".aws"]

    def machine_access_mode(self, runtime: RuntimeBridge | None = None) -> str:
        if runtime is not None:
            return str(runtime.get_setting("machineAccessMode", "full-access") or "full-access").strip().lower()
        return "full-access"

    def full_access_enabled(self, runtime: RuntimeBridge | None = None) -> bool:
        return self.machine_access_mode(runtime) == "full-access"

    def resolve_path(self, raw_path: str) -> Path:
        text = str(raw_path or "").strip()
        return Path.home() if not text else Path(text).expanduser().resolve()

    def is_protected(self, path: Path, runtime: RuntimeBridge | None = None) -> bool:
        if self.full_access_enabled(runtime):
            return False
        resolved = path.resolve()
        for prefix in self.protected_prefixes():
            try:
                resolved.relative_to(prefix.resolve())
                return True
            except ValueError:
                continue
        return False

    def validate_path(self, path: Path, *, allow_missing: bool = False, runtime: RuntimeBridge | None = None) -> tuple[bool, str]:
        try:
            resolved = path.resolve() if path.exists() or not allow_missing else path
        except OSError as exc:
            return False, str(exc)
        if self.is_protected(resolved, runtime):
            return False, "protected_path"
        if not allow_missing and not resolved.exists():
            return False, "path_not_found"
        return True, ""

    def zh(self, locale: str, zh_text: str, en_text: str) -> str:
        return zh_text if locale == "zh-CN" else en_text

    def extract_path_hint(self, message: str) -> str:
        text = str(message or "").strip()
        for pattern in [r"([A-Za-z]:\\[^\n，。,]+)", r"(~\/[^\n，。,]+)", r"(\/Users\/[^\n，。,]+)", r"(\/Volumes\/[^\n，。,]+)", r"(\/tmp\/[^\n，。,]+)"]:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if match:
                return self.normalize_extracted_path(match.group(1))
        return ""

    def normalize_extracted_path(self, raw_path: str) -> str:
        text = str(raw_path or "").strip().strip("，。,")
        for marker in [" 下", " 下面", " 里面", " 里", " 之下", " 分类", " 整理", " 发给我", " 发送", " 搜索", " 查找", " download ", " send me ", " search "]:
            if marker in text:
                text = text.split(marker, 1)[0].strip()
        return text.rstrip("\\/")

    def extract_search_query_hint(self, message: str) -> str:
        text = str(message or "").strip()
        patterns = [
            r"(?:搜索|查找|寻找)\s+.+?\s+下面的\s+(.+?)\s*(?:文件|文件夹|file|files)$",
            r"(?:搜索|查找|寻找)\s+(.+?)\s*(?:文件|文件夹|file|files)$",
            r"(?:search|find|lookup)\s+.+?\s+for\s+(.+?)\s*(?:file|files)$",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if match:
                return str(match.group(1) or "").strip(" ，。")
        return ""

    def extract_filename_hint(self, message: str) -> str:
        explicit = re.findall(r"([A-Za-z0-9_\- .]+\.(?:pptx|ppt|xlsx|xls|docx|doc|pdf|txt|csv|md|jpg|jpeg|png|zip|mp4|mov|mp3|wav|json|ini|log))", str(message or ""), flags=re.IGNORECASE)
        return explicit[0].strip() if explicit else ""

    def looks_like_file_request(self, message: str) -> bool:
        text = str(message or "")
        lowered = text.lower()
        has_action = any(token in text for token in self.SEND_TOKENS + self.LIST_TOKENS + self.SEARCH_TOKENS + self.READ_TOKENS + self.CLASSIFY_TOKENS)
        has_action = has_action or any(token in lowered for token in self.SEND_TOKENS + self.LIST_TOKENS + self.SEARCH_TOKENS + self.READ_TOKENS + self.CLASSIFY_TOKENS)
        has_target = any(token in text for token in self.FILE_HINT_TOKENS) or any(token in lowered for token in self.FILE_HINT_TOKENS)
        return bool(self.extract_path_hint(text) or self.extract_filename_hint(text) or (has_action and has_target))

    def classify_file_request(self, message: str, locale: str, runtime: RuntimeBridge) -> dict:
        payload = runtime.openai_json(
            "Return JSON only with keys action,path,destinationPath,query,content,fileName,lineLimit,confidence for a local file command. action must be one of none,list,search,read,write,move,delete,send,classify,confirm_delete,cancel_delete.",
            f"locale: {locale}\nrequest:\n{message}",
            "gpt-4o-mini",
        ) or {}
        result = {
            "action": str(payload.get("action", "")).strip().lower() or "none",
            "path": str(payload.get("path", "")).strip(),
            "destinationPath": str(payload.get("destinationPath", "")).strip(),
            "query": str(payload.get("query", "")).strip(),
            "content": str(payload.get("content", "")).strip(),
            "fileName": str(payload.get("fileName", "")).strip(),
            "lineLimit": int(payload.get("lineLimit", 80) or 80),
            "confidence": float(payload.get("confidence", 0.0) or 0.0),
        }
        return self.apply_rule_fallbacks(message, result)

    def apply_rule_fallbacks(self, message: str, classified: dict) -> dict:
        result = dict(classified or {})
        text = str(message or "").strip()
        lowered = text.lower()
        result["path"] = result.get("path") or self.extract_path_hint(text)
        result["fileName"] = result.get("fileName") or self.extract_filename_hint(text)
        result["query"] = result.get("query") or result["fileName"]
        action = str(result.get("action", "")).strip().lower() or "none"
        if action == "none":
            if any(token in text for token in self.CLASSIFY_TOKENS) or any(token in lowered for token in self.CLASSIFY_TOKENS):
                action = "classify"
            elif any(token in text for token in self.SEND_TOKENS) or any(token in lowered for token in self.SEND_TOKENS):
                action = "send"
            elif any(token in text for token in self.LIST_TOKENS) or any(token in lowered for token in self.LIST_TOKENS):
                action = "list"
            elif any(token in text for token in self.SEARCH_TOKENS) or any(token in lowered for token in self.SEARCH_TOKENS):
                action = "search"
            elif any(token in text for token in self.READ_TOKENS) or any(token in lowered for token in self.READ_TOKENS):
                action = "read"
            elif result["fileName"]:
                action = "search"
        result["action"] = action
        if action == "search" and not str(result.get("query", "")).strip():
            result["query"] = self.extract_search_query_hint(text)
        query = str(result.get("query", "")).strip()
        query = re.sub(r"\s*(文件|文件夹|目录|路径|file|files|folder|directory)\s*$", "", query, flags=re.IGNORECASE).strip()
        result["query"] = query or result.get("fileName", "")
        result["confidence"] = max(float(result.get("confidence", 0.0) or 0.0), 0.8 if action != "none" else 0.0)
        if not result["path"] and action in {"list", "search", "send", "classify"}:
            result["path"] = str(Path.home())
        return result

    def match_voice_intent(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        if not self.looks_like_file_request(message):
            return None
        classified = self.classify_file_request(message, locale, runtime)
        if classified.get("action") == "none":
            return None
        return {"intent": "local-files", "action": classified.get("action", "none"), "score": min(0.98, max(0.74, float(classified.get("confidence", 0.0) or 0.0)))}

    def list_directory(self, path: Path, limit: int = 40) -> dict:
        items = []
        for child in sorted(path.iterdir(), key=lambda item: (not item.is_dir(), item.name.lower()))[:limit]:
            try:
                item_type = "dir" if child.is_dir() else "file"
                size = child.stat().st_size if child.is_file() else 0
            except OSError:
                item_type = "unknown"
                size = 0
            items.append({"name": child.name, "path": str(child), "type": item_type, "sizeBytes": size})
        return {"path": str(path), "items": items}

    def search_files(self, base: Path, query: str, runtime: RuntimeBridge | None = None, limit: int = 30) -> dict:
        matches = []
        needle = str(query or "").strip().lower()
        if not needle:
            return {"base": str(base), "query": "", "items": []}
        for root, dirs, files in os.walk(base):
            dirs[:] = [name for name in dirs if not name.startswith(".")]
            for name in files:
                if needle not in name.lower():
                    continue
                candidate = Path(root) / name
                if self.is_protected(candidate, runtime):
                    continue
                matches.append({"name": name, "path": str(candidate), "type": "file"})
                if len(matches) >= limit:
                    return {"base": str(base), "query": query, "items": matches}
        return {"base": str(base), "query": query, "items": matches}

    def choose_file_match(self, base: Path, file_name: str, runtime: RuntimeBridge | None = None, limit: int = 20) -> Path | None:
        needle = str(file_name or "").strip().lower()
        if not needle:
            return None
        exact: list[Path] = []
        partial: list[Path] = []
        for root, dirs, files in os.walk(base):
            dirs[:] = [name for name in dirs if not name.startswith(".")]
            for name in files:
                candidate = Path(root) / name
                if self.is_protected(candidate, runtime):
                    continue
                lowered = name.lower()
                if lowered == needle:
                    exact.append(candidate)
                elif needle in lowered:
                    partial.append(candidate)
                if len(exact) + len(partial) >= limit:
                    break
            if len(exact) + len(partial) >= limit:
                break
        if exact:
            return exact[0]
        if partial:
            partial.sort(key=lambda item: (len(item.name), item.name.lower()))
            return partial[0]
        return None

    def create_download_artifact(self, source: Path, runtime: RuntimeBridge) -> dict:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        safe_name = re.sub(r"[^A-Za-z0-9._-]+", "-", source.name).strip("-") or "download"
        target = self.generated_root(runtime) / f"{stamp}-{safe_name}"
        shutil.copy2(source, target)
        return {"kind": "file", "label": "Local File", "fileName": source.name, "path": str(target.relative_to(runtime.root)), "url": f"/generated/local-files/{target.name}", "sourcePath": str(source)}

    def read_text_file(self, path: Path, line_limit: int = 80) -> dict:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        return {"path": str(path), "lineCount": len(lines), "content": "\n".join(lines[: max(1, min(line_limit, 200))]).strip()}

    def write_text_file(self, path: Path, content: str) -> dict:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(str(content or ""), encoding="utf-8")
        return {"path": str(path), "sizeBytes": path.stat().st_size}

    def move_path(self, source: Path, target: Path) -> dict:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(source), str(target))
        return {"source": str(source), "target": str(target)}

    def request_delete_confirmation(self, path: Path, runtime: RuntimeBridge) -> dict:
        store = self.get_store(runtime)
        store["pendingDelete"] = {"path": str(path), "createdAt": self.now_iso()}
        self.save_store(store, runtime)
        return store["pendingDelete"]

    def confirm_delete(self, runtime: RuntimeBridge) -> dict | None:
        store = self.get_store(runtime)
        pending = store.get("pendingDelete")
        if not isinstance(pending, dict):
            return None
        path = self.resolve_path(str(pending.get("path", "")).strip())
        ok, error = self.validate_path(path)
        if not ok:
            store["pendingDelete"] = None
            self.save_store(store, runtime)
            return {"ok": False, "error": error, "path": str(path)}
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                return {"ok": False, "error": "directory_not_empty", "path": str(path)}
        else:
            path.unlink()
        store["pendingDelete"] = None
        self.save_store(store, runtime)
        return {"ok": True, "path": str(path)}

    def cancel_delete(self, runtime: RuntimeBridge) -> None:
        store = self.get_store(runtime)
        store["pendingDelete"] = None
        self.save_store(store, runtime)

    def category_for_path(self, path: Path) -> str:
        suffix = path.suffix.lower()
        for category, extensions in self.CATEGORY_MAP.items():
            if suffix in extensions:
                return category
        return "Documents"

    def classify_directory(self, base: Path) -> dict:
        moved = []
        created_dirs = set()
        for child in sorted(base.iterdir(), key=lambda item: item.name.lower()):
            if child.is_dir():
                continue
            category = self.category_for_path(child)
            target_dir = base / category
            try:
                target_dir.mkdir(parents=True, exist_ok=True)
            except OSError as exc:
                return {
                    "path": str(base),
                    "createdDirs": sorted(created_dirs),
                    "moved": moved,
                    "error": f"mkdir_failed:{exc}",
                }
            created_dirs.add(category)
            target = target_dir / child.name
            if target.exists():
                stem = child.stem
                suffix = child.suffix
                index = 1
                while target.exists():
                    target = target_dir / f"{stem}-{index}{suffix}"
                    index += 1
            try:
                shutil.move(str(child), str(target))
            except OSError as exc:
                return {
                    "path": str(base),
                    "createdDirs": sorted(created_dirs),
                    "moved": moved,
                    "error": f"move_failed:{exc}",
                }
            moved.append({"source": str(child), "target": str(target), "category": category})
        return {"path": str(base), "createdDirs": sorted(created_dirs), "moved": moved}

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        if not self.looks_like_file_request(message):
            return None
        classified = self.classify_file_request(message, locale, runtime)
        action = classified.get("action", "none")
        if action == "none":
            return None
        if action == "confirm_delete":
            result = self.confirm_delete(runtime)
            if not result:
                return {"reply": self.zh(locale, "当前没有待确认的删除操作。", "There is no pending delete operation right now.")}
            if result.get("ok"):
                self.remember_action(runtime, f"Deleted {result['path']}.")
                return {"reply": self.zh(locale, f"已删除：{result['path']}", f"Deleted: {result['path']}")}
            return {"reply": self.zh(locale, f"删除失败：{result.get('error', 'unknown_error')}", f"Delete failed: {result.get('error', 'unknown_error')}")}
        if action == "cancel_delete":
            self.cancel_delete(runtime)
            return {"reply": self.zh(locale, "已取消删除。", "Delete canceled.")}

        path = self.resolve_path(classified.get("path", ""))
        if action in {"list", "read", "move", "delete", "classify"}:
            ok, error = self.validate_path(path, runtime=runtime)
            if not ok:
                return {"reply": self.zh(locale, f"路径不可用：{error}", f"Path is not available: {error}")}
        elif action == "write":
            ok, error = self.validate_path(path, allow_missing=True, runtime=runtime)
            if not ok:
                return {"reply": self.zh(locale, f"目标路径不可用：{error}", f"Target path is not available: {error}")}

        if action == "list":
            if not path.is_dir():
                return {"reply": self.zh(locale, f"{path} 不是目录。", f"{path} is not a directory.")}
            listing = self.list_directory(path)
            names = "、".join(item["name"] for item in listing["items"][:12]) if locale == "zh-CN" else ", ".join(item["name"] for item in listing["items"][:12])
            requested_file = classified.get("fileName", "") or self.extract_filename_hint(message)
            lowered_message = str(message or "").lower()
            send_requested = (bool(requested_file) and any(token in message for token in self.SEND_TOKENS)) or any(token in lowered_message for token in self.SEND_TOKENS)
            if send_requested and requested_file:
                matched = self.choose_file_match(path, requested_file, runtime=runtime)
                if matched:
                    artifact = self.create_download_artifact(matched, runtime)
                    self.remember_action(runtime, f"Listed {path} and prepared download for {matched}.")
                    return {
                        "reply": self.zh(locale, f"{path} 下有这些文件：{names or '空目录'}。我也已经把 {matched.name} 准备成附件了。", f"{path} contains: {names or 'empty directory'}. I also prepared {matched.name} for download."),
                        "artifacts": [artifact],
                    }
            self.remember_action(runtime, f"Listed {path}.")
            return {"reply": self.zh(locale, f"{path} 下有这些文件：{names or '空目录'}", f"{path} contains: {names or 'empty directory'}")}

        if action == "search":
            base = self.resolve_path(classified.get("path", "")) if classified.get("path") else Path.home()
            if base.is_file():
                base = base.parent
            ok, error = self.validate_path(base, runtime=runtime)
            if not ok or not base.is_dir():
                return {"reply": self.zh(locale, f"搜索目录不可用：{error or 'not_a_directory'}", f"Search directory is not available: {error or 'not_a_directory'}")}
            result = self.search_files(base, classified.get("query", ""), runtime=runtime)
            names = "、".join(item["path"] for item in result["items"][:8]) if locale == "zh-CN" else ", ".join(item["path"] for item in result["items"][:8])
            self.remember_action(runtime, f"Searched {base} for {classified.get('query', '')}.")
            return {"reply": self.zh(locale, f"搜索结果：{names or '没有找到匹配文件'}", f"Search results: {names or 'No matching files found'}")}

        if action == "send":
            base = self.resolve_path(classified.get("path", "")) if classified.get("path") else Path.home()
            file_name = classified.get("fileName", "") or self.extract_filename_hint(message) or classified.get("query", "")
            ok, error = self.validate_path(base, runtime=runtime)
            if ok and base.is_file():
                matched = base
            else:
                if not ok or not base.is_dir():
                    return {"reply": self.zh(locale, f"搜索目录不可用：{error or 'not_a_directory'}", f"Search directory is not available: {error or 'not_a_directory'}")}
                if not file_name:
                    return {"reply": self.zh(locale, "请告诉我你想发送哪个文件。", "Tell me which file you want me to send.")}
                matched = self.choose_file_match(base, file_name, runtime=runtime)
            if not file_name:
                return {"reply": self.zh(locale, "请告诉我你想发送哪个文件。", "Tell me which file you want me to send.")}
            if not matched:
                return {"reply": self.zh(locale, f"我没在 {base} 下找到 {file_name}。", f"I could not find {file_name} under {base}.")}
            artifact = self.create_download_artifact(matched, runtime)
            self.remember_action(runtime, f"Prepared download for {matched}.")
            return {"reply": self.zh(locale, f"我找到这个文件了，并已经准备成附件：{matched.name}。你可以直接下载。", f"I found the file and prepared it for download: {matched.name}."), "artifacts": [artifact]}

        if action == "classify":
            if not path.is_dir():
                return {"reply": self.zh(locale, f"{path} 不是目录。", f"{path} is not a directory.")}
            result = self.classify_directory(path)
            if result.get("error"):
                return {
                    "reply": self.zh(
                        locale,
                        f"我识别到这是一个分类请求，但当前进程没有权限在 {path} 下创建分类文件夹。请换到 HomeHub 工作区目录或 /tmp 再试一次。",
                        f"I recognized this as a classify request, but the current process cannot create category folders under {path}. Try again in the HomeHub workspace or under /tmp.",
                    ),
                    "result": result,
                }
            created_dirs = "、".join(result["createdDirs"]) if locale == "zh-CN" else ", ".join(result["createdDirs"])
            self.remember_action(runtime, f"Classified files under {path}.")
            return {"reply": self.zh(locale, f"我已经按类型整理了 {path} 下的文件，并创建了这些文件夹：{created_dirs or '没有新增文件夹'}。", f"I organized the files under {path} by type and created: {created_dirs or 'no new folders'}."), "result": result}

        if action == "read":
            if not path.is_file() or path.suffix.lower() not in self.TEXT_EXTENSIONS:
                return {"reply": self.zh(locale, f"{path} 不是可读取的文本文件。", f"{path} is not a readable text file.")}
            result = self.read_text_file(path, classified.get("lineLimit", 80))
            self.remember_action(runtime, f"Read {path}.")
            return {"reply": self.zh(locale, f"文件内容如下：\n{result['content']}", f"File contents:\n{result['content']}")}

        if action == "write":
            result = self.write_text_file(path, classified.get("content", ""))
            self.remember_action(runtime, f"Wrote {path}.")
            return {"reply": self.zh(locale, f"已写入文件：{result['path']}", f"Wrote file: {result['path']}")}

        if action == "move":
            destination = self.resolve_path(classified.get("destinationPath", ""))
            ok, error = self.validate_path(destination, allow_missing=True)
            if not ok:
                return {"reply": self.zh(locale, f"目标路径不可用：{error}", f"Destination path is not available: {error}")}
            result = self.move_path(path, destination)
            self.remember_action(runtime, f"Moved {path} to {destination}.")
            return {"reply": self.zh(locale, f"已移动到：{result['target']}", f"Moved to: {result['target']}")}

        if action == "delete":
            pending = self.request_delete_confirmation(path, runtime)
            return {"reply": self.zh(locale, f"待确认删除：{pending['path']}。回复“确认删除”继续。", f"Pending delete: {pending['path']}. Reply with 'confirm delete' to continue.")}
        return None

    def handle_api(self, method: str, path: str, query: dict, body: dict | None, runtime: RuntimeBridge) -> dict | None:
        payload = body or {}
        if method == "GET" and path == API_ROOT:
            store = self.get_store(runtime)
            return {"status": 200, "body": {"ok": True, "pendingDelete": store.get("pendingDelete"), "recentActions": store.get("recentActions", [])[:12]}}
        if method == "POST" and path == API_LIST:
            target = self.resolve_path(str(payload.get("path", "")).strip())
            ok, error = self.validate_path(target, runtime=runtime)
            if not ok or not target.is_dir():
                return {"status": 400, "body": {"ok": False, "error": error or "not_a_directory"}}
            return {"status": 200, "body": {"ok": True, "result": self.list_directory(target)}}
        if method == "POST" and path == API_SEARCH:
            base = self.resolve_path(str(payload.get("path", "")).strip() or str(Path.home()))
            ok, error = self.validate_path(base, runtime=runtime)
            if not ok or not base.is_dir():
                return {"status": 400, "body": {"ok": False, "error": error or "not_a_directory"}}
            return {"status": 200, "body": {"ok": True, "result": self.search_files(base, str(payload.get("query", "")).strip(), runtime=runtime)}}
        if method == "POST" and path == API_READ:
            target = self.resolve_path(str(payload.get("path", "")).strip())
            ok, error = self.validate_path(target, runtime=runtime)
            if not ok or not target.is_file():
                return {"status": 400, "body": {"ok": False, "error": error or "not_a_file"}}
            return {"status": 200, "body": {"ok": True, "result": self.read_text_file(target, int(payload.get("lineLimit", 80) or 80))}}
        if method == "POST" and path == API_WRITE:
            target = self.resolve_path(str(payload.get("path", "")).strip())
            ok, error = self.validate_path(target, allow_missing=True, runtime=runtime)
            if not ok:
                return {"status": 400, "body": {"ok": False, "error": error}}
            return {"status": 200, "body": {"ok": True, "result": self.write_text_file(target, str(payload.get("content", "")))}} 
        if method == "POST" and path == API_MOVE:
            source = self.resolve_path(str(payload.get("path", "")).strip())
            destination = self.resolve_path(str(payload.get("destinationPath", "")).strip())
            ok_source, error_source = self.validate_path(source, runtime=runtime)
            ok_dest, error_dest = self.validate_path(destination, allow_missing=True, runtime=runtime)
            if not ok_source or not ok_dest:
                return {"status": 400, "body": {"ok": False, "error": error_source or error_dest}}
            return {"status": 200, "body": {"ok": True, "result": self.move_path(source, destination)}}
        if method == "POST" and path == API_DELETE:
            target = self.resolve_path(str(payload.get("path", "")).strip())
            ok, error = self.validate_path(target, runtime=runtime)
            if not ok:
                return {"status": 400, "body": {"ok": False, "error": error}}
            return {"status": 200, "body": {"ok": True, "pendingDelete": self.request_delete_confirmation(target, runtime)}}
        if method == "POST" and path == API_CONFIRM:
            result = self.confirm_delete(runtime)
            if result is None:
                return {"status": 400, "body": {"ok": False, "error": "no_pending_delete"}}
            return {"status": 200 if result.get("ok") else 400, "body": result}
        if method == "POST" and path == API_CLASSIFY:
            target = self.resolve_path(str(payload.get("path", "")).strip())
            ok, error = self.validate_path(target, runtime=runtime)
            if not ok or not target.is_dir():
                return {"status": 400, "body": {"ok": False, "error": error or "not_a_directory"}}
            return {"status": 200, "body": {"ok": True, "result": self.classify_directory(target)}}
        return None


def load_feature() -> HomeHubFeature:
    return Feature()
