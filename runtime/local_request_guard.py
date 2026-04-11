from __future__ import annotations

import re


LOCAL_PATH_PATTERNS = [
    r"(?:^|[\s'\"(])~/",
    r"(?:^|[\s'\"(])/users/",
    r"(?:^|[\s'\"(])/tmp/",
    r"(?:^|[\s'\"(])/volumes/",
    r"(?:^|[\s'\"(])[a-z]:\\",
]

LOCAL_FILE_EXTENSIONS = [
    ".pptx",
    ".ppt",
    ".xlsx",
    ".xls",
    ".docx",
    ".doc",
    ".pdf",
    ".txt",
    ".csv",
    ".md",
    ".zip",
    ".mp4",
    ".json",
    ".png",
    ".jpg",
    ".jpeg",
]

LOCAL_FILE_NOUN_TOKENS = [
    "文件",
    "文件夹",
    "目录",
    "路径",
    "附件",
    "documents",
    "downloads",
    "desktop",
    "directory",
    "folder",
    "file",
    "path",
    "attachment",
]

LOCAL_FILE_ACTION_TOKENS = [
    "读取",
    "打开文件",
    "发给我",
    "发送文件",
    "搜索文件",
    "查找文件",
    "分类",
    "整理文件",
    "查看",
    "列出",
    "下面有什么",
    "read file",
    "open file",
    "send me",
    "search file",
    "classify files",
    "list files",
]

NON_FILE_FINANCE_TOKENS = [
    "消费",
    "账单",
    "支出",
    "总额",
    "excel文档",
    "生成excel",
    "导出账单",
    "提醒",
]


def looks_like_explicit_local_path_request(user_text: str) -> bool:
    text = str(user_text or "")
    lowered = text.lower()
    explicit_path = any(re.search(pattern, lowered) for pattern in LOCAL_PATH_PATTERNS)
    explicit_file = any(token in lowered for token in LOCAL_FILE_EXTENSIONS)
    has_file_noun = any(token in text or token in lowered for token in LOCAL_FILE_NOUN_TOKENS)
    has_file_action = any(token in text or token in lowered for token in LOCAL_FILE_ACTION_TOKENS)
    if not explicit_path and not explicit_file and any(token in text for token in NON_FILE_FINANCE_TOKENS):
        return False
    return explicit_path or explicit_file or (has_file_noun and has_file_action)
