from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import runtime.server as server


DOCS_DIR = ROOT / "docs"
CASES_PATH = DOCS_DIR / "homehub-3-phase-test-cases-2026-04-10.md"
RESULTS_PATH = DOCS_DIR / "homehub-3-phase-test-results-2026-04-10.md"
WINDOWS_DOCUMENTS_DIR = Path(r"C:\Users\hy\OneDrive\ドキュメント")
MAC_DOCUMENTS_DIR = Path("/Users/home/Documents")
TEST_FILENAME = "AI_Agent_Build2026 en.pptx"
SAMPLE_DOCS_DIR = Path(r"E:\sample documents")
CLASSIFICATION_DIR_NAMES = ["Archives", "Documents", "Finance", "Media", "Text"]


@dataclass
class CaseSpec:
    stage: str
    name: str
    query: str
    expected: str
    check: str


@dataclass
class CaseResult:
    stage: str
    name: str
    query: str
    expected: str
    status: str
    actual: str
    notes: str = ""


def now_iso() -> str:
    return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")


def resolve_documents_dir() -> Path:
    override = os.environ.get("HOMEHUB_TEST_DOCUMENTS_DIR", "").strip()
    if override:
        return Path(override).expanduser()
    return WINDOWS_DOCUMENTS_DIR if os.name == "nt" else MAC_DOCUMENTS_DIR


TEST_DOCUMENTS_DIR = resolve_documents_dir()
TEST_DOCUMENTS_TEXT = "~/Documents" if TEST_DOCUMENTS_DIR == MAC_DOCUMENTS_DIR else str(TEST_DOCUMENTS_DIR)


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def ensure_documents_fixture() -> None:
    TEST_DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
    target = TEST_DOCUMENTS_DIR / TEST_FILENAME
    if not target.exists():
        target.write_bytes(b"HomeHub test fixture")


def reset_sample_documents_fixture() -> None:
    SAMPLE_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for child in SAMPLE_DOCS_DIR.iterdir():
        if child.is_dir() and child.name in CLASSIFICATION_DIR_NAMES:
            shutil.rmtree(child, ignore_errors=True)


def reset_runtime_state() -> None:
    stamp = now_iso()
    ensure_documents_fixture()
    reset_sample_documents_fixture()
    for path in [
        ROOT / "runtime" / "generated" / "local-files",
        ROOT / "runtime" / "generated" / "custom-agents",
        ROOT / "runtime" / "generated" / "family_bills",
        ROOT / "runtime" / "generated" / "reminder",
        ROOT / "runtime" / "generated" / "bills",
    ]:
        if path.exists():
            shutil.rmtree(path, ignore_errors=True)
    customize_dir = ROOT / "runtime" / "features" / "customize"
    if customize_dir.exists():
        for path in customize_dir.iterdir():
            if path.name != "__init__.py":
                if path.is_dir():
                    shutil.rmtree(path, ignore_errors=True)
                else:
                    path.unlink(missing_ok=True)
    for feature_id in ["family_bills", "reminder", "bills"]:
        target = ROOT / "runtime" / "data" / f"{feature_id}.json"
        if target.exists():
            target.unlink()
    write_json(ROOT / "runtime" / "home_memory.json", {"events": [], "reminders": [], "recentActions": [{"id": "home-memory-ready", "summary": "HomeHub memory is ready.", "createdAt": stamp}]})
    write_json(ROOT / "runtime" / "weather_state.json", {"location": "", "locationLabel": "", "condition": "", "temperatureC": 0, "highC": 0, "lowC": 0, "latitude": 0, "longitude": 0, "source": "", "updatedAt": "", "gpsEnabled": False, "gpsPermission": "prompt"})
    write_json(ROOT / "runtime" / "data" / "external_channels.json", {"apps": {}, "mail": {}, "lastRun": "", "recentActions": [{"id": "external-ready", "summary": "External channels are ready.", "createdAt": stamp}]})
    write_json(ROOT / "runtime" / "agents" / "custom_agents.json", {"settings": {"testingMode": True}, "items": [], "recentActions": [{"id": "custom-agents-ready", "summary": "Custom agent studio is ready for test drafts.", "createdAt": stamp}], "lastRun": ""})
    write_json(ROOT / "runtime" / "data" / "local_files.json", {"pendingDelete": None, "recentActions": [], "lastRun": ""})
    write_json(ROOT / "runtime" / "data" / "task_semantic_memory.json", {"meta": {"schemaVersion": "1.0", "backend": "json-hybrid-indexed", "brainFamily": "homehub-semantic-memory", "updatedAt": stamp, "version": 1}, "items": []})
    (ROOT / "runtime" / "conversation_log.jsonl").write_text("", encoding="utf-8")
    runtime = server.build_runtime_bridge()
    server.FEATURE_MANAGER.refresh(runtime)
    server.FEATURE_MANAGER.reset(runtime)
    server.HOME_MEMORY = json.loads((ROOT / "runtime" / "home_memory.json").read_text(encoding="utf-8"))
    server.WEATHER = json.loads((ROOT / "runtime" / "weather_state.json").read_text(encoding="utf-8"))
    server.PENDING_VOICE_CLARIFICATION = None
    initial_conversation = server.build_initial_conversation(server.PERSISTED_SETTINGS["language"])
    server.CURRENT_CONVERSATION[:] = initial_conversation
    server.VOICE_CONVERSATION[:] = list(initial_conversation)


def run_voice_with_timeout(query: str, locale: str = "zh-CN", timeout_seconds: int = 30) -> dict:
    worker = (
        "import json, sys;"
        "sys.path.insert(0, r'%s');"
        "payload=json.loads(sys.stdin.buffer.read().decode('utf-8'));"
        "import runtime.server as s;"
        "result=s.resolve_voice_request(payload['query'], payload['locale']);"
        "sys.stdout.buffer.write(json.dumps(result, ensure_ascii=False).encode('utf-8'))"
    ) % str(ROOT)
    try:
        completed = subprocess.run(
            [sys.executable, "-c", worker],
            cwd=ROOT,
            capture_output=True,
            input=json.dumps({"query": query, "locale": locale}, ensure_ascii=False).encode("utf-8"),
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return {"reply": f"TIMEOUT after {timeout_seconds}s", "route": {"kind": "timeout"}, "artifacts": []}
    stdout = (completed.stdout or b"").decode("utf-8", errors="replace").strip()
    stderr = (completed.stderr or b"").decode("utf-8", errors="replace").strip()
    if not stdout:
        return {"reply": f"EMPTY_RESPONSE: {stderr}", "route": {"kind": "error"}, "artifacts": []}
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return {"reply": f"INVALID_RESPONSE: {stdout}", "route": {"kind": "error"}, "artifacts": []}


def build_cases() -> list[CaseSpec]:
    return [
        CaseSpec("阶段1", "本地问候", "你好", "返回自然问候。", "reply_contains_greeting"),
        CaseSpec("阶段1", "城市天气查询", "请告诉我今天的天气，并告诉我最高温度。", "返回天气和温度信息。", "reply_has_weather_shape"),
        CaseSpec("阶段1", "联网航班查询", "帮我查询今天从东京到上海的航班，5月1日有什么航班和价格", "返回航班或联网查询结果。", "reply_has_flight_shape"),
        CaseSpec("阶段1", "本地文件查询与附件回传", f"查看 {TEST_DOCUMENTS_TEXT} 下面有什么文件，{TEST_FILENAME} 文件发给我。", "返回目录内容并附带目标文件。", "artifacts_contains_test_file"),
        CaseSpec("阶段2", "创建提醒智能体", "创建智能体，名称为提醒。", "进入提醒智能体创建流程。", "reply_mentions_reminder_flow"),
        CaseSpec("阶段2", "提醒智能体补充信息", "用于定时提醒家人，提醒内容包括家庭日程和账单。", "出现确认或继续补充提示。", "reply_mentions_followup"),
        CaseSpec("阶段2", "确认生成提醒 feature", "确认创建提醒智能体。", "生成 reminder feature 文件。", "reminder_feature_generated"),
        CaseSpec("阶段2", "创建家庭账单智能体", "创建智能体，名称为家庭账单。", "进入家庭账单智能体创建流程。", "reply_mentions_bills_flow"),
        CaseSpec("阶段2", "家庭账单智能体补充信息", "可以通过 OCR 和文字记录家庭账单。", "出现确认或继续补充提示。", "reply_mentions_followup"),
        CaseSpec("阶段2", "确认生成账单 feature", "确认创建家庭账单智能体。", "生成 bills feature 文件。", "bills_feature_generated"),
        CaseSpec("阶段3", "消费记录 10:20", "记录今天10点20分消费2000日元", "调用家庭账单智能体记录消费。", "reply_mentions_spending_record"),
        CaseSpec("阶段3", "消费记录 12:00", "记录今天12点00分午饭消费800日元", "调用家庭账单智能体记录消费。", "reply_mentions_spending_record"),
        CaseSpec("阶段3", "消费记录 17:00", "记录今天17点00分购物消费5800日元", "调用家庭账单智能体记录消费。", "reply_mentions_spending_record"),
        CaseSpec("阶段3", "消费汇总与导出", "到今天为止消费总额是多少，并将消费的信息生成excel文档", "返回汇总并导出 Excel。", "reply_or_artifact_for_spending"),
        CaseSpec("阶段3", "消费汇总与提醒", "到今天为止消费总额是多少，如果超过2000日元产生提醒，并把提醒发送到 homehub", "返回汇总，并在超阈值时触发提醒。", "reply_mentions_threshold"),
        CaseSpec("扩展", "样本文档分类", r"将E:\sample documents下的文件，进行分类。类型创建新的文件夹。", "按类型创建文件夹并完成分类。", "sample_documents_classified"),
    ]


def evaluate_case(spec: CaseSpec, response: dict) -> CaseResult:
    reply = str(response.get("reply", ""))
    artifacts = response.get("artifacts", []) if isinstance(response.get("artifacts"), list) else []
    notes = f"route={(response.get('route') or {}).get('kind', '')}; artifacts={artifacts}"
    status = "FAIL"
    if spec.check == "reply_contains_greeting":
        status = "PASS" if any(token in reply.lower() for token in ["你好", "您好", "hello", "hi"]) else "FAIL"
    elif spec.check == "reply_has_weather_shape":
        status = "PASS" if any(token in reply for token in ["天气", "温度", "最高", "最低"]) else "FAIL"
    elif spec.check == "reply_has_flight_shape":
        status = "PASS" if any(token in reply for token in ["航班", "价格", "flight"]) else "FAIL"
    elif spec.check == "artifacts_contains_test_file":
        status = "PASS" if any(str(item.get("fileName", "")).strip() == TEST_FILENAME for item in artifacts if isinstance(item, dict)) else "FAIL"
    elif spec.check == "reply_mentions_reminder_flow":
        status = "PASS" if all(token in reply for token in ["提醒", "智能体"]) else "FAIL"
    elif spec.check == "reply_mentions_followup":
        status = "PASS" if any(token in reply for token in ["确认", "补充", "继续", "智能体"]) else "FAIL"
    elif spec.check == "reminder_feature_generated":
        feature = ROOT / "runtime" / "features" / "customize" / "reminder_feature.py"
        status = "PASS" if feature.exists() else "FAIL"
        notes = f"{notes}; feature={feature}"
    elif spec.check == "reply_mentions_bills_flow":
        status = "PASS" if all(token in reply for token in ["账单", "智能体"]) else "FAIL"
    elif spec.check == "bills_feature_generated":
        customize_dir = ROOT / "runtime" / "features" / "customize"
        candidates = sorted(path.name for path in customize_dir.glob("*bills*_feature.py"))
        status = "PASS" if bool(candidates) else "FAIL"
        notes = f"{notes}; generated={candidates}"
    elif spec.check == "reply_mentions_spending_record":
        status = "PASS" if any(token in reply for token in ["记录", "账单", "消费", "已添加"]) else "FAIL"
    elif spec.check == "reply_or_artifact_for_spending":
        status = "PASS" if ("总额" in reply or "消费" in reply or bool(artifacts)) else "FAIL"
    elif spec.check == "reply_mentions_threshold":
        status = "PASS" if any(token in reply for token in ["提醒", "超过", "阈值", "总额"]) else "FAIL"
    elif spec.check == "sample_documents_classified":
        existing_dirs = sorted(path.name for path in SAMPLE_DOCS_DIR.iterdir() if path.is_dir())
        status = "PASS" if bool(existing_dirs) else "FAIL"
        notes = f"{notes}; sample_dirs={existing_dirs}"
    return CaseResult(spec.stage, spec.name, spec.query, spec.expected, status, reply, notes)


def write_cases_doc(cases: list[CaseSpec]) -> None:
    lines = [
        "# HomeHub 3-Phase Test Cases",
        "",
        f"- Generated at: {now_iso()}",
        f"- Project path: {ROOT}",
        f"- Documents fixture: {TEST_DOCUMENTS_TEXT}",
        f"- Sample classification fixture: {SAMPLE_DOCS_DIR}",
        "",
    ]
    current_stage = ""
    for idx, case in enumerate(cases, start=1):
        if case.stage != current_stage:
            current_stage = case.stage
            lines.extend([f"## {current_stage}", ""])
        lines.extend([f"### {idx}. {case.name}", "", f"- Query: `{case.query}`", f"- Expected: {case.expected}", ""])
    CASES_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_results_doc(results: list[CaseResult]) -> None:
    passed = sum(1 for item in results if item.status == "PASS")
    failed = sum(1 for item in results if item.status == "FAIL")
    lines = [
        "# HomeHub 3-Phase Test Results",
        "",
        f"- Generated at: {now_iso()}",
        f"- Total cases: {len(results)}",
        f"- PASS: {passed}",
        f"- FAIL: {failed}",
        "",
    ]
    current_stage = ""
    for item in results:
        if item.stage != current_stage:
            current_stage = item.stage
            lines.extend([f"## {current_stage}", ""])
        lines.extend([f"### {item.name}", "", f"- Status: `{item.status}`", f"- Query: `{item.query}`", f"- Expected: {item.expected}", f"- Actual: {item.actual}", f"- Notes: {item.notes}", ""])
    RESULTS_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    reset_runtime_state()
    cases = build_cases()
    results = [evaluate_case(spec, run_voice_with_timeout(spec.query)) for spec in cases]
    write_cases_doc(cases)
    write_results_doc(results)
    print(json.dumps({"cases": str(CASES_PATH), "results": str(RESULTS_PATH), "pass": sum(1 for item in results if item.status == "PASS"), "fail": sum(1 for item in results if item.status == "FAIL")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
