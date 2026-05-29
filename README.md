# WBB Player Intel Dashboard

**A 2025-26 women’s college basketball player-intel dashboard for role comps, player profiles, team mix, and coach-facing scouting context.**

This project packages a static WBB player-intel dashboard that brings together player profiles, role-based comps, percentile indicators, team roster mix, and coach-facing prompts in one portable HTML artifact. The goal is to make player evaluation faster to scan, easier to compare, and more useful for basketball operations, scouting, and player-development review.

## How To Use This Repo

1. Start with `notebooks/index.html` or the live dashboard link to explore the full player-intel experience.

2. Use the evidence files in `data/processed/` to inspect the player, comp, role, and coaching layers behind the published artifact.

3. Review the supporting docs for methodology, validation, and data definitions.

```bash
python scripts/generate_docs.py
python scripts/validate_data.py
python scripts/generate_readme.py
```

## Live Project

- **Dashboard:** https://kbsmd-sportsmusicdata.github.io/wbb-player-intel-dashboard/
- **GitHub Repo:** https://github.com/kbsmd-sportsmusicdata/wbb-player-intel-dashboard

## Why This Project Matters

Player intel work is most useful when it connects the numbers to basketball context. This dashboard turns a player dataset into a scouting-style review surface: role labels, percentile signals, player comps, team mix, and coach-facing prompts are presented together so a reviewer can quickly understand how a player profiles and where they may fit.

For a lean basketball operation, this type of tool can support player evaluation, opponent prep, tryout review, roster tracking, and player-development conversations without requiring a full internal analytics department.

## Key Questions

- Which 2025-26 players share similar role-based profiles?
- How do percentile, role, and derived-metric layers translate into player intel?
- Which players stand out by role, team context, or comparable-player profile?
- How can coach-facing prompts support faster scouting and development review?

## Audience

- Player development and coaching staff
- Basketball operations and scouting reviewers
- Front office and roster-construction decision-makers
- Sports analytics portfolio reviewers

## Project Outputs

- **Primary deliverable:** Static HTML player-intel dashboard
- **Dashboard path:** `notebooks/index.html`
- **Executive summary:** `docs/executive_summary.md`
- **Methodology:** `docs/methodology.md`
- **Data dictionary:** `docs/data_dictionary.md`
- **Validation report:** `docs/validation_report.md`

## Supporting Evidence Tables

- `data/processed/dashboard_slim_k6_enriched.json`: exact-source player-intel layer mirrored into the published HTML, including player records, role taxonomy, percentiles, comps, and derived metrics.

- `data/processed/sample_comp_narratives.json`: narrative comparison rules used for player comps, matchup notes, and structured scouting summaries.

- `data/processed/coaching_implication_templates.json`: role-usage coaching templates used in the coach-facing interpretation layer.

## Data Sources

- Saiem Gilani and Geoff Hutchinson. wehoop: The SportsDataverse's R Package for Women's Basketball Data. Retrieved from https://doi.org/10.32614/CRAN.package.wehoop

The static dashboard also uses runtime presentation dependencies, including Google Fonts, Chart.js CDN assets, and ESPN-hosted logos or headshots.

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
/tests
```

## How To Run

```bash
pip install -r requirements.txt
python scripts/generate_docs.py
python scripts/validate_data.py
python scripts/generate_readme.py
```

## Future Extensions

- Add a one-page player intel brief for scouting or player development review.
- Expand the comp layer with clearer role/family explanations.
- Add a lightweight user guide for coaches or front-office reviewers.
