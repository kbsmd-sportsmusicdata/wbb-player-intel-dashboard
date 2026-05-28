# Methodology: WBB Player Intel Dashboard

## Data Sources


### dashboard_slim_k6_enriched.json

- URL: 
- Notes: Exact-source player-intel layer mirrored into the published HTML. Includes player records, six-role taxonomy, percentiles, comps, and derived metrics.

### sample_comp_narratives.json

- URL: 
- Notes: Comp-narrative library used for matchup and scouting text blocks embedded in the dashboard.

### coaching_implication_templates.json

- URL: 
- Notes: Coaching-template rules used for the coach-facing interpretation layer embedded in the dashboard.

### Remote presentation dependencies

- URL: 
- Notes: Google Fonts, Chart.js CDN, and ESPN-hosted logos/headshots remain runtime dependencies of the static dashboard.


## Cleaning Steps


- Copied the approved final HTML deliverable from `deliverables/WBB_PlayerIntelDashboard_v13.html` into `notebooks/index.html` without changing the artifact.

- Selected a slim public-safe evidence bundle of three exact-source JSON files and excluded heavier or taxonomy-drifted support outputs from the first publish pass.

- Initialized a fresh child repo from the sports analytics template scaffold and regenerated the repo-facing docs from this config.


## Feature Engineering


- Player profiles expose per-40 metrics, percentile views, role assignments, comp lists, and derived metrics embedded from `dashboard_slim_k6_enriched.json`.

- Coach-facing scouting panels layer in comp narratives and coaching templates from the two smaller JSON support files.

- Team-intel and coach Q&A surfaces are embedded directly inside the HTML artifact rather than shipped as separate public tables in this first publish pass.



## Embedded Artifact Layers


- The published HTML embeds the player dataset, team-intel dataset, coaching templates, and comp narratives directly into the page.

- Because the dashboard is self-contained, the repo ships exact-source JSON evidence for the player, comp, and coaching layers rather than rebuilding a live app runtime.



## Metrics

### Primary Metrics


- **Points Per 40**: Points scored per 40 minutes of playing time.
  - Interpretation: Higher values indicate stronger scoring volume independent of raw playing-time totals.

- **Rebounds Per 40**: Total rebounds collected per 40 minutes.
  - Interpretation: Higher values indicate stronger possession-ending and second-chance involvement.

- **Assists Per 40**: Assists created per 40 minutes.
  - Interpretation: Higher values indicate stronger playmaking and table-setting value.


### Derived Metrics


- **Assist-to-Turnover Ratio**: Assists divided by turnovers.
  - Interpretation: Higher values indicate stronger decision-making efficiency and ball security.

- **Stocks Per 40**: Steals per 40 plus blocks per 40.
  - Interpretation: Higher values indicate stronger event creation and defensive disruption.

- **Effective Field Goal Percentage**: (FGM + 0.5 * 3PM) / FGA.
  - Interpretation: Higher values indicate more efficient shot-making after accounting for three-point value.

- **Usage Percentage**: Embedded derived usage estimate from the source player-intel layer.
  - Interpretation: Higher values indicate a player carries more offensive creation burden.


## Modeling Approach

Not applicable. This repo packages a finished static analytics artifact rather than a training or model-building pipeline.

## Validation Checks


- HTML artifact exists at `notebooks/index.html` and matches the approved source deliverable.

- Expected evidence bundle files exist and JSON files parse successfully.

- Generated docs, README, and GitHub Pages scaffold files are present.



## Excluded Support Files


- Excluded `data/player_box_with_game_type.json` from the public bundle because it is too large for a slim template repo.

- Excluded visible CSV derivatives from canonical evidence because their taxonomy drifts from the dashboard's six-role presentation.



## Reproducibility Notes

This project uses a config-driven documentation workflow. Update `project_config.yml`, then regenerate docs using:

```bash
python scripts/generate_docs.py
python scripts/generate_readme.py
```
