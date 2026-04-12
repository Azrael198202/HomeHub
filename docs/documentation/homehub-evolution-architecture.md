# HomeHub Evolution Architecture

- Date: 2026-04-10
- Branch baseline: `feature/homehub-research-knowledge-context`
- Scope: evolve HomeHub without replacing the current runtime execution spine

## 1. Goal

HomeHub should remain a household-first execution system:

- Understand the user's goal
- Route the request into the correct execution lane
- Decide whether to answer locally, use feature logic, use local knowledge, or do external research
- Keep task context across multiple steps
- Support controlled local execution for file-system work
- Create new household agents/features when the current system has a capability gap

HomeHub should not become a default high-permission developer coding agent.

## 2. Current Execution Spine To Preserve

The current HomeHub flow is already a strong base and should stay intact:

1. User input enters `resolve_voice_request()`
2. HomeHub builds a `taskSpec`
3. HomeHub routes into `feature`, `general`, `agent_factory`, or `clarify`
4. HomeHub builds a tool plan and model route
5. HomeHub executes through feature handlers or direct runtime handlers
6. HomeHub can promote a weak answer into controlled network lookup
7. HomeHub returns reply, UI actions, artifacts, and route metadata

This means the evolution should be additive, not a rewrite.

## 3. Final Architecture

### 3.1 Core Layers

HomeHub should be structured into these cooperating layers:

1. `Routing Layer`
   - Existing responsibility
   - Builds `taskSpec`
   - Chooses route kind
   - Selects tool plan and model route

2. `Research Layer`
   - Handles external information gathering
   - Replaces the current lightweight fetch-only network path with a full research pipeline

3. `Knowledge Layer`
   - Stores reusable non-real-time knowledge
   - Separates route memory from long-term knowledge memory

4. `Context Layer`
   - Maintains the unified task execution context
   - Carries state across reasoning, retrieval, feature execution, and response building

5. `Controlled Local Executor`
   - Handles safe local execution for household tasks, especially file-system operations

6. `Feature Builder`
   - Creates new household agents/features when HomeHub detects a capability gap
   - Generates controlled feature code in the customize area and lets the runtime auto-load it

### 3.2 Explicit Non-Goal

HomeHub should not, in this phase, become:

- A general-purpose coding agent
- A default arbitrary shell executor
- A high-permission autonomous repo modification system

## 4. Research Layer

## 4.1 Why It Is Needed

The current controlled network path is useful but shallow:

- It can fetch allowed URLs
- It can fall back to Wikipedia
- It can synthesize a short grounded answer

It does not yet behave like a proper research workflow.

## 4.2 Required Pipeline

When HomeHub needs external research, it should use this pipeline:

1. Search candidate pages
2. Fetch page content
3. Extract structured fields:
   - title
   - url
   - source/domain
   - publish time when available
   - cleaned body text
4. Remove:
   - navigation
   - ads
   - footer
   - unrelated boilerplate
5. Generate a short per-page summary
6. Produce a final synthesized answer over the summaries

## 4.3 Output Contract

Research should return structured evidence, not raw pages.

Suggested evidence item:

```json
{
  "title": "...",
  "url": "...",
  "source": "...",
  "publishedAt": "...",
  "cleanText": "...",
  "summary": "...",
  "score": 0.0
}
```

The final answer path should consume evidence items and not the full raw page bodies.

## 4.4 Provider Strategy

The architecture should support pluggable providers:

- Search providers:
  - Tavily
  - SerpAPI
  - Bing Search
  - Google Custom Search
- Fetch/extraction providers:
  - `requests + BeautifulSoup`
  - `Playwright` when dynamic rendering is required

Provider selection should stay configurable and should not be hard-coded into the routing layer.

## 5. Knowledge Layer

## 5.1 Split Memory Model

HomeHub should use two different memory roles:

1. `routing_memory`
   - Stores route corrections and semantic examples
   - Helps task classification and route disambiguation

2. `knowledge_memory`
   - Stores stable, reusable, non-real-time knowledge
   - Used for retrieval-augmented answering when the local model lacks knowledge

## 5.2 Writeback Rules

HomeHub should only write new knowledge into long-term knowledge memory when:

- The local model does not already know the answer well enough
- The knowledge store does not already contain the information
- The result is not strongly real-time
- The source is trustworthy enough
- The content was cleaned and summarized first
- The information is likely reusable in future tasks

HomeHub should not store:

- transient news
- unstable prices
- dynamic rankings
- highly time-sensitive status pages

## 5.3 Storage Backends

The architecture should allow a vector backend such as:

- Weaviate
- Chroma
- FAISS

The backend should be behind a small storage interface so HomeHub does not depend on one specific provider.

## 6. Context Layer

## 6.1 Problem

Current runtime state exists in several places:

- pending clarification
- feature stores
- cortex state
- route payload
- semantic memory

This works, but multi-step tasks still lack a single execution context object.

## 6.2 Required Context Shape

HomeHub should maintain one task execution context that can move through routing, feature execution, research, and response synthesis.

Suggested fields:

```json
{
  "goal": "",
  "taskSpec": {},
  "route": {},
  "toolPlan": [],
  "modelRoute": {},
  "artifacts": [],
  "toolResults": [],
  "evidence": [],
  "retrievedKnowledge": [],
  "intermediateConclusions": [],
  "failures": [],
  "nextStep": "",
  "memoryWriteback": {}
}
```

## 6.3 Benefits

This context layer lets HomeHub:

- reason across multiple steps
- degrade gracefully
- explain why it chose a path
- decide what to store
- avoid scattering task state across unrelated modules

## 7. Controlled Local Executor

## 7.1 Why It Stays In Scope

HomeHub is household-first, but it still needs local execution for practical tasks, especially local file handling.

This means local execution should remain, but only in a controlled form.

## 7.2 Allowed Scope

Controlled local execution should support:

- list directories
- search files
- read files
- write text files
- move files
- rename files
- copy/export files
- delete with confirmation
- limited white-listed helper commands for household workflows

## 7.3 Safety Rules

The executor should enforce:

- path validation
- protected path boundaries
- confirmation for destructive actions
- structured return payloads
- action logging
- white-listed command families only

This is not a general shell.

## 8. Agent, Skill, Executor, and Feature Builder

## 8.1 Definitions

HomeHub should use these definitions consistently:

- `Agent`
  - the smallest business execution unit
  - owns a long-running or reusable household responsibility

- `Skill`
  - a capability an agent can call
  - examples: OCR, research, local files, export, reminders

- `Executor`
  - the runtime mechanism that actually performs the work
  - examples: Python handler, local file executor, research pipeline

- `Feature Builder`
  - a controlled code-generation path that creates a missing household feature/agent

## 8.2 Why Feature Builder Is Needed

If HomeHub does not already have a fitting household agent, it must be able to create one.

This should happen through a controlled path:

1. detect capability gap
2. generate agent blueprint
3. generate a feature file in `runtime/features/customize/`
4. let the feature loader auto-load it
5. use the newly added feature in later runs

This is code generation, but it is not the same as a full coding agent.

## 8.3 Why A Full Coding Agent Is Deferred

A full coding agent would add:

- arbitrary repo reading and modification
- broad shell execution
- debugging loops
- much higher permission and safety complexity

That is not required for the current HomeHub household product direction.

## 9. Implementation Direction

The implementation should be staged.

### Stage A: Research Foundation

- add research context structures
- add search/fetch/extract/summary interfaces
- integrate research results into the current network answer path

### Stage B: Knowledge Foundation

- split routing memory from long-term knowledge memory
- add knowledge retrieval before research fallback
- add writeback rules after successful research

### Stage C: Unified Context

- create a shared execution context object
- thread it through route selection, feature execution, research, and answer synthesis

### Stage D: Controlled Executor and Feature Builder Cleanup

- formalize local execution boundaries
- keep local file operations in the safe household lane
- formalize feature-builder creation flow for missing agents

## 10. Code-Level Mapping

This evolution should extend, not replace, the current files:

- `runtime/server_voice.py`
  - keep as the main voice resolution path
  - thread execution context through it

- `runtime/server_components/task_router.py`
  - keep task classification logic
  - integrate knowledge-aware decision hints

- `runtime/server_network.py`
  - evolve into a research-capable network layer

- `runtime/features/custom_agents.py`
  - keep as the agent/factory and feature-builder center
  - formalize capability-gap detection and generated feature lifecycle

- `runtime/features/local_files.py`
  - keep as the household-safe local executor entry point

## 11. Final Decision Summary

HomeHub will:

- preserve the current routing-and-feature execution spine
- add a proper research layer
- add a real knowledge layer
- add a unified execution context layer
- retain controlled local execution for file-system work
- retain a controlled feature-builder path for missing agents

HomeHub will not, in this phase:

- become a full default coding agent
- expose arbitrary shell execution
- shift its product identity from household assistant to developer agent
