import http from "node:http";
import { getAgentDashboard, simulateParallelRun } from "./agents.js";
import { loadSkills } from "./skills.js";
import { listModelProviders } from "./providers.js";

const port = Number(process.env.PORT || 4100);

const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");

  if (req.url === "/health") {
    res.end(JSON.stringify({ ok: true, service: "core-engine" }));
    return;
  }

  if (req.url === "/providers") {
    res.end(JSON.stringify(listModelProviders(), null, 2));
    return;
  }

  if (req.url === "/skills") {
    res.end(JSON.stringify(loadSkills().map((skill) => skill.descriptor), null, 2));
    return;
  }

  if (req.url?.startsWith("/run")) {
    res.end(JSON.stringify(simulateParallelRun("Build a household trip plan and show progress on TV"), null, 2));
    return;
  }

  if (req.url === "/dashboard") {
    res.end(JSON.stringify(getAgentDashboard(), null, 2));
    return;
  }

  res.statusCode = 404;
  res.end(JSON.stringify({ error: "Not found" }));
});

server.listen(port, () => {
  console.log(`core-engine listening on http://localhost:${port}`);
});
