import http from "node:http";
import {
  boxProfile,
  householdModules,
  pairingSession,
  relayMessages,
  timelineEvents,
  voiceProfile
} from "../../packages/shared/src/demo-data.js";

const port = Number(process.env.PORT || 4200);

const routes = {
  "/health": { ok: true, service: "companion-api" },
  "/box": boxProfile,
  "/pairing": pairingSession,
  "/modules": householdModules,
  "/timeline": timelineEvents,
  "/relay": relayMessages,
  "/voice": voiceProfile
};

const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  const payload = routes[req.url || ""];

  if (payload) {
    res.end(JSON.stringify(payload, null, 2));
    return;
  }

  if (req.url === "/relay/policy") {
    res.end(JSON.stringify({
      mode: "ephemeral-relay",
      deletionRule: "delete payload immediately after delivery acknowledgement"
    }, null, 2));
    return;
  }

  res.statusCode = 404;
  res.end(JSON.stringify({ error: "Not found" }));
});

server.listen(port, () => {
  console.log(`companion-api listening on http://localhost:${port}`);
});
