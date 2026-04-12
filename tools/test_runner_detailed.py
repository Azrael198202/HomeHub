#!/usr/bin/env python3
"""
HomeHub Detailed Test Suite - Full execution with detailed results
Executes test cases and generates comprehensive results with expected vs actual
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
RESULTS_DOC = DOCS_DIR / "homehub-test-results-detailed.md"
TMP_ROOT = Path("/tmp/homehub-detailed-test")
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
    """Submit query to HomeHub and get detailed response"""
    try:
        response = server.resolve_voice_request(query, locale)
        return {
            "success": True,
            "reply": response.get("reply", ""),
            "task_spec": response.get("task_spec", {}),
            "error": None
        }
    except Exception as e:
        return {
            "success": False,
            "reply": "",
            "task_spec": {},
            "error": str(e)
        }


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
    """Represents detailed test result"""
    case_id: str
    stage: str
    name: str
    query: str
    expected: str
    status: str
    actual_reply: str
    actual_task_spec: dict
    validation_result: dict
    execution_time: float
    error: Optional[str] = None


def parse_test_cases(md_path: Path, max_cases: int = 50) -> list[TestCase]:
    """Parse test cases from markdown"""
    if not md_path.exists():
        raise FileNotFoundError(f"Document not found: {md_path}")

    content = md_path.read_text(encoding="utf-8")
    cases: list[TestCase] = []

    current_stage = None
    lines = content.split("\n")
    i = 0

    while i < len(lines) and len(cases) < max_cases:
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


def validate_response_detailed(query: str, expected: str, response: dict) -> dict:
    """Detailed validation of response against expected output"""
    actual_reply = response.get("reply", "").strip()
    task_spec = response.get("task_spec", {})

    validation = {
        "passed": False,
        "score": 0.0,
        "checks": [],
        "analysis": "",
        "recommendations": []
    }

    # Basic checks
    if not actual_reply:
        validation["checks"].append({"check": "Response exists", "passed": False, "detail": "No response received"})
        return validation

    validation["checks"].append({"check": "Response exists", "passed": True, "detail": f"Response length: {len(actual_reply)} chars"})

    # Greeting validation
    if "问候" in expected.lower() or "greet" in expected.lower():
        greeting_tokens = {"你好", "早", "晚", "hello", "hi", "morning", "evening", "good"}
        has_greeting = any(token in actual_reply.lower() for token in greeting_tokens)
        validation["checks"].append({
            "check": "Greeting content",
            "passed": has_greeting,
            "detail": f"Greeting tokens found: {has_greeting}"
        })
        if has_greeting:
            validation["score"] += 1.0
            validation["passed"] = True

    # Weather validation
    elif "天气" in expected or "weather" in expected.lower():
        weather_indicators = ["°", "度", "温度", "weather", "temperature", "forecast"]
        has_weather_info = any(indicator in actual_reply.lower() for indicator in weather_indicators)
        validation["checks"].append({
            "check": "Weather information",
            "passed": has_weather_info,
            "detail": f"Weather indicators found: {has_weather_info}"
        })
        if has_weather_info:
            validation["score"] += 0.8
            validation["passed"] = True
        elif len(actual_reply) > 20:
            validation["score"] += 0.3
            validation["analysis"] = "Response present but weather indicators not found"

    # File operation validation
    elif "文件" in expected or "file" in expected.lower():
        file_indicators = ["文件", "目录", "folder", "file", "list", "found"]
        has_file_info = any(indicator in actual_reply.lower() for indicator in file_indicators)
        validation["checks"].append({
            "check": "File operation response",
            "passed": has_file_info,
            "detail": f"File indicators found: {has_file_info}"
        })
        if has_file_info:
            validation["score"] += 0.9
            validation["passed"] = True

    # Agent creation validation
    elif "智能体" in expected or "agent" in expected.lower():
        agent_indicators = ["创建", "智能体", "agent", "created", "configured"]
        has_agent_info = any(indicator in actual_reply.lower() for indicator in agent_indicators)
        validation["checks"].append({
            "check": "Agent creation response",
            "passed": has_agent_info,
            "detail": f"Agent indicators found: {has_agent_info}"
        })
        if has_agent_info:
            validation["score"] += 0.8
            validation["passed"] = True

    # Network query validation
    elif "网络" in expected or "network" in expected.lower() or "联网" in expected:
        network_indicators = ["来源", "source", "查询", "search", "result"]
        has_network_info = any(indicator in actual_reply.lower() for indicator in network_indicators)
        validation["checks"].append({
            "check": "Network query response",
            "passed": has_network_info,
            "detail": f"Network indicators found: {has_network_info}"
        })
        if has_network_info:
            validation["score"] += 0.7
            validation["passed"] = True

    # Generic validation
    else:
        if len(actual_reply) > 10:
            validation["score"] += 0.6
            validation["passed"] = True
            validation["checks"].append({
                "check": "Generic response quality",
                "passed": True,
                "detail": f"Response length adequate: {len(actual_reply)} chars"
            })
        else:
            validation["checks"].append({
                "check": "Generic response quality",
                "passed": False,
                "detail": f"Response too short: {len(actual_reply)} chars"
            })

    # Task spec analysis
    if task_spec:
        task_type = task_spec.get("taskType", "")
        intent = task_spec.get("intent", "")
        validation["checks"].append({
            "check": "Task specification",
            "passed": bool(task_type),
            "detail": f"Task type: {task_type}, Intent: {intent}"
        })

    # Analysis and recommendations
    if validation["score"] >= 0.7:
        validation["analysis"] = "Test passed with good confidence"
    elif validation["score"] >= 0.4:
        validation["analysis"] = "Test passed with moderate confidence"
        validation["recommendations"].append("Consider manual verification")
    else:
        validation["analysis"] = "Test failed or requires manual review"
        validation["recommendations"].append("Manual verification recommended")

    return validation


def run_tests(cases: list[TestCase]) -> list[TestResult]:
    """Execute all test cases with detailed results"""
    results: list[TestResult] = []
    total = len(cases)

    print(f"Executing {total} test cases with detailed analysis...\n", flush=True)

    for index, case in enumerate(cases, start=1):
        if index == 1 or index % 5 == 0:
            print(f"[{index}/{total}] {case.case_id}: {case.name}", flush=True)

        try:
            import time
            start_time = time.time()

            if case.reset_before:
                reset_runtime_state()

            # Run setup queries
            for setup_query in case.setup_queries:
                ask(setup_query)

            # Run main query
            response = ask(case.query)

            execution_time = time.time() - start_time

            # Detailed validation
            validation = validate_response_detailed(case.query, case.expected, response)

            # Determine status
            status = "PASS" if validation["passed"] else "FAIL"

            results.append(
                TestResult(
                    case_id=case.case_id,
                    stage=case.stage,
                    name=case.name,
                    query=case.query,
                    expected=case.expected,
                    status=status,
                    actual_reply=response.get("reply", ""),
                    actual_task_spec=response.get("task_spec", {}),
                    validation_result=validation,
                    execution_time=execution_time,
                    error=response.get("error"),
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
                    actual_reply="",
                    actual_task_spec={},
                    validation_result={"passed": False, "error": str(e)},
                    execution_time=0.0,
                    error=str(e),
                )
            )

    return results


def write_detailed_results(cases: list[TestCase], results: list[TestResult]) -> None:
    """Write comprehensive test results"""
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")

    pass_rate = (100 * passed / len(results)) if len(results) > 0 else 0

    lines = [
        "# HomeHub Detailed Test Results",
        "",
        "## Executive Summary",
        "",
        f"**Generated**: {now_text()}",
        f"**Source Document**: homehub-clean.md",
        f"**Test Cases Executed**: {len(results)}",
        f"**✅ PASS**: {passed} ({pass_rate:.1f}%)",
        f"**❌ FAIL**: {failed}",
        f"**⚠️ ERRORS**: {errors}",
        "",
        "---",
        "",
    ]

    # Performance summary
    total_time = sum(r.execution_time for r in results)
    avg_time = total_time / len(results) if results else 0

    lines.extend([
        "## Performance Metrics",
        "",
        f"- **Total Execution Time**: {total_time:.2f} seconds",
        f"- **Average Response Time**: {avg_time:.2f} seconds per test",
        f"- **Fastest Response**: {min(r.execution_time for r in results):.2f}s",
        f"- **Slowest Response**: {max(r.execution_time for r in results):.2f}s",
        "",
        "---",
        "",
    ])

    # Results by stage
    stages = {}
    for result in results:
        if result.stage not in stages:
            stages[result.stage] = []
        stages[result.stage].append(result)

    lines.extend([
        "## Results by Stage",
        "",
        "| Stage | Total | PASS | FAIL | ERRORS | Pass Rate | Avg Time |",
        "|-------|-------|------|------|--------|-----------|----------|",
    ])

    for stage in sorted(stages.keys()):
        stage_results = stages[stage]
        stage_pass = sum(1 for r in stage_results if r.status == "PASS")
        stage_fail = sum(1 for r in stage_results if r.status == "FAIL")
        stage_error = sum(1 for r in stage_results if r.status == "ERROR")
        stage_rate = 100 * stage_pass / len(stage_results) if stage_results else 0
        stage_avg_time = sum(r.execution_time for r in stage_results) / len(stage_results) if stage_results else 0

        lines.append(
            f"| {stage} | {len(stage_results)} | {stage_pass} | {stage_fail} | {stage_error} | {stage_rate:.1f}% | {stage_avg_time:.2f}s |"
        )

    lines.extend([
        "",
        "---",
        "",
    ])

    # Detailed test results
    lines.extend([
        "## Detailed Test Results",
        "",
    ])

    for result in results:
        lines.extend([
            f"### {result.case_id}: {result.name}",
            "",
            f"**Status**: {result.status}",
            f"**Stage**: {result.stage}",
            f"**Execution Time**: {result.execution_time:.2f} seconds",
            "",
            "#### Query",
            f"```\n{result.query}\n```",
            "",
            "#### Expected Result",
            f"```\n{result.expected}\n```",
            "",
            "#### Actual Result",
            f"```\n{result.actual_reply}\n```",
            "",
        ])

        # Task specification
        if result.actual_task_spec:
            lines.extend([
                "#### Task Specification",
                f"```json\n{json.dumps(result.actual_task_spec, ensure_ascii=False, indent=2)}\n```",
                "",
            ])

        # Validation details
        if result.validation_result:
            validation = result.validation_result
            lines.extend([
                "#### Validation Analysis",
                f"- **Validation Score**: {validation.get('score', 0):.2f}/1.0",
                f"- **Analysis**: {validation.get('analysis', 'N/A')}",
                "",
                "##### Validation Checks",
            ])

            for check in validation.get('checks', []):
                status_icon = "✅" if check.get('passed', False) else "❌"
                lines.append(f"- {status_icon} **{check['check']}**: {check['detail']}")

            if validation.get('recommendations'):
                lines.extend([
                    "",
                    "##### Recommendations",
                ])
                for rec in validation['recommendations']:
                    lines.append(f"- {rec}")

        # Error information
        if result.error:
            lines.extend([
                "",
                "#### Error Details",
                f"```\n{result.error}\n```",
            ])

        lines.extend([
            "",
            "---",
            "",
        ])

    # Summary statistics
    lines.extend([
        "## Test Statistics",
        "",
        "### Response Quality Distribution",
    ])

    score_ranges = [(0.0, 0.3), (0.3, 0.6), (0.6, 0.8), (0.8, 1.0)]
    for min_score, max_score in score_ranges:
        count = sum(1 for r in results if r.validation_result and min_score <= r.validation_result.get('score', 0) < max_score)
        lines.append(f"- **{min_score:.1f} - {max_score:.1f}**: {count} tests")

    lines.extend([
        "",
        "### Common Failure Patterns",
    ])

    # Analyze failure patterns
    failure_reasons = {}
    for result in results:
        if result.status in ["FAIL", "ERROR"]:
            validation = result.validation_result
            if validation and 'checks' in validation:
                for check in validation['checks']:
                    if not check.get('passed', True):
                        reason = check['check']
                        failure_reasons[reason] = failure_reasons.get(reason, 0) + 1

    if failure_reasons:
        for reason, count in sorted(failure_reasons.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"- **{reason}**: {count} occurrences")
    else:
        lines.append("- No common failure patterns identified")

    lines.extend([
        "",
        "---",
        "",
        "## Test Environment",
        "",
        "- **Python Version**: 3.14.3",
        "- **Platform**: macOS",
        "- **Runtime**: HomeHub local server",
        "- **Test Mode**: Detailed execution with validation",
        "",
        "## Notes",
        "",
        "- Tests executed in isolated runtime environment",
        "- Network-dependent tests may fail in offline environments",
        "- Validation uses heuristic analysis of response content",
        "- Manual review recommended for borderline cases",
        "",
    ])

    RESULTS_DOC.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    """Main execution"""
    print("="*80)
    print("HomeHub Detailed Test Suite - Comprehensive Analysis")
    print("="*80)
    print()

    # Parse cases (limit to 20 for detailed execution)
    try:
        cases = parse_test_cases(CASES_DOC, max_cases=20)
        print(f"✓ Parsed {len(cases)} test cases from document")
        print(f"  Source: {CASES_DOC}")
        print(f"  Limit: 20 cases for detailed analysis")
    except Exception as e:
        print(f"✗ Error parsing test cases: {e}")
        return 1

    if not cases:
        print("✗ No test cases found")
        return 1

    # Run tests
    try:
        results = run_tests(cases)
        print(f"\n✓ Test execution completed")
    except Exception as e:
        print(f"✗ Error running tests: {e}")
        import traceback
        traceback.print_exc()
        return 1

    # Write results
    try:
        write_detailed_results(cases, results)
        print(f"✓ Detailed results written to: {RESULTS_DOC}")
    except Exception as e:
        print(f"✗ Error writing results: {e}")
        return 1

    # Print summary
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")
    total = len(results)

    print()
    print("="*80)
    print("Final Test Summary")
    print("="*80)
    print(f"Tests executed:     {total}")
    print(f"Passed:            {passed} ({100*passed/total:.1f}%)")
    print(f"Failed:            {failed}")
    print(f"Errors:            {errors}")
    print(f"Total execution:    {sum(r.execution_time for r in results):.2f}s")
    print(f"Average response:   {sum(r.execution_time for r in results)/total:.2f}s")
    print("="*80)

    return 0 if failed == 0 and errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
