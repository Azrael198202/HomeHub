from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionContext:
    goal: str
    locale: str
    task_spec: dict[str, Any] = field(default_factory=dict)
    route: dict[str, Any] = field(default_factory=dict)
    tool_plan: list[dict[str, Any]] = field(default_factory=list)
    model_route: dict[str, Any] = field(default_factory=dict)
    artifacts: list[dict[str, Any]] = field(default_factory=list)
    tool_results: list[dict[str, Any]] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    retrieved_knowledge: list[dict[str, Any]] = field(default_factory=list)
    intermediate_conclusions: list[str] = field(default_factory=list)
    failures: list[dict[str, Any]] = field(default_factory=list)
    next_step: str = ""
    memory_writeback: dict[str, Any] = field(default_factory=dict)

    def set_route_payload(self, route: dict[str, Any]) -> None:
        self.route = route if isinstance(route, dict) else {}
        self.task_spec = self.route.get("taskSpec", {}) if isinstance(self.route.get("taskSpec", {}), dict) else self.task_spec
        self.tool_plan = self.route.get("toolPlan", []) if isinstance(self.route.get("toolPlan", []), list) else self.tool_plan
        self.model_route = self.route.get("modelRoute", {}) if isinstance(self.route.get("modelRoute", {}), dict) else self.model_route

    def add_tool_result(self, item: dict[str, Any]) -> None:
        if isinstance(item, dict):
            self.tool_results.append(item)

    def add_evidence(self, items: list[dict[str, Any]] | None) -> None:
        if not isinstance(items, list):
            return
        for item in items:
            if isinstance(item, dict):
                self.evidence.append(item)

    def add_knowledge(self, items: list[dict[str, Any]] | None) -> None:
        if not isinstance(items, list):
            return
        for item in items:
            if isinstance(item, dict):
                self.retrieved_knowledge.append(item)

    def add_failure(self, stage: str, error: str) -> None:
        if stage or error:
            self.failures.append({"stage": str(stage or "").strip(), "error": str(error or "").strip()})

    def add_conclusion(self, text: str) -> None:
        value = str(text or "").strip()
        if value:
            self.intermediate_conclusions.append(value)

    def to_dict(self) -> dict[str, Any]:
        return {
            "goal": self.goal,
            "locale": self.locale,
            "taskSpec": self.task_spec,
            "route": self.route,
            "toolPlan": self.tool_plan,
            "modelRoute": self.model_route,
            "artifacts": self.artifacts,
            "toolResults": self.tool_results,
            "evidence": self.evidence,
            "retrievedKnowledge": self.retrieved_knowledge,
            "intermediateConclusions": self.intermediate_conclusions,
            "failures": self.failures,
            "nextStep": self.next_step,
            "memoryWriteback": self.memory_writeback,
        }


def create_execution_context(goal: str, locale: str) -> ExecutionContext:
    return ExecutionContext(goal=str(goal or "").strip(), locale=str(locale or "zh-CN").strip() or "zh-CN")
