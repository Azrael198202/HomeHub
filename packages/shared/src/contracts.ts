export type AgentStatus = "idle" | "planning" | "running" | "blocked" | "complete";

export interface ModelProvider {
  id: string;
  name: string;
  type: "cloud" | "local";
  capabilities: Array<"chat" | "vision" | "voice" | "tool-use" | "reasoning">;
  endpointHint: string;
}

export interface SkillDescriptor {
  id: string;
  name: string;
  category: "automation" | "knowledge" | "communication" | "lifestyle" | "developer";
  description: string;
  inputModes: Array<"text" | "voice" | "image" | "event">;
}

export interface AgentCard {
  id: string;
  name: string;
  role: string;
  status: AgentStatus;
  model: string;
  progress: number;
  lastUpdate: string;
}

export interface TimelineEvent {
  id: string;
  time: string;
  title: string;
  detail: string;
  stream: "analysis" | "implementation" | "voice" | "system" | "family";
}

export interface HouseholdModule {
  id: string;
  name: string;
  summary: string;
  state: "ready" | "attention" | "active";
  actionLabel: string;
}

export interface PairingSession {
  code: string;
  expiresInSeconds: number;
  qrPayload: string;
  pairedClientName?: string;
}

export interface BoxProfile {
  id: string;
  name: string;
  location: string;
  networkState: "online" | "offline" | "limited";
  pairedClients: number;
  voiceReady: boolean;
}

export interface VoiceProfile {
  wakeWord: string;
  sttProvider: string;
  ttsProvider: string;
  locale: string;
}

export interface RelayMessage {
  id: string;
  source: "mobile-app" | "line" | "wechat" | "box-mic";
  kind: "text" | "image" | "voice";
  preview: string;
  createdAt: string;
  retentionPolicy: "delete-after-delivery";
}
