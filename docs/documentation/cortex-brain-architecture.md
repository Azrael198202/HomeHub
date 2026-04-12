# HomeHub Cortex Brain Architecture

## Goal

This cortex layer turns HomeHub into a brain with three explicit zones:

- `pre-brain`
  - normalize text, voice, and image into one command packet
- `exec-brain`
  - find or create the right execution units, compile taskflow, and run it
- `repo-brain`
  - package results into text, voice, and multimodal artifacts

The design follows the current HomeHub runtime instead of replacing it:

- `runtime/server.py` remains the runtime entry
- `runtime/features/*` remains the execution surface
- `runtime/cortex/*` becomes the brain designer and specialization layer

## File Layout

- `runtime/cortex/catalog.py`
  - functional model library split into `local`, `cloud`, `huggingface`
  - returns role-based model assignments
- `runtime/cortex/brains.py`
  - builds `pre-brain`, `exec-brain`, `repo-brain`
  - builds taskflow and memory contracts
- `runtime/cortex/architect.py`
  - compiles one cortex state into a complete brain blueprint
- `runtime/cortex/core.py`
  - keeps current `AgentCortex` APIs
  - now also exposes brain and taskflow interfaces
- `runtime/cortex/store.py`
  - persists cortex items and meta schema
- `runtime/cortex/models.py`
  - default state shape
- `runtime/cortex/reasoning.py`
  - behavior/evolution scoring

## Model Split

### Local models

- `qwen2.5:1.5b-instruct`
  - router / triage
- `qwen2.5:3b-instruct`
  - semantic understanding / response draft
- `qwen2.5:7b-instruct`
  - planner / executor
- `qwen2.5-coder:7b`
  - workflow compiler / artifact builder
- `qwen2.5vl:7b`
  - vision / OCR fallback / document understanding

### Cloud models

- `gpt-5.4`
  - deep planner / complex controller
- `gpt-5.4-mini`
  - fast controller / response polish
- `Gemini multimodal`
  - image-heavy and document-heavy reasoning
- `Anthropic long-context reasoner`
  - policy-heavy and long-document synthesis

### Hugging Face references

- `BAAI/bge-m3`
  - multilingual embeddings / repo-brain memory
- `BAAI/bge-reranker-v2-m3`
  - reranking
- `paraphrase-multilingual-MiniLM-L12-v2`
  - semantic matching / brain lookup
- `jina-embeddings-v4`
  - multimodal document memory
- `audio-flamingo-3-hf`
  - future audio-text reasoning

## Required Technologies

The following technologies are now explicitly represented in the cortex design:

1. `Vector Database`
   - used for semantic memory, smart-unit lookup, and health/archive retrieval
2. `LangChain / LangGraph`
   - used as the graph orchestration target for exec-brain taskflows
3. `RAG`
   - used for grounded reasoning over local and external evidence
4. `Elasticsearch`
   - used for keyword and hybrid search over OCR text, reports, and structured records
5. `Fine-Tuning`
   - reserved for later specialization, not required for the first working brain
6. `Agents`
   - actively used as the smallest execution units
7. `LoRA`
   - reserved for later lightweight local specialization

Additional support technologies used because they are necessary:

- event sourcing
- policy engine
- structured extraction
- multimodal indexing
- artifact compiler
- memory adapters

## Current Interfaces Left For Runtime

This version intentionally leaves clean interfaces for the current runtime:

- `RuntimeBridge.openai_json`
- `RuntimeBridge.analyze_image`
- `RuntimeBridge.network_lookup`
- `RuntimeBridge.call_feature`
- `FeatureManager.list_features`
- `FeatureManager.invoke_feature`
- `FeatureManager.route_voice_intent`

Current HTTP/runtime entrypoints that still remain valid:

- `/api/voice/chat`
- `/api/audio/transcribe`
- `/api/audio/synthesize`
- `/api/network/query`
- `/api/custom-agents`

## New Cortex Interfaces

`AgentCortex` now keeps compatibility and adds:

- `get_brain(agent_id, request=None)`
  - return the full brain blueprint
- `brains_for(agents, request=None)`
  - batch brain blueprint lookup
- `compile_request(agent_id, request=None)`
  - return only the compiled taskflow

Existing methods still work:

- `sync_agent(...)`
- `record_event(...)`
- `get_summary(...)`
- `summaries_for(...)`

## Validation Principle

This cortex version no longer treats any single vertical scenario as the default template.

The validation target is now:

1. the user raises a requirement
2. HomeHub normalizes the requirement into capability needs
3. HomeHub checks whether an existing smart unit is sufficient
4. only if the capability gap is real does HomeHub create a new smart unit
5. HomeHub decides by itself whether OCR, search, RAG, archive writing, follow-up questioning, or artifact generation are needed

Example domains are only demos, not templates:

- hospital report analysis
- weekly family bill review
- trip planning
- study-plan assistant
- device setup assistant

The logic is represented in:

- `runtime/cortex/requirements.py`
- `runtime/cortex/use_cases.py`
- `runtime/cortex/tech.py`
- `runtime/cortex/architect.py`

## Design Principle

The cortex layer does not hardcode a single model as “the brain”.
It treats the brain as:

1. input normalization
2. function-based model routing
3. taskflow compilation
4. persistent specialization memory
5. multimodal result packaging

That matches HomeHub better than a single-model architecture because the project already has:

- voice entry
- image entry
- feature plugins
- local and cloud model paths
- generated artifacts
- long-lived custom agents
