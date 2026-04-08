from __future__ import annotations

from datetime import datetime


def now_iso() -> str:
    return datetime.now().replace(second=0, microsecond=0).isoformat(timespec="minutes")


def default_agent_cortex(agent_id: str, agent_name: str = "") -> dict:
    stamp = now_iso()
    return {
        "agentId": agent_id,
        "agentName": agent_name,
        "createdAt": stamp,
        "updatedAt": stamp,
        "stage": "seed",
        "blueprint": {
            "mission": "",
            "primaryUser": "",
            "trigger": "",
            "inputs": "",
            "output": "",
            "constraints": "",
            "networkEnabled": False,
            "generatedFeatureId": "",
        },
        "stats": {
            "totalEvents": 0,
            "usageEvents": 0,
            "confirmations": 0,
            "networkLookups": 0,
            "attachmentInputs": 0,
            "textInputs": 0,
            "successfulRuns": 0,
        },
        "signals": {
            "inputModes": {"text": 0, "image": 0},
            "topics": {},
            "toolDependence": {"local": 0, "network": 0},
            "workingStyle": {
                "proactive": 0,
                "structured": 0,
                "cautious": 0,
            },
        },
        "evolution": {
            "stageLabel": "seed",
            "personalizationScore": 0.0,
            "ownModelReadiness": "low",
            "recommendedBrain": "shared",
            "nextUpgrade": "Collect more confirmed interactions before specializing this agent.",
        },
        "brain": {
            "brainFamily": "homehub-exec-brain",
            "pattern": "pre-brain -> exec-brain -> repo-brain",
            "summary": {
                "agentId": agent_id,
                "agentName": agent_name,
                "mission": "",
                "brainMode": "execution-first",
                "inputModes": ["text"],
                "primaryPlanner": "",
                "primaryExecutor": "",
                "primaryArtifactModel": "",
            },
            "taskflow": {
                "command": "",
                "taskType": "general_chat",
                "missionFit": "",
                "stages": [],
                "selectedModels": {},
            },
        },
        "recentEvents": [],
    }
