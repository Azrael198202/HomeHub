import "./styles.css";
import { tvDashboardData } from "./data";

const stateColor: Record<string, string> = {
  ready: "is-ready",
  attention: "is-attention",
  active: "is-active",
  running: "is-active",
  planning: "is-planning",
  complete: "is-ready",
  blocked: "is-attention",
  idle: "is-muted"
};

export function App() {
  const data = tvDashboardData;

  return (
    <main className="screen">
      <section className="hero panel">
        <div>
          <p className="eyebrow">{data.hero.subtitle}</p>
          <h1>{data.hero.title}</h1>
          <p className="tagline">{data.hero.tagline}</p>
        </div>
        <div className="hero-meta">
          <div className="stat-card">
            <span>Paired Devices</span>
            <strong>{data.boxProfile.pairedClients}</strong>
          </div>
          <div className="stat-card">
            <span>Voice</span>
            <strong>{data.boxProfile.voiceReady ? "Ready" : "Off"}</strong>
          </div>
          <div className="stat-card">
            <span>Network</span>
            <strong>{data.boxProfile.networkState}</strong>
          </div>
        </div>
      </section>

      <section className="grid">
        <article className="panel focus-panel">
          <div className="panel-header">
            <h2>AI Development Board</h2>
            <span className="pill">TV Visible Workflow</span>
          </div>
          <div className="timeline">
            {data.timelineEvents.map((event) => (
              <div className="timeline-item" key={event.id}>
                <span className="timeline-time">{event.time}</span>
                <div>
                  <strong>{event.title}</strong>
                  <p>{event.detail}</p>
                </div>
              </div>
            ))}
          </div>
        </article>

        <article className="panel">
          <div className="panel-header">
            <h2>Household Assistant</h2>
            <span className="pill">Starter Layer</span>
          </div>
          <div className="module-list">
            {data.householdModules.map((module) => (
              <div className="module-card" key={module.id}>
                <div className={`dot ${stateColor[module.state]}`} />
                <div>
                  <strong>{module.name}</strong>
                  <p>{module.summary}</p>
                </div>
                <button>{module.actionLabel}</button>
              </div>
            ))}
          </div>
        </article>

        <article className="panel">
          <div className="panel-header">
            <h2>Parallel Agents</h2>
            <span className="pill">Core Engine</span>
          </div>
          <div className="agent-list">
            {data.activeAgents.map((agent) => (
              <div className="agent-card" key={agent.id}>
                <div className="agent-row">
                  <strong>{agent.name}</strong>
                  <span className={`pill ${stateColor[agent.status]}`}>{agent.status}</span>
                </div>
                <p>{agent.role}</p>
                <div className="progress">
                  <div style={{ width: `${agent.progress}%` }} />
                </div>
                <small>{agent.lastUpdate}</small>
              </div>
            ))}
          </div>
        </article>

        <article className="panel">
          <div className="panel-header">
            <h2>Models and Skills</h2>
            <span className="pill">Extensible</span>
          </div>
          <div className="split">
            <div>
              <h3>Models</h3>
              <ul className="mini-list">
                {data.modelProviders.map((provider) => (
                  <li key={provider.id}>
                    <strong>{provider.name}</strong>
                    <span>{provider.capabilities.join(" / ")}</span>
                  </li>
                ))}
              </ul>
            </div>
            <div>
              <h3>Skills</h3>
              <ul className="mini-list">
                {data.skillCatalog.map((skill) => (
                  <li key={skill.id}>
                    <strong>{skill.name}</strong>
                    <span>{skill.description}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </article>

        <article className="panel pairing-panel">
          <div className="panel-header">
            <h2>Pairing and Relay</h2>
            <span className="pill">QR + Relay</span>
          </div>
          <div className="qr-box">
            <div className="fake-qr" aria-label="pairing qr">
              <span>{data.pairingSession.code}</span>
            </div>
            <div>
              <p>Pair with the mobile app or IM bridge by scanning this code.</p>
              <p>Expires in: {data.pairingSession.expiresInSeconds}s</p>
              <small>{data.pairingSession.qrPayload}</small>
            </div>
          </div>
          <div className="mini-list">
            {data.relayMessages.map((message) => (
              <div className="relay-item" key={message.id}>
                <strong>{message.source}</strong>
                <span>{message.preview}</span>
              </div>
            ))}
          </div>
        </article>

        <article className="panel">
          <div className="panel-header">
            <h2>Voice Layer</h2>
            <span className="pill">STT / TTS</span>
          </div>
          <div className="voice-card">
            <p>Wake Word: {data.voiceProfile.wakeWord}</p>
            <p>STT: {data.voiceProfile.sttProvider}</p>
            <p>TTS: {data.voiceProfile.ttsProvider}</p>
            <p>Locale: {data.voiceProfile.locale}</p>
          </div>
        </article>
      </section>
    </main>
  );
}
