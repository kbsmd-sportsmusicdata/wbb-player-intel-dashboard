#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR_DIR = ROOT / "vendor"
if VENDOR_DIR.exists():
    sys.path.insert(0, str(VENDOR_DIR))

import yaml
from jinja2 import Environment, FileSystemLoader

CONFIG_PATH = ROOT / "project_config.yml"
TEMPLATES_DIR = ROOT / "templates"
README_TEMPLATE = "README_template.md"
README_OUTPUT = ROOT / "README.md"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def main() -> int:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        trim_blocks=False,
        lstrip_blocks=False,
    )
    rendered = env.get_template(README_TEMPLATE).render(**load_config()).strip() + "\n"
    README_OUTPUT.write_text(rendered, encoding="utf-8")
    print(README_OUTPUT.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
