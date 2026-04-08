from __future__ import annotations

from .brains import (
    build_exec_brain,
    build_interface_contracts,
    build_pre_brain,
    build_repo_brain,
    build_repo_memory_contracts,
    build_support_stack,
    compile_taskflow,
)
from .catalog import build_model_catalog, build_model_plan
from .requirements import build_autonomous_creation_plan, infer_requirement_spec
from .tech import build_technology_stack
from .use_cases import build_requirement_validation


class CortexArchitect:
    def design_state(self, state: dict, request: dict | None = None) -> dict:
        request = self.normalize_request(request)
        model_catalog = build_model_catalog()
        model_plan = build_model_plan(state, request)
        pre_brain = build_pre_brain(request, model_plan)
        exec_brain = build_exec_brain(state, request, model_plan, model_catalog)
        repo_brain = build_repo_brain(request, model_plan)
        taskflow = compile_taskflow(state, request, model_plan)
        requirement_spec = infer_requirement_spec(request)
        autonomous_creation = build_autonomous_creation_plan(state, request)
        return {
            "brainFamily": "homehub-exec-brain",
            "pattern": "pre-brain -> exec-brain -> repo-brain",
            "summary": self._summary(state, request, model_plan),
            "request": request,
            "requirementSpec": requirement_spec,
            "autonomousCreation": autonomous_creation,
            "modelPlan": model_plan,
            "preBrain": pre_brain,
            "execBrain": exec_brain,
            "repoBrain": repo_brain,
            "repoMemory": build_repo_memory_contracts(state),
            "interfaces": build_interface_contracts(state),
            "supportStack": build_support_stack(),
            "technologyStack": build_technology_stack(request),
            "validation": build_requirement_validation(state, request),
            "taskflow": taskflow,
        }

    def normalize_request(self, request: dict | None = None) -> dict:
        request = request if isinstance(request, dict) else {}
        input_modes = request.get("inputModes", ["text"])
        if not isinstance(input_modes, list) or not input_modes:
            input_modes = ["text"]
        return {
            "command": str(request.get("command", "")).strip(),
            "locale": str(request.get("locale", "zh-CN")).strip() or "zh-CN",
            "taskType": str(request.get("taskType", "general_chat")).strip() or "general_chat",
            "inputModes": sorted(set(str(item).strip() for item in input_modes if str(item).strip())) or ["text"],
            "requireArtifacts": bool(request.get("requireArtifacts", False)),
            "requiresNetwork": bool(request.get("requiresNetwork", False)),
            "speakReply": bool(request.get("speakReply", False)),
        }

    def _summary(self, state: dict, request: dict, model_plan: dict) -> dict:
        blueprint = state.get("blueprint", {}) if isinstance(state.get("blueprint", {}), dict) else {}
        assignments = model_plan.get("assignments", {})
        return {
            "agentId": state.get("agentId", ""),
            "agentName": state.get("agentName", ""),
            "mission": blueprint.get("mission", ""),
            "brainMode": "execution-first",
            "inputModes": request.get("inputModes", ["text"]),
            "primaryPlanner": assignments.get("planner", ""),
            "primaryExecutor": assignments.get("executor", ""),
            "primaryArtifactModel": assignments.get("artifact", ""),
        }
