import { activeAgents, timelineEvents } from "../../../packages/shared/src/demo-data.js";

export function getAgentDashboard() {
  return {
    agents: activeAgents,
    timeline: timelineEvents
  };
}

export function simulateParallelRun(task) {
  return {
    task,
    fanout: 4,
    strategy: "planner -> device | lifestyle | developer | voice",
    status: "running"
  };
}
