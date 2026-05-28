# Project Handoff: WBB Player Intel Dashboard

## Current Status

approval-ready

## Project Purpose

This repo packages a publishable WBB player-intel dashboard that combines player profiles, role-based comps, team roster mix, and coach-facing prompts in a single portable HTML artifact.

## Key Deliverables

- Primary deliverable: Static HTML dashboard
- Notebook: `notebooks/index.html`
- Executive summary: `docs/executive_summary.md`
- Methodology: `docs/methodology.md`
- Data dictionary: `docs/data_dictionary.md`
- Validation report: `docs/validation_report.md`

## Important Scripts

- `scripts/init_project.py`
- `scripts/generate_docs.py`
- `scripts/generate_readme.py`
- `scripts/validate_data.py`
- `scripts/publish_check.py`

## Included Evidence Files


- `data/processed/dashboard_slim_k6_enriched.json`: Player, role, percentile, comp, and derived-metric layer mirrored into the HTML.

- `data/processed/sample_comp_narratives.json`: Narrative comparison rules for player comps and scouting summaries.

- `data/processed/coaching_implication_templates.json`: Role-usage coaching templates used in the coach-facing card and interpretation layer.



## Excluded Support Files


- Excluded `data/player_box_with_game_type.json` from the public bundle because it is too large for a slim template repo.

- Excluded visible CSV derivatives from canonical evidence because their taxonomy drifts from the dashboard's six-role presentation.



## Known Limitations


- This repo ships a static dashboard and a slim exact-source evidence bundle, not the full upstream build workspace.

- Remote presentation assets still rely on Google Fonts, Chart.js CDN, and ESPN-hosted logos/headshots.

- The team-intel and coach-Q&A views are embedded inside the HTML artifact rather than exposed as separate public tables in this first publish pass.

- Visible CSV derivatives from the source folder were intentionally excluded because their taxonomy does not cleanly match the shipped dashboard.


## Next Steps


- Review the packaged repo locally and approve the public-facing narrative before creating the GitHub repository.

- After approval, create the destination GitHub repo and push this local child repo.

- Optionally add curated CSV appendix tables in a second pass if taxonomy is normalized or clearly labeled as non-canonical.


## Deployment Notes

GitHub Pages should deploy `notebooks/index.html` through the workflow in `.github/workflows/deploy_pages.yml`.
