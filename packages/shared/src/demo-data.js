export const modelProviders = [
  {
    id: "openai",
    name: "OpenAI",
    type: "cloud",
    capabilities: ["chat", "vision", "voice", "tool-use", "reasoning"],
    endpointHint: "https://api.openai.com/v1"
  },
  {
    id: "anthropic",
    name: "Anthropic",
    type: "cloud",
    capabilities: ["chat", "vision", "reasoning"],
    endpointHint: "https://api.anthropic.com"
  },
  {
    id: "gemini",
    name: "Google Gemini",
    type: "cloud",
    capabilities: ["chat", "vision", "tool-use"],
    endpointHint: "https://generativelanguage.googleapis.com"
  },
  {
    id: "ollama",
    name: "Ollama Local",
    type: "local",
    capabilities: ["chat", "vision"],
    endpointHint: "http://localhost:11434"
  }
];

export const skillCatalog = [
  {
    id: "daily-briefing",
    name: "Daily Briefing",
    category: "lifestyle",
    description: "Combine weather, calendars, reminders, and commute context into a family morning digest.",
    inputModes: ["text", "voice", "event"]
  },
  {
    id: "family-schedule-sync",
    name: "Family Schedule Sync",
    category: "lifestyle",
    description: "Merge events across devices and surface conflicts on the TV home screen.",
    inputModes: ["text", "event"]
  },
  {
    id: "knowledge-qa",
    name: "Local Knowledge Q&A",
    category: "knowledge",
    description: "Search local household documents and answer with citations from a private knowledge base.",
    inputModes: ["text", "voice", "image"]
  },
  {
    id: "im-command-bridge",
    name: "IM Command Bridge",
    category: "communication",
    description: "Receive commands from LINE, WeChat, or the mobile companion and normalize them for the core engine.",
    inputModes: ["text", "voice", "image", "event"]
  }
];

export const activeAgents = [
  {
    id: "planner",
    name: "Planner Agent",
    role: "Task decomposition and routing",
    status: "running",
    model: "OpenAI",
    progress: 84,
    lastUpdate: "Mapped family request into 3 parallel sub-tasks"
  },
  {
    id: "device",
    name: "Device Agent",
    role: "Box automation and pairing",
    status: "running",
    model: "Gemini",
    progress: 61,
    lastUpdate: "Refreshing pairing state for mobile and IM clients"
  },
  {
    id: "lifestyle",
    name: "Lifestyle Agent",
    role: "Household assistant orchestration",
    status: "planning",
    model: "Anthropic",
    progress: 39,
    lastUpdate: "Assembling morning briefing and bill reminder digest"
  },
  {
    id: "developer",
    name: "Developer Agent",
    role: "AI-driven development stream",
    status: "running",
    model: "OpenAI",
    progress: 72,
    lastUpdate: "Publishing UI state updates to the TV timeline"
  }
];

export const timelineEvents = [
  {
    id: "t1",
    time: "07:05",
    title: "Request Parsed",
    detail: "Planner Agent split the household task into device setup, family sync, and voice configuration tracks.",
    stream: "analysis"
  },
  {
    id: "t2",
    time: "07:07",
    title: "Parallel Agents Started",
    detail: "Four agents are working concurrently with separate models and skills.",
    stream: "implementation"
  },
  {
    id: "t3",
    time: "07:10",
    title: "Voice Link Ready",
    detail: "Voice gateway selected local STT and cloud TTS fallback.",
    stream: "voice"
  },
  {
    id: "t4",
    time: "07:12",
    title: "Morning Briefing Built",
    detail: "Family summary is ready to display on the living room home screen.",
    stream: "family"
  }
];

export const householdModules = [
  {
    id: "briefing",
    name: "Morning Briefing",
    summary: "Weather, schedule, bills, and tasks are already merged.",
    state: "active",
    actionLabel: "Open Briefing"
  },
  {
    id: "schedule",
    name: "Family Schedule Sync",
    summary: "Two time conflicts were detected for tonight.",
    state: "attention",
    actionLabel: "Resolve Now"
  },
  {
    id: "travel",
    name: "Travel Checklist",
    summary: "Power bank and document copies are still missing.",
    state: "ready",
    actionLabel: "Open List"
  },
  {
    id: "knowledge",
    name: "Local Knowledge Q&A",
    summary: "Policies, manuals, receipts, and home docs are indexed.",
    state: "ready",
    actionLabel: "Ask Now"
  }
];

export const pairingSession = {
  code: "HH-7K2P",
  expiresInSeconds: 180,
  qrPayload: "homehub://pair?box=homehub-living-room&code=HH-7K2P"
};

export const boxProfile = {
  id: "homehub-living-room",
  name: "Living Room Box",
  location: "Home / TV Console",
  networkState: "online",
  pairedClients: 3,
  voiceReady: true
};

export const voiceProfile = {
  wakeWord: "Hello HomeHub",
  sttProvider: "Local Whisper Runtime",
  ttsProvider: "Cloud Neural Voice",
  locale: "zh-CN"
};

export const relayMessages = [
  {
    id: "r1",
    source: "mobile-app",
    kind: "voice",
    preview: "Remind me about the family meeting at 8 PM.",
    createdAt: "07:13",
    retentionPolicy: "delete-after-delivery"
  },
  {
    id: "r2",
    source: "wechat",
    kind: "image",
    preview: "A bill screenshot is waiting for OCR and filing.",
    createdAt: "07:14",
    retentionPolicy: "delete-after-delivery"
  }
];
