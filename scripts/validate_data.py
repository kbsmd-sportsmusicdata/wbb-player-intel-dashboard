#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR_DIR = ROOT / "vendor"
if VENDOR_DIR.exists():
    sys.path.insert(0, str(VENDOR_DIR))

import pandas as pd
import yaml

CONFIG_PATH = ROOT / "project_config.yml"
REPORTS_DIR = ROOT / "reports"
JSON_OUTPUT = REPORTS_DIR / "validation_summary.json"
MD_OUTPUT = REPORTS_DIR / "validation_summary.md"


def load_config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def format_pct(value: float) -> str:
    return f"{value:.1f}%"


def validate_json_file(path: Path, rel_path: str, file_spec: dict) -> tuple[dict, list[str], list[str]]:
    warnings: list[str] = []
    errors: list[str] = []
    entry = {
        "path": rel_path,
        "required": bool(file_spec.get("required", False)),
        "description": file_spec.get("description", ""),
        "status": "validated_json",
        "file_type": "json",
        "size_bytes": path.stat().st_size,
    }

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        entry["status"] = "invalid_json"
        errors.append(f"{rel_path} could not be parsed as JSON: {exc}")
        return entry, warnings, errors

    if isinstance(payload, list):
        entry["top_level_type"] = "list"
        entry["record_count"] = len(payload)
    elif isinstance(payload, dict):
        entry["top_level_type"] = "dict"
        entry["top_level_keys"] = list(payload.keys())[:10]
        if "p" in payload and isinstance(payload["p"], list):
            entry["record_count"] = len(payload["p"])
        elif "games" in payload and isinstance(payload["games"], list):
            entry["record_count"] = len(payload["games"])
        else:
            entry["record_count"] = len(payload)
    else:
        entry["top_level_type"] = type(payload).__name__
        entry["record_count"] = 1

    return entry, warnings, errors


def validate_expected_file(file_spec: dict, config: dict) -> tuple[dict, list[str], list[str]]:
    warnings: list[str] = []
    errors: list[str] = []
    rel_path = file_spec["path"]
    required = bool(file_spec.get("required", False))
    path = ROOT / rel_path
    entry = {
        "path": rel_path,
        "required": required,
        "description": file_spec.get("description", ""),
        "status": "not_checked",
    }

    if not path.exists():
        entry["status"] = "missing"
        message = f"{rel_path} is missing"
        if required and config["validation"].get("fail_on_missing_required_files", False):
            errors.append(message)
        else:
            warnings.append(message)
        return entry, warnings, errors

    if path.suffix.lower() == ".json":
        return validate_json_file(path, rel_path, file_spec)

    if path.suffix.lower() != ".csv":
        entry["status"] = "exists_only"
        entry["file_type"] = path.suffix.lower().lstrip(".") or "unknown"
        entry["size_bytes"] = path.stat().st_size
        return entry, warnings, errors

    frame = pd.read_csv(path)
    missing_pct = (frame.isna().mean() * 100).round(2)
    duplicate_rows = int(frame.duplicated().sum())
    required_columns = config["data"].get("required_columns", [])
    missing_columns = [column for column in required_columns if column not in frame.columns]

    entry.update(
        {
            "status": "validated",
            "row_count": int(len(frame)),
            "column_count": int(len(frame.columns)),
            "duplicate_rows": duplicate_rows,
            "missing_columns": missing_columns,
            "missing_pct_by_column": {
                column: float(value)
                for column, value in missing_pct.items()
                if value > 0
            },
        }
    )

    threshold = float(config["validation"].get("max_missing_pct_warning", 20))
    for column, pct in entry["missing_pct_by_column"].items():
        if pct >= threshold:
            message = f"{rel_path} has {format_pct(pct)} missing values in column '{column}'"
            if config["validation"].get("fail_on_missing_values", False):
                errors.append(message)
            else:
                warnings.append(message)

    if duplicate_rows:
        message = f"{rel_path} has {duplicate_rows} duplicate rows"
        if config["validation"].get("fail_on_duplicate_rows", False):
            errors.append(message)
        else:
            warnings.append(message)

    if missing_columns:
        message = f"{rel_path} is missing required columns: {', '.join(missing_columns)}"
        errors.append(message)

    return entry, warnings, errors


def build_summary() -> dict:
    config = load_config()
    summary = {
        "project_title": config["project"]["title"],
        "run_at": datetime.now(timezone.utc).isoformat(),
        "status": "pass",
        "files": [],
        "warnings": [],
        "errors": [],
    }

    for file_spec in config["data"].get("expected_files", []):
        entry, warnings, errors = validate_expected_file(file_spec, config)
        summary["files"].append(entry)
        summary["warnings"].extend(warnings)
        summary["errors"].extend(errors)

    if summary["errors"]:
        summary["status"] = "fail"
    elif summary["warnings"]:
        summary["status"] = "warning"

    return summary


def write_markdown(summary: dict) -> None:
    lines = [
        f"# Validation Summary: {summary['project_title']}",
        "",
        f"- Run at: {summary['run_at']}",
        f"- Status: {summary['status']}",
        "",
        "## Files Checked",
        "",
        "| File | Status | Rows | Columns | Duplicate Rows |",
        "|---|---|---:|---:|---:|",
    ]

    for entry in summary["files"]:
        lines.append(
            "| {path} | {status} | {row_count} | {column_count} | {duplicate_rows} |".format(
                path=entry["path"],
                status=entry.get("status", "unknown"),
                row_count=entry.get("row_count", 0),
                column_count=entry.get("column_count", 0),
                duplicate_rows=entry.get("duplicate_rows", 0),
            )
        )

    lines.extend(["", "## Warnings", ""])
    if summary["warnings"]:
        lines.extend([f"- {warning}" for warning in summary["warnings"]])
    else:
        lines.append("- None")

    lines.extend(["", "## Errors", ""])
    if summary["errors"]:
        lines.extend([f"- {error}" for error in summary["errors"]])
    else:
        lines.append("- None")

    MD_OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    summary = build_summary()
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUTPUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    write_markdown(summary)
    print(JSON_OUTPUT.relative_to(ROOT))
    print(MD_OUTPUT.relative_to(ROOT))
    return 1 if summary["status"] == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
