from __future__ import annotations

import argparse
import importlib.util
import json
import os
import platform
import time
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DIR = ROOT / "runtime"
SETTINGS_FILE = RUNTIME_DIR / "settings.json"
SECRETS_LOCAL_FILE = RUNTIME_DIR / "secrets.local.json"
SECRETS_PROD_TEMPLATE = RUNTIME_DIR / "secrets.prod.example.json"
BOOTSTRAP_REQUIREMENTS = RUNTIME_DIR / "requirements.bootstrap.txt"

REQUIRED_COMMANDS = [
    {
        "id": "git",
        "label": "Git",
        "commands": ["git"],
        "install": {
            "Darwin": ["brew", "install", "git"],
            "Windows": ["winget", "install", "--id", "Git.Git", "-e", "--silent", "--accept-source-agreements", "--accept-package-agreements"],
        },
    },
    {
        "id": "node",
        "label": "Node.js",
        "commands": ["node", "npm"],
        "install": {
            "Darwin": ["brew", "install", "node"],
            "Windows": ["winget", "install", "--id", "OpenJS.NodeJS.LTS", "-e", "--silent", "--accept-source-agreements", "--accept-package-agreements"],
        },
    },
    {
        "id": "ollama",
        "label": "Ollama",
        "commands": ["ollama"],
        "install": {
            "Darwin": ["brew", "install", "ollama"],
            "Windows": ["winget", "install", "--id", "Ollama.Ollama", "-e", "--silent", "--accept-source-agreements", "--accept-package-agreements"],
        },
    },
]

PYTHON_MODULES = [
    ("docx", "python-docx"),
    ("openpyxl", "openpyxl"),
    ("pptx", "python-pptx"),
    ("pypdf", "pypdf"),
    ("PIL", "pillow"),
    ("rapidocr_onnxruntime", "rapidocr-onnxruntime"),
]

DEFAULT_REQUIRED_OLLAMA_MODELS = [
    "qwen2.5:1.5b-instruct",
    "qwen2.5:3b-instruct",
    "qwen2.5:7b-instruct",
    "qwen2.5-coder:7b",
    "qwen2.5vl:7b",
]

LOW_MEMORY_REQUIRED_OLLAMA_MODELS = [
    "qwen2.5:1.5b-instruct",
    "qwen2.5:3b-instruct",
]


def write_status(status_file: str, payload: dict) -> None:
    if not status_file:
        return
    path = Path(status_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def run_command(command: list[str], quiet: bool = False) -> bool:
    try:
        result = subprocess.run(
            command,
            check=False,
            cwd=str(ROOT),
            stdout=subprocess.PIPE if quiet else None,
            stderr=subprocess.PIPE if quiet else None,
            text=True,
        )
    except OSError:
        return False
    return result.returncode == 0


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def detect_missing_commands() -> list[dict]:
    missing: list[dict] = []
    for item in REQUIRED_COMMANDS:
        if all(command_exists(command) for command in item["commands"]):
            continue
        missing.append(item)
    return missing


def ensure_settings_file() -> None:
    if SETTINGS_FILE.exists():
        return
    SETTINGS_FILE.write_text(
        json.dumps(
            {
                "language": "zh-CN",
                "sttProvider": "google",
                "ttsProvider": "google",
                "runtimeProfile": "low-memory",
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def ensure_secrets_file() -> None:
    if SECRETS_LOCAL_FILE.exists():
        return
    template = {
        "googleApiKey": "",
        "googleAccessToken": "",
        "openaiApiKey": "",
    }
    if SECRETS_PROD_TEMPLATE.exists():
        try:
            template.update(json.loads(SECRETS_PROD_TEMPLATE.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError):
            pass
    SECRETS_LOCAL_FILE.write_text(json.dumps(template, ensure_ascii=False, indent=2), encoding="utf-8")


def detect_missing_python_modules() -> list[str]:
    missing: list[str] = []
    for module_name, package_name in PYTHON_MODULES:
        if not module_available(module_name):
            missing.append(package_name)
    return missing


def current_runtime_profile() -> str:
    if not SETTINGS_FILE.exists():
        return "low-memory"
    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return "low-memory"
    return str(data.get("runtimeProfile", "low-memory")).strip() or "low-memory"


def required_ollama_models() -> list[str]:
    profile = current_runtime_profile()
    if profile == "low-memory":
        return LOW_MEMORY_REQUIRED_OLLAMA_MODELS
    return DEFAULT_REQUIRED_OLLAMA_MODELS


def module_available(module_name: str) -> bool:
    try:
        return importlib.util.find_spec(module_name) is not None
    except (ImportError, ValueError, AttributeError):
        return False


def install_python_modules(packages: list[str], quiet: bool = False) -> bool:
    if not packages:
        return True
    return run_command([sys.executable, "-m", "pip", "install", "-r", str(BOOTSTRAP_REQUIREMENTS)], quiet=quiet)


def read_ollama_models() -> set[str]:
    if not command_exists("ollama"):
        return set()
    try:
        result = subprocess.run(
            ["ollama", "list"],
            check=False,
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except OSError:
        return set()
    if result.returncode != 0:
        return set()
    models: set[str] = set()
    for raw_line in result.stdout.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("NAME"):
            continue
        models.add(line.split()[0])
    return models


def ollama_ready() -> bool:
    if not command_exists("ollama"):
        return False
    try:
        result = subprocess.run(
            ["ollama", "list"],
            check=False,
            cwd=str(ROOT),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except OSError:
        return False
    return result.returncode == 0


def ensure_ollama_service(quiet: bool = False) -> bool:
    if not command_exists("ollama"):
        return False
    if ollama_ready():
        return True
    system = platform.system()
    if system == "Darwin" and command_exists("brew"):
        run_command(["brew", "services", "start", "ollama"], quiet=quiet)
    elif system == "Windows":
        try:
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except OSError:
            return False
    else:
        try:
            subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except OSError:
            return False
    for _ in range(12):
        if ollama_ready():
            return True
        time.sleep(1)
    return False


def detect_missing_ollama_models() -> list[str]:
    installed = read_ollama_models()
    return [model for model in required_ollama_models() if model not in installed]


def install_ollama_models(models: list[str], quiet: bool = False, status_file: str = "") -> list[str]:
    installed: list[str] = []
    for model in models:
        if run_command(["ollama", "pull", model], quiet=quiet):
            installed.append(model)
        remaining = detect_missing_ollama_models()
        write_status(
            status_file,
            {
                "stage": "installing-models" if remaining else "completed",
                "message": "Downloading local Ollama models." if remaining else "Local Ollama models are ready.",
                "completed": not remaining,
                "installedOllamaModels": installed,
                "missingOllamaModels": remaining,
            },
        )
    return installed


def try_install_missing_commands(missing: list[dict], quiet: bool = False) -> list[str]:
    system = platform.system()
    installed: list[str] = []
    for item in missing:
        install_command = item.get("install", {}).get(system)
        if not install_command:
            continue
        if run_command(install_command, quiet=quiet):
            installed.append(item["id"])
    return installed


def build_report(quiet: bool = False) -> dict:
    missing_commands = detect_missing_commands()
    missing_modules = detect_missing_python_modules()
    ensure_ollama_service(quiet=quiet)
    missing_models = detect_missing_ollama_models()
    return {
        "platform": platform.system(),
        "missingCommands": [item["id"] for item in missing_commands],
        "missingPythonModules": missing_modules,
        "missingOllamaModels": missing_models,
        "requirementsFile": str(BOOTSTRAP_REQUIREMENTS),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap HomeHub for first run.")
    parser.add_argument("--apply", action="store_true", help="Install what can be installed automatically.")
    parser.add_argument("--quiet", action="store_true", help="Reduce command output.")
    parser.add_argument("--status-file", default="", help="Optional JSON file where bootstrap progress is written.")
    args = parser.parse_args()

    write_status(args.status_file, {"stage": "starting", "message": "Preparing first-run bootstrap.", "completed": False})
    ensure_settings_file()
    ensure_secrets_file()

    missing_commands = detect_missing_commands()
    installed_commands: list[str] = []
    if args.apply and missing_commands:
        write_status(args.status_file, {"stage": "installing-tools", "message": "Installing missing base tools.", "completed": False, "missingCommands": [item["id"] for item in missing_commands]})
        installed_commands = try_install_missing_commands(missing_commands, quiet=args.quiet)
        missing_commands = detect_missing_commands()

    missing_modules = detect_missing_python_modules()
    installed_modules = False
    if args.apply and missing_modules:
        write_status(args.status_file, {"stage": "installing-python", "message": "Installing document and OCR Python libraries.", "completed": False, "missingPythonModules": missing_modules})
        installed_modules = install_python_modules(missing_modules, quiet=args.quiet)
        missing_modules = detect_missing_python_modules()

    ensure_ollama_service(quiet=args.quiet)
    missing_models = detect_missing_ollama_models()
    installed_models: list[str] = []
    if args.apply and missing_models and command_exists("ollama"):
        write_status(args.status_file, {"stage": "installing-models", "message": "Downloading local Ollama models.", "completed": False, "missingOllamaModels": missing_models})
        installed_models = install_ollama_models(missing_models, quiet=args.quiet, status_file=args.status_file)
        missing_models = detect_missing_ollama_models()

    report = {
        "ok": not missing_commands and not missing_modules and not missing_models,
        "installedCommands": installed_commands,
        "installedPythonModules": [] if not installed_modules else ["requirements.bootstrap.txt"],
        "installedOllamaModels": installed_models,
        **build_report(quiet=args.quiet),
    }
    write_status(
        args.status_file,
        {
            "stage": "completed" if report["ok"] else "partial",
            "message": "Bootstrap finished." if report["ok"] else "Bootstrap finished with pending items.",
            "completed": report["ok"],
            **report,
        },
    )

    if not args.quiet:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if missing_commands:
            print("Missing commands still need manual install:")
            for item in missing_commands:
                print(f"- {item['label']}")
        if missing_modules:
            print("Missing Python modules:")
            for package_name in missing_modules:
                print(f"- {package_name}")
        if missing_models:
            print("Missing Ollama models:")
            for model in missing_models:
                print(f"- {model}")

    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
