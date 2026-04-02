const stateColor = {
  ready: "is-ready",
  attention: "is-attention",
  active: "is-active",
  running: "is-active",
  planning: "is-planning",
  complete: "is-ready",
  blocked: "is-attention",
  idle: "is-muted"
};

const tabs = ["home", "agents", "voice", "pairing", "settings"];
let activeTab = "home";
let latestDashboard = null;
let currentLocale = "en-US";
let mediaRecorder = null;
let mediaChunks = [];
let isRecording = false;
let isBuddySpeaking = false;
let isBuddyThinking = false;
let buddySpeechTimer = null;
let buddyDragState = { dragging: false, offsetX: 0, offsetY: 0, x: null, y: null };
let activeReminderId = null;
let announcedReminderId = null;
let isCompletingReminder = false;

const UI_TEXT = {
  "en-US": {
    metaTitle: "HomeHub TV Box",
    brandEyebrow: "AI Box for the Living Room",
    tabs: { home: "Home", agents: "Agents", voice: "Voice", pairing: "Pairing", settings: "Settings" },
    top: {
      homeAssistant: "Household Assistant",
      starterLayer: "Starter Layer",
      aiBoard: "AI Development Board",
      liveWorkflow: "Live Workflow",
      parallelAgents: "Parallel Agents",
      coreEngine: "Core Engine",
      modelsSkills: "Models and Skills",
      extensible: "Extensible",
      models: "Models",
      skills: "Skills",
      voiceSession: "Voice Session",
      transcript: "Transcript",
      pairingRelay: "Pairing and Relay",
      relayInbox: "Relay Inbox",
      transient: "Transient",
      languageMode: "Language Mode",
      audioStack: "AI Capability Catalog",
      sttProvider: "STT Provider",
      ttsProvider: "TTS Provider",
      conversationDock: "Conversation Dock",
      currentRequest: "Current Spoken Request"
    },
    hero: {
      tagline: "Boot like a TV box, collaborate like a multi-agent team.",
      hint: "Use Left/Right to switch tabs, Enter to open cards.",
      pairedDevices: "Paired Devices",
      voice: "Voice",
      network: "Network",
      ready: "Ready",
      off: "Off"
    },
    status: {
      status: "Status",
      weather: "Weather",
      box: "Box",
      tip: "Tip",
      remoteReady: "Remote Ready",
      listening: "Listening"
    },
    voice: {
      guidance: "Press the microphone once to start, and once again to stop.",
      onScreenConversation: "On-Screen Conversation",
      wakeWord: "Wake Word",
      stt: "STT",
      tts: "TTS",
      locale: "Locale",
      weather: "Weather",
      upcomingEvents: "Upcoming Events",
      pendingReminders: "Pending Reminders",
      recentActions: "Recent Actions",
      studyAgents: "Study Plan Agents",
      studyRecent: "Agent Updates",
      agentTypes: "Available Agent Types",
      noUpcoming: "No local schedule items yet.",
      sample: "Sample",
      noConversation: "No conversation yet.",
      micIdle: "Stopped",
      micRecording: "Recording",
      browserNoMic: "This browser does not support microphone recording.",
      transcribing: "Transcribing your voice...",
      sendFailure: "Failed to send message.",
      sttFailure: "Voice recognition failed.",
      route: "Router",
      routeKind: "Flow",
      routeTarget: "Handler",
      routeAction: "Action",
      routeReasoning: "Reasoning",
      routeClarify: "Clarification",
      routeGeneral: "General chat",
      routeAgentFactory: "Agent factory",
      pendingClarification: "Pending clarification",
      originalRequest: "Original request"
    },
    reminder: {
      eyebrow: "Time Reminder",
      dueNow: "Due now",
      noNotes: "HomeHub will move to the next reminder after you confirm this one.",
      markComplete: "Mark Complete",
      completing: "Completing...",
      completed: "HomeHub: Reminder completed.",
      voicePrefix: "Reminder"
    },
    pairing: {
      description: "Pair with the companion app or IM bridge by scanning this code.",
      expiresIn: "Expires in"
    },
    settings: {
      languageBadge: "ZH / EN / JA",
      speechToText: "Speech to Text",
      textToSpeech: "Text to Speech",
      realtimeRecommendation: "Realtime Recommendation",
      totalStacks: "Total stacks",
      capabilityCatalog: "AI Capability Catalog",
      provider: "Provider",
      primary: "Primary",
      fallback: "Fallback",
      mode: "Mode",
      runnable: "Runnable",
      catalogOnly: "Catalog only",
      selected: "Selected",
      syncOpenclaw: "OpenClaw sync",
      syncWorkbuddy: "WorkBuddy sync",
      customStackTitle: "Add Custom Capability",
      customStackBadge: "Custom",
      customSave: "Save Custom Capability",
      catalogBadge: "Catalog",
      useStt: "Use STT",
      useTts: "Use TTS",
      currentUiLanguage: "Current UI language",
      googleKey: "Google Key",
      openaiKey: "OpenAI Key",
      configured: "Configured",
      missing: "Missing"
    },
    prompts: {
      switchedTab: "HomeHub: Switched to {tab}.",
      returnedTab: "HomeHub: Returned to {tab}.",
      qrHighlighted: "HomeHub: Pairing QR is highlighted. Scan this code with the companion app to connect.",
      actionReady: "HomeHub: {title} selected. Action ready: {action}.",
      selected: "HomeHub: {title} is now selected.",
      saveLanguageFailed: "HomeHub: Failed to save language setting.",
      languageSwitched: "HomeHub: Language mode switched to {language}.",
      saveAudioFailed: "HomeHub: Failed to save audio provider setting.",
      saveCustomProviderFailed: "HomeHub: Failed to save the custom stack.",
      customProviderSaved: "HomeHub: Custom stack {label} is ready.",
      audioUpdated: "HomeHub: Audio providers updated. STT={stt}, TTS={tts}.",
      recordingStarted: "HomeHub: Microphone is recording.",
      recordingStopped: "HomeHub: Recording stopped.",
      micAccessFailed: "HomeHub: Microphone access failed. {error}"
    },
    speakers: { you: "You", homehub: "HomeHub" }
  },
  "zh-CN": {
    metaTitle: "HomeHub 电视盒子",
    brandEyebrow: "客厅 AI 盒子",
    tabs: { home: "首页", agents: "智能体", voice: "语音", pairing: "配对", settings: "设置" },
    top: {
      homeAssistant: "家庭助理",
      starterLayer: "基础能力层",
      aiBoard: "AI 开发看板",
      liveWorkflow: "实时流程",
      parallelAgents: "并行智能体",
      coreEngine: "核心引擎",
      modelsSkills: "模型与技能",
      extensible: "可扩展",
      models: "模型",
      skills: "技能",
      voiceSession: "语音会话",
      transcript: "转写记录",
      pairingRelay: "配对与中转",
      relayInbox: "中转收件箱",
      transient: "临时消息",
      languageMode: "语言模式",
      audioStack: "AI 能力模型目录",
      sttProvider: "语音识别提供方",
      ttsProvider: "语音合成提供方",
      conversationDock: "对话底座",
      currentRequest: "当前语音请求"
    },
    hero: {
      tagline: "像电视盒子一样开机，像多智能体团队一样协作。",
      hint: "使用左右键切换标签，按回车进入卡片。",
      pairedDevices: "已配对设备",
      voice: "语音",
      network: "网络",
      ready: "就绪",
      off: "关闭"
    },
    status: {
      status: "状态",
      weather: "天气",
      box: "盒子",
      tip: "提示",
      remoteReady: "遥控可用",
      listening: "监听中"
    },
    voice: {
      guidance: "按一次麦克风开始，再按一次停止。",
      onScreenConversation: "屏幕对话",
      wakeWord: "唤醒词",
      stt: "语音识别",
      tts: "语音合成",
      locale: "语言",
      weather: "天气",
      upcomingEvents: "即将开始的日程",
      pendingReminders: "待触发提醒",
      recentActions: "最近动作",
      studyAgents: "学习计划智能体",
      studyRecent: "智能体更新",
      agentTypes: "可创建智能体类型",
      noUpcoming: "还没有本地日程。",
      sample: "示例",
      noConversation: "还没有对话内容。",
      micIdle: "已停止",
      micRecording: "录音中",
      browserNoMic: "当前浏览器不支持麦克风录音。",
      transcribing: "正在识别语音...",
      sendFailure: "发送消息失败。",
      sttFailure: "语音识别失败。",
      route: "路由器",
      routeKind: "流向",
      routeTarget: "处理者",
      routeAction: "动作",
      routeReasoning: "判断依据",
      routeClarify: "待澄清",
      routeGeneral: "普通对话",
      routeAgentFactory: "智能体工厂",
      pendingClarification: "待补充信息",
      originalRequest: "原始请求"
    },
    reminder: {
      eyebrow: "时间提醒",
      dueNow: "现在需要处理",
      noNotes: "确认这条提醒后，HomeHub 会自动切换到下一件事。",
      markComplete: "完成提醒",
      completing: "正在完成...",
      completed: "HomeHub：这条提醒已完成。",
      voicePrefix: "提醒你"
    },
    pairing: {
      description: "扫描此码即可通过手机伴侣应用或 IM 桥接进行配对。",
      expiresIn: "剩余时间"
    },
    settings: {
      languageBadge: "中 / 英 / 日",
      speechToText: "语音转文字",
      textToSpeech: "文字转语音",
      realtimeRecommendation: "实时建议",
      totalStacks: "模型栈总数",
      capabilityCatalog: "AI 能力模型目录",
      provider: "提供方",
      primary: "主模型",
      fallback: "回退模型",
      mode: "模式",
      runnable: "可执行",
      catalogOnly: "仅目录展示",
      selected: "已选中",
      syncOpenclaw: "OpenClaw 同步",
      syncWorkbuddy: "WorkBuddy 同步",
      customStackTitle: "新增自定义能力条目",
      customStackBadge: "自定义",
      customSave: "保存自定义能力条目",
      catalogBadge: "目录",
      useStt: "设为语音识别",
      useTts: "设为语音合成",
      currentUiLanguage: "当前界面语言",
      googleKey: "Google 密钥",
      openaiKey: "OpenAI 密钥",
      configured: "已配置",
      missing: "未配置"
    },
    prompts: {
      switchedTab: "HomeHub：已切换到 {tab}。",
      returnedTab: "HomeHub：已返回 {tab}。",
      qrHighlighted: "HomeHub：二维码已高亮，请使用伴侣应用扫描配对。",
      actionReady: "HomeHub：已选择 {title}，可执行操作：{action}。",
      selected: "HomeHub：已选中 {title}。",
      saveLanguageFailed: "HomeHub：语言设置保存失败。",
      languageSwitched: "HomeHub：界面语言已切换为 {language}。",
      saveAudioFailed: "HomeHub：音频提供方保存失败。",
      saveCustomProviderFailed: "HomeHub：保存自定义模型栈失败。",
      customProviderSaved: "HomeHub：自定义模型栈 {label} 已保存。",
      audioUpdated: "HomeHub：音频提供方已更新。语音识别={stt}，语音合成={tts}。",
      recordingStarted: "HomeHub：麦克风已开始录音。",
      recordingStopped: "HomeHub：录音已结束。",
      micAccessFailed: "HomeHub：麦克风权限获取失败。{error}"
    },
    speakers: { you: "你", homehub: "HomeHub" }
  },
  "ja-JP": {
    metaTitle: "HomeHub テレビボックス",
    brandEyebrow: "リビング向け AI ボックス",
    tabs: { home: "ホーム", agents: "エージェント", voice: "音声", pairing: "ペアリング", settings: "設定" },
    top: {
      homeAssistant: "家庭アシスタント",
      starterLayer: "基本レイヤー",
      aiBoard: "AI 開発ボード",
      liveWorkflow: "ライブ進行",
      parallelAgents: "並列エージェント",
      coreEngine: "コアエンジン",
      modelsSkills: "モデルとスキル",
      extensible: "拡張可能",
      models: "モデル",
      skills: "スキル",
      voiceSession: "音声セッション",
      transcript: "文字起こし",
      pairingRelay: "ペアリングと中継",
      relayInbox: "中継受信箱",
      transient: "一時保存",
      languageMode: "言語モード",
      audioStack: "AI 機能モデル一覧",
      sttProvider: "音声認識プロバイダー",
      ttsProvider: "音声合成プロバイダー",
      conversationDock: "会話ドック",
      currentRequest: "現在の音声リクエスト"
    },
    hero: {
      tagline: "テレビボックスのように起動し、マルチエージェントのように協調します。",
      hint: "左右キーでタブ切替、Enter キーでカードを開きます。",
      pairedDevices: "接続済み端末",
      voice: "音声",
      network: "ネットワーク",
      ready: "準備完了",
      off: "オフ"
    },
    status: {
      status: "状態",
      weather: "天気",
      box: "ボックス",
      tip: "ヒント",
      remoteReady: "リモコン操作可",
      listening: "待機中"
    },
    voice: {
      guidance: "マイクを一度押すと開始し、もう一度押すと停止します。",
      onScreenConversation: "画面上の会話",
      wakeWord: "ウェイクワード",
      stt: "音声認識",
      tts: "音声合成",
      locale: "言語",
      weather: "天気",
      upcomingEvents: "今後の予定",
      pendingReminders: "保留中のリマインダー",
      recentActions: "最近の操作",
      studyAgents: "学習計画エージェント",
      studyRecent: "エージェント更新",
      agentTypes: "作成可能なエージェント",
      noUpcoming: "ローカル予定はまだありません。",
      sample: "サンプル",
      noConversation: "まだ会話がありません。",
      micIdle: "停止",
      micRecording: "録音中",
      browserNoMic: "このブラウザはマイク録音に対応していません。",
      transcribing: "音声を認識しています...",
      sendFailure: "メッセージ送信に失敗しました。",
      sttFailure: "音声認識に失敗しました。",
      route: "ルーター",
      routeKind: "フロー",
      routeTarget: "担当",
      routeAction: "アクション",
      routeReasoning: "判断理由",
      routeClarify: "確認待ち",
      routeGeneral: "通常会話",
      routeAgentFactory: "エージェント工場",
      pendingClarification: "確認待ち情報",
      originalRequest: "元の依頼"
    },
    reminder: {
      eyebrow: "時間リマインダー",
      dueNow: "今すぐ対応",
      noNotes: "このリマインダーを完了すると、HomeHub は次の予定に切り替えます。",
      markComplete: "完了にする",
      completing: "完了処理中...",
      completed: "HomeHub: このリマインダーを完了しました。",
      voicePrefix: "リマインダーです"
    },
    pairing: {
      description: "このコードをスキャンすると、コンパニオンアプリや IM ブリッジとペアリングできます。",
      expiresIn: "残り時間"
    },
    settings: {
      languageBadge: "中 / 英 / 日",
      speechToText: "音声から文字へ",
      textToSpeech: "文字から音声へ",
      realtimeRecommendation: "リアルタイム推奨",
      totalStacks: "スタック総数",
      capabilityCatalog: "AI 機能モデル一覧",
      provider: "提供元",
      primary: "主要モデル",
      fallback: "フォールバック",
      mode: "モード",
      runnable: "実行可能",
      catalogOnly: "カタログ表示のみ",
      selected: "選択中",
      syncOpenclaw: "OpenClaw 連携",
      syncWorkbuddy: "WorkBuddy 連携",
      customStackTitle: "カスタム機能を追加",
      customStackBadge: "カスタム",
      customSave: "カスタム機能を保存",
      catalogBadge: "一覧",
      useStt: "STT に使用",
      useTts: "TTS に使用",
      currentUiLanguage: "現在の UI 言語",
      googleKey: "Google キー",
      openaiKey: "OpenAI キー",
      configured: "設定済み",
      missing: "未設定"
    },
    prompts: {
      switchedTab: "HomeHub: {tab} タブに切り替えました。",
      returnedTab: "HomeHub: {tab} タブに戻りました。",
      qrHighlighted: "HomeHub: ペアリング QR を選択しました。コンパニオンアプリで読み取ってください。",
      actionReady: "HomeHub: {title} を選択しました。実行可能な操作: {action}。",
      selected: "HomeHub: {title} を選択しました。",
      saveLanguageFailed: "HomeHub: 言語設定の保存に失敗しました。",
      languageSwitched: "HomeHub: 表示言語を {language} に切り替えました。",
      saveAudioFailed: "HomeHub: 音声プロバイダーの保存に失敗しました。",
      saveCustomProviderFailed: "HomeHub: カスタムスタックの保存に失敗しました。",
      customProviderSaved: "HomeHub: カスタムスタック {label} を保存しました。",
      audioUpdated: "HomeHub: 音声プロバイダーを更新しました。STT={stt}、TTS={tts}。",
      recordingStarted: "HomeHub: マイク録音を開始しました。",
      recordingStopped: "HomeHub: 録音を停止しました。",
      micAccessFailed: "HomeHub: マイクアクセスに失敗しました。{error}"
    },
    speakers: { you: "あなた", homehub: "HomeHub" }
  }
};
function t(path, vars = {}) {
  const fallback = UI_TEXT["en-US"];
  const bundle = UI_TEXT[currentLocale] || fallback;
  const value = path.split(".").reduce((acc, key) => acc?.[key], bundle)
    ?? path.split(".").reduce((acc, key) => acc?.[key], fallback)
    ?? path;
  if (typeof value !== "string") return path;
  return value.replace(/\{(\w+)\}/g, (_, key) => String(vars[key] ?? ""));
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function localizeSpeaker(speaker) {
  if (speaker === "You") return t("speakers.you");
  if (speaker === "HomeHub") return t("speakers.homehub");
  return speaker;
}

function localizeMode(mode) {
  return mode === "Listening" ? t("status.listening") : mode;
}

function localizeStatusWord(status) {
  const map = {
    running: { "zh-CN": "运行中", "ja-JP": "実行中" },
    planning: { "zh-CN": "规划中", "ja-JP": "計画中" },
    complete: { "zh-CN": "已完成", "ja-JP": "完了" },
    ready: { "zh-CN": "就绪", "ja-JP": "準備完了" },
    attention: { "zh-CN": "注意", "ja-JP": "注意" }
  };
  return map[status]?.[currentLocale] || status;
}

function translateItem(item, table) {
  return { ...item, ...(table[item.id]?.[currentLocale] || {}) };
}

const moduleTranslations = {
  briefing: {
    "zh-CN": { name: "每日晨报", summary: "天气、日程、任务和账单已完成整合。", actionLabel: "打开晨报" },
    "ja-JP": { name: "朝のブリーフィング", summary: "天気、予定、タスク、請求をまとめました。", actionLabel: "ブリーフを見る" }
  },
  schedule: {
    "zh-CN": { name: "家庭日程同步", summary: "今晚检测到两个时间冲突。", actionLabel: "立即处理" },
    "ja-JP": { name: "家族予定同期", summary: "今夜の予定に 2 件の競合があります。", actionLabel: "今すぐ確認" }
  },
  travel: {
    "zh-CN": { name: "旅行准备清单", summary: "充电宝和证件复印件仍未准备。", actionLabel: "打开清单" },
    "ja-JP": { name: "旅行チェックリスト", summary: "モバイルバッテリーと書類コピーが未準備です。", actionLabel: "リストを開く" }
  },
  knowledge: {
    "zh-CN": { name: "本地知识问答", summary: "政策、手册和票据已建立本地索引。", actionLabel: "立即提问" },
    "ja-JP": { name: "ローカル知識 Q&A", summary: "規約、マニュアル、領収書をローカル索引化しました。", actionLabel: "質問する" }
  },
  messages: {
    "zh-CN": { name: "统一消息", summary: "来自 LINE、微信和伴侣应用的最近更新。", actionLabel: "查看收件箱" },
    "ja-JP": { name: "統合メッセージ", summary: "LINE、WeChat、コンパニオンアプリの最新更新です。", actionLabel: "受信箱を見る" }
  }
};

const timelineTranslations = {
  t1: {
    "zh-CN": { title: "请求已解析", detail: "规划智能体已把任务拆分为设备设置、家庭同步和语音配置三条路径。" },
    "ja-JP": { title: "リクエスト解析完了", detail: "プランナーが端末設定、家族同期、音声設定の 3 系統に分解しました。" }
  },
  t2: {
    "zh-CN": { title: "并行智能体已启动", detail: "四个智能体正在使用不同模型和技能并行运行。" },
    "ja-JP": { title: "並列エージェント開始", detail: "4 つのエージェントが異なるモデルとスキルで並列実行中です。" }
  },
  t3: {
    "zh-CN": { title: "语音链路已就绪", detail: "本地语音识别已激活，并保留云端语音合成兜底。" },
    "ja-JP": { title: "音声経路準備完了", detail: "ローカル音声認識が有効になり、クラウド音声合成を予備にしています。" }
  },
  t4: {
    "zh-CN": { title: "晨报已生成", detail: "家庭摘要已经准备好，可直接显示在客厅屏幕。" },
    "ja-JP": { title: "朝の要約を生成", detail: "家族向けサマリーが完成し、リビング画面に表示できます。" }
  }
};

const agentTranslations = {
  planner: {
    "zh-CN": { role: "任务拆解与路由", lastUpdate: "已将家庭请求映射为三条执行路径。" },
    "ja-JP": { role: "タスク分解とルーティング", lastUpdate: "家庭内リクエストを 3 つの実行経路に整理しました。" }
  },
  device: {
    "zh-CN": { role: "配对、盒子状态与自动化", lastUpdate: "正在刷新伴侣设备的配对状态。" },
    "ja-JP": { role: "ペアリング、ボックス状態、自動化", lastUpdate: "コンパニオン端末のペアリング状態を更新しています。" }
  },
  lifestyle: {
    "zh-CN": { role: "家庭助理编排", lastUpdate: "正在准备晨报与提醒。" },
    "ja-JP": { role: "家庭アシスタントのオーケストレーション", lastUpdate: "朝の要約とリマインダーを準備しています。" }
  },
  developer: {
    "zh-CN": { role: "AI 驱动开发流程", lastUpdate: "正在向电视壳层发布工作流更新。" },
    "ja-JP": { role: "AI 駆動開発流", lastUpdate: "TV シェルへワークフロー更新を反映しています。" }
  }
};

const skillTranslations = {
  "daily-briefing": {
    "zh-CN": { name: "每日晨报", description: "组合天气、日程、账单和提醒，生成家庭晨报。" },
    "ja-JP": { name: "朝のブリーフィング", description: "天気、予定、請求、リマインダーをまとめて朝の要約を作成します。" }
  },
  "family-schedule-sync": {
    "zh-CN": { name: "家庭日程同步", description: "合并家庭事件并在电视首页展示冲突。" },
    "ja-JP": { name: "家族予定同期", description: "家族イベントを統合し、TV ホームで競合を表示します。" }
  },
  "knowledge-qa": {
    "zh-CN": { name: "本地知识问答", description: "检索家庭私有文档并带引用回答。" },
    "ja-JP": { name: "ローカル知識 Q&A", description: "家庭内の非公開文書を検索し、出典付きで回答します。" }
  },
  "im-command-bridge": {
    "zh-CN": { name: "IM 指令桥接", description: "接收来自 LINE、微信与伴侣应用的命令。" },
    "ja-JP": { name: "IM コマンドブリッジ", description: "LINE、WeChat、コンパニオンアプリからの命令を受け取ります。" }
  }
};
function iconSvg(name) {
  const icons = {
    status: `<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="rgba(85,208,177,0.14)" stroke="rgba(136,239,214,0.6)"/><circle cx="12" cy="12" r="3.2" fill="#82eed3"/></svg>`,
    weather: `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 18h9a4 4 0 0 0 .4-8A5.5 5.5 0 0 0 6 11.2 3.4 3.4 0 0 0 7 18Z" fill="rgba(101,182,255,0.18)" stroke="rgba(170,215,255,0.75)"/><path d="M9 6.5l.9 1.7M14.1 6.5l-.9 1.7M7 8.9l1.7.5M16.9 8.9l-1.7.5" stroke="#ffd27a" stroke-linecap="round"/></svg>`,
    box: `<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4.5" y="7" width="15" height="10" rx="3" fill="rgba(164,188,212,0.12)" stroke="rgba(189,210,232,0.58)"/><circle cx="9" cy="12" r="1.2" fill="#6edfc5"/><circle cx="15" cy="12" r="1.2" fill="#65b6ff"/></svg>`,
    tip: `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4.8a6 6 0 0 0-3.5 10.8c.9.7 1.4 1.4 1.6 2.1h3.8c.2-.7.7-1.4 1.6-2.1A6 6 0 0 0 12 4.8Z" fill="rgba(255,189,92,0.18)" stroke="rgba(255,220,150,0.7)"/><path d="M10.2 19h3.6" stroke="#ffe6ab" stroke-linecap="round"/></svg>`,
  };
  return icons[name] || icons.status;
}

function mascotSvg(mode = "idle", pose = "home") {
  const bubble = pose === "voice"
    ? `<path d="M184 40c0-19.9 16.1-36 36-36h90c19.9 0 36 16.1 36 36v34c0 19.9-16.1 36-36 36h-54l-22 18v-18h-14c-19.9 0-36-16.1-36-36V40Z" fill="rgba(101,182,255,0.14)" stroke="rgba(174,220,255,0.45)"/>`
    : "";
  const eyeRx = mode === "listening" ? 12 : mode === "speaking" ? 8 : 9;
  const eyeRy = mode === "listening" ? 6 : mode === "speaking" ? 10 : 9;
  const mouth = mode === "speaking"
    ? `<ellipse class="mouth-speaker" cx="142" cy="165" rx="16" ry="10" fill="#95f5de"/>`
    : mode === "listening"
      ? `<path class="mouth-speaker" d="M126 166c10-8 22-8 32 0" fill="none" stroke="#95f5de" stroke-width="4" stroke-linecap="round"/>`
      : `<path class="mouth-speaker" d="M124 164c7 6 29 6 36 0" fill="none" stroke="#95f5de" stroke-width="4" stroke-linecap="round"/>`;
  const armLeft = pose === "agents"
    ? `<path d="M76 116c-24 -6 -38 10 -40 28" fill="none" stroke="rgba(125,222,210,0.58)" stroke-width="6" stroke-linecap="round"/>`
    : `<path d="M80 116c-18 2-28 12-30 28" fill="none" stroke="rgba(125,222,210,0.5)" stroke-width="6" stroke-linecap="round"/>`;
  const armRight = pose === "settings"
    ? `<path d="M206 116c28 -8 40 8 42 28" fill="none" stroke="rgba(125,222,210,0.58)" stroke-width="6" stroke-linecap="round"/>`
    : `<path d="M206 116c18 2 28 12 30 28" fill="none" stroke="rgba(125,222,210,0.5)" stroke-width="6" stroke-linecap="round"/>`;
  const accessory = {
    home: `<path d="M262 38c10-8 24-4 29 7 4 10 0 20-18 32-18-12-22-22-18-32 5-11 19-15 29-7 2-2 4-3 6-4Z" fill="rgba(255,189,92,0.22)" stroke="rgba(255,219,160,0.55)"/>`,
    agents: `<circle cx="286" cy="46" r="8" fill="rgba(101,182,255,0.18)" stroke="rgba(174,220,255,0.55)"/><circle cx="310" cy="64" r="8" fill="rgba(125,222,210,0.18)" stroke="rgba(159,243,222,0.55)"/><circle cx="284" cy="82" r="8" fill="rgba(181,126,255,0.18)" stroke="rgba(218,190,255,0.55)"/><path d="M292 52 302 60M292 76 302 68" stroke="rgba(174,220,255,0.6)" stroke-width="4" stroke-linecap="round"/>`,
    pairing: `<path d="M274 44h18a10 10 0 0 1 0 20h-10" fill="none" stroke="rgba(174,220,255,0.7)" stroke-width="5" stroke-linecap="round"/><path d="M306 58h-18a10 10 0 0 0 0 20h10" fill="none" stroke="rgba(125,222,210,0.7)" stroke-width="5" stroke-linecap="round"/>`,
    settings: `<circle cx="290" cy="58" r="15" fill="rgba(101,182,255,0.14)" stroke="rgba(174,220,255,0.55)"/><circle cx="290" cy="58" r="5" fill="#8ff1db"/><path d="M290 34v8M290 74v8M266 58h8M306 58h8M273 41l5 5M302 70l5 5M273 75l5-5M302 46l5-5" stroke="rgba(174,220,255,0.55)" stroke-width="4" stroke-linecap="round"/>`,
    voice: `<path d="M276 44v30" stroke="rgba(159,243,222,0.68)" stroke-width="6" stroke-linecap="round"/><path d="M292 50c7 6 7 18 0 24M308 44c12 10 12 30 0 40" fill="none" stroke="rgba(174,220,255,0.58)" stroke-width="5" stroke-linecap="round"/>`,
  }[pose] || "";
  return `
    <svg viewBox="0 0 360 240" class="house-mascot-svg is-${mode} pose-${pose}" aria-hidden="true">
      <defs>
        <linearGradient id="roofGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#7dded2"/>
          <stop offset="100%" stop-color="#57a9ff"/>
        </linearGradient>
        <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#143047"/>
          <stop offset="100%" stop-color="#1c425f"/>
        </linearGradient>
        <radialGradient id="cheekGrad" cx="50%" cy="50%" r="50%">
          <stop offset="0%" stop-color="rgba(255,182,182,0.9)"/>
          <stop offset="100%" stop-color="rgba(255,182,182,0.05)"/>
        </radialGradient>
      </defs>
      <ellipse cx="140" cy="208" rx="94" ry="18" fill="rgba(0,0,0,0.22)"/>
      ${bubble}
      <path d="M64 94 142 34l78 60v84c0 14.4-11.6 26-26 26H90c-14.4 0-26-11.6-26-26V94Z" fill="url(#bodyGrad)" stroke="rgba(154,210,243,0.5)" stroke-width="3"/>
      <path d="M48 102 142 24l94 78" fill="none" stroke="url(#roofGrad)" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
      <rect x="104" y="124" width="76" height="54" rx="22" fill="rgba(9,20,30,0.66)" stroke="rgba(144,220,203,0.36)"/>
      <ellipse class="eye-listener eye-blink" cx="124" cy="146" rx="${eyeRx}" ry="${eyeRy}" fill="#8ff1db"/>
      <ellipse class="eye-listener eye-blink" cx="160" cy="146" rx="${eyeRx}" ry="${eyeRy}" fill="#8ff1db"/>
      <circle cx="120" cy="142" r="2.4" fill="#103c35"/>
      <circle cx="156" cy="142" r="2.4" fill="#103c35"/>
      ${mouth}
      <ellipse cx="108" cy="156" rx="10" ry="7" fill="url(#cheekGrad)"/>
      <ellipse cx="176" cy="156" rx="10" ry="7" fill="url(#cheekGrad)"/>
      <rect x="128" y="178" width="28" height="26" rx="10" fill="rgba(101,182,255,0.18)" stroke="rgba(174,220,255,0.35)"/>
      ${armLeft}
      ${armRight}
      <circle cx="42" cy="150" r="12" fill="rgba(101,182,255,0.16)" stroke="rgba(174,220,255,0.5)"/>
      <circle cx="244" cy="150" r="12" fill="rgba(101,182,255,0.16)" stroke="rgba(174,220,255,0.5)"/>
      ${accessory}
    </svg>
  `;
}

function getActiveTabLabel() {
  const tab = document.getElementById(`tab-${activeTab}`);
  return tab?.textContent?.trim() || "Home";
}

function buddyDisplayName() {
  const names = {
    "zh-CN": "小栖",
    "en-US": "Nestly",
    "ja-JP": "スミカ",
  };
  return names[currentLocale] || names["en-US"];
}

function buddyPoseForTab() {
  const map = {
    home: "home",
    agents: "agents",
    voice: "voice",
    pairing: "pairing",
    settings: "settings",
  };
  return map[activeTab] || "home";
}

function buddyPromptForTab() {
  const bundle = {
    "zh-CN": {
      home: "我在这里陪你整理家庭与工作。",
      agents: "我在协调多智能体任务。",
      voice: isRecording ? "我正在认真听你说话。" : "按下麦克风，我们开始对话。",
      pairing: "我可以帮你把设备和消息连起来。",
      settings: "这里可以继续扩展我的能力边界。"
    },
    "en-US": {
      home: "I am here for both family life and focused work.",
      agents: "I am coordinating the multi-agent workflow.",
      voice: isRecording ? "I am listening carefully." : "Press the mic and let's talk.",
      pairing: "I can help bridge your devices and messages.",
      settings: "This is where we expand my capabilities."
    },
    "ja-JP": {
      home: "暮らしにも仕事にも寄り添います。",
      agents: "マルチエージェントの流れを整えています。",
      voice: isRecording ? "今、しっかり聞いています。" : "マイクを押して話しかけてください。",
      pairing: "端末とメッセージの接続を手伝います。",
      settings: "ここで私の機能を広げていきます。"
    }
  };
  return bundle[currentLocale]?.[activeTab] || bundle["en-US"][activeTab] || bundle["en-US"].home;
}

function buddySubtitleForTab() {
  const bundle = {
    "zh-CN": {
      home: "陪伴生活，也陪伴工作",
      agents: "多智能体协作中",
      voice: isRecording ? "正在倾听" : "随时可以开口",
      pairing: "连接更多设备与消息",
      settings: "继续扩展无限想象"
    },
    "en-US": {
      home: "For home life and focused work",
      agents: "Coordinating multi-agent flows",
      voice: isRecording ? "Listening now" : "Ready whenever you are",
      pairing: "Bridging devices and messages",
      settings: "Expanding into more possibilities"
    },
    "ja-JP": {
      home: "暮らしにも仕事にも寄り添う",
      agents: "マルチエージェントを調整中",
      voice: isRecording ? "聞いています" : "いつでも話せます",
      pairing: "端末とメッセージをつなぐ",
      settings: "可能性を広げていく"
    }
  };
  return bundle[currentLocale]?.[activeTab] || bundle["en-US"][activeTab] || "";
}

function currentBuddyMode() {
  if (isRecording) return "listening";
  if (isBuddyThinking) return "thinking";
  if (isBuddySpeaking) return "speaking";
  return "idle";
}

function renderFloatingBuddy() {
  const shell = document.getElementById("floating-buddy");
  if (!shell) return;
  const spoken = document.getElementById("spoken-line")?.textContent?.trim() || "";
  const preview = spoken && spoken !== t("voice.noConversation")
    ? spoken.slice(0, 54)
    : buddyPromptForTab();
  const buddyName = buddyDisplayName();
  const pose = buddyPoseForTab();
  const mode = currentBuddyMode();
  shell.innerHTML = `
    <div class="floating-buddy is-${mode} pose-${pose}">
      <div class="floating-buddy-bubble">
        <strong>${buddyName}</strong>
        <em>${escapeHtml(buddySubtitleForTab())}</em>
        <span>${escapeHtml(preview)}</span>
      </div>
      <div class="floating-buddy-avatar">
        ${mascotSvg(mode, pose)}
      </div>
    </div>
  `;
  if (buddyDragState.x !== null && buddyDragState.y !== null) {
    shell.style.right = "auto";
    shell.style.bottom = "auto";
    shell.style.left = `${buddyDragState.x}px`;
    shell.style.top = `${buddyDragState.y}px`;
  }
}

function loadBuddyPosition() {
  try {
    const raw = localStorage.getItem("homehubBuddyPosition");
    if (!raw) return;
    const parsed = JSON.parse(raw);
    if (typeof parsed.x === "number" && typeof parsed.y === "number") {
      buddyDragState.x = parsed.x;
      buddyDragState.y = parsed.y;
    }
  } catch {}
}

function persistBuddyPosition() {
  try {
    if (buddyDragState.x !== null && buddyDragState.y !== null) {
      localStorage.setItem("homehubBuddyPosition", JSON.stringify({ x: buddyDragState.x, y: buddyDragState.y }));
    }
  } catch {}
}

function clampBuddyPosition(x, y, shell) {
  const width = shell.offsetWidth || 480;
  const height = shell.offsetHeight || 260;
  const maxX = Math.max(12, window.innerWidth - width - 12);
  const maxY = Math.max(12, window.innerHeight - height - 12);
  return {
    x: Math.min(Math.max(12, x), maxX),
    y: Math.min(Math.max(12, y), maxY),
  };
}

function statCard(label, value, meta = "", icon = "status", className = "") {
  return `
    <div class="stat-card ${className}">
      <div class="stat-card-head">
        <span class="stat-icon">${iconSvg(icon)}</span>
        <span>${label}</span>
      </div>
      <strong>${value}</strong>
      ${meta ? `<small class="stat-meta">${meta}</small>` : ""}
    </div>
  `;
}

function getSelectedProviders() {
  return latestDashboard?.audioProviders?.selected || { stt: "google", tts: "google" };
}

function applyStaticTranslations() {
  document.documentElement.lang = currentLocale;
  document.title = t("metaTitle");
  document.getElementById("brand-eyebrow").textContent = t("brandEyebrow");
  document.getElementById("tab-home").textContent = t("tabs.home");
  document.getElementById("tab-agents").textContent = t("tabs.agents");
  document.getElementById("tab-voice").textContent = t("tabs.voice");
  document.getElementById("tab-pairing").textContent = t("tabs.pairing");
  document.getElementById("tab-settings").textContent = t("tabs.settings");
  document.getElementById("home-assistant-title").textContent = t("top.homeAssistant");
  document.getElementById("home-assistant-pill").textContent = t("top.starterLayer");
  document.getElementById("home-dev-title").textContent = t("top.aiBoard");
  document.getElementById("home-dev-pill").textContent = t("top.liveWorkflow");
  document.getElementById("agents-title").textContent = t("top.parallelAgents");
  document.getElementById("agents-pill").textContent = t("top.coreEngine");
  document.getElementById("models-skills-title").textContent = t("top.modelsSkills");
  document.getElementById("models-skills-pill").textContent = t("top.extensible");
  document.getElementById("models-title").textContent = t("top.models");
  document.getElementById("skills-title").textContent = t("top.skills");
  document.getElementById("voice-title").textContent = t("top.voiceSession");
  document.getElementById("voice-pill").textContent = "STT / TTS";
  document.getElementById("voice-guidance").textContent = t("voice.guidance");
  document.getElementById("conversation-title").textContent = t("voice.onScreenConversation");
  document.getElementById("conversation-pill").textContent = t("top.transcript");
  document.getElementById("pairing-title").textContent = t("top.pairingRelay");
  document.getElementById("pairing-pill").textContent = "QR + Relay";
  document.getElementById("pairing-description").textContent = t("pairing.description");
  document.getElementById("relay-title").textContent = t("top.relayInbox");
  document.getElementById("relay-pill").textContent = t("top.transient");
  document.getElementById("language-title").textContent = t("top.languageMode");
  document.getElementById("language-pill").textContent = t("settings.languageBadge");
  document.getElementById("audio-stack-title").textContent = t("top.audioStack");
  document.getElementById("audio-stack-pill").textContent = t("settings.catalogBadge");
  document.getElementById("custom-stack-title").textContent = t("settings.customStackTitle");
  document.getElementById("custom-stack-pill").textContent = t("settings.customStackBadge");
  document.getElementById("custom-provider-save").textContent = t("settings.customSave");
  document.getElementById("dock-eyebrow").textContent = t("top.conversationDock");
  document.getElementById("dock-title").textContent = t("top.currentRequest");
  document.getElementById("reminder-eyebrow").textContent = t("reminder.eyebrow");
  syncReminderButtonState();
  const micCore = document.querySelector("#mic-orb .mic-core");
  if (micCore && !isRecording) micCore.textContent = t("voice.micIdle");
}

function renderClock() {
  const now = new Date();
  document.getElementById("clock-time").textContent = now.toLocaleTimeString(currentLocale, { hour: "2-digit", minute: "2-digit" });
  document.getElementById("clock-date").textContent = now.toLocaleDateString(currentLocale, { weekday: "short", month: "short", day: "numeric" });
}

function renderStatusStrip(data) {
  const weatherValue = `${data.weather.condition} ${data.weather.temperatureC}°C`;
  const weatherMeta = `${data.weather.location} · ${data.weather.highC}° / ${data.weather.lowC}°`;
  const nextReminder = data.assistantMemory?.dueReminders?.[0] || data.assistantMemory?.pendingReminders?.[0];
  const tipValue = nextReminder ? nextReminder.title : t("status.remoteReady");
  const tipMeta = nextReminder ? nextReminder.triggerAt.replace("T", " ") : "Directional navigation enabled";
  document.getElementById("status-strip").innerHTML = `
    ${statCard(t("status.status"), localizeMode(data.systemStatus.mode), "Voice link active", "status", "status-card status-card-status")}
    ${statCard(t("status.weather"), weatherValue, weatherMeta, "weather", "status-card status-card-weather")}
    ${statCard(t("status.box"), data.systemStatus.boxHealth, "Living room runtime", "box", "status-card status-card-box")}
    ${statCard(t("status.tip"), tipValue, tipMeta, "tip", "status-card status-card-tip")}
  `;
  document.getElementById("mic-status").textContent = localizeMode(data.systemStatus.mode);
}

function formatReminderTimestamp(value) {
  if (!value) return "";
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime())) {
    return String(value).replace("T", " ");
  }
  return parsed.toLocaleString(currentLocale, {
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  });
}

function buildReminderSpeech(reminder) {
  const title = reminder?.title || "";
  const localePrefix = t("reminder.voicePrefix");
  if (currentLocale === "zh-CN") {
    return `${localePrefix}，现在该${title}了。`;
  }
  if (currentLocale === "ja-JP") {
    return `${localePrefix}。${title}の時間です。`;
  }
  return `${localePrefix}: it is time to ${title}.`;
}

function syncReminderButtonState() {
  const completeButton = document.getElementById("reminder-complete");
  const overlay = document.getElementById("reminder-overlay");
  if (!completeButton) return;
  completeButton.disabled = isCompletingReminder;
  completeButton.setAttribute("aria-busy", isCompletingReminder ? "true" : "false");
  completeButton.textContent = isCompletingReminder ? t("reminder.completing") : t("reminder.markComplete");
  if (overlay) {
    overlay.classList.toggle("is-processing", isCompletingReminder);
  }
}

function speakWithHomeHub(text, lang = currentLocale) {
  if (!("speechSynthesis" in window) || !text) return;
  window.speechSynthesis.cancel();
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = lang;
  utterance.rate = 1;
  utterance.pitch = 1;
  isBuddySpeaking = true;
  if (buddySpeechTimer) clearTimeout(buddySpeechTimer);
  renderFloatingBuddy();
  utterance.onend = () => {
    isBuddySpeaking = false;
    renderFloatingBuddy();
  };
  window.speechSynthesis.speak(utterance);
  buddySpeechTimer = setTimeout(() => {
    isBuddySpeaking = false;
    renderFloatingBuddy();
  }, 4200);
}

function renderReminderOverlay(data) {
  const overlay = document.getElementById("reminder-overlay");
  const dueReminder = data.assistantMemory?.dueReminders?.[0] || null;
  if (!overlay) return;
  if (!dueReminder) {
    overlay.hidden = true;
    activeReminderId = null;
    return;
  }

  activeReminderId = dueReminder.id;
  overlay.hidden = false;
  document.getElementById("reminder-title").textContent = dueReminder.title || t("reminder.dueNow");
  document.getElementById("reminder-time").textContent = `${t("reminder.dueNow")} · ${formatReminderTimestamp(dueReminder.triggerAt)}`;
  document.getElementById("reminder-notes").textContent = dueReminder.notes || t("reminder.noNotes");
  const completeButton = document.getElementById("reminder-complete");
  syncReminderButtonState();
  requestAnimationFrame(() => {
    if (!overlay.hidden && !isCompletingReminder) completeButton.focus();
  });

  if (announcedReminderId !== dueReminder.id) {
    announcedReminderId = dueReminder.id;
    const spoken = buildReminderSpeech(dueReminder);
    updateSpokenLine(`${localizeSpeaker("HomeHub")}: ${spoken}`);
    speakWithHomeHub(spoken);
  }
}

function getCurrentLanguage(data) {
  const supported = data.languageSettings?.supported || [];
  return supported.find((item) => item.code === currentLocale) || supported[0] || null;
}

function renderHero(data) {
  document.getElementById("hero").innerHTML = `
    <div class="hero-copy">
      <p class="eyebrow">${t("brandEyebrow")}</p>
      <h2 class="hero-title">${data.hero.title}</h2>
      <p class="tagline">${t("hero.tagline")}</p>
      <p class="hero-hint">${t("hero.hint")}</p>
      <div class="hero-ambient" aria-hidden="true">
        <svg viewBox="0 0 420 120" class="hero-wave">
          <defs>
            <linearGradient id="heroLine" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="rgba(85,208,177,0.0)" />
              <stop offset="35%" stop-color="rgba(85,208,177,0.9)" />
              <stop offset="100%" stop-color="rgba(101,182,255,0.0)" />
            </linearGradient>
          </defs>
          <path d="M0 76 C48 70, 78 40, 122 46 S203 103, 255 82 S343 40, 420 54" fill="none" stroke="url(#heroLine)" stroke-width="4" stroke-linecap="round"/>
        </svg>
      </div>
    </div>
    <div class="hero-meta">
      ${statCard(t("hero.pairedDevices"), data.boxProfile.pairedClients)}
      ${statCard(t("hero.voice"), data.boxProfile.voiceReady ? t("hero.ready") : t("hero.off"))}
      ${statCard(t("hero.network"), data.boxProfile.networkState)}
    </div>
  `;
}

function renderTimeline(events) {
  document.getElementById("timeline").innerHTML = events.slice().reverse().map((item) => translateItem(item, timelineTranslations)).map((event) => `
    <div class="timeline-item remote-target focusable-card" tabindex="0">
      <span class="timeline-time">${event.time}</span>
      <div>
        <strong>${event.title}</strong>
        <p>${event.detail}</p>
      </div>
    </div>
  `).join("");
}

function renderModules(modules) {
  document.getElementById("modules").innerHTML = modules.map((item) => {
    const localized = moduleTranslations[item.id]?.[currentLocale] || {};
    return {
      ...item,
      name: localized.name || item.name,
      actionLabel: localized.actionLabel || item.actionLabel
    };
  }).map((module) => `
      <div class="module-card remote-target focusable-card" tabindex="0" data-action-text="${escapeHtml(module.actionLabel)}" data-title="${escapeHtml(module.name)}">
        <div class="dot ${stateColor[module.state] || "is-muted"}"></div>
        <div>
          <strong>${module.name}</strong>
        <p>${module.summary}</p>
      </div>
      <button type="button">${module.actionLabel}</button>
    </div>
  `).join("");
}

function renderAgents(agents) {
  document.getElementById("agents").innerHTML = agents.map((item) => translateItem(item, agentTranslations)).map((agent) => `
    <div class="agent-card remote-target focusable-card" tabindex="0" data-title="${escapeHtml(agent.name)}">
      <div class="agent-row">
        <strong>${agent.name}</strong>
        <span class="pill ${stateColor[agent.status] || "is-muted"}">${localizeStatusWord(agent.status)}</span>
      </div>
      <p>${agent.role}</p>
      <div class="progress"><div style="width:${agent.progress}%"></div></div>
      <small>${agent.lastUpdate}</small>
    </div>
  `).join("");
}

function renderModels(models) {
  document.getElementById("models").innerHTML = models.map((provider) => `
    <li class="remote-target focusable-card" tabindex="0" data-title="${escapeHtml(provider.name)}">
      <strong>${provider.name}</strong>
      <span>${provider.capabilities.join(" / ")}</span>
    </li>
  `).join("");
}

function renderSkills(skills) {
  document.getElementById("skills").innerHTML = skills.map((item) => translateItem(item, skillTranslations)).map((skill) => `
    <li class="remote-target focusable-card" tabindex="0" data-title="${escapeHtml(skill.name)}">
      <strong>${skill.name}</strong>
      <span>${skill.description}</span>
    </li>
  `).join("");
}
function renderPairing(pairing, relayMessages) {
  document.getElementById("pairing-code").textContent = pairing.code;
  document.getElementById("pairing-expiry").textContent = `${t("pairing.expiresIn")}: ${pairing.expiresInSeconds}s`;
  document.getElementById("pairing-payload").textContent = pairing.qrPayload;
  document.getElementById("relay").innerHTML = relayMessages.map((message) => `
    <div class="relay-item remote-target focusable-card" tabindex="0" data-title="${escapeHtml(message.source)}">
      <strong>${message.source}</strong>
      <span>${message.preview}</span>
    </div>
  `).join("");
}

function renderVoice(data) {
  const language = getCurrentLanguage(data);
  const upcomingEvents = data.assistantMemory?.upcomingEvents || [];
  const reminders = data.assistantMemory?.pendingReminders || [];
  const recentActions = data.assistantMemory?.recentActions || [];
  const studyAgents = data.studyPlanAgents || [];
  const studyRecent = data.studyPlanRecentActions || [];
  const agentTypes = data.agentTypes || [];
  const voiceRoute = data.lastVoiceRoute || data.voiceRoute || null;
  const pendingClarification = data.pendingVoiceClarification || null;
  const routeKindLabel = voiceRoute?.kind === "feature"
    ? (voiceRoute.selected?.intent || "-")
    : voiceRoute?.kind === "agent_factory"
      ? t("voice.routeAgentFactory")
      : voiceRoute?.kind === "clarify"
        ? t("voice.routeClarify")
        : t("voice.routeGeneral");
  const routeTargetLabel = voiceRoute?.selected
    ? `${voiceRoute.selected.featureName || "-"} / ${voiceRoute.selected.intent || "-"}`
    : "-";
  const routeActionLabel = voiceRoute?.selected?.action || "-";
  const routeReasoning = voiceRoute?.clarificationQuestion || voiceRoute?.reasoning || "-";
  const clarificationLine = pendingClarification
    ? `<p><strong>${t("voice.pendingClarification")}:</strong> ${pendingClarification.clarificationQuestion || "-"} · ${t("voice.originalRequest")} ${pendingClarification.originalRequest || "-"}</p>`
    : "";
  document.getElementById("voice").innerHTML = `
    <p>${t("voice.wakeWord")}: ${data.voiceProfile.wakeWord}</p>
    <p>${t("voice.stt")}: ${data.voiceProfile.sttProvider}</p>
    <p>${t("voice.tts")}: ${data.voiceProfile.ttsProvider}</p>
    <p>${t("voice.locale")}: ${language?.code || data.voiceProfile.locale}</p>
    <p>${t("voice.weather")}: ${data.weather.condition}, ${data.weather.highC}C / ${data.weather.lowC}C</p>
    <p><strong>${t("voice.route")}:</strong> ${t("voice.routeKind")} ${routeKindLabel} · ${t("voice.routeTarget")} ${routeTargetLabel} · ${t("voice.routeAction")} ${routeActionLabel}</p>
    <p><strong>${t("voice.routeReasoning")}:</strong> ${routeReasoning}</p>
    ${clarificationLine}
    <p><strong>${t("voice.upcomingEvents")}:</strong> ${upcomingEvents.length ? upcomingEvents.map((event) => `${event.title} (${event.startAt.replace("T", " ")})`).join(" · ") : t("voice.noUpcoming")}</p>
    <p><strong>${t("voice.pendingReminders")}:</strong> ${reminders.length ? reminders.map((item) => `${item.title} (${item.triggerAt.replace("T", " ")})`).join(" · ") : t("voice.noUpcoming")}</p>
    <p><strong>${t("voice.recentActions")}:</strong> ${recentActions.length ? recentActions.map((item) => item.summary).join(" · ") : "-"}</p>
    <p><strong>${t("voice.studyAgents")}:</strong> ${studyAgents.length ? studyAgents.map((item) => `${item.name} (${item.status})${item.artifact ? ` ${item.artifact.split("\n")[1] || ""}` : ""}`).join(" · ") : "-"}</p>
    <p><strong>${t("voice.studyRecent")}:</strong> ${studyRecent.length ? studyRecent.map((item) => item.summary).join(" · ") : "-"}</p>
    <p><strong>${t("voice.agentTypes")}:</strong> ${agentTypes.length ? agentTypes.map((item) => `${item.name}: ${item.summary}`).join(" · ") : "-"}</p>
  `;

  document.getElementById("conversation").innerHTML = data.conversation.map((item, index, list) => `
    <div class="conversation-item ${item.speaker === "You" ? "is-user" : "is-bot"} ${index === list.length - 1 ? "is-latest" : ""}">
      <div class="conversation-avatar">${item.speaker === "You" ? "ME" : "HH"}</div>
      <div class="conversation-bubble">
        <div class="conversation-head">
          <strong>${localizeSpeaker(item.speaker)}</strong>
          <span>${item.time}</span>
        </div>
        <p>${item.text}</p>
      </div>
    </div>
  `).join("");

  const lastSpoken = data.conversation[data.conversation.length - 1];
  document.getElementById("spoken-line").textContent = lastSpoken ? `${localizeSpeaker(lastSpoken.speaker)}: ${lastSpoken.text}` : t("voice.noConversation");
  const conversation = document.getElementById("conversation");
  requestAnimationFrame(() => {
    conversation.scrollTop = conversation.scrollHeight;
  });
  renderFloatingBuddy();
}

async function completeActiveReminder() {
  if (!activeReminderId || isCompletingReminder) return;
  const reminderId = activeReminderId;
  const overlay = document.getElementById("reminder-overlay");
  isCompletingReminder = true;
  syncReminderButtonState();
  try {
    if (overlay) {
      overlay.hidden = true;
    }
    activeReminderId = null;
    const response = await fetch("/api/memory/reminders/complete", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id: reminderId })
    });
    const payload = await response.json();
    if (!response.ok) {
      activeReminderId = reminderId;
      if (overlay) {
        overlay.hidden = false;
      }
      updateSpokenLine(`HomeHub: ${payload.error || "Failed to complete reminder."}`);
      return;
    }
    if (latestDashboard) {
      latestDashboard.assistantMemory = payload.assistantMemory || latestDashboard.assistantMemory;
      renderStatusStrip(latestDashboard);
      renderVoice(latestDashboard);
      renderReminderOverlay(latestDashboard);
    }
    updateSpokenLine(t("reminder.completed"));
    await loadDashboard();
  } finally {
    isCompletingReminder = false;
    syncReminderButtonState();
  }
}

function renderSettings(data) {
  const language = getCurrentLanguage(data);
  const selectedAudio = data.audioProviders?.selected || {};
  const catalog = data.audioProviders?.catalog || {};
  const secrets = data.audioProviders?.secrets || {};
  const modelCatalog = data.modelCatalog || [];
  const counts = data.audioProviders?.counts || { total: modelCatalog.length, editable: 0 };

  document.getElementById("languages").innerHTML = (data.languageSettings?.supported || []).map((item) => `
    <div class="language-card remote-target focusable-card ${item.code === language?.code ? "is-selected-language" : ""}" tabindex="0" data-language-code="${item.code}" data-title="${escapeHtml(item.label)}">
      <strong>${item.label}</strong>
      <span>${item.code}</span>
      <p>${item.sample}</p>
    </div>
  `).join("");

  document.getElementById("model-stack-cards").innerHTML = modelCatalog.map((item) => `
    <div class="provider-card focusable-card ${item.editable ? "is-selected-provider" : ""}" tabindex="0" data-title="${escapeHtml(item.label)}">
      <strong>${item.label}</strong>
      <div class="meta-row">
        <span class="mini-pill source">${item.source}</span>
        ${item.capabilities.map((capability) => `<span class="mini-pill capability">${capability}</span>`).join("")}
      </div>
      <p>${item.summary}</p>
      <div class="provider-models">
        ${item.models.map((model) => `<span>${escapeHtml(model)}</span>`).join("")}
      </div>
      <small>${(item.languages || []).join(" / ")}</small>
      <small>${t("settings.syncOpenclaw")}: ${item.sync?.openclaw || "manual"} | ${t("settings.syncWorkbuddy")}: ${item.sync?.workbuddy || "manual"}</small>
      <div class="provider-actions">
        ${(item.actions || []).map((action) => `
          <button
            type="button"
            class="provider-action remote-target ${action.selected ? "is-selected" : ""}"
            data-provider-type="${action.type}"
            data-provider-id="${item.id.replace(/^provider-/, "")}"
            data-title="${escapeHtml(item.label)}"
          >${action.type === "stt" ? t("settings.useStt") : t("settings.useTts")}${action.selected ? ` · ${t("settings.selected")}` : ""}</button>
        `).join("")}
      </div>
    </div>
  `).join("");

  document.getElementById("audio-stack").innerHTML = `
    <div class="settings-card">
      <strong>${t("settings.speechToText")}</strong>
      <p>${t("settings.provider")}: ${data.audioStack.stt.provider}</p>
      <p>${t("settings.primary")}: ${data.audioStack.stt.primaryModel}</p>
      <p>${t("settings.fallback")}: ${data.audioStack.stt.fallbackModel}</p>
      <p>${t("settings.mode")}: ${data.audioStack.stt.mode}</p>
    </div>
    <div class="settings-card">
      <strong>${t("settings.textToSpeech")}</strong>
      <p>${t("settings.provider")}: ${data.audioStack.tts.provider}</p>
      <p>${t("settings.primary")}: ${data.audioStack.tts.primaryModel}</p>
      <p>${t("settings.fallback")}: ${data.audioStack.tts.fallbackModel}</p>
      <p>${t("settings.mode")}: ${data.audioStack.tts.mode}</p>
    </div>
    <div class="settings-card">
      <strong>${t("settings.realtimeRecommendation")}</strong>
      <p>${data.audioStack.recommendedRealtime}</p>
      <p>${t("settings.currentUiLanguage")}: ${language?.label || data.voiceProfile.locale}</p>
      <p>${t("settings.totalStacks")}: ${counts.total}</p>
      <p>${t("settings.googleKey")}: ${secrets.googleConfigured ? t("settings.configured") : t("settings.missing")}</p>
      <p>${t("settings.openaiKey")}: ${secrets.openaiConfigured ? t("settings.configured") : t("settings.missing")}</p>
    </div>
    <div class="settings-card">
      <strong>${t("settings.syncOpenclaw")}</strong>
      <p>${Object.values(catalog).some((provider) => provider.sync?.openclaw) ? "Manual import / export" : "Not set"}</p>
      <p>${t("settings.syncWorkbuddy")}: Public sync API not confirmed</p>
    </div>
  `;
}

function updateSpokenLine(text) {
  document.getElementById("spoken-line").textContent = text;
  renderFloatingBuddy();
}

function updateConversation(conversation) {
  if (!latestDashboard) return;
  latestDashboard.conversation = conversation;
  renderVoice(latestDashboard);
}

function revealInScrollableParent(target) {
  const scrollParent = target.closest("#modules, #timeline, #agents, #models, #skills, #relay, #conversation, #voice");
  if (!scrollParent) return;
  target.scrollIntoView({ block: "nearest", inline: "nearest", behavior: "smooth" });
}

function getVisibleRemoteTargets() {
  return Array.from(document.querySelectorAll(".remote-target")).filter((element) => {
    const style = window.getComputedStyle(element);
    if (style.display === "none" || style.visibility === "hidden") return false;
    if (element.closest("[hidden]")) return false;
    const rect = element.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
  });
}

function getCenter(rect) {
  return { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
}

function pickDirectionalTarget(current, direction) {
  const candidates = getVisibleRemoteTargets();
  if (!current || !candidates.length) return candidates[0] || null;
  const currentRect = current.getBoundingClientRect();
  const currentCenter = getCenter(currentRect);
  let best = null;
  let bestScore = Number.POSITIVE_INFINITY;
  for (const candidate of candidates) {
    if (candidate === current) continue;
    const rect = candidate.getBoundingClientRect();
    const center = getCenter(rect);
    const dx = center.x - currentCenter.x;
    const dy = center.y - currentCenter.y;
    if (direction === "right" && dx <= 12) continue;
    if (direction === "left" && dx >= -12) continue;
    if (direction === "down" && dy <= 12) continue;
    if (direction === "up" && dy >= -12) continue;
    const primary = direction === "left" || direction === "right" ? Math.abs(dx) : Math.abs(dy);
    const secondary = direction === "left" || direction === "right" ? Math.abs(dy) : Math.abs(dx);
    const score = primary * 1000 + secondary;
    if (score < bestScore) {
      best = candidate;
      bestScore = score;
    }
  }
  return best;
}
async function triggerRemoteAction(target) {
  if (!target) return;
  if (target.dataset.tab) {
    activateTab(target.dataset.tab);
    updateSpokenLine(t("prompts.switchedTab", { tab: target.textContent }));
    return;
  }
  if (target.id === "reminder-complete") {
    await completeActiveReminder();
    return;
  }
  if (target.id === "mic-orb") {
    await toggleMicrophoneRecording();
    return;
  }
  if (target.dataset.languageCode) {
    await persistLanguage(target.dataset.languageCode);
    return;
  }
  if (target.dataset.providerType && target.dataset.providerId) {
    await persistAudioProvider(target.dataset.providerType, target.dataset.providerId);
    return;
  }
  if (target.classList.contains("fake-qr")) {
    updateSpokenLine(t("prompts.qrHighlighted"));
    return;
  }
  const title = target.dataset.title || target.querySelector("strong")?.textContent || "item";
  const actionText = target.dataset.actionText;
  if (actionText) {
    updateSpokenLine(t("prompts.actionReady", { title, action: actionText }));
    return;
  }
  updateSpokenLine(t("prompts.selected", { title }));
}

function activateTab(tabName, focusTab = true) {
  activeTab = tabName;
  tabs.forEach((name) => {
    const tab = document.getElementById(`tab-${name}`);
    const panel = document.getElementById(`panel-${name}`);
    const selected = name === tabName;
    tab.classList.toggle("is-selected", selected);
    tab.setAttribute("aria-selected", String(selected));
    tab.tabIndex = selected ? 0 : -1;
    if (selected && focusTab) tab.focus();
    panel.hidden = !selected;
    panel.classList.toggle("is-visible", selected);
  });
  renderFloatingBuddy();
}

function goToPreviousTab() {
  const currentIndex = tabs.indexOf(activeTab);
  if (currentIndex > 0) {
    activateTab(tabs[currentIndex - 1]);
    updateSpokenLine(t("prompts.returnedTab", { tab: document.getElementById(`tab-${tabs[currentIndex - 1]}`).textContent }));
  } else {
    activateTab("home");
    updateSpokenLine(t("prompts.returnedTab", { tab: document.getElementById("tab-home").textContent }));
  }
}

function setupTabs() {
  document.getElementById("tabbar").addEventListener("click", (event) => {
    const button = event.target.closest("[data-tab]");
    if (!button) return;
    activateTab(button.dataset.tab);
  });
}

function setupRemoteNavigation() {
  document.addEventListener("focusin", (event) => {
    const target = event.target;
    if (!(target instanceof HTMLElement)) return;
    if (target.classList.contains("remote-target")) revealInScrollableParent(target);
  });

  document.addEventListener("click", async (event) => {
    const target = event.target.closest(".remote-target");
    if (!target) return;
    if (target.dataset.languageCode || target.dataset.providerType || target.classList.contains("fake-qr") || target.id === "mic-orb" || target.id === "reminder-complete") {
      await triggerRemoteAction(target);
    }
  });

  document.addEventListener("keydown", async (event) => {
    const activeElement = document.activeElement;
    const keyToDirection = { ArrowRight: "right", ArrowLeft: "left", ArrowUp: "up", ArrowDown: "down" };
    if (keyToDirection[event.key]) {
      const next = pickDirectionalTarget(activeElement, keyToDirection[event.key]);
      if (next) {
        next.focus();
        revealInScrollableParent(next);
        event.preventDefault();
      }
      return;
    }
    if (event.key === "Enter" || event.key === " ") {
      if (activeElement && activeElement.classList.contains("remote-target")) {
        await triggerRemoteAction(activeElement);
        event.preventDefault();
      }
      return;
    }
    if (event.key === "Escape" || event.key === "Backspace") {
      goToPreviousTab();
      event.preventDefault();
    }
  });
}

async function loadDashboard() {
  const response = await fetch("/api/dashboard");
  const data = await response.json();
  latestDashboard = data;
  currentLocale = data.languageSettings?.current || currentLocale;
  applyStaticTranslations();
  renderClock();
  renderStatusStrip(data);
  renderHero(data);
  renderTimeline(data.timelineEvents);
  renderModules(data.householdModules);
  renderAgents(data.activeAgents);
  renderModels(data.modelProviders);
  renderSkills(data.skillCatalog);
  renderPairing(data.pairingSession, data.relayMessages);
  renderVoice(data);
  renderReminderOverlay(data);
  renderSettings(data);
  renderFloatingBuddy();
}

async function persistLanguage(languageCode) {
  const response = await fetch("/api/settings/language", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ language: languageCode })
  });
  if (!response.ok) {
    updateSpokenLine(t("prompts.saveLanguageFailed"));
    return;
  }
  currentLocale = languageCode;
  await loadDashboard();
  const language = getCurrentLanguage(latestDashboard);
  updateSpokenLine(t("prompts.languageSwitched", { language: language?.label || currentLocale }));
}

async function persistAudioProvider(providerType, providerId) {
  const catalog = latestDashboard?.audioProviders?.catalog || {};
  const provider = catalog[providerId];
  const runtime = providerType === "stt" ? provider?.stt?.runtime : provider?.tts?.runtime;
  if (runtime === "catalog") {
    updateSpokenLine(`HomeHub: ${provider?.label || providerId} is catalog-only right now.`);
    return;
  }
  const selected = getSelectedProviders();
  const body = {
    sttProvider: providerType === "stt" ? providerId : selected.stt,
    ttsProvider: providerType === "tts" ? providerId : selected.tts
  };
  const response = await fetch("/api/settings/audio", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  if (!response.ok) {
    updateSpokenLine(t("prompts.saveAudioFailed"));
    return;
  }
  await loadDashboard();
  updateSpokenLine(t("prompts.audioUpdated", { stt: body.sttProvider, tts: body.ttsProvider }));
}

async function saveCustomProvider() {
  const body = {
    entryType: "capability",
    id: document.getElementById("custom-provider-id").value.trim(),
    label: document.getElementById("custom-provider-label").value.trim(),
    source: document.getElementById("custom-source").value.trim(),
    capabilities: document.getElementById("custom-capabilities").value.trim(),
    models: document.getElementById("custom-models").value.trim(),
    summary: document.getElementById("custom-summary").value.trim(),
    syncOpenclaw: document.getElementById("custom-sync-openclaw").value,
    syncWorkbuddy: document.getElementById("custom-sync-workbuddy").value,
    supportedLanguages: document.getElementById("custom-languages").value.trim()
  };
  const response = await fetch("/api/settings/audio-provider", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  const payload = await response.json();
  if (!response.ok) {
    updateSpokenLine(payload.error || t("prompts.saveCustomProviderFailed"));
    return;
  }
  document.getElementById("custom-provider-id").value = "";
  document.getElementById("custom-provider-label").value = "";
  document.getElementById("custom-source").value = "";
  document.getElementById("custom-capabilities").value = "";
  document.getElementById("custom-models").value = "";
  document.getElementById("custom-summary").value = "";
  document.getElementById("custom-languages").value = "zh-CN,en-US,ja-JP";
  await loadDashboard();
  updateSpokenLine(t("prompts.customProviderSaved", { label: body.label || body.id }));
}
async function sendVoiceMessage(message) {
  const clean = String(message || "").trim();
  if (!clean) return;
  updateSpokenLine(`${t("speakers.you")}: ${clean}`);
  isBuddyThinking = true;
  renderFloatingBuddy();
  const response = await fetch("/api/voice/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: clean, locale: currentLocale, speakReply: false })
  });
  const payload = await response.json();
  await new Promise((resolve) => setTimeout(resolve, 380));
  isBuddyThinking = false;
  if (!response.ok) {
    updateSpokenLine(`HomeHub: ${payload.error || t("voice.sendFailure")}`);
    return;
  }
  updateConversation(payload.conversation || []);
  if (payload.voiceRoute && latestDashboard) {
    latestDashboard.lastVoiceRoute = payload.voiceRoute;
    latestDashboard.pendingVoiceClarification = payload.pendingVoiceClarification || null;
    renderVoice(latestDashboard);
  }
  if (payload.assistantMemory && latestDashboard) {
    latestDashboard.assistantMemory = payload.assistantMemory;
    renderStatusStrip(latestDashboard);
    renderVoice(latestDashboard);
    renderReminderOverlay(latestDashboard);
  }
  await loadDashboard();
  updateSpokenLine(`${localizeSpeaker("HomeHub")}: ${payload.reply}`);
  speakWithHomeHub(payload.reply);
}

async function transcribeBlob(blob) {
  const base64Audio = await new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onloadend = () => {
      const result = String(reader.result || "");
      const marker = "base64,";
      const index = result.indexOf(marker);
      if (index === -1) {
        reject(new Error("Unable to encode audio."));
        return;
      }
      resolve(result.slice(index + marker.length));
    };
    reader.onerror = () => reject(reader.error || new Error("FileReader failed."));
    reader.readAsDataURL(blob);
  });

  const provider = getSelectedProviders().stt;
  const response = await fetch("/api/audio/transcribe", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ provider, locale: currentLocale, mimeType: blob.type || "audio/webm", audioBase64: base64Audio })
  });
  const payload = await response.json();
  if (!response.ok) {
    throw new Error(payload.error || t("voice.sttFailure"));
  }
  return String(payload.transcript || "").trim();
}

async function transcribeAudioFile(file) {
  updateSpokenLine(t("voice.transcribing"));
  try {
    const transcript = await transcribeBlob(file);
    await sendVoiceMessage(transcript);
  } catch (error) {
    updateSpokenLine(`HomeHub: ${error.message || t("voice.sttFailure")}`);
  }
}

async function toggleMicrophoneRecording() {
  if (!navigator.mediaDevices?.getUserMedia) {
    updateSpokenLine(`HomeHub: ${t("voice.browserNoMic")}`);
    return;
  }
  const micCore = document.querySelector("#mic-orb .mic-core");
  const micOrb = document.getElementById("mic-orb");
  if (isRecording && mediaRecorder && mediaRecorder.state === "recording") {
    mediaRecorder.stop();
    isRecording = false;
    micCore.textContent = t("voice.micIdle");
    micOrb.classList.remove("is-recording");
    updateSpokenLine(t("prompts.recordingStopped"));
    return;
  }

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaChunks = [];
    const preferredMimeType = MediaRecorder.isTypeSupported("audio/webm;codecs=opus")
      ? "audio/webm;codecs=opus"
      : MediaRecorder.isTypeSupported("audio/ogg;codecs=opus")
        ? "audio/ogg;codecs=opus"
        : "";
    mediaRecorder = preferredMimeType ? new MediaRecorder(stream, { mimeType: preferredMimeType }) : new MediaRecorder(stream);
    const activeMimeType = mediaRecorder.mimeType || preferredMimeType || "audio/webm";
    mediaRecorder.ondataavailable = (event) => {
      if (event.data.size > 0) mediaChunks.push(event.data);
    };
    mediaRecorder.onstop = async () => {
      stream.getTracks().forEach((track) => track.stop());
      mediaRecorder = null;
      const blob = new Blob(mediaChunks, { type: activeMimeType });
      updateSpokenLine(t("voice.transcribing"));
      try {
        const transcript = await transcribeBlob(blob);
        await sendVoiceMessage(transcript);
      } catch (error) {
        updateSpokenLine(`HomeHub: ${error.message || t("voice.sttFailure")}`);
      }
    };
    mediaRecorder.start();
    isRecording = true;
    micCore.textContent = t("voice.micRecording");
    micOrb.classList.add("is-recording");
    updateSpokenLine(t("prompts.recordingStarted"));
  } catch (error) {
    mediaRecorder = null;
    micCore.textContent = t("voice.micIdle");
    micOrb.classList.remove("is-recording");
    updateSpokenLine(t("prompts.micAccessFailed", { error: String(error) }));
  }
}

function setupVoiceControls() {
  const micCore = document.querySelector("#mic-orb .mic-core");
  if (micCore) {
    micCore.textContent = t("voice.micIdle");
  }
}

function setupFloatingBuddyControls() {
  const shell = document.getElementById("floating-buddy");
  if (!shell) return;

  const startDrag = (clientX, clientY) => {
    const rect = shell.getBoundingClientRect();
    buddyDragState.dragging = true;
    buddyDragState.offsetX = clientX - rect.left;
    buddyDragState.offsetY = clientY - rect.top;
    shell.classList.add("is-dragging");
  };

  const moveDrag = (clientX, clientY) => {
    if (!buddyDragState.dragging) return;
    const next = clampBuddyPosition(clientX - buddyDragState.offsetX, clientY - buddyDragState.offsetY, shell);
    buddyDragState.x = next.x;
    buddyDragState.y = next.y;
    shell.style.right = "auto";
    shell.style.bottom = "auto";
    shell.style.left = `${next.x}px`;
    shell.style.top = `${next.y}px`;
  };

  const stopDrag = () => {
    if (!buddyDragState.dragging) return;
    buddyDragState.dragging = false;
    shell.classList.remove("is-dragging");
    persistBuddyPosition();
  };

  shell.addEventListener("pointerdown", (event) => {
    startDrag(event.clientX, event.clientY);
  });
  window.addEventListener("pointermove", (event) => {
    moveDrag(event.clientX, event.clientY);
  });
  window.addEventListener("pointerup", stopDrag);
  window.addEventListener("resize", () => {
    if (buddyDragState.x === null || buddyDragState.y === null) return;
    const next = clampBuddyPosition(buddyDragState.x, buddyDragState.y, shell);
    buddyDragState.x = next.x;
    buddyDragState.y = next.y;
    shell.style.left = `${next.x}px`;
    shell.style.top = `${next.y}px`;
  });
}

function setupCustomProviderControls() {
  const saveButton = document.getElementById("custom-provider-save");
  const languagesInput = document.getElementById("custom-languages");
  if (languagesInput && !languagesInput.value) {
    languagesInput.value = "zh-CN,en-US,ja-JP";
  }
  saveButton.addEventListener("click", async () => {
    await saveCustomProvider();
  });
}

function setupReminderOverlayControls() {
  const completeButton = document.getElementById("reminder-complete");
  if (!completeButton) return;
  const runComplete = async (event) => {
    if (event) {
      event.preventDefault();
      event.stopPropagation();
    }
    await completeActiveReminder();
  };
  completeButton.onclick = runComplete;
  completeButton.addEventListener("pointerup", runComplete);
  completeButton.addEventListener("keydown", async (event) => {
    if (event.key === "Enter" || event.key === " ") {
      await runComplete(event);
    }
  });
}

setupTabs();
setupRemoteNavigation();
setupVoiceControls();
setupCustomProviderControls();
setupReminderOverlayControls();
loadBuddyPosition();
setupFloatingBuddyControls();
applyStaticTranslations();
activateTab("home", false);
renderClock();
loadDashboard();
setInterval(renderClock, 1000);
setInterval(loadDashboard, 5000);
