# HomeHub Cortex

`runtime/cortex` is HomeHub's per-agent brain layer.

It does not pretend that every custom agent already owns a separately trained foundation model. Instead, it gives each agent a local evolving profile that can later drive routing, personalization, distillation, or fine-tuning.

## What It Stores

- Blueprint digest: mission, trigger, inputs, outputs, constraints, network policy
- Usage traces: draft creation, question answering, confirmation, intake, attachment handling, lookup usage
- Working signals: preferred input modes, recurring topics, local vs network dependence, cautious/proactive structure
- Evolution snapshot: personalization score, stage, recommended brain, next upgrade

## Current Stages

- `seed`: just created, still collecting structure
- `learning`: some interactions exist, but not enough to specialize
- `adapting`: enough repeated behavior to use memory-shaped routing
- `specialized`: enough stable traces to justify a dedicated routing profile or future distilled model

## Why This Exists

The user asked whether every HomeHub agent could gradually form "its own model" through repeated use.

The safe implementation path is:

1. Build a per-agent cortex first
2. Let it accumulate stable traces and preferences
3. Use readiness signals to decide when a personalized route is justified
4. Only then consider heavier steps such as distillation, adapter tuning, or local task-specific models

This keeps the system honest: HomeHub can evolve like a brain before it evolves like a training pipeline.
