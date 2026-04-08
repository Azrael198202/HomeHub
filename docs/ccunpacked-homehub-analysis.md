# ccunpacked.dev Analysis For HomeHub

Source analyzed: https://ccunpacked.dev/

## What the site is doing well

`ccunpacked.dev` is not just a landing page. It turns a complex AI coding system into a navigable explanation product.

Key patterns:

- Agent loop first:
  It explains the lifecycle from user input to render in a visible step-by-step chain.
- Architecture as exploration:
  It exposes folders, tool groups, and commands as things users can click through.
- Tooling made concrete:
  It groups tools by job, not by implementation detail.
- Hidden features surfaced:
  It shows what exists, what is gated, and what is experimental.
- Source-backed trust:
  It anchors explanations in source references instead of pure marketing.

## Sections mapped from the site

### 1. Agent Loop

The site explains a full request lifecycle:

- Input
- Message
- History
- System
- API
- Tokens
- Tools
- Loop
- Render
- Hooks
- Await

HomeHub reference:

- Build a visible HomeHub loop view:
  `voice/text/image -> normalize -> route -> retrieve -> agent reuse/create -> execute -> render -> learn`

### 2. Architecture Explorer

The site exposes source tree categories such as:

- tools and commands
- core processing
- UI layer
- infrastructure
- support and utilities
- personality and UX

HomeHub reference:

- Expose `runtime`, `features`, `cortex`, `services`, `server_components` as a live explorer.
- Let users inspect:
  - active routes
  - loaded features
  - cortex brains
  - semantic memory backend
  - current model routing

### 3. Tool System

The site groups tools by purpose:

- file operations
- execution
- search and fetch
- agents and tasks
- planning
- MCP
- system
- experimental

HomeHub reference:

- Show HomeHub capabilities by job:
  - speech
  - OCR
  - semantic memory
  - network research
  - custom agents
  - schedule/reminders
  - artifact generation
  - bridge/external channels

### 4. Command Catalog

The site presents commands as a discoverable operating surface.

HomeHub reference:

- Build a HomeHub command surface for:
  - reset voice memory
  - inspect semantic memory
  - export training pairs
  - inspect agent draft reasoning
  - force rebuild cortex profile
  - refresh local model inventory

### 5. Hidden Features

The site clearly separates:

- shipped features
- env-gated features
- experimental features
- internal but not launched features

HomeHub reference:

- Add explicit status labels:
  - stable
  - experimental
  - local-only
  - cloud-required
  - planned

This is especially useful for:

- Qdrant mode
- OCR fallback layers
- autonomous agent creation
- LoRA export pipeline
- long-running background agents

## Best ideas HomeHub should borrow

### A. Make the brain visible

HomeHub should not only *have* a cortex. It should expose:

- current pre-brain inputs
- current exec-brain decision
- whether an existing agent was reused
- whether a new agent was drafted
- which memory backend answered
- whether network research was used

### B. Make routing inspectable

For every request, HomeHub should show:

- detected locale
- task spec
- selected feature
- selected model route
- retrieval hits
- network sources
- final execution plan

### C. Treat tools as a product surface

HomeHub already has many capabilities, but they are still mostly code-level concepts.
This site shows the value of turning internal capability into visible product language.

### D. Separate stable vs experimental

This helps users trust the system and helps development planning.

## Recommended HomeHub implementation

### Short-term

- Add a dashboard section called `Request Loop`
- Add a dashboard section called `Capability Explorer`
- Add a dashboard section called `Semantic Memory Backend`
- Add a dashboard section called `Experimental Features`

### Mid-term

- Add per-request trace cards
- Add agent creation/reuse explanation panels
- Add vector backend health cards
- Add a command palette for debug and operator actions

### Long-term

- Build a full `HomeHub Unpacked` page
- Link each visible module to source files and runtime status
- Let users replay a request through the whole loop

## HomeHub impact

If HomeHub borrows the right patterns from `ccunpacked.dev`, the gain is not just visual polish.

It would improve:

- explainability
- debugging
- user trust
- onboarding
- agent design transparency
- model and memory observability
