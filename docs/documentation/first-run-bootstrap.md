# HomeHub First-Run Bootstrap

HomeHub now includes a first-run bootstrap step before startup.

## What It Prepares

- Base developer tools: `git`, `node`, `npm`, `ollama`
- Local Python document stack: `python-docx`, `openpyxl`, `python-pptx`, `pypdf`, `pillow`, `rapidocr-onnxruntime`
- Local Ollama models:
  - `qwen2.5:1.5b-instruct`
  - `qwen2.5:3b-instruct`
  - `qwen2.5:7b-instruct`
  - `qwen2.5-coder:7b`
  - `qwen2.5vl:7b`
- Default runtime files:
  - `runtime/settings.json`
  - `runtime/secrets.local.json`

## Startup Behavior

The startup scripts now call `tools/bootstrap_homehub.py --apply --quiet` before launching the runtime:

- [start_homehub.bat](/Users/home/workspace/HomeHub/start_homehub.bat)
- [start_homehub.ps1](/Users/home/workspace/HomeHub/start_homehub.ps1)
- [start_homehub.sh](/Users/home/workspace/HomeHub/start_homehub.sh)

## Why These Models

- `qwen2.5vl:7b`: OCR-style understanding, screenshots, receipts, mixed document vision
- `qwen2.5-coder:7b`: deterministic file-oriented generation and automation helpers
- `qwen2.5:*instruct`: local fallback chat and routing
- Python document libraries: actual `.pptx`, `.xlsx`, `.docx` creation and editing

This gives HomeHub a usable first-run path for OCR, PowerPoint, Excel, and Word workflows instead of requiring manual setup each time.
