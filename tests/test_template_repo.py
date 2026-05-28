import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run(args, cwd):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True)


def copy_repo_to_tmp():
    tmpdir = tempfile.TemporaryDirectory()
    target = Path(tmpdir.name) / REPO_ROOT.name
    shutil.copytree(
        REPO_ROOT,
        target,
        ignore=shutil.ignore_patterns("__pycache__", ".DS_Store", "*.pyc"),
    )
    return tmpdir, target


class TemplateRepoTests(unittest.TestCase):
    def test_expected_repo_files_exist(self):
        expected = [
            "README.md",
            "project_config.yml",
            "requirements.txt",
            ".gitignore",
            "docs/executive_summary.md",
            "docs/methodology.md",
            "docs/data_dictionary.md",
            "docs/validation_report.md",
            "docs/project_handoff.md",
            "docs/publishing_checklist.md",
            "notebooks/index.html",
            "reports/validation_summary.json",
            "reports/validation_summary.md",
            "scripts/init_project.py",
            "scripts/generate_docs.py",
            "scripts/generate_readme.py",
            "scripts/validate_data.py",
            "scripts/publish_check.py",
            "templates/README_template.md",
            ".github/workflows/validate.yml",
            ".github/workflows/deploy_pages.yml",
            "data/processed/dashboard_slim_k6_enriched.json",
            "data/processed/sample_comp_narratives.json",
            "data/processed/coaching_implication_templates.json",
        ]

        missing = [path for path in expected if not (REPO_ROOT / path).exists()]
        self.assertEqual([], missing)

    def test_init_project_generates_docs_and_readme(self):
        tmpdir, repo_copy = copy_repo_to_tmp()
        self.addCleanup(tmpdir.cleanup)

        (repo_copy / "README.md").unlink(missing_ok=True)
        for rel_path in [
            "docs/executive_summary.md",
            "docs/methodology.md",
            "docs/data_dictionary.md",
            "docs/validation_report.md",
            "docs/project_handoff.md",
            "docs/publishing_checklist.md",
        ]:
            (repo_copy / rel_path).unlink(missing_ok=True)

        result = run(["python3", "scripts/init_project.py"], cwd=repo_copy)
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("README.md", result.stdout)
        self.assertTrue((repo_copy / "README.md").exists())
        self.assertTrue((repo_copy / "docs" / "executive_summary.md").exists())

    def test_validate_data_writes_reports_for_expected_json_evidence(self):
        tmpdir, repo_copy = copy_repo_to_tmp()
        self.addCleanup(tmpdir.cleanup)

        result = run(["python3", "scripts/validate_data.py"], cwd=repo_copy)
        self.assertEqual(result.returncode, 0, msg=result.stderr)

        summary_path = repo_copy / "reports" / "validation_summary.json"
        self.assertTrue(summary_path.exists())
        summary = json.loads(summary_path.read_text())

        self.assertEqual("pass", summary["status"])
        self.assertEqual(3, len(summary["files"]))
        self.assertEqual([], summary["errors"])
        self.assertTrue((repo_copy / "reports" / "validation_summary.md").exists())

    def test_publish_check_passes_with_placeholder_files(self):
        tmpdir, repo_copy = copy_repo_to_tmp()
        self.addCleanup(tmpdir.cleanup)

        init_result = run(["python3", "scripts/init_project.py"], cwd=repo_copy)
        self.assertEqual(init_result.returncode, 0, msg=init_result.stderr)

        result = run(["python3", "scripts/publish_check.py"], cwd=repo_copy)
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
