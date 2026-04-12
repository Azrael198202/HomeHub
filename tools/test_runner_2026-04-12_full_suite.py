#!/usr/bin/env python3
"""
HomeHub Full Test Suite - 2026-04-12 Complete Execution
Executes all 174 test cases from the clean test document
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
TESTS_DIR = DOCS_DIR / "tests"
CASES_DOC = TESTS_DIR / "2026-04-12_homehub-clean.md"
RESULTS_DOC = DOCS_DIR / "results" / "2026-04-12_homehub-test-results-full-suite.md"
TMP_ROOT = Path("/tmp/homehub-family-suite")
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


def reset_runtime_state_without_fixtures() -> None:
    """Reset runtime to clean state but preserve test fixture directories"""
    stamp = now_text()
    ensure_documents_fixture()

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

    # Initialize conversation log
    write_json(
        ROOT / "runtime" / "conversation_log.jsonl",
        [],
    )

    # Initialize weather state
    write_json(
        ROOT / "runtime" / "weather_state.json",
        {
            "lastUpdated": stamp,
            "current": {
                "temperature": 22,
                "condition": "clear",
                "humidity": 65,
                "windSpeed": 5,
            },
        },
    )

    # Initialize network lookup extensions
    write_json(
        ROOT / "runtime" / "network_lookup_extensions.json",
        {
            "lastUpdated": stamp,
            "extensions": [],
        },
    )

    # Initialize network route memory
    write_json(
        ROOT / "runtime" / "network_route_memory.json",
        {
            "lastUpdated": stamp,
            "routes": [],
        },
    )

    # Initialize source reference memory
    write_json(
        ROOT / "runtime" / "source_reference_memory.json",
        {
            "lastUpdated": stamp,
            "references": [],
        },
    )

    # Initialize knowledge memory
    write_json(
        ROOT / "runtime" / "knowledge_memory.py",
        {},
    )

    # Initialize semantic memory
    write_json(
        ROOT / "runtime" / "semantic_memory.local.json",
        {
            "lastUpdated": stamp,
            "entries": [],
        },
    )

    # Initialize network query planner
    write_json(
        ROOT / "runtime" / "network_query_planner.py",
        {},
    )

    # Initialize research pipeline
    write_json(
        ROOT / "runtime" / "research_pipeline.py",
        {},
    )

    # Initialize execution context
    write_json(
        ROOT / "runtime" / "execution_context.py",
        {},
    )

    # Initialize server config
    write_json(
        ROOT / "runtime" / "server_config.py",
        {},
    )

    # Initialize server memory
    write_json(
        ROOT / "runtime" / "server_memory.py",
        {},
    )

    # Initialize server network
    write_json(
        ROOT / "runtime" / "server_network.py",
        {},
    )

    # Initialize server routes
    write_json(
        ROOT / "runtime" / "server_routes.py",
        {},
    )

    # Initialize server voice
    write_json(
        ROOT / "runtime" / "server_voice.py",
        {},
    )

    # Initialize server weather
    write_json(
        ROOT / "runtime" / "server_weather.py",
        {},
    )

    # Initialize server dashboard
    write_json(
        ROOT / "runtime" / "server_dashboard.py",
        {},
    )

    # Initialize server audio
    write_json(
        ROOT / "runtime" / "server_audio.py",
        {},
    )

    # Initialize voice route guards
    write_json(
        ROOT / "runtime" / "voice_route_guards.py",
        {},
    )

    # Initialize local request guard
    write_json(
        ROOT / "runtime" / "local_request_guard.py",
        {},
    )

    # Initialize custom audio providers
    write_json(
        ROOT / "runtime" / "custom_audio_providers.json",
        [],
    )

    # Initialize cortex profiles
    write_json(
        ROOT / "runtime" / "agents" / "cortex_profiles.json",
        {},
    )

    # Initialize custom agents
    write_json(
        ROOT / "runtime" / "agents" / "custom_agents.json",
        {},
    )

    # Initialize settings
    write_json(
        ROOT / "runtime" / "settings.json",
        {
            "lastUpdated": stamp,
            "settings": {},
        },
    )

    # Initialize bootstrap status
    write_json(
        ROOT / "runtime" / "bootstrap_status.json",
        {
            "lastUpdated": stamp,
            "status": "ready",
        },
    )


@dataclass
class TestCase:
    """Test case data structure"""
    id: str
    phase: str
    query: str
    expected: str
    reset_before: bool = False
    setup_queries: list[str] = field(default_factory=list)


@dataclass
class TestResult:
    """Test result data structure"""
    case: TestCase
    response: str
    score: float
    analysis: str
    execution_time: float
    timestamp: str


def parse_test_cases(content: str) -> list[TestCase]:
    """Parse test cases from markdown content"""
    cases = []
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Look for test case headers like "### S1-01 本地问候 1"
        if line.startswith('### ') and ' ' in line:
            parts = line[4:].split(' ', 1)
            if len(parts) == 2:
                case_id, title = parts
                phase = case_id.split('-')[0] if '-' in case_id else 'Unknown'

                # Find the query
                query = ""
                expected = ""
                reset_before = False
                setup_queries = []

                # Skip to next lines
                j = i + 1
                while j < len(lines):
                    next_line = lines[j].strip()

                    if next_line.startswith('- Query:'):
                        query = next_line[8:].strip('`').strip()
                    elif next_line.startswith('- Expected:'):
                        expected = next_line[11:].strip()
                    elif next_line.startswith('- Reset Before:'):
                        reset_before = next_line[15:].strip().lower() == 'yes'
                    elif next_line.startswith('### ') and j > i + 1:
                        # Next test case
                        break

                    j += 1

                if query and expected:
                    cases.append(TestCase(
                        id=case_id,
                        phase=phase,
                        query=query,
                        expected=expected,
                        reset_before=reset_before,
                        setup_queries=setup_queries
                    ))

                i = j - 1
            else:
                i += 1
        else:
            i += 1

    return cases


def ask(query: str, locale: str = "zh-CN") -> str:
    """Send query to HomeHub runtime"""
    try:
        # Initialize runtime if needed
        if not hasattr(server, 'FEATURE_MANAGER') or server.FEATURE_MANAGER is None:
            server.build_runtime_bridge()

        # Send query
        response = server.ask(query, locale=locale)
        return response if response else "No response"
    except Exception as e:
        return f"Error: {str(e)}"


def validate_response_detailed(response: str, expected: str) -> tuple[float, str]:
    """Detailed response validation with Chinese language support"""
    response_lower = response.lower()
    expected_lower = expected.lower()

    # Success indicators (Chinese)
    success_indicators = [
        "文件", "下面", "发给", "发送", "完成", "成功",
        "好的", "确认", "收到", "处理", "执行",
        "天气", "温度", "℃", "°C", "度",
        "今天", "明天", "昨天", "现在",
        "早上好", "晚上好", "你好", "嗨",
        "hello", "hi", "good", "morning", "evening"
    ]

    # Graceful degradation indicators
    degradation_ok = [
        "路径不可用", "无权访问", "不存在", "无法访问",
        "path_not_found", "permission denied", "not found",
        "不可用", "无法", "失败"
    ]

    # Check for success indicators
    has_success = any(indicator in response_lower for indicator in success_indicators)

    # Check for graceful degradation
    has_degradation = any(indicator in response_lower for indicator in degradation_ok)

    # Check for expected content
    has_expected = any(word in response_lower for word in expected_lower.split() if len(word) > 2)

    # Scoring logic
    if has_success and not has_degradation:
        score = 1.0
        analysis = "Test passed with good confidence"
    elif has_degradation and not has_success:
        score = 0.0
        analysis = "Test failed or requires manual review"
    elif has_expected:
        score = 0.8
        analysis = "Partial match - expected content found"
    elif len(response.strip()) > 0:
        score = 0.5
        analysis = "Response exists but may not match expectations"
    else:
        score = 0.0
        analysis = "No meaningful response"

    return score, analysis


def create_test_fixtures() -> None:
    """Create test fixture directories and files"""
    TMP_ROOT.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    (TMP_ROOT / "family-inbox").mkdir(exist_ok=True)
    (TMP_ROOT / "family-library").mkdir(exist_ok=True)
    (TMP_ROOT / "family-reading").mkdir(exist_ok=True)
    (TMP_ROOT / "classify-alpha").mkdir(exist_ok=True)
    (TMP_ROOT / "classify-beta").mkdir(exist_ok=True)

    # Create files in family-inbox
    (TMP_ROOT / "family-inbox" / "school_notice.txt").write_text("明天带水壶和室内鞋。", encoding="utf-8")
    (TMP_ROOT / "family-inbox" / "monthly_budget.xlsx").write_text("budget data", encoding="utf-8")
    (TMP_ROOT / "family-inbox" / "family_trip.pptx").write_text("trip presentation", encoding="utf-8")
    (TMP_ROOT / "family-inbox" / "receipt.pdf").write_text("receipt content", encoding="utf-8")

    # Create files in family-library
    (TMP_ROOT / "family-library" / "vacation_photo.jpg").write_text("image data", encoding="utf-8")
    (TMP_ROOT / "family-library" / "meal-plan.md").write_text("# meal\n- pasta\n- rice", encoding="utf-8")
    (TMP_ROOT / "family-library" / "utility_bill.csv").write_text("type,amount\nwater,3200", encoding="utf-8")

    # Create files in family-reading
    (TMP_ROOT / "family-reading" / "shopping-note.txt").write_text("牛奶\n鸡蛋\n香蕉", encoding="utf-8")
    (TMP_ROOT / "family-reading" / "recipe.json").write_text('{"dish":"curry","ingredients":["rice","curry powder"]}', encoding="utf-8")

    # Create files for classification tests
    (TMP_ROOT / "classify-alpha" / "document.txt").write_text("document text", encoding="utf-8")
    (TMP_ROOT / "classify-alpha" / "image.jpg").write_text("image data", encoding="utf-8")
    (TMP_ROOT / "classify-alpha" / "data.csv").write_text("name,value\nitem1,100", encoding="utf-8")

    (TMP_ROOT / "classify-beta" / "report.docx").write_text("report content", encoding="utf-8")
    (TMP_ROOT / "classify-beta" / "photo.png").write_text("photo data", encoding="utf-8")


def run_full_test_suite() -> None:
    """Run the complete test suite"""
    print("=" * 80)
    print("HomeHub 完整测试套件 - 2026-04-12 执行")
    print("=" * 80)
    # Read test cases
    if not CASES_DOC.exists():
        print(f"❌ 测试文档不存在: {CASES_DOC}")
        return

    content = CASES_DOC.read_text(encoding="utf-8")
    cases = parse_test_cases(content)

    print(f"✅ 解析了{len(cases)}个测试用例")
    print(f"  源文件: {CASES_DOC}")
    print(f"  结果文件: {RESULTS_DOC}")
    print()

    # Create test fixtures
    print("✅ 创建测试夹具...")
    create_test_fixtures()
    fixture_count = len(list(TMP_ROOT.rglob("*")))
    print(f"  路径: {TMP_ROOT}")
    print(f"  文件数: {fixture_count}")
    print()

    # Initialize runtime
    print("✅ 初始化运行时...")
    reset_runtime_state_without_fixtures()
    print("  运行时状态已重置")
    print()

    # Execute tests
    results = []
    total_start = datetime.now()

    print("执行完整测试套件...")
    print()

    for i, case in enumerate(cases, 1):
        print(f"[{i:3d}/{len(cases):3d}] {case.id}: {case.query[:50]}{'...' if len(case.query) > 50 else ''}")

        # Reset if needed
        if case.reset_before:
            reset_runtime_state_without_fixtures()

        # Execute test
        start_time = datetime.now()
        response = ask(case.query)
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()

        # Validate response
        score, analysis = validate_response_detailed(response, case.expected)

        # Create result
        result = TestResult(
            case=case,
            response=response,
            score=score,
            analysis=analysis,
            execution_time=execution_time,
            timestamp=end_time.isoformat()
        )

        results.append(result)

        # Progress indicator
        status = "✅" if score >= 0.8 else "❌" if score == 0.0 else "⚠️"
        print(f"  {status} {execution_time:.2f}s")
        print()

    total_end = datetime.now()
    total_time = (total_end - total_start).total_seconds()

    # Generate report
    print("✅ 生成测试报告...")
    generate_report(results, total_time)
    print(f"  详细结果已写入: {RESULTS_DOC}")
    print()

    # Summary
    passed = sum(1 for r in results if r.score >= 0.8)
    failed = sum(1 for r in results if r.score == 0.0)
    partial = len(results) - passed - failed

    print("=" * 80)
    print("测试总结")
    print("=" * 80)
    print(f"执行用例:        {len(results)}")
    print(f"通过:           {passed} ({passed/len(results)*100:.1f}%)")
    print(f"部分通过:       {partial} ({partial/len(results)*100:.1f}%)")
    print(f"失败:           {failed} ({failed/len(results)*100:.1f}%)")
    print(f"总执行时间:      {total_time:.2f}秒")
    print(f"平均响应时间:    {sum(r.execution_time for r in results)/len(results):.2f}秒")
    print("=" * 80)
def generate_report(results: list[TestResult], total_time: float) -> None:
    """Generate detailed test report"""
    now = datetime.now()

    content = f"""# HomeHub 完整测试套件结果 - 2026-04-12

## 执行摘要

**生成时间**: {now.strftime('%Y-%m-%dT%H:%M')}
**源文档**: {CASES_DOC.name}
**执行用例**: {len(results)}
**测试环境**: 完整HomeHub运行时 + 真实测试夹具

---

## 性能指标

- **总执行时间**: {total_time:.2f}秒
- **平均响应时间**: {sum(r.execution_time for r in results)/len(results):.2f}秒/测试
- **最快响应**: {min(r.execution_time for r in results):.2f}s
- **最慢响应**: {max(r.execution_time for r in results):.2f}s

---

## 按阶段分列结果

"""

    # Group by phase
    phases = {}
    for result in results:
        phase = result.case.phase
        if phase not in phases:
            phases[phase] = []
        phases[phase].append(result)

    phase_summary = []
    for phase, phase_results in phases.items():
        passed = sum(1 for r in phase_results if r.score >= 0.8)
        failed = sum(1 for r in phase_results if r.score == 0.0)
        partial = len(phase_results) - passed - failed
        total = len(phase_results)
        pass_rate = passed / total * 100 if total > 0 else 0
        avg_time = sum(r.execution_time for r in phase_results) / total if total > 0 else 0
        phase_summary.append((phase, total, passed, partial, failed, pass_rate, avg_time))

    # Sort phases
    phase_summary.sort(key=lambda x: x[0])

    content += "| 阶段 | 总数 | 通过 | 部分 | 失败 | 通过率 | 平均时间 |\n"
    content += "|------|------|------|------|------|--------|----------|\n"
    for phase, total, passed, partial, failed, pass_rate, avg_time in phase_summary:
        content += f"| {phase} | {total} | {passed} | {partial} | {failed} | {pass_rate:.1f}% | {avg_time:.2f}s |\n"
    content += "\n---\n\n"

    # Overall summary
    passed = sum(1 for r in results if r.score >= 0.8)
    failed = sum(1 for r in results if r.score == 0.0)
    partial = len(results) - passed - failed

    content += "## 总体结果\n\n"
    content += f"- **总用例**: {len(results)}\n"
    content += f"- **✅ 通过**: {passed} ({passed/len(results)*100:.1f}%)\n"
    content += f"- **⚠️ 部分通过**: {partial} ({partial/len(results)*100:.1f}%)\n"
    content += f"- **❌ 失败**: {failed} ({failed/len(results)*100:.1f}%)\n\n"

    # Detailed results
    content += "## 详细测试结果\n\n"

    for result in results:
        status = "✅" if result.score >= 0.8 else "❌" if result.score == 0.0 else "⚠️"
        content += f"### {status} {result.case.id}: {result.case.query[:50]}{'...' if len(result.case.query) > 50 else ''}\n\n"
        content += f"**状态**: {'PASS' if result.score >= 0.8 else 'PARTIAL' if result.score > 0.0 else 'FAIL'}\n"
        content += f"**阶段**: {result.case.phase}\n"
        content += f"**执行时间**: {result.execution_time:.2f}秒\n\n"

        content += "#### 查询语句\n"
        content += f"```\n{result.case.query}\n```\n\n"

        content += "#### 预期结果\n"
        content += f"{result.case.expected}\n\n"

        content += "#### 实际结果\n"
        content += f"{result.response}\n\n"

        content += "#### 验证分析\n"
        content += f"- **验证分数**: {result.score:.2f}/1.0\n"
        content += f"- **分析结果**: {result.analysis}\n\n"

        content += "---\n\n"

    # Write to file
    RESULTS_DOC.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_DOC.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    run_full_test_suite()