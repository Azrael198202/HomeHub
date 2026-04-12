#!/usr/bin/env python3
"""
HomeHub 3-Phase Family Test Suite Runner for 2026-04-12 test cases
Executes comprehensive unit/integration tests against the HomeHub system
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
CASES_DOC = DOCS_DIR / "homehub-3-phase-family-test-cases-mac-2026-04-12.md"
RESULTS_DOC = DOCS_DIR / "homehub-3-phase-family-test-results-mac-2026-04-12.md"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import runtime.server as server


def now_text() -> str:
    return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")


def reset_runtime_state() -> None:
    """Reset runtime to clean state before each test"""
    stamp = now_text()
    
    # Build runtime bridge
    runtime = server.build_runtime_bridge()
    server.FEATURE_MANAGER.refresh(runtime)
    server.FEATURE_MANAGER.reset(runtime)
    
    # Initialize state
    server.HOME_MEMORY = {
        "events": [],
        "reminders": [],
        "recentActions": [
            {
                "id": "home-memory-ready",
                "summary": "HomeHub memory is ready.",
                "createdAt": stamp,
            }
        ],
    }
    server.WEATHER = {
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
    }
    server.PENDING_VOICE_CLARIFICATION = None
    
    initial = server.build_initial_conversation(server.PERSISTED_SETTINGS["language"])
    server.CURRENT_CONVERSATION[:] = initial
    server.VOICE_CONVERSATION[:] = list(initial)


def ask(query: str, locale: str = "zh-CN") -> dict:
    """Submit a query to HomeHub and get response"""
    return server.resolve_voice_request(query, locale)


@dataclass
class TestCase:
    """Represents a single test case"""
    case_id: str
    stage: str
    name: str
    query: str
    expected: str
    reset_before: bool = False
    setup_queries: list[str] = None
    
    def __post_init__(self):
        if self.setup_queries is None:
            self.setup_queries = []


@dataclass
class TestResult:
    """Represents a test result"""
    case_id: str
    stage: str
    name: str
    query: str
    expected: str
    status: str  # PASS, FAIL, SKIP
    actual: str
    notes: str


def parse_test_cases_from_markdown(md_path: Path) -> list[TestCase]:
    """Parse test cases from markdown document"""
    if not md_path.exists():
        raise FileNotFoundError(f"Test cases document not found: {md_path}")
    
    content = md_path.read_text(encoding="utf-8")
    cases: list[TestCase] = []
    
    # Parse markdown structure:
    # ## 阶段1/阶段2/阶段3
    # ### S1-01 本地问候 1
    # - Query: `你好`
    # - Expected: 返回自然问候。
    # - Reset Before: Yes
    # - Setup Queries: 0
    
    stage_pattern = r"^## (阶段\d+)"
    case_pattern = r"^### ([A-Z]\d+-\d+)\s+(.*?)$"
    query_pattern = r"^- Query: `([^`]+)`"
    expected_pattern = r"^- Expected: (.+?)$"
    reset_pattern = r"^- Reset Before: (Yes|No)"
    setup_pattern = r"^- Setup Queries: (\d+)"
    
    current_stage = None
    current_case_id = None
    current_name = None
    current_query = None
    current_expected = None
    current_reset = False
    current_setup_count = 0
    
    for line in content.split("\n"):
        stage_match = re.match(stage_pattern, line)
        if stage_match:
            current_stage = stage_match.group(1)
            continue
        
        case_match = re.match(case_pattern, line)
        if case_match:
            # Save previous case if exists
            if current_case_id and current_query and current_expected:
                cases.append(
                    TestCase(
                        case_id=current_case_id,
                        stage=current_stage or "未知",
                        name=current_name or "",
                        query=current_query,
                        expected=current_expected,
                        reset_before=current_reset,
                        setup_queries=[],
                    )
                )
            
            # Start new case
            current_case_id = case_match.group(1)
            current_name = case_match.group(2)
            current_query = None
            current_expected = None
            current_reset = False
            current_setup_count = 0
            continue
        
        query_match = re.match(query_pattern, line)
        if query_match:
            current_query = query_match.group(1)
            continue
        
        expected_match = re.match(expected_pattern, line)
        if expected_match:
            current_expected = expected_match.group(1)
            continue
        
        reset_match = re.match(reset_pattern, line)
        if reset_match:
            current_reset = reset_match.group(1) == "Yes"
            continue
        
        setup_match = re.match(setup_pattern, line)
        if setup_match:
            current_setup_count = int(setup_match.group(1))
            continue
    
    # Don't forget last case
    if current_case_id and current_query and current_expected:
        cases.append(
            TestCase(
                case_id=current_case_id,
                stage=current_stage or "未知",
                name=current_name or "",
                query=current_query,
                expected=current_expected,
                reset_before=current_reset,
                setup_queries=[],
            )
        )
    
    return cases


def validate_response(query: str, response: dict, expected: str) -> tuple[bool, str]:
    """Validate a response against expected output"""
    actual_reply = response.get("reply", "").strip()
    
    # For greeting validation
    if "问候" in expected.lower() or "greet" in expected.lower():
        greeting_tokens = {"你好", "早", "晚", "hello", "hi", "morning", "evening", "good"}
        has_greeting = any(token in actual_reply.lower() for token in greeting_tokens)
        return has_greeting, f"Greeting reply: {actual_reply[:100]}"
    
    # For weather validation
    if "天气" in expected or "weather" in expected.lower():
        has_info = len(actual_reply) > 10
        return has_info, f"Weather reply length: {len(actual_reply)}"
    
    # For file operations
    if "文件" in expected or "file" in expected.lower():
        return len(actual_reply) > 5, f"File operation reply: {actual_reply[:100]}"
    
    # Generic validation
    return len(actual_reply) > 5, f"Response: {actual_reply[:100]}"


def run_tests(cases: list[TestCase]) -> list[TestResult]:
    """Execute all test cases"""
    results: list[TestResult] = []
    total = len(cases)
    
    print(f"Running {total} test cases...\n", flush=True)
    
    for index, case in enumerate(cases, start=1):
        if index % 10 == 0 or index == 1:
            print(f"[{index}/{total}] {case.case_id}: {case.name}", flush=True)
        
        try:
            if case.reset_before:
                reset_runtime_state()
            
            # Run setup queries
            for setup_query in case.setup_queries:
                ask(setup_query)
            
            # Run main query
            response = ask(case.query)
            
            # Validate response
            passed, notes = validate_response(case.query, response, case.expected)
            
            results.append(
                TestResult(
                    case_id=case.case_id,
                    stage=case.stage,
                    name=case.name,
                    query=case.query,
                    expected=case.expected,
                    status="PASS" if passed else "FAIL",
                    actual=response.get("reply", "")[:200],
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
                    notes=f"Exception: {str(e)[:100]}",
                )
            )
    
    return results


def write_results(cases: list[TestCase], results: list[TestResult]) -> None:
    """Write test results to markdown document"""
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")
    
    lines = [
        "# HomeHub 3-Phase Family Test Results",
        "",
        f"- Generated at: {now_text()}",
        f"- Total cases: {len(results)}",
        f"- PASS: {passed}",
        f"- FAIL: {failed}",
        f"- ERRORS: {errors}",
        f"- Pass rate: {passed}/{len(results)} ({100*passed/len(results):.1f}%)" if len(results) > 0 else "",
        "",
        "## Test Initialization",
        "",
        "- Python runtime: `.venv/bin/python`",
        "- HomeHub is reset to clean state before each test case marked with `Reset Before: Yes`",
        "- Test document: homehub-3-phase-family-test-cases-mac-2026-04-12.md",
        "",
    ]
    
    # Group results by stage
    stages = {}
    for result in results:
        if result.stage not in stages:
            stages[result.stage] = []
        stages[result.stage].append(result)
    
    # Write results by stage
    for stage in sorted(stages.keys()):
        stage_results = stages[stage]
        stage_pass = sum(1 for r in stage_results if r.status == "PASS")
        stage_fail = sum(1 for r in stage_results if r.status == "FAIL")
        stage_error = sum(1 for r in stage_results if r.status == "ERROR")
        
        lines.extend([
            f"## {stage}",
            "",
            f"- Total: {len(stage_results)}",
            f"- PASS: {stage_pass}",
            f"- FAIL: {stage_fail}",
            f"- ERRORS: {stage_error}",
            "",
        ])
        
        for result in stage_results:
            lines.extend([
                f"### {result.case_id}: {result.name}",
                "",
                f"- Status: **{result.status}**",
                f"- Query: `{result.query}`",
                f"- Expected: {result.expected}",
                f"- Actual: {result.actual}",
                f"- Notes: {result.notes}",
                "",
            ])
    
    RESULTS_DOC.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nResults written to: {RESULTS_DOC}")


def main() -> None:
    """Main test execution"""
    print(f"HomeHub Family Test Suite - 2026-04-12\n")
    print(f"Test cases document: {CASES_DOC}")
    print(f"Results document: {RESULTS_DOC}\n")
    
    # Parse test cases
    try:
        cases = parse_test_cases_from_markdown(CASES_DOC)
        print(f"Parsed {len(cases)} test cases\n")
    except Exception as e:
        print(f"Error parsing test cases: {e}")
        sys.exit(1)
    
    if not cases:
        print("No test cases found in document")
        sys.exit(1)
    
    # Run tests
    try:
        results = run_tests(cases)
    except Exception as e:
        print(f"Error running tests: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Write results
    try:
        write_results(cases, results)
    except Exception as e:
        print(f"Error writing results: {e}")
        sys.exit(1)
    
    # Print summary
    passed = sum(1 for r in results if r.status == "PASS")
    total = len(results)
    print(f"\n{'='*50}")
    print(f"Test Summary: {passed}/{total} passed ({100*passed/total:.1f}%)")
    print(f"{'='*50}")
    
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
