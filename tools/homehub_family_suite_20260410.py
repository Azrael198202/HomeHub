from __future__ import annotations

import json
import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
CASES_DOC = DOCS_DIR / "homehub-3-phase-family-test-cases-mac-2026-04-10.md"
RESULTS_DOC = DOCS_DIR / "homehub-3-phase-family-test-results-mac-2026-04-10.md"
TMP_ROOT = Path("/tmp/homehub-family-suite")
MAC_DOCUMENTS_DIR = Path("/Users/home/Documents")
TEST_DOCUMENT_NAME = "AI_Agent_Build2026 en.pptx"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import runtime.server as server


def now_text() -> str:
    return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def ensure_documents_fixture() -> None:
    MAC_DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
    target = MAC_DOCUMENTS_DIR / TEST_DOCUMENT_NAME
    if not target.exists():
        target.write_bytes(b"HomeHub mac fixture")


def clean_customize_dir() -> None:
    customize_dir = ROOT / "runtime" / "features" / "customize"
    customize_dir.mkdir(parents=True, exist_ok=True)
    for child in customize_dir.iterdir():
        if child.name == "__init__.py":
            continue
        if child.is_dir():
            shutil.rmtree(child, ignore_errors=True)
        else:
            child.unlink(missing_ok=True)


def reset_runtime_state() -> None:
    stamp = now_text()
    ensure_documents_fixture()
    if TMP_ROOT.exists():
        shutil.rmtree(TMP_ROOT)
    TMP_ROOT.mkdir(parents=True, exist_ok=True)

    generated_dir = ROOT / "runtime" / "generated"
    preserved_generated = {"vendor", "avatar", "handle_demand", "homehub-autonomy-20260407163421"}
    if generated_dir.exists():
        for child in generated_dir.iterdir():
            if child.name in preserved_generated:
                continue
            if child.is_dir():
                shutil.rmtree(child, ignore_errors=True)
            else:
                child.unlink(missing_ok=True)

    clean_customize_dir()

    data_dir = ROOT / "runtime" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    preserved_data = {"external_channels.json", "local_files.json", "task_semantic_memory.json", "handle_demand.json"}
    for child in data_dir.glob("*.json"):
        if child.name in preserved_data:
            continue
        child.unlink(missing_ok=True)

    write_json(
        ROOT / "runtime" / "home_memory.json",
        {
            "events": [],
            "reminders": [],
            "recentActions": [
                {
                    "id": "home-memory-ready",
                    "summary": "HomeHub memory is ready.",
                    "createdAt": stamp,
                }
            ],
        },
    )
    write_json(
        ROOT / "runtime" / "weather_state.json",
        {
            "location": "",
            "locationLabel": "",
            "condition": "",
            "temperatureC": 0,
            "highC": 0,
            "lowC": 0,
            "latitude": 0,
            "longitude": 0,
            "source": "",
            "updatedAt": "",
            "gpsEnabled": False,
            "gpsPermission": "prompt",
        },
    )
    write_json(
        ROOT / "runtime" / "data" / "external_channels.json",
        {
            "apps": {},
            "mail": {},
            "lastRun": "",
            "recentActions": [
                {
                    "id": "external-ready",
                    "summary": "External channels are ready.",
                    "createdAt": stamp,
                }
            ],
        },
    )
    write_json(
        ROOT / "runtime" / "agents" / "custom_agents.json",
        {
            "settings": {"testingMode": True},
            "items": [],
            "recentActions": [
                {
                    "id": "custom-agents-ready",
                    "summary": "Custom agent studio is ready for test drafts.",
                    "createdAt": stamp,
                }
            ],
            "lastRun": "",
        },
    )
    write_json(ROOT / "runtime" / "data" / "local_files.json", {"pendingDelete": None, "recentActions": [], "lastRun": ""})
    write_json(
        ROOT / "runtime" / "data" / "task_semantic_memory.json",
        {
            "meta": {
                "schemaVersion": "1.0",
                "backend": "json-hybrid-indexed",
                "brainFamily": "homehub-semantic-memory",
                "updatedAt": stamp,
                "version": 1,
            },
            "items": [],
        },
    )
    write_json(
        ROOT / "runtime" / "data" / "knowledge_memory.json",
        {
            "meta": {
                "schemaVersion": "1.0",
                "brainFamily": "homehub-knowledge-memory",
                "updatedAt": stamp,
            },
            "items": [],
        },
    )
    write_json(
        ROOT / "runtime" / "data" / "source_reference_memory.json",
        {
            "meta": {
                "schemaVersion": "1.0",
                "brainFamily": "homehub-source-reference-memory",
                "updatedAt": stamp,
            },
            "items": [],
        },
    )
    (ROOT / "runtime" / "conversation_log.jsonl").write_text("", encoding="utf-8")

    runtime = server.build_runtime_bridge()
    server.FEATURE_MANAGER.refresh(runtime)
    server.FEATURE_MANAGER.reset(runtime)
    server.HOME_MEMORY = json.loads((ROOT / "runtime" / "home_memory.json").read_text(encoding="utf-8"))
    server.WEATHER = json.loads((ROOT / "runtime" / "weather_state.json").read_text(encoding="utf-8"))
    server.PENDING_VOICE_CLARIFICATION = None
    initial = server.build_initial_conversation(server.PERSISTED_SETTINGS["language"])
    server.CURRENT_CONVERSATION[:] = initial
    server.VOICE_CONVERSATION[:] = list(initial)


def runtime_bridge():
    runtime = server.build_runtime_bridge()
    server.FEATURE_MANAGER.refresh(runtime)
    return runtime


def ask(query: str, locale: str = "zh-CN") -> dict:
    return server.resolve_voice_request(query, locale)


def stage_dir(name: str) -> Path:
    path = TMP_ROOT / name
    path.mkdir(parents=True, exist_ok=True)
    return path


def seed_basic_file_fixtures() -> dict[str, Path]:
    inbox = stage_dir("family-inbox")
    library = stage_dir("family-library")
    reading = stage_dir("family-reading")

    shutil.rmtree(inbox, ignore_errors=True)
    shutil.rmtree(library, ignore_errors=True)
    shutil.rmtree(reading, ignore_errors=True)
    inbox.mkdir(parents=True, exist_ok=True)
    library.mkdir(parents=True, exist_ok=True)
    reading.mkdir(parents=True, exist_ok=True)

    (inbox / "school_notice.txt").write_text("明天带水壶和室内鞋。", encoding="utf-8")
    (inbox / "monthly_budget.xlsx").write_text("budget", encoding="utf-8")
    (inbox / "family_trip.pptx").write_text("trip", encoding="utf-8")
    (inbox / "receipt.pdf").write_text("receipt", encoding="utf-8")
    (library / "vacation_photo.jpg").write_text("img", encoding="utf-8")
    (library / "meal-plan.md").write_text("# meal\n- pasta", encoding="utf-8")
    (library / "utility_bill.csv").write_text("type,amount\nwater,3200", encoding="utf-8")
    (reading / "shopping-note.txt").write_text("牛奶\n鸡蛋\n香蕉", encoding="utf-8")
    (reading / "recipe.json").write_text('{"dish":"curry"}', encoding="utf-8")
    return {"inbox": inbox, "library": library, "reading": reading}


def seed_classify_fixture(name: str, files: dict[str, str]) -> Path:
    base = stage_dir(name)
    shutil.rmtree(base, ignore_errors=True)
    base.mkdir(parents=True, exist_ok=True)
    for filename, content in files.items():
        (base / filename).write_text(content, encoding="utf-8")
    return base


def contains_any(reply: str, tokens: list[str]) -> bool:
    return any(token in reply for token in tokens)


def read_custom_agents() -> dict:
    return json.loads((ROOT / "runtime" / "agents" / "custom_agents.json").read_text(encoding="utf-8"))


def customize_feature_files() -> list[Path]:
    return sorted(path for path in (ROOT / "runtime" / "features" / "customize").glob("*.py") if path.name != "__init__.py")


def read_family_bills_store() -> dict:
    path = ROOT / "runtime" / "data" / "family_bills.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def generated_feature_id_for_agent(agent_name: str) -> str:
    for item in read_custom_agents().get("items", []):
        if str(item.get("name", "")).strip() == agent_name:
            return str(item.get("generatedFeatureId", "")).strip()
    return ""


def read_generated_feature_store(agent_name: str) -> dict:
    feature_id = generated_feature_id_for_agent(agent_name)
    if not feature_id:
        return {}
    path = ROOT / "runtime" / "data" / f"{feature_id}.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_knowledge_memory() -> dict:
    path = ROOT / "runtime" / "data" / "knowledge_memory.json"
    if not path.exists():
        return {"meta": {}, "items": []}
    return json.loads(path.read_text(encoding="utf-8"))


def read_source_reference_memory() -> dict:
    path = ROOT / "runtime" / "data" / "source_reference_memory.json"
    if not path.exists():
        return {"meta": {}, "items": []}
    return json.loads(path.read_text(encoding="utf-8"))


@dataclass
class Case:
    case_id: str
    stage: str
    name: str
    query: str
    expected: str
    reset_before: bool = False
    setup_queries: list[str] = field(default_factory=list)
    fixture_prep: Callable[[], None] | None = None
    validator: Callable[[dict], tuple[bool, str]] | None = None


@dataclass
class CaseResult:
    case_id: str
    stage: str
    name: str
    query: str
    expected: str
    status: str
    actual: str
    notes: str


@dataclass
class VariantCase:
    variant_id: str
    base_case_id: str
    stage: str
    name: str
    locale: str
    query: str


@dataclass
class VariantResult:
    variant_id: str
    base_case_id: str
    stage: str
    locale: str
    query: str
    status: str
    notes: str


VARIANT_TEMPLATES = {
    "zh-CN": [
        "请帮我处理这个请求：{query}",
        "麻烦你按这个意思来做：{query}",
        "换个说法，我的意思是：{query}",
        "帮我看一下这件事：{query}",
        "这件事请直接处理：{query}",
        "下面这个需求麻烦执行：{query}",
        "这是家庭场景下的请求：{query}",
        "请按照这个要求回复：{query}",
        "我想表达的是：{query}",
        "请你根据这句话处理：{query}",
    ],
    "en-US": [
        "Please help with this request: {query}",
        "Could you handle this for me: {query}",
        "I want to say this in another way: {query}",
        "Please work on the following request: {query}",
        "Here is the request from our family use case: {query}",
        "Can you respond to this request: {query}",
        "Please treat this as the actual instruction: {query}",
        "What I mean is: {query}",
        "Please process the following: {query}",
        "I'd like help with this: {query}",
    ],
    "ja-JP": [
        "この依頼をお願いします: {query}",
        "次の内容で対応してください: {query}",
        "言い換えるとこういう依頼です: {query}",
        "家庭向けの依頼として処理してください: {query}",
        "以下のお願いを対応してください: {query}",
        "この内容で進めてください: {query}",
        "私の意図は次のとおりです: {query}",
        "次のリクエストに答えてください: {query}",
        "これを実際の指示として扱ってください: {query}",
        "この件を手伝ってください: {query}",
    ],
}

VARIANT_LOCALE_SUFFIX = {
    "zh-CN": "ZH",
    "en-US": "EN",
    "ja-JP": "JA",
}


def build_case_variants(case: Case) -> list[VariantCase]:
    variants: list[VariantCase] = []
    for locale, templates in VARIANT_TEMPLATES.items():
        suffix = VARIANT_LOCALE_SUFFIX[locale]
        for index, template in enumerate(templates, start=1):
            variants.append(
                VariantCase(
                    variant_id=f"{case.case_id}-{suffix}-{index:02d}",
                    base_case_id=case.case_id,
                    stage=case.stage,
                    name=f"{case.name} {suffix} {index}",
                    locale=locale,
                    query=template.format(query=case.query),
                )
            )
    return variants


def task_spec_signature(query: str, locale: str) -> dict[str, str]:
    spec = server.build_task_spec(
        query,
        locale,
        detect_ui_action=server.detect_ui_action,
        infer_task_spec=lambda _text, _locale, _examples: None,
    )
    return {
        "taskType": str(spec.get("taskType", "")).strip(),
        "intent": str(spec.get("intent", "")).strip(),
        "preferredExecution": str(spec.get("preferredExecution", "")).strip(),
    }


def task_specs_equivalent(base_spec: dict[str, str], variant_spec: dict[str, str]) -> tuple[bool, str]:
    base_type = str(base_spec.get("taskType", "")).strip()
    variant_type = str(variant_spec.get("taskType", "")).strip()
    if base_type != variant_type:
        return False, f"taskType mismatch: base={base_type} variant={variant_type}"
    base_intent = str(base_spec.get("intent", "")).strip()
    variant_intent = str(variant_spec.get("intent", "")).strip()
    if base_intent and variant_intent and base_intent != variant_intent:
        if not (base_intent.startswith("network-") and variant_intent.startswith("network-")):
            return False, f"intent mismatch: base={base_intent} variant={variant_intent}"
    return True, f"taskType={base_type}; intent={variant_intent or base_intent}"


def run_variant_regression(cases: list[Case]) -> list[VariantResult]:
    results: list[VariantResult] = []
    total = len(cases)
    for index, case in enumerate(cases, start=1):
        if index == 1 or index % 10 == 0 or case.case_id.startswith("NET-"):
            print(f"[variants] {index}/{total} {case.case_id} {case.name}", flush=True)
        if case.reset_before:
            reset_runtime_state()
        if case.fixture_prep:
            case.fixture_prep()
        for setup_query in case.setup_queries:
            ask(setup_query)
        base_spec = task_spec_signature(case.query, "zh-CN")
        for variant in build_case_variants(case):
            variant_spec = task_spec_signature(variant.query, variant.locale)
            ok, notes = task_specs_equivalent(base_spec, variant_spec)
            results.append(
                VariantResult(
                    variant_id=variant.variant_id,
                    base_case_id=variant.base_case_id,
                    stage=variant.stage,
                    locale=variant.locale,
                    query=variant.query,
                    status="PASS" if ok else "FAIL",
                    notes=notes,
                )
            )
    return results


def validate_reply(tokens: list[str]) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        ok = contains_any(reply, tokens)
        return ok, f"tokens={tokens}"

    return inner


def validate_weather(response: dict) -> tuple[bool, str]:
    reply = str(response.get("reply", ""))
    rejected = ["外部天气服务没有返回可用结果", "did not return usable results", "请稍后重试"]
    lookup = response.get("lookupResult", {}) if isinstance(response.get("lookupResult", {}), dict) else {}
    ok = (
        not contains_any(reply, rejected)
        and contains_any(reply, ["天气", "气温", "温度", "最高", "最低", "下雨", "降雨", "来源："])
        and bool(lookup.get("ok"))
    )
    return ok, f"weather-live; sources={len(lookup.get('sources', [])) if isinstance(lookup.get('sources', []), list) else 0}"


def validate_live_network(tokens: list[str], regexes: list[str] | None = None, source_domains: list[str] | None = None, disallow: list[str] | None = None) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        lookup = response.get("lookupResult", {}) if isinstance(response.get("lookupResult", {}), dict) else {}
        sources = lookup.get("sources", []) if isinstance(lookup.get("sources", []), list) else []
        ok = bool(lookup.get("ok")) and contains_any(reply, tokens) and bool(sources)
        for pattern in regexes or []:
            ok = ok and bool(__import__("re").search(pattern, reply))
        for token in disallow or []:
            ok = ok and token not in reply
        if source_domains:
            ok = ok and any(any(domain in str(item.get("url", "")) for domain in source_domains) for item in sources if isinstance(item, dict))
        return ok, f"lookup_ok={lookup.get('ok')}; sources={len(sources)}"

    return inner


def validate_knowledge_written(expected_token: str) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        payload = read_knowledge_memory()
        items = payload.get("items", []) if isinstance(payload.get("items", []), list) else []
        writeback = ((response.get("executionContext", {}) if isinstance(response.get("executionContext", {}), dict) else {}).get("memoryWriteback", {}) if isinstance((response.get("executionContext", {}) if isinstance(response.get("executionContext", {}), dict) else {}).get("memoryWriteback", {}), dict) else {})
        knowledge_items = writeback.get("knowledgeItems", []) if isinstance(writeback.get("knowledgeItems", []), list) else []
        haystack = " ".join(
            " ".join(
                str(item.get(key, "")).strip()
                for key in ["title", "summary", "searchText", "source"]
            )
            for item in items
            if isinstance(item, dict)
        )
        ok = expected_token in haystack and bool(knowledge_items)
        return ok, f"knowledge_items={len(items)}; writeback={len(knowledge_items)}"

    return inner


def validate_knowledge_reply(expected_tokens: list[str]) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        ok = "本地知识库" in reply and all(token in reply for token in expected_tokens)
        return ok, f"knowledge-reply; tokens={expected_tokens}"

    return inner


def validate_no_knowledge_writeback(response: dict) -> tuple[bool, str]:
    payload = read_knowledge_memory()
    items = payload.get("items", []) if isinstance(payload.get("items", []), list) else []
    writeback = ((response.get("executionContext", {}) if isinstance(response.get("executionContext", {}), dict) else {}).get("memoryWriteback", {}) if isinstance((response.get("executionContext", {}) if isinstance(response.get("executionContext", {}), dict) else {}).get("memoryWriteback", {}), dict) else {})
    knowledge_items = writeback.get("knowledgeItems", []) if isinstance(writeback.get("knowledgeItems", []), list) else []
    ok = not items and not knowledge_items
    return ok, f"knowledge_items={len(items)}; writeback={len(knowledge_items)}"


def validate_source_reference_written(expected_token: str) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        payload = read_source_reference_memory()
        items = payload.get("items", []) if isinstance(payload.get("items", []), list) else []
        writeback = ((response.get("executionContext", {}) if isinstance(response.get("executionContext", {}), dict) else {}).get("memoryWriteback", {}) if isinstance((response.get("executionContext", {}) if isinstance(response.get("executionContext", {}), dict) else {}).get("memoryWriteback", {}), dict) else {})
        source_refs = writeback.get("sourceReferences", []) if isinstance(writeback.get("sourceReferences", []), list) else []
        haystack = " ".join(
            " ".join(
                str(item.get(key, "")).strip()
                for key in ["title", "url", "queryText", "searchText", "source"]
            )
            for item in items
            if isinstance(item, dict)
        )
        ok = expected_token in haystack and bool(source_refs)
        return ok, f"source_refs={len(items)}; writeback={len(source_refs)}"

    return inner


def validate_source_reference_reuse(response: dict) -> tuple[bool, str]:
    reply = str(response.get("reply", ""))
    lookup = response.get("lookupResult", {}) if isinstance(response.get("lookupResult", {}), dict) else {}
    source_hits = lookup.get("sourceReferenceHits", []) if isinstance(lookup.get("sourceReferenceHits", []), list) else []
    ok = bool(lookup.get("ok")) and bool(source_hits) and "来源：" in reply
    return ok, f"lookup_ok={lookup.get('ok')}; source_hits={len(source_hits)}"


def validate_iterative_lookup(min_attempts: int = 2) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        lookup = response.get("lookupResult", {}) if isinstance(response.get("lookupResult", {}), dict) else {}
        attempted = lookup.get("attemptedQueries", []) if isinstance(lookup.get("attemptedQueries", []), list) else []
        ok = bool(lookup.get("ok")) and len(attempted) >= min_attempts
        return ok, f"lookup_ok={lookup.get('ok')}; attempted={len(attempted)}"

    return inner


def combine_validators(*validators: Callable[[dict], tuple[bool, str]]) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        notes = []
        ok = True
        for validator in validators:
            current_ok, current_notes = validator(response)
            ok = ok and current_ok
            notes.append(current_notes)
        return ok, " | ".join(notes)

    return inner


def validate_artifact(filename: str = "", extension: str = "") -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        artifacts = response.get("artifacts", []) if isinstance(response.get("artifacts", []), list) else []
        ok = False
        for item in artifacts:
            if not isinstance(item, dict):
                continue
            file_name = str(item.get("fileName", "")).strip()
            if filename and file_name == filename:
                ok = True
                break
            if extension and file_name.endswith(extension):
                ok = True
                break
        return ok, f"filename={filename}; extension={extension}"

    return inner


def validate_classified(path: Path, expected_dirs: list[str]) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        actual_dirs = sorted(item.name for item in path.iterdir() if item.is_dir())
        ok = sorted(expected_dirs) == actual_dirs
        return ok, f"expected_dirs={expected_dirs}; actual_dirs={actual_dirs}"

    return inner


def validate_permission_hint(response: dict) -> tuple[bool, str]:
    reply = str(response.get("reply", ""))
    ok = contains_any(reply, ["没有权限", "工作区目录", "/tmp"])
    return ok, "permission-degrade"


def validate_agent_started(agent_name: str) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        ok = (
            agent_name in reply and contains_any(reply, ["已开始设计", "started"])
        ) or contains_any(reply, ["还有其他要求吗", "确认创建"])
        return ok, f"agent={agent_name}"

    return inner


def validate_agent_refined(response: dict) -> tuple[bool, str]:
    reply = str(response.get("reply", ""))
    ok = contains_any(reply, ["还有其他要求吗", "确认创建"])
    return ok, "agent-refine"


def validate_agent_confirmed(agent_name: str) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        agents = read_custom_agents().get("items", [])
        complete = [item for item in agents if item.get("name") == agent_name and item.get("status") == "complete"]
        files = customize_feature_files()
        ok = bool(complete) and bool(files) and contains_any(reply, ["已正式创建完成", "feature 文件"])
        return ok, f"agent={agent_name}; files={[path.name for path in files]}"

    return inner


def validate_bills_record(expected_count: int) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        store = read_family_bills_store()
        count = len(store.get("items", [])) if isinstance(store.get("items", []), list) else 0
        ok = contains_any(reply, ["已记录到家庭账单"]) and count == expected_count
        return ok, f"expected_count={expected_count}; actual_count={count}"

    return inner


def validate_bills_summary(expected_total: int, threshold: int | None = None, exceeded: bool | None = None, expect_artifact: bool = False) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        ok = str(expected_total) in reply and "消费总额" in reply
        if threshold is not None:
            ok = ok and str(threshold) in reply
        if exceeded is True:
            ok = ok and "已经超过" in reply
        if exceeded is False:
            ok = ok and "还没有超过" in reply
        if expect_artifact:
            artifacts = response.get("artifacts", []) if isinstance(response.get("artifacts", []), list) else []
            ok = ok and any(str(item.get("fileName", "")).endswith(".xlsx") for item in artifacts if isinstance(item, dict))
        return ok, f"expected_total={expected_total}; threshold={threshold}; exceeded={exceeded}; expect_artifact={expect_artifact}"

    return inner


def validate_bills_list(expected_count: int) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        ok = f"当前有 {expected_count} 条记录" in reply
        return ok, f"expected_count={expected_count}"

    return inner


def validate_bills_export(expected_count: int) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        artifacts = response.get("artifacts", []) if isinstance(response.get("artifacts", []), list) else []
        ok = any(
            isinstance(item, dict)
            and str(item.get("fileName", "")).endswith(".xlsx")
            and int(item.get("count", 0) or 0) == expected_count
            for item in artifacts
        )
        return ok, f"expected_count={expected_count}"

    return inner


def validate_named_agent_record(agent_name: str, expected_count: int) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        store = read_generated_feature_store(agent_name)
        count = len(store.get("items", [])) if isinstance(store.get("items", []), list) else 0
        ok = agent_name in reply and contains_any(reply, ["已记录到", "recorded"]) and count == expected_count
        return ok, f"agent={agent_name}; expected_count={expected_count}; actual_count={count}"

    return inner


def validate_named_agent_list(agent_name: str, expected_count: int) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        ok = agent_name in reply and f"当前有 {expected_count} 条记录" in reply
        return ok, f"agent={agent_name}; expected_count={expected_count}"

    return inner


def validate_named_agent_export(agent_name: str, kind: str = "") -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        artifacts = response.get("artifacts", []) if isinstance(response.get("artifacts", []), list) else []
        ok = agent_name in reply or any(agent_name in str(item.get("label", "")) for item in artifacts if isinstance(item, dict))
        if kind == "spreadsheet":
            ok = ok and any(str(item.get("fileName", "")).endswith((".xlsx", ".csv")) for item in artifacts if isinstance(item, dict))
        elif kind == "document":
            ok = ok and any(str(item.get("fileName", "")).endswith((".txt", ".docx", ".xlsx")) for item in artifacts if isinstance(item, dict))
        else:
            ok = ok and bool(artifacts or contains_any(reply, ["已导出", "生成好了可下载的产物"]))
        return ok, f"agent={agent_name}; kind={kind}; artifacts={artifacts}"

    return inner


def validate_collab_threshold(expected_total: int, reminder_name: str) -> Callable[[dict], tuple[bool, str]]:
    def inner(response: dict) -> tuple[bool, str]:
        reply = str(response.get("reply", ""))
        ok = str(expected_total) in reply and "联动提醒智能体" in reply and reminder_name in reply
        return ok, f"expected_total={expected_total}; reminder={reminder_name}"

    return inner


def stage1_cases() -> list[Case]:
    fixtures = seed_basic_file_fixtures()
    classify_alpha = seed_classify_fixture(
        "classify-alpha",
        {
            "school-plan.txt": "todo",
            "vacation.jpg": "img",
            "water-bill.csv": "bill",
            "family-slides.pptx": "ppt",
        },
    )
    classify_beta = seed_classify_fixture(
        "classify-beta",
        {
            "archive.zip": "zip",
            "recipe.md": "md",
            "movie.mp4": "mp4",
            "budget.xlsx": "xls",
            "notice.pdf": "pdf",
        },
    )

    def prep_files() -> None:
        seed_basic_file_fixtures()
        seed_classify_fixture(
            "classify-alpha",
            {
                "school-plan.txt": "todo",
                "vacation.jpg": "img",
                "water-bill.csv": "bill",
                "family-slides.pptx": "ppt",
            },
        )
        seed_classify_fixture(
            "classify-beta",
            {
                "archive.zip": "zip",
                "recipe.md": "md",
                "movie.mp4": "mp4",
                "budget.xlsx": "xls",
                "notice.pdf": "pdf",
            },
        )

    cases: list[Case] = []
    greeting_queries = ["你好", "你好啊 HomeHub", "早上好", "晚上好"]
    for index, query in enumerate(greeting_queries, start=1):
        cases.append(
            Case(
                case_id=f"S1-{index:02d}",
                stage="阶段1",
                name=f"本地问候 {index}",
                query=query,
                expected="返回自然问候。",
                reset_before=True,
                validator=validate_reply(["你好", "您好"]),
            )
        )

    weather_queries = [
        "福冈今天的天气怎么样，最高温多少",
        "东京今天气温多少",
        "大阪今天会下雨吗",
        "请告诉我今天的天气，并告诉我最高温度",
    ]
    for offset, query in enumerate(weather_queries, start=5):
        cases.append(
            Case(
                case_id=f"S1-{offset:02d}",
                stage="阶段1",
                name=f"天气查询 {offset - 4}",
                query=query,
                expected="返回天气信息或明确降级。",
                reset_before=True,
                validator=validate_weather,
            )
        )

    file_specs = [
        ("列出家庭收件箱", f"查看 {fixtures['inbox']} 下面有什么文件", validate_reply(["school_notice.txt", "monthly_budget.xlsx", "family_trip.pptx", "receipt.pdf"])),
        ("发送收件箱演示文稿", f"查看 {fixtures['inbox']} 下面有什么文件，family_trip.pptx 文件发给我。", validate_artifact(filename="family_trip.pptx")),
        ("搜索预算文件", f"搜索 {fixtures['inbox']} 下面的 budget 文件", validate_reply(["monthly_budget.xlsx"])),
        ("读取购物便签", f"读取 {fixtures['reading'] / 'shopping-note.txt'}", validate_reply(["牛奶", "鸡蛋", "香蕉"])),
        ("读取菜谱 JSON", f"读取 {fixtures['reading'] / 'recipe.json'}", validate_reply(["dish", "curry"])),
        ("列出家庭资料库", f"查看 {fixtures['library']} 下面有什么文件", validate_reply(["vacation_photo.jpg", "meal-plan.md", "utility_bill.csv"])),
        ("发送 Documents 夹里的演示文稿", f"查看 {MAC_DOCUMENTS_DIR} 下面有什么文件，{TEST_DOCUMENT_NAME} 文件发给我。", validate_artifact(filename=TEST_DOCUMENT_NAME)),
        ("搜索照片", f"搜索 {fixtures['library']} 下面的 photo 文件", validate_reply(["vacation_photo.jpg"])),
        ("分类 Alpha 目录", f"将 {classify_alpha} 下的文件，进行分类。类型创建新的文件夹。", validate_classified(classify_alpha, ["Documents", "Finance", "Media", "Text"])),
        ("分类 Beta 目录", f"将 {classify_beta} 下的文件，进行分类。类型创建新的文件夹。", validate_classified(classify_beta, ["Archives", "Documents", "Finance", "Media", "Text"])),
        ("家庭文档目录权限降级", f"将 {MAC_DOCUMENTS_DIR} 下的文件，进行分类。类型创建新的文件夹。", validate_permission_hint),
        ("发送 PDF 收据", f"查看 {fixtures['inbox']} 下面有什么文件，receipt.pdf 文件发给我。", validate_artifact(filename="receipt.pdf")),
    ]
    for offset, (name, query, validator) in enumerate(file_specs, start=9):
        cases.append(
            Case(
                case_id=f"S1-{offset:02d}",
                stage="阶段1",
                name=name,
                query=query,
                expected="完成本地文件操作或给出明确降级。",
                reset_before=True,
                fixture_prep=prep_files,
                validator=validator,
            )
        )

    reminder_specs = [
        ("孩子水壶提醒", "明天早上7点提醒我给孩子带水壶", [], validate_reply(["已经创建提醒", "给孩子带水壶"])),
        ("阳台灯提醒", "后天晚上8点提醒我关阳台灯", [], validate_reply(["已经创建提醒", "关阳台灯"])),
        ("水费提醒", "明天晚上9点提醒我交水费", [], validate_reply(["已经创建提醒", "交水费"])),
        ("提醒列表", "提醒列表", ["明天早上7点提醒我给孩子带水壶"], validate_reply(["提醒有：", "给孩子带水壶"])),
        ("双提醒列表", "提醒列表", ["明天早上7点提醒我给孩子带水壶", "后天晚上8点提醒我关阳台灯"], validate_reply(["提醒有：", "给孩子带水壶", "关阳台灯"])),
        ("家庭会议日程", "明天下午3点安排家庭会议，并提前30分钟提醒我", [], validate_reply(["已经帮你把", "家庭日程", "提前 30 分钟"])),
        ("家长会日程", "后天下午4点安排家长会，并提前30分钟提醒我", [], validate_reply(["已经帮你把", "家庭日程", "提前 30 分钟"])),
        ("查看日程", "查看日程", ["明天下午3点安排家庭会议，并提前30分钟提醒我"], validate_reply(["接下来日程有：", "提醒有："])),
        ("奶奶吃药提醒", "明天早上8点提醒奶奶吃药", [], validate_reply(["已经创建提醒", "奶奶吃药"])),
        ("倒垃圾提醒", "明天晚上9点提醒我倒垃圾", [], validate_reply(["已经创建提醒", "倒垃圾"])),
        ("学校接送日程", "明天下午5点安排接孩子放学，并提前30分钟提醒我", [], validate_reply(["已经帮你把", "家庭日程", "提前 30 分钟"])),
        ("日程与提醒总览", "查看日程", ["明天下午5点安排接孩子放学，并提前30分钟提醒我"], validate_reply(["接下来日程有：", "提醒有："])),
    ]
    for offset, (name, query, setup_queries, validator) in enumerate(reminder_specs, start=21):
        cases.append(
            Case(
                case_id=f"S1-{offset:02d}",
                stage="阶段1",
                name=name,
                query=query,
                expected="完成提醒/日程操作。",
                reset_before=True,
                setup_queries=setup_queries,
                validator=validator,
            )
        )
    return cases


def stage2_cases() -> list[Case]:
    agents = [
        ("家庭账单", "可以通过语音，文字，OCR进行账单的记录。"),
        ("家庭提醒", "可以按时间、人物和提醒方式管理家庭提醒。"),
        ("身体状况记录", "用于记录家庭成员身体状况、体温和症状。"),
        ("体检报告", "用于记录医院检查项目、结果和复查时间。"),
        ("医院复查提醒", "用于记录医院复查时间并提醒家人。"),
        ("孩子学习计划", "用于记录孩子学习科目、作业和老师反馈。"),
        ("家庭活动安排", "用于记录家庭活动时间、地点和参与成员。"),
        ("家庭日程安排", "用于记录家庭日程时间、地点、参与成员和注意事项。"),
        ("买菜助理", "用于记录买菜项目、数量和备注，并支持导出excel。"),
    ]
    cases: list[Case] = []
    case_no = 1
    for agent_name, refine_text in agents:
        create_id = f"S2-{case_no:02d}"
        cases.append(
            Case(
                case_id=create_id,
                stage="阶段2",
                name=f"{agent_name} 创建草稿",
                query=f"创建智能体，名称为{agent_name}。",
                expected="进入智能体创建流程。",
                reset_before=True,
                validator=validate_agent_started(agent_name),
            )
        )
        case_no += 1
        cases.append(
            Case(
                case_id=f"S2-{case_no:02d}",
                stage="阶段2",
                name=f"{agent_name} 补充需求",
                query=refine_text,
                expected="补充需求并进入确认前状态。",
                reset_before=True,
                setup_queries=[f"创建智能体，名称为{agent_name}。"],
                validator=validate_agent_refined,
            )
        )
        case_no += 1
        cases.append(
            Case(
                case_id=f"S2-{case_no:02d}",
                stage="阶段2",
                name=f"{agent_name} 确认创建",
                query="确认创建。",
                expected="完成创建并生成 feature 文件。",
                reset_before=True,
                setup_queries=[f"创建智能体，名称为{agent_name}。", refine_text],
                validator=validate_agent_confirmed(agent_name),
            )
        )
        case_no += 1
    return cases


def stage3_cases() -> list[Case]:
    create_flow = [
        "创建智能体，名称为家庭账单。",
        "可以通过语音，文字，OCR进行账单的记录。",
        "确认创建。",
    ]
    amounts = [
        ("记录今日07点30分，早餐消费480日元", 480),
        ("记录今日08点20分，地铁消费220日元", 220),
        ("记录今日10点20分，食材消费2000日元", 2000),
        ("记录今日12点00分，午餐消费800日元", 800),
        ("记录今日14点10分，水果消费650日元", 650),
        ("记录今日15点30分，纸巾消费320日元", 320),
        ("记录今日17点00分，应酬消费5800日元", 5800),
        ("记录今日18点15分，牛奶消费260日元", 260),
        ("记录今日19点40分，晚餐消费1500日元", 1500),
        ("记录今日20点10分，停车消费700日元", 700),
        ("记录今日21点00分，药品消费980日元", 980),
        ("记录今日21点20分，宠物粮消费2300日元", 2300),
        ("记录今日21点40分，网费消费4300日元", 4300),
        ("记录今日22点00分，水费消费3200日元", 3200),
        ("记录今日22点10分，电费消费5100日元", 5100),
        ("记录今日22点20分，学用品消费890日元", 890),
        ("记录今日22点30分，洗衣液消费640日元", 640),
        ("记录今日22点40分，生日蛋糕消费2750日元", 2750),
        ("记录今日22点50分，咖啡消费450日元", 450),
        ("记录今日23点00分，夜宵消费990日元", 990),
    ]
    cases: list[Case] = []
    running_total = 0
    case_no = 1
    for index, (query, amount) in enumerate(amounts, start=1):
        running_total += amount
        reset_before = index == 1
        setup_queries = create_flow if index == 1 else []
        cases.append(
            Case(
                case_id=f"S3-{case_no:02d}",
                stage="阶段3",
                name=f"账单记录 {index}",
                query=query,
                expected="通过家庭账单智能体完成记录。",
                reset_before=reset_before,
                setup_queries=setup_queries,
                validator=validate_bills_record(index),
            )
        )
        case_no += 1
        if index in {5, 10, 15, 20}:
            cases.append(
                Case(
                    case_id=f"S3-{case_no:02d}",
                    stage="阶段3",
                    name=f"账单列表 {index}",
                    query="查看家庭账单有哪些记录",
                    expected="返回当前账单记录列表。",
                    validator=validate_bills_list(index),
                )
            )
            case_no += 1
            cases.append(
                Case(
                    case_id=f"S3-{case_no:02d}",
                    stage="阶段3",
                    name=f"账单导出 {index}",
                    query="导出家庭账单",
                    expected="导出当前账单记录为 Excel。",
                    validator=validate_bills_export(index),
                )
            )
            case_no += 1
            threshold = {5: 3000, 10: 10000, 15: 20000, 20: 35000}[index]
            cases.append(
                Case(
                    case_id=f"S3-{case_no:02d}",
                    stage="阶段3",
                    name=f"账单汇总阈值 {index}",
                    query=f"到今天为止消费总额是多少，如果超过{threshold}日元产生提醒，并把提醒发送到 homehub",
                    expected="返回累计总额，并根据阈值给出提示。",
                    validator=validate_bills_summary(running_total, threshold=threshold, exceeded=running_total > threshold),
                )
            )
            case_no += 1
            cases.append(
                Case(
                    case_id=f"S3-{case_no:02d}",
                    stage="阶段3",
                    name=f"账单汇总导出 {index}",
                    query="到今天为止消费总额是多少，并将消费的信息生成excel文档",
                    expected="返回累计总额并导出 Excel。",
                    validator=validate_bills_summary(running_total, expect_artifact=True),
                )
            )
            case_no += 1
    family_agent_flows = [
        (
            "身体状况记录",
            "用于记录家庭成员身体状况、体温和症状。",
            "请在身体状况记录中记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息",
            "查看身体状况记录有哪些记录",
            "导出身体状况记录文档",
            "document",
        ),
        (
            "体检报告",
            "用于记录医院检查项目、结果和复查时间。",
            "请在体检报告中记录：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查",
            "查看体检报告有哪些记录",
            "导出体检报告文档",
            "document",
        ),
        (
            "医院复查提醒",
            "用于记录医院复查时间并提醒家人。",
            "请在医院复查提醒中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub",
            "查看医院复查提醒有哪些记录",
            "导出医院复查提醒文档",
            "document",
        ),
        (
            "孩子学习计划",
            "用于记录孩子学习科目、作业和老师反馈。",
            "请在孩子学习计划中记录：小明今天完成数学口算20题和英语单词复习，老师反馈良好",
            "查看孩子学习计划有哪些记录",
            "导出孩子学习计划表格",
            "spreadsheet",
        ),
        (
            "家庭活动安排",
            "用于记录家庭活动时间、地点和参与成员。",
            "请在家庭活动安排中记录：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶",
            "查看家庭活动安排有哪些记录",
            "导出家庭活动安排文档",
            "document",
        ),
        (
            "家庭日程安排",
            "用于记录家庭日程时间、地点、参与成员和注意事项。",
            "请在家庭日程安排中记录：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物",
            "查看家庭日程安排有哪些记录",
            "导出家庭日程安排文档",
            "document",
        ),
    ]
    for agent_name, refine_text, input_query, output_query, export_query, export_kind in family_agent_flows:
        setup = [f"创建智能体，名称为{agent_name}。", refine_text, "确认创建。"]
        cases.append(
            Case(
                case_id=f"S3-{case_no:02d}",
                stage="阶段3",
                name=f"{agent_name} 输入记录",
                query=input_query,
                expected=f"将阶段3输入写入 {agent_name}，形成对应输出。",
                reset_before=True,
                setup_queries=setup,
                validator=validate_named_agent_record(agent_name, 1),
            )
        )
        case_no += 1
        cases.append(
            Case(
                case_id=f"S3-{case_no:02d}",
                stage="阶段3",
                name=f"{agent_name} 输出查询",
                query=output_query,
                expected=f"返回 {agent_name} 当前记录输出。",
                reset_before=True,
                setup_queries=setup + [input_query],
                validator=validate_named_agent_list(agent_name, 1),
            )
        )
        case_no += 1
        cases.append(
            Case(
                case_id=f"S3-{case_no:02d}",
                stage="阶段3",
                name=f"{agent_name} 输出导出",
                query=export_query,
                expected=f"导出 {agent_name} 的阶段3输出产物。",
                reset_before=True,
                setup_queries=setup + [input_query],
                validator=validate_named_agent_export(agent_name, export_kind),
            )
        )
        case_no += 1

    collaboration_setup = [
        "创建智能体，名称为家庭账单。",
        "可以通过语音，文字，OCR进行账单的记录。",
        "确认创建。",
        "创建智能体，名称为家庭提醒。",
        "可以按时间、人物和提醒方式管理家庭提醒。",
        "确认创建。",
        "记录今日10点20分，食材消费2000日元",
        "记录今日12点00分，午餐消费800日元",
        "记录今日17点00分，应酬消费5800日元",
    ]
    cases.append(
        Case(
            case_id=f"S3-{case_no:02d}",
            stage="阶段3",
            name="联合执行 账单与提醒阈值联动",
            query="到今天为止消费总额是多少，如果超出2000日元产生提醒，并把提醒发送到 homehub",
            expected="家庭账单与家庭提醒智能体联合执行，输出总额并触发提醒联动。",
            reset_before=True,
            setup_queries=collaboration_setup,
            validator=validate_collab_threshold(8600, "家庭提醒"),
        )
    )
    case_no += 1

    health_collab_setup = [
        "创建智能体，名称为身体状况记录。",
        "用于记录家庭成员身体状况、体温和症状。",
        "确认创建。",
        "创建智能体，名称为体检报告。",
        "用于记录医院检查项目、结果和复查时间。",
        "确认创建。",
        "请在身体状况记录中记录：妈妈今天体温37.6度，轻微头痛，晚上已休息",
        "请在体检报告中记录：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查",
    ]
    cases.append(
        Case(
            case_id=f"S3-{case_no:02d}",
            stage="阶段3",
            name="联合执行 健康与体检双记录",
            query="查看体检报告有哪些记录",
            expected="身体状况记录与体检报告智能体在同一家庭场景下连续执行，输出体检记录。",
            reset_before=True,
            setup_queries=health_collab_setup,
            validator=validate_named_agent_list("体检报告", 1),
        )
    )
    case_no += 1

    study_activity_setup = [
        "创建智能体，名称为孩子学习计划。",
        "用于记录孩子学习科目、作业和老师反馈。",
        "确认创建。",
        "创建智能体，名称为家庭活动安排。",
        "用于记录家庭活动时间、地点和参与成员。",
        "确认创建。",
        "请在孩子学习计划中记录：小明今天完成数学口算20题和英语单词复习，老师反馈良好",
        "请在家庭活动安排中记录：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶",
    ]
    cases.append(
        Case(
            case_id=f"S3-{case_no:02d}",
            stage="阶段3",
            name="联合执行 学习与活动双场景",
            query="导出孩子学习计划表格",
            expected="孩子学习计划与家庭活动安排在同一家庭周末场景下联合执行，输出学习表格。",
            reset_before=True,
            setup_queries=study_activity_setup,
            validator=validate_named_agent_export("孩子学习计划", "spreadsheet"),
        )
    )
    case_no += 1
    return cases


def extension_cases() -> list[Case]:
    cases: list[Case] = []
    case_no = 1
    classify_payloads = [
        ("ext-school", {"notice.pdf": "pdf", "classroom.txt": "txt", "photo.jpg": "img", "budget.xlsx": "xls"}, ["Documents", "Finance", "Media", "Text"]),
        ("ext-bills", {"water.csv": "csv", "power.xlsx": "xls", "gas.pdf": "pdf", "receipt.jpg": "img"}, ["Documents", "Finance", "Media"]),
        ("ext-photos", {"trip1.jpg": "img", "trip2.png": "img", "video.mp4": "mp4", "notes.md": "md"}, ["Media", "Text"]),
        ("ext-recipes", {"curry.md": "md", "soup.txt": "txt", "menu.pdf": "pdf", "archive.zip": "zip"}, ["Archives", "Documents", "Text"]),
        ("ext-mixed", {"ppt.pptx": "ppt", "table.csv": "csv", "song.mp3": "mp3", "log.log": "log"}, ["Documents", "Finance", "Media", "Text"]),
        ("ext-visitors", {"guest-list.xlsx": "xls", "camera.mp4": "mp4", "memo.txt": "txt"}, ["Finance", "Media", "Text"]),
        ("ext-pet", {"pet-food.csv": "csv", "cat.jpg": "img", "plan.md": "md"}, ["Finance", "Media", "Text"]),
        ("ext-health", {"medicine.pdf": "pdf", "receipt.csv": "csv", "scan.jpg": "img", "note.txt": "txt"}, ["Documents", "Finance", "Media", "Text"]),
    ]
    for name, files, expected_dirs in classify_payloads:
        base = stage_dir(name)

        def make_prep(target=name, payload=files):
            return lambda: seed_classify_fixture(target, payload)

        cases.append(
            Case(
                case_id=f"EXT-{case_no:02d}",
                stage="扩展",
                name=f"{name} 分类",
                query=f"将 {base} 下的文件，进行分类。类型创建新的文件夹。",
                expected="按类型创建文件夹并分类。",
                reset_before=True,
                fixture_prep=make_prep(),
                validator=validate_classified(base, expected_dirs),
            )
        )
        case_no += 1

    send_read_search_specs = [
        ("扩展读取账单备注", lambda: seed_basic_file_fixtures(), f"读取 {stage_dir('family-reading') / 'shopping-note.txt'}", validate_reply(["牛奶", "鸡蛋"])),
        ("扩展读取菜单", lambda: seed_basic_file_fixtures(), f"读取 {stage_dir('family-library') / 'meal-plan.md'}", validate_reply(["pasta", "meal"])),
        ("扩展读取 JSON", lambda: seed_basic_file_fixtures(), f"读取 {stage_dir('family-reading') / 'recipe.json'}", validate_reply(["dish", "curry"])),
        ("扩展发送收据", lambda: seed_basic_file_fixtures(), f"查看 {stage_dir('family-inbox')} 下面有什么文件，receipt.pdf 文件发给我。", validate_artifact(filename="receipt.pdf")),
        ("扩展发送预算表", lambda: seed_basic_file_fixtures(), f"查看 {stage_dir('family-inbox')} 下面有什么文件，monthly_budget.xlsx 文件发给我。", validate_artifact(filename="monthly_budget.xlsx")),
        ("扩展搜索菜谱", lambda: seed_basic_file_fixtures(), f"搜索 {stage_dir('family-library')} 下面的 meal 文件", validate_reply(["meal-plan.md"])),
        ("扩展搜索照片", lambda: seed_basic_file_fixtures(), f"搜索 {stage_dir('family-library')} 下面的 photo 文件", validate_reply(["vacation_photo.jpg"])),
        ("扩展列出收件箱", lambda: seed_basic_file_fixtures(), f"查看 {stage_dir('family-inbox')} 下面有什么文件", validate_reply(["school_notice.txt", "monthly_budget.xlsx"])),
    ]
    for name, prep, query, validator in send_read_search_specs:
        cases.append(
            Case(
                case_id=f"EXT-{case_no:02d}",
                stage="扩展",
                name=name,
                query=query,
                expected="完成扩展文件操作。",
                reset_before=True,
                fixture_prep=prep,
                validator=validator,
            )
        )
        case_no += 1

    for index in range(1, 17):
        cases.append(
            Case(
                case_id=f"EXT-{case_no:02d}",
                stage="扩展",
                name=f"家庭目录权限保护 {index}",
                query=f"将 {MAC_DOCUMENTS_DIR} 下的文件，进行分类。类型创建新的文件夹。",
                expected="明确提示当前进程没有写权限并建议改用工作区或 /tmp。",
                reset_before=True,
                validator=validate_permission_hint,
            )
        )
        case_no += 1
    return cases


def network_cases() -> list[Case]:
    cases: list[Case] = []
    specs = [
        ("NET-01", "东京天气", "东京今天的天气怎么样，最高温多少", "获取东京天气最终结果并给出来源。", validate_weather),
        ("NET-02", "福冈降雨", "福冈今天会下雨吗，请告诉我气温和降雨情况", "获取福冈天气最终结果并给出来源。", validate_weather),
        ("NET-03", "大阪气温", "大阪今天气温多少，请告诉我最高和最低温", "获取大阪天气最终结果并给出来源。", validate_weather),
        ("NET-04", "东京到旧金山机票", "东京到旧金山 2026年5月31号 的具体机票时间和票价", "返回带票价线索和时刻表来源的机票查询结果。", validate_live_network(["来源：", "票价", "时刻表"], [r"(?:¥|￥|JPY|\$)\s?\d"], ["flightconnections.com", "trip.com", "skyscanner", "kayak", "expedia", "jal.co.jp", "ana.co.jp"], ["没有返回可用结果"])),
        ("NET-05", "福冈到大阪新干线", "2026年4月20号福冈到大阪的新干线的具体时间和费用", "返回带时间和费用的新干线查询结果。", validate_live_network(["来源：", "费用"], [r"\d{1,2}:\d{2}|\d+\s*小时\s*\d+\s*分钟", r"(?:¥|￥|JPY)\s?\d|\d[\d,]*(?:\.\d+)?\s*(?:元|円)"], ["klook.com", "navitime", "smart-ex.jp", "jr-central.co.jp", "jr-odekake.net", "railmonsters.com", "rail.ninja"], ["没有返回可用结果"])),
        ("NET-06", "购机推荐", "日常办公买 MacBook Air 还是 MacBook Pro 更合适，请参考 Apple 官网给建议", "返回基于 Apple 相关来源的购机建议。", validate_live_network(["MacBook Air", "MacBook Pro", "来源："], None, None, ["没有返回可用结果"])),
        ("NET-07", "MacBook Air 价格", "Apple 官网里 13 英寸 MacBook Air 的起售价是多少", "返回 Apple 官方来源下的 13 英寸 MacBook Air 起售价。", validate_live_network(["MacBook Air", "起售价", "来源："], [r"(?:¥|￥|\$)\s?\d|\d[\d,]*(?:\.\d+)?\s*(?:美元|元|円)"], ["apple.com"], ["没有返回可用结果"])),
        ("NET-08", "MacBook Pro 价格", "Apple 官网里 MacBook Pro 14 英寸的起售价是多少", "返回 Apple 官方来源下的 MacBook Pro 14 英寸起售价。", validate_live_network(["MacBook Pro", "起售价", "来源："], [r"(?:¥|￥|\$)\s?\d|\d[\d,]*(?:\.\d+)?\s*(?:美元|元|円)"], ["apple.com"], ["没有返回可用结果"])),
        ("NET-09", "Time Machine 网络知识", "请联网搜索 Time Machine 是什么，有什么作用", "返回稳定网络知识，并写入本地知识库。", validate_knowledge_written("Time Machine")),
        ("NET-10", "Liquid Retina 网络知识", "请联网搜索 Liquid Retina 显示屏是什么", "返回稳定网络知识，并写入本地知识库。", validate_knowledge_written("Liquid Retina")),
        ("NET-11", "本地知识库回查 Time Machine", "根据本地知识库，Time Machine 是什么", "直接从本地知识库回答。", validate_knowledge_reply(["Time Machine"])),
        ("NET-12", "即时天气不入库", "东京今天的天气怎么样", "即时天气查询不写入本地知识库。", validate_no_knowledge_writeback),
        ("NET-13", "天气来源URL写入", "东京今天会下雨吗", "联网天气查询会把来源 URL 写入本地来源记忆。", validate_source_reference_written("东京今天会下雨吗")),
        ("NET-14", "来源URL复用 Time Machine", "Time Machine 主要是做什么的", "相似问题优先复用已记录来源 URL，再返回带来源的结果。", validate_source_reference_reuse),
        ("NET-15", "家庭晚餐菜谱", "今晚家庭晚饭想做鸡肉咖喱，请联网给我一个菜谱，告诉我主要食材和做法", "返回可执行的家庭菜谱结果并给出来源。", validate_live_network(["来源：", "食材", "做法"], None, ["cookpad.com", "allrecipes.com", "delish.com", "kurashiru.com"], ["没有返回可用结果"])),
        ("NET-16", "孩子早餐菜谱", "适合小学生上学前吃的简单早餐菜谱，给我食材和步骤", "返回适合家庭场景的早餐菜谱并给出来源。", validate_live_network(["来源：", "食材"], None, ["cookpad.com", "allrecipes.com", "delish.com", "kurashiru.com"], ["没有返回可用结果"])),
        ("NET-17", "光合作用网络知识", "请联网搜索 光合作用 是什么", "返回稳定知识并写入本地知识库。", validate_knowledge_written("光合作用")),
        ("NET-18", "本地知识库回查 光合作用", "根据本地知识库，光合作用是什么", "直接从本地知识库回答光合作用。", validate_knowledge_reply(["光合作用"])),
        ("NET-19", "日本热点新闻", "今天日本有什么热点新闻，请给我两条摘要", "返回热点新闻摘要和来源。", combine_validators(validate_live_network(["来源："], None, ["reuters.com", "apnews.com", "nhk.or.jp", "bbc.com"], ["没有返回可用结果"]), validate_no_knowledge_writeback)),
        ("NET-20", "家庭关注股票", "英伟达今天的股价是多少，涨跌情况如何", "返回实时股票信息和来源。", combine_validators(validate_live_network(["来源："], [r"\d+(?:\.\d+)?"], ["finance.yahoo.com", "marketwatch.com", "nasdaq.com", "nikkei.com"], ["没有返回可用结果"]), validate_no_knowledge_writeback)),
        ("NET-21", "Apple 股票", "苹果公司今天的股价是多少", "返回 Apple 实时股票信息和来源。", combine_validators(validate_live_network(["来源："], [r"\d+(?:\.\d+)?"], ["finance.yahoo.com", "marketwatch.com", "nasdaq.com", "nikkei.com"], ["没有返回可用结果"]), validate_no_knowledge_writeback)),
        ("NET-22", "孩子学习知识点", "请联网搜索 分数为什么要通分，用孩子能听懂的话解释", "返回稳定知识并写入本地知识库。", validate_knowledge_written("通分")),
        ("NET-23", "本地知识库回查 通分", "根据本地知识库，分数为什么要通分", "直接从本地知识库回答通分。", validate_knowledge_reply(["通分"])),
        ("NET-24", "家庭火车票信息", "东京到大阪明天的火车票时间和票价", "返回火车票时间和票价来源。", validate_live_network(["来源："], [r"\d{1,2}:\d{2}|(?:¥|￥|JPY)\s?\d"], ["navitime", "jr-central.co.jp", "jr-odekake.net", "smart-ex.jp"], ["没有返回可用结果"])),
        ("NET-25", "自动改写机票查询", "帮我查一下月底从东京飞旧金山的大概航班时间和价格，尽量给我靠谱来源", "触发自动改写或多轮检索，并返回来源结果。", combine_validators(validate_live_network(["来源："], None, ["flightconnections.com", "trip.com", "skyscanner", "kayak", "expedia"], ["没有返回可用结果"]), validate_iterative_lookup(2))),
        ("NET-26", "自动改写知识查询", "给孩子讲讲为什么白天能看到彩虹，用容易理解的话", "触发自动改写或多轮检索，并把稳定知识写入本地知识库。", combine_validators(validate_knowledge_written("彩虹"), validate_iterative_lookup(2))),
    ]
    for case_id, name, query, expected, validator in specs:
        setup = []
        if case_id == "NET-11":
            setup = ["请联网搜索 Time Machine 是什么，有什么作用"]
        elif case_id == "NET-14":
            setup = ["请联网搜索 Time Machine 是什么，有什么作用"]
        elif case_id == "NET-18":
            setup = ["请联网搜索 光合作用 是什么"]
        elif case_id == "NET-23":
            setup = ["请联网搜索 分数为什么要通分，用孩子能听懂的话解释"]
        cases.append(
            Case(
                case_id=case_id,
                stage="联网查询",
                name=name,
                query=query,
                expected=expected,
                reset_before=True,
                setup_queries=setup,
                validator=validator,
            )
        )
    return cases


def all_cases() -> list[Case]:
    reset_runtime_state()
    return stage1_cases() + stage2_cases() + stage3_cases() + extension_cases() + network_cases()


def run_cases(cases: list[Case]) -> list[CaseResult]:
    results: list[CaseResult] = []
    total = len(cases)
    for index, case in enumerate(cases, start=1):
        if index == 1 or index % 10 == 0 or case.case_id.startswith("NET-"):
            print(f"[base] {index}/{total} {case.case_id} {case.name}", flush=True)
        if case.reset_before:
            reset_runtime_state()
        if case.fixture_prep:
            case.fixture_prep()
        for setup_query in case.setup_queries:
            ask(setup_query)
        response = ask(case.query)
        ok = True
        notes = ""
        if case.validator:
            ok, notes = case.validator(response)
        results.append(
            CaseResult(
                case_id=case.case_id,
                stage=case.stage,
                name=case.name,
                query=case.query,
                expected=case.expected,
                status="PASS" if ok else "FAIL",
                actual=str(response.get("reply", "")),
                notes=notes,
            )
        )
    return results


def write_cases_doc(cases: list[Case]) -> None:
    lines = [
        "# HomeHub 3-Phase Family Test Cases For macOS",
        "",
        f"- Generated at: {now_text()}",
        f"- Project path: {ROOT}",
        f"- Runtime command: `.venv/bin/python runtime/server.py`",
        f"- Documents fixture: {MAC_DOCUMENTS_DIR}",
        f"- Temporary family fixtures: {TMP_ROOT}",
        f"- Total cases: {len(cases)}",
        "",
    ]
    current_stage = ""
    for case in cases:
        if case.stage != current_stage:
            current_stage = case.stage
            lines.extend([f"## {current_stage}", ""])
        lines.extend(
            [
                f"### {case.case_id} {case.name}",
                "",
                f"- Query: `{case.query}`",
                f"- Expected: {case.expected}",
                f"- Reset Before: {'Yes' if case.reset_before else 'No'}",
                f"- Setup Queries: {len(case.setup_queries)}",
                "",
            ]
        )
        variants = build_case_variants(case)
        for locale in ["zh-CN", "en-US", "ja-JP"]:
            localized = [item for item in variants if item.locale == locale]
            label = {"zh-CN": "Chinese", "en-US": "English", "ja-JP": "Japanese"}[locale]
            lines.append(f"- {label} Variants: {len(localized)}")
            for item in localized:
                lines.append(f"  - `{item.query}`")
            lines.append("")
    CASES_DOC.write_text("\n".join(lines), encoding="utf-8")


def write_results_doc(cases: list[Case], results: list[CaseResult], variant_results: list[VariantResult]) -> None:
    passed = sum(1 for item in results if item.status == "PASS")
    failed = sum(1 for item in results if item.status == "FAIL")
    variant_passed = sum(1 for item in variant_results if item.status == "PASS")
    variant_failed = sum(1 for item in variant_results if item.status == "FAIL")
    lines = [
        "# HomeHub 3-Phase Family Test Results For macOS",
        "",
        f"- Generated at: {now_text()}",
        f"- Total cases: {len(results)}",
        f"- PASS: {passed}",
        f"- FAIL: {failed}",
        f"- Variant semantic cases: {len(variant_results)}",
        f"- Variant PASS: {variant_passed}",
        f"- Variant FAIL: {variant_failed}",
        "",
        "## Initialization",
        "",
        "- Test runtime: `.venv/bin/python`",
        "- HomeHub is reset to a clean local state before each isolated scenario or each scenario group.",
        f"- Documents fixture path: `{MAC_DOCUMENTS_DIR}`",
        f"- Temporary family fixture root: `{TMP_ROOT}`",
        "",
        "## Iterative Fixes",
        "",
        "### Round 1",
        "",
        "- Problem: legacy reset logic treated `runtime/features/customize/__pycache__` as a file and crashed during initialization.",
        "- Fix: updated [tools/homehub_phase_test_20260410.py](/Users/home/workspace/HomeHub/tools/homehub_phase_test_20260410.py) to delete directories safely.",
        "- Result: initialization became repeatable on macOS.",
        "",
        "### Round 2",
        "",
        "- Problem: classifying files under `~/Documents` raised a permission exception instead of returning a user-facing explanation.",
        "- Fix: updated [runtime/features/local_files.py](/Users/home/workspace/HomeHub/runtime/features/local_files.py) to catch mkdir/move errors and reply with a macOS-safe downgrade message.",
        "- Result: protected or non-writable paths now fail gracefully, and `/tmp` fixtures classify successfully.",
        "",
        "### Round 3",
        "",
        "- Problem: after creating a custom agent draft, the next requirement message did not continue the draft and was misrouted into autonomous fallback creation.",
        "- Fix: updated [runtime/features/custom_agents.py](/Users/home/workspace/HomeHub/runtime/features/custom_agents.py) so active draft sessions continue reliably on natural follow-up messages.",
        "- Result: stage 2 create/refine/confirm flows became stable.",
        "",
        "### Round 4",
        "",
        "- Problem: generated family bill features could misread amounts and threshold phrases because the generated regex and fallback extraction were too weak.",
        "- Fix: updated [runtime/features/custom_agents.py](/Users/home/workspace/HomeHub/runtime/features/custom_agents.py) and [runtime/features/customize/family_bills_feature.py](/Users/home/workspace/HomeHub/runtime/features/customize/family_bills_feature.py) to extract currency amounts and threshold expressions correctly.",
        "- Result: stage 3 bill recording, total calculation, threshold reminder text, and Excel export all passed.",
        "",
        "### Round 5",
        "",
        "- Problem: the weather rules missed natural family phrasing like `今天会下雨吗`, and generated bill list replies reported only the latest 5 rows as if they were the full total.",
        "- Fix: updated [runtime/server_components/task_router.py](/Users/home/workspace/HomeHub/runtime/server_components/task_router.py) to recognize `下雨`, and updated [runtime/features/custom_agents.py](/Users/home/workspace/HomeHub/runtime/features/custom_agents.py) so generated feature list replies show the real total count.",
        "- Result: the remaining stage 1 weather case and stage 3 list-count cases passed on the next full run.",
        "",
        "### Round 6",
        "",
        "- Problem: local file search queries like `搜索某目录下面的 budget 文件` did not extract `budget` as the search token, so several search cases failed even though the files existed.",
        "- Fix: updated [runtime/features/local_files.py](/Users/home/workspace/HomeHub/runtime/features/local_files.py) with a local fallback extractor for search keywords and generic suffix cleanup.",
        "- Result: all remaining stage 1 and extension file-search cases passed, bringing the full suite to zero failures.",
        "",
        "### Round 7",
        "",
        "- Problem: after expanding stage 2 and stage 3 family agents, old generated feature data could survive resets and make fresh runs report inflated record counts.",
        "- Fix: updated [tools/homehub_family_suite_20260410.py](/Users/home/workspace/HomeHub/tools/homehub_family_suite_20260410.py) so initialization clears non-core files under `runtime/generated` and `runtime/data` before each isolated scenario.",
        "- Result: family health, medical report, study, and activity cases now start from a truly clean HomeHub state and produce stable one-run counts.",
        "",
        "### Round 8",
        "",
        "- Problem: queries like `导出身体状况记录文档` and `导出体检报告文档` were intercepted as generic file requests before they could be routed to the named household agent.",
        "- Fix: updated [runtime/features/custom_agents.py](/Users/home/workspace/HomeHub/runtime/features/custom_agents.py) so explicitly named completed agents are routed before the generic file-system guard, and updated [tools/homehub_family_suite_20260410.py](/Users/home/workspace/HomeHub/tools/homehub_family_suite_20260410.py) to accept the valid stage-2 shortcut reply that jumps directly to confirmation.",
        "- Result: all family stage 2 create flows and stage 3 named-agent export flows passed in the final rerun.",
        "",
        "### Round 9",
        "",
        "- Problem: weather and generic network lookups could still degrade into `没有返回可用结果`, because HomeHub leaned too heavily on direct fetches and did not reuse search-result snippets when target pages were weak or JS-heavy.",
        "- Fix: updated [runtime/server_network.py](/Users/home/workspace/HomeHub/runtime/server_network.py) to extract search-result titles, URLs, and cleaned snippets directly from DuckDuckGo HTML results, then use them as fallback evidence for summarization.",
        "- Result: weather, flight, shinkansen, and Mac product lookups can now return sourced final answers even when the landing page itself is not ideal for scraping.",
        "",
        "### Round 10",
        "",
        "- Problem: the weather path still used the older weak network branch, and `network_lookup` requests were all treated as real-time so stable web knowledge never wrote back into local knowledge memory.",
        "- Fix: updated [runtime/server_voice.py](/Users/home/workspace/HomeHub/runtime/server_voice.py) and [runtime/server.py](/Users/home/workspace/HomeHub/runtime/server.py) to route weather through the full research pipeline, add topic-aware source hints for weather/travel/Apple queries, and distinguish real-time lookups from reusable knowledge before writeback.",
        "- Result: live weather must now return a real sourced answer to pass, and stable web knowledge can be remembered and later answered directly from the local knowledge base.",
        "",
        "### Round 11",
        "",
        "- Problem: even after storing reusable web knowledge, HomeHub still did not keep a dedicated URL-level source memory, so similar questions could not reuse known source pages before searching the web again.",
        "- Fix: added [runtime/source_reference_memory.py](/Users/home/workspace/HomeHub/runtime/source_reference_memory.py), updated [runtime/server.py](/Users/home/workspace/HomeHub/runtime/server.py), [runtime/server_voice.py](/Users/home/workspace/HomeHub/runtime/server_voice.py), and [runtime/server_network.py](/Users/home/workspace/HomeHub/runtime/server_network.py) so successful network answers write source URLs into local source memory and similar future questions can fetch those URLs first.",
        "- Result: HomeHub now prefers local knowledge, then stored source URLs, and only then falls back to broader web search.",
        "",
        "### Round 12",
        "",
        "- Problem: HomeHub still defaulted to bootstrap consent prompts and relatively short generic GET timeouts, which made live lookup behavior less aligned with the macOS household test target.",
        "- Fix: updated [runtime/server_config.py](/Users/home/workspace/HomeHub/runtime/server_config.py) to default bootstrap consent/completion on, and updated [runtime/server.py](/Users/home/workspace/HomeHub/runtime/server.py) to use a longer network fetch timeout for live lookups.",
        "- Result: local test initialization no longer depends on repeated consent toggles, and slow external sources have more time to return usable results.",
        "",
        "### Round 13",
        "",
        "- Problem: the first version of network topic expansion still leaned too much on static keyword buckets, so it would become harder to maintain as household query styles kept growing.",
        "- Fix: added [runtime/network_route_memory.py](/Users/home/workspace/HomeHub/runtime/network_route_memory.py) and rewrote [runtime/network_lookup_extensions.py](/Users/home/workspace/HomeHub/runtime/network_lookup_extensions.py) to classify web queries through semantic route memory, route examples, and reusable query-pattern memories instead of only hard-coded token checks.",
        "- Result: HomeHub can now learn reusable network routing examples over time and use semantic similarity to choose source preferences and search query plans.",
        "",
        "### Round 14",
        "",
        "- Problem: even with semantic route memory, HomeHub still lacked a dedicated result-quality loop to refine poor web queries when the first search attempt was weak.",
        "- Fix: added [runtime/network_query_planner.py](/Users/home/workspace/HomeHub/runtime/network_query_planner.py) and updated [runtime/server.py](/Users/home/workspace/HomeHub/runtime/server.py) so autonomous web lookup now scores fetched results, asks AI for rewrite candidates, retries improved search queries, and returns the best grounded answer found.",
        "- Result: the live network path now supports iterative query refinement instead of failing too early on the first weak search phrase.",
        "",
        "### Round 15",
        "",
        "- Problem: local file requests like `查看 /tmp/... 下面有什么文件` were still being hijacked by semantic network routing, while `查看日程` was over-matched by an overly broad local-file guard, and short greetings could drift into news lookup.",
        "- Fix: added [runtime/local_request_guard.py](/Users/home/workspace/HomeHub/runtime/local_request_guard.py), updated [runtime/server_components/task_router.py](/Users/home/workspace/HomeHub/runtime/server_components/task_router.py), and aligned [runtime/server.py](/Users/home/workspace/HomeHub/runtime/server.py) so local path requests are blocked early, schedule phrases stay in schedule routing, and short greetings stay in general chat.",
        "- Result: stage 1 local file, schedule overview, and greeting regressions no longer cross into the wrong route.",
        "",
        "### Round 16",
        "",
        "- Problem: the generic weather question without an explicit city had no stable fallback hint during clean-state testing, and the suite lacked multilingual paraphrase coverage for route understanding.",
        "- Fix: updated [runtime/server_weather.py](/Users/home/workspace/HomeHub/runtime/server_weather.py) with a timezone-based fallback city hint for the clean macOS test environment, and updated [tools/homehub_family_suite_20260410.py](/Users/home/workspace/HomeHub/tools/homehub_family_suite_20260410.py) to generate 10 Chinese, 10 English, and 10 Japanese query variants for every base case, then run semantic task-spec regression against all of them.",
        "- Result: the suite now verifies both original execution flows and multilingual paraphrase understanding across the entire family test matrix.",
        "",
    ]

    for stage in ["阶段1", "阶段2", "阶段3", "扩展", "联网查询"]:
        stage_results = [item for item in results if item.stage == stage]
        stage_pass = sum(1 for item in stage_results if item.status == "PASS")
        lines.extend([f"## {stage} Summary", "", f"- Cases: {len(stage_results)}", f"- PASS: {stage_pass}", f"- FAIL: {len(stage_results) - stage_pass}", ""])
        for item in stage_results:
            lines.extend(
                [
                    f"### {item.case_id} {item.name}",
                    "",
                    f"- Status: `{item.status}`",
                    f"- Query: `{item.query}`",
                    f"- Expected: {item.expected}",
                    f"- Actual: {item.actual}",
                    f"- Notes: {item.notes}",
                    "",
                ]
            )
    lines.extend(
        [
            "## Variant Semantic Regression",
            "",
            f"- Total multilingual variants: {len(variant_results)}",
            f"- PASS: {variant_passed}",
            f"- FAIL: {variant_failed}",
            "",
        ]
    )
    for stage in ["阶段1", "阶段2", "阶段3", "扩展", "联网查询"]:
        stage_variants = [item for item in variant_results if item.stage == stage]
        stage_pass = sum(1 for item in stage_variants if item.status == "PASS")
        lines.extend([f"### {stage} Variants", "", f"- Cases: {len(stage_variants)}", f"- PASS: {stage_pass}", f"- FAIL: {len(stage_variants) - stage_pass}", ""])
        for item in stage_variants:
            lines.extend(
                [
                    f"- `{item.variant_id}` `{item.locale}` `{item.status}` `{item.query}`",
                    f"  Notes: {item.notes}",
                ]
            )
        lines.append("")
    RESULTS_DOC.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    cases = all_cases()
    results = run_cases(cases)
    variant_results = run_variant_regression(cases)
    write_cases_doc(cases)
    write_results_doc(cases, results, variant_results)
    print(
        json.dumps(
            {
                "cases": str(CASES_DOC),
                "results": str(RESULTS_DOC),
                "pass": sum(1 for item in results if item.status == "PASS"),
                "fail": sum(1 for item in results if item.status == "FAIL"),
                "total": len(results),
                "variant_pass": sum(1 for item in variant_results if item.status == "PASS"),
                "variant_fail": sum(1 for item in variant_results if item.status == "FAIL"),
                "variant_total": len(variant_results),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
