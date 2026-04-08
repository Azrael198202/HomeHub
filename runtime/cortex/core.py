from __future__ import annotations

from pathlib import Path

from .architect import CortexArchitect
from .models import default_agent_cortex, now_iso
from .reasoning import apply_blueprint_signals, evolution_snapshot, record_event_signals
from .store import CortexStore


class AgentCortex:
    def __init__(self, runtime_root: Path):
        self.store = CortexStore(runtime_root)
        self.architect = CortexArchitect()

    def _load_items(self) -> dict[str, dict]:
        payload = self.store.load()
        items = payload.get("items", {})
        return items if isinstance(items, dict) else {}

    def _save_items(self, items: dict[str, dict]) -> None:
        self.store.save({"items": items})

    def sync_agent(self, agent: dict, stage: str = "") -> dict:
        agent_id = str(agent.get("id", "")).strip()
        if not agent_id:
            return {}
        items = self._load_items()
        state = items.get(agent_id)
        if not isinstance(state, dict):
            state = default_agent_cortex(agent_id, str(agent.get("name", "")).strip())
        apply_blueprint_signals(state, agent)
        if stage:
            state["stage"] = stage
        state["updatedAt"] = now_iso()
        state["evolution"] = evolution_snapshot(state)
        state["brain"] = self.architect.design_state(state)
        items[agent_id] = state
        self._save_items(items)
        return state

    def record_event(self, agent: dict, event_type: str, payload: dict | None = None) -> dict:
        payload = payload if isinstance(payload, dict) else {}
        state = self.sync_agent(agent, stage=event_type)
        if not state:
            return {}
        record_event_signals(state, event_type, payload)
        recent = state.setdefault("recentEvents", [])
        recent.insert(
            0,
            {
                "type": event_type,
                "createdAt": now_iso(),
                "message": str(payload.get("message", "")).strip(),
            },
        )
        del recent[12:]
        state["updatedAt"] = now_iso()
        state["evolution"] = evolution_snapshot(state)
        state["brain"] = self.architect.design_state(state, self._request_from_payload(payload))
        items = self._load_items()
        items[str(agent.get("id", "")).strip()] = state
        self._save_items(items)
        return state

    def get_summary(self, agent_id: str) -> dict:
        state = self._load_items().get(agent_id, {})
        if not isinstance(state, dict):
            return {}
        summary = {
            "agentId": state.get("agentId", ""),
            "agentName": state.get("agentName", ""),
            "stage": state.get("stage", ""),
            "updatedAt": state.get("updatedAt", ""),
            "evolution": state.get("evolution", {}),
            "stats": state.get("stats", {}),
            "topTopics": self._top_topics(state),
            "brain": self._brain_summary(state),
        }
        return summary

    def summaries_for(self, agents: list[dict]) -> dict[str, dict]:
        return {
            str(agent.get("id", "")).strip(): self.get_summary(str(agent.get("id", "")).strip())
            for agent in agents
            if str(agent.get("id", "")).strip()
        }

    def get_brain(self, agent_id: str, request: dict | None = None) -> dict:
        state = self._load_items().get(agent_id, {})
        if not isinstance(state, dict):
            return {}
        brain = self.architect.design_state(state, request)
        state["brain"] = brain
        items = self._load_items()
        items[agent_id] = state
        self._save_items(items)
        return brain

    def brains_for(self, agents: list[dict], request: dict | None = None) -> dict[str, dict]:
        return {
            str(agent.get("id", "")).strip(): self.get_brain(str(agent.get("id", "")).strip(), request)
            for agent in agents
            if str(agent.get("id", "")).strip()
        }

    def compile_request(self, agent_id: str, request: dict | None = None) -> dict:
        brain = self.get_brain(agent_id, request)
        return brain.get("taskflow", {}) if isinstance(brain, dict) else {}

    def _top_topics(self, state: dict) -> list[str]:
        topics = state.get("signals", {}).get("topics", {})
        if not isinstance(topics, dict):
            return []
        ranked = sorted(topics.items(), key=lambda item: item[1], reverse=True)
        return [name for name, score in ranked[:3] if score]

    def _brain_summary(self, state: dict) -> dict:
        brain = state.get("brain", {})
        if not isinstance(brain, dict):
            return {}
        return {
            "brainFamily": brain.get("brainFamily", "homehub-exec-brain"),
            "pattern": brain.get("pattern", "pre-brain -> exec-brain -> repo-brain"),
            "summary": brain.get("summary", {}),
            "taskflow": brain.get("taskflow", {}),
        }

    def _request_from_payload(self, payload: dict) -> dict:
        attachments = payload.get("attachments", []) if isinstance(payload.get("attachments", []), list) else []
        input_modes = ["text"]
        if attachments:
            input_modes.append("image")
        message = str(payload.get("message", "")).strip()
        if payload.get("voice") or "voice" in message.lower():
            input_modes.append("voice")
        return {
            "command": message,
            "taskType": str(payload.get("taskType", "general_chat")).strip() or "general_chat",
            "inputModes": sorted(set(input_modes)),
            "requiresNetwork": bool(payload.get("networkLookup") or payload.get("query")),
            "requireArtifacts": bool(attachments),
            "speakReply": bool(payload.get("speakReply", False)),
        }
