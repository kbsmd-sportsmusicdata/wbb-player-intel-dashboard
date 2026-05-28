# WBB Player Intel Dashboard

**A static 2025-26 women's college basketball player-intel dashboard for role comps, team mix, and coach-facing scouting context.**

This repo packages a publishable WBB player-intel dashboard that combines player profiles, role-based comps, team roster mix, and coach-facing prompts in a single portable HTML artifact.


## How To Use This Repo


1. Open `notebooks/index.html` first for the full player-intel dashboard experience.

2. Use the exact-source JSON bundle in `data/processed/` to inspect the player, comp, and coaching layers behind the published artifact.

3. Regenerate docs and rerun validation after any metadata or artifact refresh using the template scripts.



## Live Project

- HTML Notebook: Pending GitHub Pages deployment
- Portfolio Page: Not published yet
- Tableau Public: Not used for this project

## Project Status

approval-ready

## Why This Project Matters

The source workspace contains a strong self-contained dashboard, but not a publish-ready repo contract. This child repo turns that artifact into a portable portfolio package while keeping the evidence bundle slim, exact-source aligned, and honest about what remains embedded directly in the HTML.

## Key Questions


- Which 2025-26 players share the strongest role-based comp profiles across the dashboard universe?

- How do percentile, role, and derived-metric layers translate into coach-facing player intel?

- How can team roster mix and embedded coach Q&A surfaces support faster scouting review?


## Audience


- sports analytics portfolio reviewers

- coaching staffs and scouting groups

- front office and roster-construction decision-makers


## Evidence Bundle


- `data/processed/dashboard_slim_k6_enriched.json` (Exact-source evidence): Player, role, percentile, comp, and derived-metric layer mirrored into the HTML.
  Notes: Primary public evidence file for the dashboard.


- `data/processed/sample_comp_narratives.json` (Exact-source evidence): Narrative comparison rules for player comps and scouting summaries.
  Notes: Supports the matchup-notes and structured scout-notes text blocks.


- `data/processed/coaching_implication_templates.json` (Exact-source evidence): Role-usage coaching templates used in the coach-facing card and interpretation layer.
  Notes: Supports the coaching-brief and deployment framing embedded in the artifact.




## Excluded From Initial Public Bundle


- Excluded `data/player_box_with_game_type.json` from the public bundle because it is too large for a slim template repo.

- Excluded visible CSV derivatives from canonical evidence because their taxonomy drifts from the dashboard's six-role presentation.



## Project Outputs

- Primary deliverable: Static HTML dashboard
- Notebook path: `notebooks/index.html`
- Report path: `docs/executive_summary.md`

## Data Sources


- dashboard_slim_k6_enriched.json — Exact-source player-intel layer mirrored into the published HTML. Includes player records, six-role taxonomy, percentiles, comps, and derived metrics.

- sample_comp_narratives.json — Comp-narrative library used for matchup and scouting text blocks embedded in the dashboard.

- coaching_implication_templates.json — Coaching-template rules used for the coach-facing interpretation layer embedded in the dashboard.

- Remote presentation dependencies — Google Fonts, Chart.js CDN, and ESPN-hosted logos/headshots remain runtime dependencies of the static dashboard.


## Methodology Summary

See [`docs/methodology.md`](docs/methodology.md).

## Validation Summary

See [`docs/validation_report.md`](docs/validation_report.md).

## Data Dictionary

See [`docs/data_dictionary.md`](docs/data_dictionary.md).

## Repo Structure

```text
/data
/docs
/notebooks
/reports
/scripts
/sql
/templates
```

## How To Run

```bash
pip install -r requirements.txt
python scripts/generate_docs.py
python scripts/validate_data.py
python scripts/generate_readme.py
```

## Next Steps


- Review the packaged repo locally and approve the public-facing narrative before creating the GitHub repository.

- After approval, create the destination GitHub repo and push this local child repo.

- Optionally add curated CSV appendix tables in a second pass if taxonomy is normalized or clearly labeled as non-canonical.
