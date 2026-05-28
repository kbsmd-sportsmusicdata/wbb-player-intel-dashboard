#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRS = [
    ROOT / "data" / "raw",
    ROOT / "data" / "processed",
    ROOT / "data" / "reference",
    ROOT / "docs",
    ROOT / "notebooks",
    ROOT / "reports",
    ROOT / "scripts",
    ROOT / "sql",
    ROOT / "templates",
    ROOT / ".github" / "workflows",
]

GITKEEP_DIRS = [
    ROOT / "data" / "raw",
    ROOT / "data" / "processed",
    ROOT / "data" / "reference",
    ROOT / "sql",
]

PLACEHOLDER_NOTEBOOK = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sports Analytics Project</title>
  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      max-width: 900px;
      margin: 48px auto;
      padding: 0 24px;
      line-height: 1.6;
    }
    .card {
      border: 1px solid #ddd;
      border-radius: 16px;
      padding: 24px;
      background: #fafafa;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Sports Analytics Project</h1>
    <p>This is a placeholder HTML notebook. Replace this file with the final project notebook or dashboard.</p>
  </div>
</body>
</html>
"""


def ensure_structure() -> None:
    for path in REQUIRED_DIRS:
        path.mkdir(parents=True, exist_ok=True)
    for path in GITKEEP_DIRS:
        gitkeep = path / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text("", encoding="utf-8")


def ensure_placeholder_notebook() -> None:
    notebook_path = ROOT / "notebooks" / "index.html"
    if not notebook_path.exists():
        notebook_path.write_text(PLACEHOLDER_NOTEBOOK, encoding="utf-8")


def run_script(script_name: str) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script_name)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip(), file=sys.stderr)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> int:
    ensure_structure()
    ensure_placeholder_notebook()
    run_script("generate_docs.py")
    run_script("generate_readme.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
