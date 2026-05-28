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

DOC_OUTPUTS = {
    "executive_summary_template.md": ROOT / "docs" / "executive_summary.md",
    "methodology_template.md": ROOT / "docs" / "methodology.md",
    "data_dictionary_template.md": ROOT / "docs" / "data_dictionary.md",
    "validation_report_template.md": ROOT / "docs" / "validation_report.md",
    "project_handoff_template.md": ROOT / "docs" / "project_handoff.md",
    "publishing_checklist_template.md": ROOT / "docs" / "publishing_checklist.md",
}


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def build_environment() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        trim_blocks=False,
        lstrip_blocks=False,
    )


def render_docs() -> list[Path]:
    config = load_config()
    env = build_environment()
    generated = []

    for template_name, output_path in DOC_OUTPUTS.items():
        rendered = env.get_template(template_name).render(**config).strip() + "\n"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(rendered, encoding="utf-8")
        generated.append(output_path)

    return generated


def main() -> int:
    for path in render_docs():
        print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
