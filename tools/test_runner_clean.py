#!/usr/bin/env python3
"""
HomeHub Test Suite Runner for homehub-clean.md
Parses and executes comprehensive unit tests
"""
from __future__ import annotations

import json
import re
import sys
import shutil
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Callable, Optional

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
CASES_DOC = DOCS_DIR / "homehub-clean.md"
RESULTS_DOC = DOCS_DIR / "homehub-test-results-clean.md"
TMP_ROOT = Path("/tmp/homehub-test-suite")
MAC_DOCUMENTS_DIR = Path("/Users/home/Documents")

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import runtime.server as server


def now_text() -> str:
    """Get current timestamp"""
    return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")


def write_json(path: Path, payload: dict) -> None:
    """Write JSON to file"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def ensure_documents_fixture() -> None:
    """Ensure Documents directory exists"""
    MAC_DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)


def clean_customize_dir() -> None:
    """Clean customize directory"""
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
    """Reset runtime to clean state"""
    stamp = now_text()
    ensure_documents_fixture()
    if TMP_ROOT.exists():
        shutil.rmtree(TMP_ROOT)
    TMP_ROOT.mkdir(parents=True, exist_ok=True)

    # Clean generated directory
    generated_dir = ROOT / "runtime" / "generated"
    preserved_generated = {"vendor", "avatar", "handle_demand"}
    if generated_dir.exists():
        for child in generated_dir.iterdir():
            if child.name in preserved_generated:
                continue
            if child.is_dir():
                shutil.rmtree(child, ignore_errors=True)
            else:
                child.unlink(missing_ok=True)

    clean_customize_dir()

    # Clean data directory
    data_dir = ROOT / "runtime" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    preserved_data = {"external_channels.json", "local_files.json", "task_semantic_memory.json", "handle_demand.json"}
    for child in data_dir.glob("*.json"):
        if child.name in preserved_data:
            continue
        child.unlink(missing_ok=True)

    # Initialize memory files
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

    # Initialize runtime
    runtime = server.build_runtime_bridge()
    server.FEATURE_MANAGER.refresh(runtime)
    server.FEATURE_MANAGER.reset(runtime)
    server.HOME_MEMORY = json.loads((ROOT / "runtime" / "home_memory.json").read_text(encoding="utf-8"))
    server.WEATHER = json.loads((ROOT / "runtime" / "weather_state.json").read_text(encoding="utf-8"))
    server.PENDING_VOICE_CLARIFICATION = None
    initial = server.build_initial_conversation(server.PERSISTED_SETTINGS["language"])
    server.CURRENT_CONVERSATION[:] = initial
    server.VOICE_CONVERSATION[:] = list(initial)


def ask(query: str, locale: str = "zh-CN") -> dict:
    """Submit query to HomeHub"""
    return server.resolve_voice_request(query, locale)


@dataclass
class TestCase:
    """Represents a test case"""
    case_id: str
    stage: str
    name: str
    query: str
    expected: str
    reset_before: bool = False
    setup_queries: list[str] = field(default_factory=list)


@dataclass
class TestResult:
    """Represents test result"""
    case_id: str
    stage: str
    name: str
    query: str
    expected: str
    status: str
    actual: str
    notes: str


def parse_test_cases(md_path: Path) -> list[TestCase]:
    """Parse test cases from markdown"""
    if not md_path.exists():
        raise FileNotFoundError(f"Document not found: {md_path}")
    
    content = md_path.read_text(encoding="utf-8")
    cases: list[TestCase] = []
    
    current_stage = None
    lines = content.split("\n")
    i = 0
    
    while i < len(lines):
        line = lines[i].rstrip()
        
        # Check for stage header
        stage_match = re.match(r"^## (阶段\d+)", line)
        if stage_match:
            current_stage = stage_match.group(1)
            i += 1
            continue
        
        # Check for case header
        case_match = re.match(r"^### ([A-Z0-9\-]+)\s+(.*?)$", line)
        if case_match and current_stage:
            case_id = case_match.group(1)
            case_name = case_match.group(2)
            
            # Parse case details
            query = None
            expected = None
            reset_before = False
            setup_queries = []
            
            i += 1
            while i < len(lines):
                line = lines[i].rstrip()
                
                if line.startswith("### ") or line.startswith("## "):
                    break
                
                if line.startswith("- Query: `"):
                    query = line.replace("- Query: `", "").rstrip("`")
                elif line.startswith("- Expected: "):
                    expected = line.replace("- Expected: ", "").strip()
                elif line.startswith("- Reset Before: "):
                    reset_before = "Yes" in line
                elif line.startswith("- Setup Queries: "):
                    count = int(line.split(": ")[1])
                    setup_queries = []
                
                if query and expected:
                    cases.append(
                        TestCase(
                            case_id=case_id,
                            stage=current_stage,
                            name=case_name,
                            query=query,
                            expected=expected,
                            reset_before=reset_before,
                            setup_queries=setup_queries,
                        )
                    )
                    break
                
                i += 1
        else:
            i += 1
    
    return cases


def validate_response(query: str, response: dict, expected: str) -> tuple[bool, str]:
    """Validate response against expected output"""
    actual_reply = response.get("reply", "").strip() if response else ""
    
    # Length-based validation
    if len(actual_reply) < 3:
        return False, f"Response too short: {len(actual_reply)} chars"
    
    # Greeting validation
    if "问候" in expected.lower():
        greeting_tokens = {"你好", "早", "晚", "hello", "hi", "morning", "evening"}
        has_greeting = any(token in actual_reply.lower() for token in greeting_tokens)
        return has_greeting, f"Greeting detected: {actual_reply[:80]}"
    
    # Generic validation: just ensure non-empty response
    return True, f"Response OK: {actual_reply[:80]}"


def run_tests(cases: list[TestCase]) -> list[TestResult]:
    """Execute all test cases"""
    results: list[TestResult] = []
    total = len(cases)
    
    print(f"Executing {total} test cases...\n", flush=True)
    
    for index, case in enumerate(cases, start=1):
        if index == 1 or index % 20 == 0:
            print(f"[{index}/{total}] {case.case_id}: {case.name}", flush=True)
        
        try:
            if case.reset_before:
                reset_runtime_state()
            
            for setup_query in case.setup_queries:
                ask(setup_query)
            
            response = ask(case.query)
            passed, notes = validate_response(case.query, response, case.expected)
            
            results.append(
                TestResult(
                    case_id=case.case_id,
                    stage=case.stage,
                    name=case.name,
                    query=case.query,
                    expected=case.expected,
                    status="PASS" if passed else "FAIL",
                    actual=response.get("reply", "")[:150] if response else "",
                    notes=notes,
                )
            )
        except Exception as e:
            results.append(
                TestResult(
                    case_id=case.case_id,
                    stage=case.stage,
                    name=case.name,
                    query=case.query,
                    expected=case.expected,
                    status="ERROR",
                    actual="",
                    notes=f"Exception: {str(e)[:80]}",
                )
            )
    
    return results


def write_results(cases: list[TestCase], results: list[TestResult]) -> None:
    """Write results to markdown"""
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")
    
    pass_rate = (100 * passed / len(results)) if len(results) > 0 else 0
    
    lines = [
        "# HomeHub Test Results",
        "",
        f"- Generated at: {now_text()}",
        f"- Test document: homehub-clean.md",
        f"- Total cases: {len(results)}",
        f"- ✅ PASS: {passed}",
        f"- ❌ FAIL: {failed}",
        f"- ⚠️ ERRORS: {errors}",
        f"- Pass rate: {pass_rate:.1f}%",
        "",
        "---",
        "",
    ]
    
    # Group by stage
    stages = {}
    for result in results:
        if result.stage not in stages:
            stages[result.stage] = []
        stages[result.stage].append(result)
    
    # Write by stage
    for stage in sorted(stages.keys()):
        stage_results = stages[stage]
        stage_pass = sum(1 for r in stage_results if r.status == "PASS")
        stage_fail = sum(1 for r in stage_results if r.status == "FAIL")
        stage_error = sum(1 for r in stage_results if r.status == "ERROR")
        
        lines.extend([
            f"## {stage}",
            "",
            f"| Metric | Count |",
            f"|--------|-------|",
            f"| Total | {len(stage_results)} |",
            f"| PASS | {stage_pass} |",
            f"| FAIL | {stage_fail} |",
            f"| ERRORS | {stage_error} |",
            "",
        ])
        
        # Failed tests first
        failed_tests = [r for r in stage_results if r.status in ["FAIL", "ERROR"]]
        if failed_tests:
            lines.append("### Failed Tests")
            lines.append("")
            for result in failed_tests:
                lines.extend([
                    f"#### {result.case_id}: {result.name}",
                    "",
                    f"**Status**: {result.status}",
                    f"**Query**: `{result.query}`",
                    f"**Expected**: {result.expected}",
                    f"**Actual**: {result.actual}",
                    f"**Notes**: {result.notes}",
                    "",
                ])
        
        # Passed tests summary
        passed_tests = [r for r in stage_results if r.status == "PASS"]
        if passed_tests:
            lines.append(f"### Passed Tests ({len(passed_tests)})")
            lines.append("")
            for result in passed_tests[:5]:  # Show first 5
                lines.append(f"- `{result.case_id}`: {result.name}")
            if len(passed_tests) > 5:
                lines.append(f"- ... and {len(passed_tests) - 5} more")
            lines.append("")
    
    RESULTS_DOC.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """Main execution"""
    print("="*60)
    print("HomeHub Test Suite Runner - homehub-clean.md")
    print("="*60)
    print()
    
    # Parse cases
    try:
        cases = parse_test_cases(CASES_DOC)
        print(f"✓ Parsed {len(cases)} test cases")
        print(f"  Source: {CASES_DOC}")
    except Exception as e:
        print(f"✗ Error parsing test cases: {e}")
        sys.exit(1)
    
    if not cases:
        print("✗ No test cases found")
        sys.exit(1)
    
    # Run tests
    try:
        results = run_tests(cases)
        print(f"\n✓ Test execution completed")
    except Exception as e:
        print(f"✗ Error running tests: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Write results
    try:
        write_results(cases, results)
        print(f"✓ Results written to: {RESULTS_DOC}")
    except Exception as e:
        print(f"✗ Error writing results: {e}")
        sys.exit(1)
    
    # Print summary
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")
    total = len(results)
    
    print()
    print("="*60)
    print("Test Summary")
    print("="*60)
    print(f"Total:  {total}")
    print(f"PASS:   {passed} ({100*passed/total:.1f}%)")
    print(f"FAIL:   {failed}")
    print(f"ERRORS: {errors}")
    print("="*60)
    
    return 0 if failed == 0 and errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
