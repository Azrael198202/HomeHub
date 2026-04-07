# HomeHub Runtime 与 Services 执行逻辑整理

## 1. 总体分层

- `runtime/`
  - Python 主运行时，负责 Web API、静态页面、语音路由、模型/音频能力选择、Feature 动态装载、后台同步任务。
- `services/`
  - 轻量 Node 服务层，当前主要用于演示或拆分后的独立接口原型。
- `packages/shared/`
  - 给 `apps/` 和 `services/` 共用的演示数据与类型定义。

## 2. runtime 的主入口

### 2.1 `runtime/server.py`

这是 HomeHub 的主控制器，承担了绝大多数运行时职责。

启动时主要做这些事：

1. 读取路径、环境变量、模型提供方、音频提供方、语言设置、默认 UI 数据。
2. 加载 secrets、settings、bootstrap 状态、Home memory。
3. 构建 `FEATURE_MANAGER`，扫描 `runtime/features/` 下所有功能模块。
4. 启动两个后台线程：
   - `run_background_email_sync()`
   - `run_background_bridge_pull()`
5. 启动 `ThreadingHTTPServer`，由 `Handler` 统一处理 HTTP 请求。

### 2.2 `runtime/api_server.py`

这是 `server.py` 的 API-only 包装器：

- 复用 `server.py` 里的 `Handler`
- 根路径 `/` 返回健康信息
- 只允许 `/api/*` 请求继续走主逻辑
- 适合部署成纯 API 服务，不暴露静态前端

## 3. runtime 的请求执行流

### 3.1 GET 请求

`runtime/server.py` 里的 `Handler.do_GET()` 大致按下面顺序执行：

1. 解析 URL 与 query 参数。
2. 构建 `RuntimeBridge`。
3. 先交给 `FEATURE_MANAGER.handle_api("GET", ...)`，让 feature 抢先处理自己的 API。
4. 如果 feature 没接管，再处理内建路由。

内建 GET 路由主要分几类：

- 静态页面与资源
  - `/`
  - `/index.html`
  - `/assets/app.css`
  - `/assets/app.js`
- 动态生成文件
  - `/generated/*`
- 运行时信息类 API
  - 仪表盘、设置、模型、音频、配对、语音路由、能力目录、bootstrap 状态等

### 3.2 POST 请求

`Handler.do_POST()` 的执行顺序更明显：

1. 读取 body。
2. 解析 JSON / 文本，并附带 headers、raw body 作为预览上下文。
3. 先交给 `FEATURE_MANAGER.handle_api("POST", ...)`。
4. 如果 feature 没有处理，再进入内建 POST 路由。

内建 POST 路由主要有：

- 设置类
  - `/api/settings/language`
  - `/api/settings/audio`
  - `/api/settings/secrets`
  - `/api/settings/audio-provider`
- bootstrap
  - `/api/bootstrap/approve`
- 音频能力
  - `/api/audio/transcribe`
  - `/api/audio/synthesize`
- 网络检索
  - `/api/network/query`
- 语音对话
  - `/api/voice/chat`
  - `/api/voice/reset`

## 4. 语音与任务路由主链路

HomeHub 的核心交互主线是：

1. 用户发消息到 `/api/voice/chat`
2. `resolve_voice_request()` 负责总调度
3. 内部先做语言识别：
   - `detect_text_locale()`
   - `normalize_locale()`
4. 再做任务规格判断：
   - `build_task_spec()`
   - 可选 AI 判断：`infer_task_spec_with_openai()`
   - 否则走规则推断：`apply_rule_based_task_hints()`
5. 构建工具计划与模型路线：
   - `build_tool_plan()`
   - `select_model_route()`
6. 执行具体分支：
   - UI 导航
   - feature intent
   - 网络检索
   - 通用聊天
   - schedule/reminder 等本地能力
7. 需要时调用 `synthesize_speech()` 生成回复音频
8. 把结果、会话、路由、UI action、artifact 一起返回前端

相关基础组件：

- `runtime/server_components/language_detector.py`
  - 识别文本/文档语言，统一 locale。
- `runtime/server_components/greetings.py`
  - 生成开场欢迎语和初始对话。
- `runtime/server_components/task_router.py`
  - 负责把自然语言请求归类成 task spec。

## 5. 运行时能力选择与模型/音频逻辑

`runtime/server.py` 里还有一层“能力编排”：

- 模型/供应商目录
  - `MODEL_PROVIDERS`
  - `get_audio_provider_catalog()`
  - `build_ai_capability_catalog()`
- 本地模型库存
  - `load_ollama_inventory()`
  - `find_ollama_binary()`
- 运行策略
  - `get_runtime_profile()`
  - `build_runtime_strategy()`
  - `select_model_route()`

音频链路：

- 语音转文字
  - `transcribe_audio()`
  - 可落到 Google / OpenAI / 本地能力
- 文字转语音
  - `synthesize_speech()`
  - 根据当前设置选择 TTS provider

图像与 OCR 链路：

- `analyze_image_with_homehub()`
- `openai_vision_json()`
- `ollama_vision_json()`

网络检索链路：

- `perform_controlled_network_lookup()`
- 只在受控策略下抓取外部网页或 Wikipedia

## 6. Feature 动态装载机制

### 6.1 `runtime/features/base.py`

定义了两个核心抽象：

- `RuntimeBridge`
  - Feature 调用主运行时能力的桥。
  - 可以拿 setting、secret、OpenAI JSON、图像分析、网络检索、Feature 调用等能力。
- `HomeHubFeature`
  - 所有功能模块的基类。
  - 规范了：
    - `descriptor()`
    - `voice_intents()`
    - `handle_voice_chat()`
    - `run_feature()`
    - `dashboard_payload()`
    - `handle_api()`
    - `reset()`

### 6.2 `runtime/features/loader.py`

`FeatureManager` 的职责：

1. 扫描 `runtime/features/**/*.py`
2. 跳过 `_` 开头、`base.py`、`loader.py`、`__init__.py`
3. 动态 import 每个 feature 文件
4. 要求模块暴露：
   - `load_feature()` 或
   - `Feature` 类
5. 在刷新时调用 `feature.on_refresh(runtime)`
6. 对外提供这些聚合入口：
   - `list_features()`
   - `route_voice_intent()`
   - `dispatch_voice_intent()`
   - `invoke_feature()`
   - `enhance_household_modules()`
   - `dashboard_payload()`
   - `list_agent_types()`
   - `handle_api()`
   - `reset()`

### 6.3 各 Feature 的职责

#### `runtime/features/local_schedule.py`

- 本地日程与提醒功能
- 数据存储：`runtime/home_memory.json`
- 支持：
  - 建事件
  - 建提醒
  - 查询 upcoming / pending / due
  - 用语音统一操作 schedule/reminder
- 也会把内容投到 dashboard / memory 视图里

#### `runtime/features/document_ocr.py`

- 文档/票据 OCR 能力
- 优先尝试本地 RapidOCR
- 识别：
  - 文本
  - 商户
  - 日期
  - 支付方式
  - 税额
  - 内容类型
- 结果会形成结构化分析，供后续 feature 或 UI 使用

#### `runtime/features/external_channels.py`

- 外部渠道总线
- 管理：
  - WeChat Official Account
  - LINE
  - Email
  - External bridge
- 主要 API：
  - webhook 接收
  - outbound send
  - email intake/send/sync
  - bridge inbound/pull/result
- 负责把外部消息拉回 HomeHub 内部统一处理

#### `runtime/features/custom_agents.py`

- 自定义智能体工作室
- 负责：
  - 收集蓝图
  - 追问缺失信息
  - 确认蓝图
  - 生成 feature scaffold
  - 给 agent 建立 cortex 画像
- 主要数据：
  - `runtime/agents/custom_agents.json`
  - `runtime/agents/cortex_profiles.json`

#### `runtime/features/study_plan_agents.py`

- 学习计划类智能体工厂
- 为不同孩子/年级创建长期 study-plan agent
- 支持继续编辑、克隆、查看、回顾

#### `runtime/features/customize/u5bb6_u5ead_u8d26_u5355_feature.py`

- 家庭账单/消费记录类 feature
- 负责：
  - 记录支出
  - 归类账单
  - 汇总统计
  - 导出文件

## 7. Cortex 子系统

`runtime/cortex/` 是给长期智能体做“状态画像”的。

### `runtime/cortex/store.py`

- `CortexStore`
- 负责把 cortex 数据读写到：
  - `runtime/agents/cortex_profiles.json`

### `runtime/cortex/core.py`

- `AgentCortex`
- 负责：
  - `sync_agent()`
    - 把 agent 蓝图同步成 cortex state
  - `record_event()`
    - 记录 agent 的运行事件
  - `get_summary()`
    - 输出某个 agent 的画像摘要
  - `summaries_for()`
    - 批量汇总

### `runtime/cortex/reasoning.py`

- 负责把蓝图和事件转成“信号”
- 输出 evolution / topics / stats 等演化视图

## 8. runtime 的后台线程

### `run_background_email_sync()`

- 周期性触发 email 同步
- 本质上会走 `external_channels` feature 的邮件能力

### `run_background_bridge_pull()`

- 周期性拉外部 bridge 的待处理消息
- 让 HomeHub 能持续吸收外部系统投递过来的任务

## 9. services 目录的执行逻辑

### 9.1 `services/core-engine/`

#### `src/server.mjs`

Node HTTP 服务，提供几个演示型接口：

- `/health`
  - 健康检查
- `/providers`
  - 返回模型提供方列表
- `/skills`
  - 返回技能目录
- `/run`
  - 返回一次并行任务模拟结果
- `/dashboard`
  - 返回 agent + timeline 仪表盘数据

#### `src/providers.js`

- `listModelProviders()`
  - 返回共享 demo-data 中的 provider 列表
- `resolveProviderByCapability(capability)`
  - 按能力过滤 provider

#### `src/skills.js`

- `loadSkills()`
  - 把共享 skill catalog 包装成带 `canHandle(inputMode)` 的对象

#### `src/agents.js`

- `getAgentDashboard()`
  - 聚合 agents 和 timeline
- `simulateParallelRun(task)`
  - 返回模拟 fanout 执行信息

结论：

- `core-engine` 现在更像“编排层原型服务”
- 还没有真正执行 AI 推理，只是在暴露演示数据和调度结构

### 9.2 `services/companion-api/`

#### `src/server.mjs`

这是移动伴侣/API 原型服务，主要暴露静态状态数据：

- `/health`
- `/box`
- `/pairing`
- `/modules`
- `/timeline`
- `/relay`
- `/voice`
- `/relay/policy`

用途：

- 给移动端或演示端读取 HomeHub box 状态、配对信息、模块摘要、relay 消息等

### 9.3 `services/voice-gateway/`

#### `src/index.mjs`

- 目前不是常驻 HTTP 服务
- 只是输出一个 `voiceGatewayProfile`
- 描述 STT/TTS 的主备策略：
  - STT: on-device whisper -> cloud fallback
  - TTS: cloud neural voice -> system tts fallback

用途：

- 更像语音网关的配置说明原型

## 10. apps / shared 与 services 的关系

### `packages/shared/`

- `src/contracts.ts`
  - TS 类型定义
- `src/demo-data.ts` / `src/demo-data.js`
  - 给 TV shell 和 Node services 共用的演示数据

### `apps/tv-shell/`

- `src/data.ts`
  - 从 `packages/shared/src/demo-data.js` 取数
- `src/App.tsx`
  - 把 box、timeline、agents、skills、voice、pairing 渲染成 TV 仪表盘

所以目前数据流是：

`packages/shared` -> `services/*` 和 `apps/tv-shell`

而 `runtime/` 是另一套更完整、动态、可扩展的 Python 运行时实现。

## 11. 一句话总结

- `runtime/` 是真正的 HomeHub 主运行时，负责 API、语音、Feature、模型选择、后台同步。
- `services/` 是 Node 侧的轻量服务/原型层，主要暴露演示数据和拆分后的接口雏形。
- `features/` 是 runtime 的插件化能力中心。
- `cortex/` 是长期智能体状态画像系统。
- `server_components/` 是语音/语言/任务路由的基础设施层。
