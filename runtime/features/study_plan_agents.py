from __future__ import annotations

import json
import re
from copy import deepcopy
from datetime import datetime
from pathlib import Path

from .base import HomeHubFeature, RuntimeBridge


QUESTIONS = [
    ("childName", "我先记录孩子的信息。孩子怎么称呼？"),
    ("grade", "孩子现在读几年级？"),
    ("goals", "这一年最重要的学习目标是什么？比如语文阅读、数学提升、英语口语。"),
    ("strengths", "孩子现在最有优势或者最感兴趣的科目是什么？"),
    ("weakSubjects", "目前最需要补强的薄弱科目或能力是什么？"),
    ("weeklySchedule", "平时每周大概能投入多少学习时间？周中和周末分别怎样安排？"),
    ("constraints", "有没有必须考虑的约束？比如培训班、运动、视力、作息、家长陪伴时间。"),
]


class Feature(HomeHubFeature):
    feature_id = "study-plan-agents"
    feature_name = "Study Plan Agents"
    version = "1.0.0"

    def descriptor(self) -> dict:
        data = super().descriptor()
        data["summary"] = "Creates reusable study-plan agent instances for different children and grades."
        data["api"] = ["/api/study-plan-agents"]
        data["voiceIntents"] = self.voice_intents()
        return data

    def voice_intents(self) -> list[dict]:
        return [
            {
                "id": "study-plan-agent",
                "name": "Study Plan Agent",
                "summary": "Creates, continues, clones, and reviews study plan agents for children.",
            }
        ]

    def list_agent_types(self, locale: str, runtime: RuntimeBridge) -> list[dict]:
        if locale == "zh-CN":
            return [
                {
                    "id": "study-plan",
                    "name": "学习计划智能体",
                    "summary": "为孩子创建可复用的年度学习计划，支持追问收集信息、生成计划、复制到其他孩子。",
                    "examplePrompt": "帮我创建一个儿子小学四年级学习计划智能体",
                }
            ]
        return [
            {
                "id": "study-plan",
                "name": "Study Plan Agent",
                "summary": "Builds reusable yearly study plans for children and can clone plans across siblings.",
                "examplePrompt": "Create a fourth-grade study plan agent for my son",
            }
        ]

    def storage_path(self, runtime: RuntimeBridge) -> Path:
        agents_dir = runtime.root / "agents"
        agents_dir.mkdir(parents=True, exist_ok=True)
        return agents_dir / "study_plan_agents.json"

    def default_store(self) -> dict:
        now = datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")
        return {
            "items": [],
            "recentActions": [
                {
                    "id": "study-plan-ready",
                    "summary": "Study plan agent factory is ready.",
                    "createdAt": now,
                }
            ],
        }

    def load_store(self, runtime: RuntimeBridge) -> dict:
        path = self.storage_path(runtime)
        if not path.exists():
            data = self.default_store()
            self.save_store(data, runtime)
            return data
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            data = self.default_store()
            self.save_store(data, runtime)
            return data
        if not isinstance(data, dict):
            return self.default_store()
        return {
            "items": data.get("items", []) if isinstance(data.get("items", []), list) else [],
            "recentActions": data.get("recentActions", []) if isinstance(data.get("recentActions", []), list) else [],
        }

    def save_store(self, store: dict, runtime: RuntimeBridge) -> None:
        self.storage_path(runtime).write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")

    def on_refresh(self, runtime: RuntimeBridge) -> None:
        runtime.state[self.feature_id] = self.load_store(runtime)

    def reset(self, runtime: RuntimeBridge) -> None:
        store = self.default_store()
        runtime.state[self.feature_id] = store
        self.save_store(store, runtime)

    def get_store(self, runtime: RuntimeBridge) -> dict:
        store = runtime.state.get(self.feature_id)
        if not isinstance(store, dict):
            store = self.load_store(runtime)
            runtime.state[self.feature_id] = store
        return store

    def now_iso(self) -> str:
        return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")

    def make_id(self, prefix: str) -> str:
        from random import randint

        return f"{prefix}-{datetime.now().strftime('%Y%m%d%H%M%S')}-{randint(100, 999)}"

    def append_action(self, runtime: RuntimeBridge, summary: str) -> None:
        store = self.get_store(runtime)
        store.setdefault("recentActions", []).insert(
            0,
            {"id": self.make_id("study-act"), "summary": summary, "createdAt": self.now_iso()},
        )
        del store["recentActions"][12:]

    def list_agents(self, runtime: RuntimeBridge) -> list[dict]:
        store = self.get_store(runtime)
        return store.get("items", [])

    def sorted_agents(self, runtime: RuntimeBridge) -> list[dict]:
        return sorted(self.list_agents(runtime), key=lambda item: item.get("updatedAt", ""), reverse=True)

    def extract_child_name(self, message: str) -> str:
        for pattern in [
            r"(?:给|为)(儿子|女儿|孩子)",
            r"(?:给|为)([^\s，。的]{1,8})(?:创建|制定|生成)",
        ]:
            match = re.search(pattern, message)
            if match:
                return match.group(1).strip()
        if "儿子" in message:
            return "儿子"
        if "女儿" in message:
            return "女儿"
        if "孩子" in message:
            return "孩子"
        for pattern in [
            r"([^\s，。]{1,8})(?:的)?学习计划",
        ]:
            match = re.search(pattern, message)
            if match:
                value = match.group(1).strip()
                if value not in {"一个", "学习计划", "智能体"}:
                    return value
        return ""

    def extract_grade(self, message: str) -> str:
        match = re.search(r"(小学|初中|高中)?\s*([一二三四五六七八九1-9])年级", message)
        if match:
            prefix = match.group(1) or ""
            return f"{prefix}{match.group(2)}年级"
        return ""

    def normalize_name(self, child_name: str, grade: str) -> str:
        if child_name and grade:
            return f"{child_name}{grade}学习计划智能体"
        if child_name:
            return f"{child_name}学习计划智能体"
        return "学习计划智能体"

    def find_agent_by_hint(self, message: str, runtime: RuntimeBridge) -> dict | None:
        for agent in self.sorted_agents(runtime):
            if agent.get("name") and agent["name"] in message:
                return agent
            if agent.get("profile", {}).get("childName") and agent["profile"]["childName"] in message:
                return agent
        return None

    def get_collecting_agent(self, runtime: RuntimeBridge) -> dict | None:
        for agent in self.sorted_agents(runtime):
            if agent.get("status") == "collecting":
                return agent
        return None

    def next_question(self, agent: dict) -> tuple[str, str] | None:
        profile = agent.get("profile", {})
        for key, prompt in QUESTIONS:
            if not str(profile.get(key, "")).strip():
                return key, prompt
        return None

    def create_agent(self, runtime: RuntimeBridge, message: str, source_agent: dict | None = None) -> dict:
        child_name = self.extract_child_name(message)
        grade = self.extract_grade(message)
        profile = {
            "childName": child_name,
            "grade": grade,
            "goals": "",
            "strengths": "",
            "weakSubjects": "",
            "weeklySchedule": "",
            "constraints": "",
        }
        if source_agent:
            source_profile = source_agent.get("profile", {})
            for key in ("goals", "strengths", "weakSubjects", "weeklySchedule", "constraints"):
                profile[key] = source_profile.get(key, "")
        name = self.normalize_name(child_name or source_agent and source_agent.get("profile", {}).get("childName", "") or "", grade or "")
        agent = {
            "id": self.make_id("study-agent"),
            "type": "study-plan",
            "name": name,
            "status": "collecting",
            "createdAt": self.now_iso(),
            "updatedAt": self.now_iso(),
            "profile": profile,
            "qaHistory": [],
            "artifact": "",
            "sourceAgentId": source_agent.get("id", "") if source_agent else "",
        }
        store = self.get_store(runtime)
        store.setdefault("items", []).insert(0, agent)
        self.append_action(runtime, f"Created study plan agent '{agent['name']}'.")
        self.save_store(store, runtime)
        return agent

    def local_plan(self, agent: dict, locale: str) -> str:
        p = agent.get("profile", {})
        child = p.get("childName") or "孩子"
        grade = p.get("grade") or "当前年级"
        lines = [
            f"# {child} {grade} 年度学习计划",
            "",
            "## 核心目标",
            f"- 年度目标: {p.get('goals') or '建立稳定的学习节奏'}",
            f"- 优势科目: {p.get('strengths') or '待补充'}",
            f"- 薄弱科目: {p.get('weakSubjects') or '待补充'}",
            "",
            "## 周节奏建议",
            f"- 时间安排: {p.get('weeklySchedule') or '周中短时巩固，周末集中复盘'}",
            "- 周中以作业复盘、错题整理、阅读积累为主",
            "- 周末安排一轮查漏补缺和一轮兴趣拓展",
            "",
            "## 执行原则",
            f"- 约束条件: {p.get('constraints') or '优先保证作息和运动'}",
            "- 每月做一次目标回看和内容调整",
            "- 每两周关注一次薄弱项是否改善",
            "",
            "## 分阶段计划",
            "1. 第 1 阶段: 建立作息、确定学科重点、完成基础摸底",
            "2. 第 2 阶段: 围绕薄弱项做专项提升，形成错题与知识清单",
            "3. 第 3 阶段: 强化综合应用，加入阅读、表达或思维训练",
            "4. 第 4 阶段: 学期复盘，按考试和成长结果调整下一阶段",
        ]
        return "\n".join(lines)

    def complete_agent(self, agent: dict, runtime: RuntimeBridge, locale: str) -> None:
        agent["status"] = "complete"
        agent["updatedAt"] = self.now_iso()
        agent["artifact"] = self.local_plan(agent, locale)
        self.append_action(runtime, f"Study plan agent '{agent['name']}' completed.")
        self.save_store(self.get_store(runtime), runtime)

    def answer_collecting_agent(self, agent: dict, message: str, runtime: RuntimeBridge, locale: str) -> str:
        next_question = self.next_question(agent)
        if not next_question:
            self.complete_agent(agent, runtime, locale)
            return self.complete_message(agent, locale)
        key, _prompt = next_question
        agent.setdefault("profile", {})[key] = message.strip()
        agent.setdefault("qaHistory", []).append(
            {"questionKey": key, "answer": message.strip(), "createdAt": self.now_iso()}
        )
        agent["updatedAt"] = self.now_iso()
        follow_up = self.next_question(agent)
        self.save_store(self.get_store(runtime), runtime)
        if follow_up:
            return follow_up[1]
        self.complete_agent(agent, runtime, locale)
        return self.complete_message(agent, locale)

    def complete_message(self, agent: dict, locale: str) -> str:
        if locale == "zh-CN":
            return f"{agent['name']} 已创建完成。现在可以在 HomeHub 里查看，也可以继续说“参考这个计划，再创建一个女儿五年级的学习计划”。"
        if locale == "ja-JP":
            return f"{agent['name']} を作成しました。"
        return f"{agent['name']} is ready and can now be viewed in HomeHub."

    def list_summary(self, runtime: RuntimeBridge, locale: str) -> str:
        agents = self.sorted_agents(runtime)
        if not agents:
            return "还没有学习计划智能体。你可以直接说“创建儿子小学四年级学习计划智能体”。" if locale == "zh-CN" else "No study plan agents yet."
        if locale == "zh-CN":
            return "当前学习计划智能体有：" + "；".join(
                f"{item['name']}（{item['status']}）" for item in agents[:5]
            )
        return "Study plan agents: " + "; ".join(f"{item['name']} ({item['status']})" for item in agents[:5])

    def agent_detail_message(self, agent: dict, locale: str) -> str:
        if agent.get("status") == "complete":
            preview = "\n".join([line for line in str(agent.get("artifact", "")).splitlines() if line.strip()][1:4])
            if locale == "zh-CN":
                return f"{agent['name']} 已完成。计划摘要：{preview or '年度目标、周节奏和阶段安排已生成。'}"
            return f"{agent['name']} is complete."
        next_question = self.next_question(agent)
        if locale == "zh-CN":
            return f"{agent['name']} 还在收集信息。下一步问题是：{next_question[1] if next_question else '继续补充信息'}"
        return f"{agent['name']} is still collecting information."

    def match_voice_intent(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        lowered = message.lower()
        collecting = self.get_collecting_agent(runtime)
        list_tokens = ["list", "show", "\u67e5\u770b", "\u5217\u51fa", "\u8be6\u60c5", "\u663e\u793a"]
        create_tokens = ["create", "\u521b\u5efa", "\u65b0\u5efa", "\u751f\u6210", "\u590d\u7528", "\u53c2\u8003"]
        study_tokens = ["study plan", "\u5b66\u4e60\u8ba1\u5212", "\u667a\u80fd\u4f53"]
        continue_blockers = ["\u51e0\u70b9", "\u65f6\u95f4", "\u5929\u6c14", "\u63d0\u9192", "\u65e5\u7a0b", "weather", "time", "schedule", "remind"]
        if collecting and not any(token in lowered or token in message for token in list_tokens + ["\u521b\u5efa\u65b0\u7684", "\u65b0\u5efa\u4e00\u4e2a"] + continue_blockers):
            return {"intent": "study-plan-agent", "action": "continue_collecting", "score": 0.96}
        if not any(token in lowered or token in message for token in study_tokens):
            return None
        if any(token in lowered or token in message for token in create_tokens):
            return {"intent": "study-plan-agent", "action": "create_agent", "score": 0.97}
        if any(token in lowered or token in message for token in list_tokens):
            return {"intent": "study-plan-agent", "action": "show_agent", "score": 0.9}
        return {"intent": "study-plan-agent", "action": "general_study_plan", "score": 0.8}

    def handle_voice_chat(self, message: str, locale: str, runtime: RuntimeBridge) -> dict | None:
        lowered = message.lower()
        collecting = self.get_collecting_agent(runtime)
        continue_blockers = ["\u51e0\u70b9", "\u65f6\u95f4", "\u5929\u6c14", "\u63d0\u9192", "\u65e5\u7a0b", "weather", "time", "schedule", "remind"]
        if collecting and not any(token in lowered or token in message for token in ["查看", "列出", "list", "show", "创建新的", "新建一个"] + continue_blockers):
            return {"reply": self.answer_collecting_agent(collecting, message, runtime, locale)}

        if "学习计划" not in message and "study plan" not in lowered:
            return None

        if any(token in message for token in ["查看", "列出", "有哪些", "调出来"]) or "list" in lowered or "show" in lowered:
            agent = self.find_agent_by_hint(message, runtime)
            if agent:
                return {"reply": self.agent_detail_message(agent, locale)}
            return {"reply": self.list_summary(runtime, locale)}

        source_agent = None
        if any(token in message for token in ["复用", "参考", "照着", "基于"]):
            source_agent = self.find_agent_by_hint(message, runtime)
            if source_agent is None:
                agents = self.sorted_agents(runtime)
                source_agent = agents[0] if agents else None

        if any(token in message for token in ["创建", "新建", "生成"]) or "create" in lowered:
            agent = self.create_agent(runtime, message, source_agent)
            first_question = self.next_question(agent)
            if first_question:
                return {"reply": f"{agent['name']} 已启动。{first_question[1]}" if locale == "zh-CN" else first_question[1]}
            self.complete_agent(agent, runtime, locale)
            return {"reply": self.complete_message(agent, locale)}

        return {"reply": self.list_summary(runtime, locale)}

    def enhance_household_modules(self, modules: list[dict], locale: str, runtime: RuntimeBridge) -> list[dict]:
        current = deepcopy(modules)
        agents = self.sorted_agents(runtime)
        completed = [item for item in agents if item.get("status") == "complete"]
        collecting = [item for item in agents if item.get("status") == "collecting"]
        if locale == "zh-CN":
            summary = (
                f"已创建 {len(agents)} 个学习计划智能体，完成 {len(completed)} 个。"
                if agents
                else "可以通过语音创建孩子的年度学习计划智能体。"
            )
            action = "查看计划"
        else:
            summary = f"{len(agents)} study plan agents, {len(completed)} complete." if agents else "Create study plan agents by voice."
            action = "Open Plans"
        current.append(
            {
                "id": "study-plan-agents",
                "name": "学习计划智能体" if locale == "zh-CN" else "Study Plan Agents",
                "summary": summary if not collecting else f"{summary} 当前有 {len(collecting)} 个正在收集信息。",
                "state": "attention" if collecting else ("active" if agents else "ready"),
                "actionLabel": action,
            }
        )
        return current

    def dashboard_payload(self, locale: str, runtime: RuntimeBridge) -> dict:
        agents = self.sorted_agents(runtime)
        return {
            "studyPlanAgents": agents[:8],
            "studyPlanRecentActions": self.get_store(runtime).get("recentActions", [])[:6],
        }

    def handle_api(self, method: str, path: str, query: dict, body: dict | None, runtime: RuntimeBridge) -> dict | None:
        if method == "GET" and path == "/api/study-plan-agents":
            return {"status": 200, "body": {"items": self.sorted_agents(runtime), "recentActions": self.get_store(runtime).get("recentActions", [])[:10]}}
        return None


def load_feature() -> HomeHubFeature:
    return Feature()
