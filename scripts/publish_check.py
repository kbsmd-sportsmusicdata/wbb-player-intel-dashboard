#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR_DIR = ROOT / "vendor"
if VENDOR_DIR.exists():
    sys.path.insert(0, str(VENDOR_DIR))

import yaml

CONFIG_PATH = ROOT / "project_config.yml"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def main() -> int:
    config = load_config()
    notebook_path = ROOT / config["outputs"]["notebook_path"]
    checks = [
        ("README.md exists", ROOT / "README.md"),
        ("docs/executive_summary.md exists", ROOT / "docs" / "executive_summary.md"),
        ("docs/methodology.md exists", ROOT / "docs" / "methodology.md"),
        ("docs/data_dictionary.md exists", ROOT / "docs" / "data_dictionary.md"),
        ("docs/validation_report.md exists", ROOT / "docs" / "validation_report.md"),
        ("Notebook deliverable exists", notebook_path),
        ("GitHub Pages workflow exists", ROOT / ".github" / "workflows" / "deploy_pages.yml"),
    ]

    failed = False
    for label, path in checks:
        exists = path.exists()
        status = "PASS" if exists else "FAIL"
        print(f"{status} - {label}: {path.relative_to(ROOT)}")
        failed = failed or not exists

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
