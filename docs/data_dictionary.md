# Data Dictionary: WBB Player Intel Dashboard

## Overview

This document defines key fields used in the project datasets.


## Included Files


- `data/processed/dashboard_slim_k6_enriched.json`: Player, role, percentile, comp, and derived-metric layer mirrored into the HTML. Primary public evidence file for the dashboard.

- `data/processed/sample_comp_narratives.json`: Narrative comparison rules for player comps and scouting summaries. Supports the matchup-notes and structured scout-notes text blocks.

- `data/processed/coaching_implication_templates.json`: Role-usage coaching templates used in the coach-facing card and interpretation layer. Supports the coaching-brief and deployment framing embedded in the artifact.




## Key Fields By File


### dashboard_slim_k6_enriched.json

Top-level player-intel payload embedded into the dashboard HTML.

| Field | Type | Description | Source | Calculation Logic | Notes |
|---|---|---|---|---|---|

| `p[].id` | integer | Unique athlete identifier for each player record. | Embedded player layer | Not applicable | Used for profile, comp, and navigation lookups. |

| `p[].n` | string | Player display name. | Embedded player layer | Not applicable | Primary player label in the dashboard. |

| `p[].r` | string | Assigned six-role taxonomy label for the player. | Embedded player layer | Upstream role classification | Examples include Shot Creator, Interior Anchor, and Perimeter Contributor. |

| `p[].s.points_per40` | float | Points scored per 40 minutes. | Embedded player stat layer | Scoring output normalized to 40 minutes | One of the main profile and comp metrics. |

| `p[].p.points_per40.rp` | float | Role-peer percentile for points per 40. | Embedded percentile layer | Percentile within the assigned role bucket | Used in the profile percentile bars. |

| `p[].d.USG_pct` | float | Embedded usage estimate for the player. | Derived metric layer | Upstream derived metric | Used for deployment and identity interpretation. |

| `cl` | object | Cluster-to-role label map for the six dashboard roles. | Embedded taxonomy layer | Not applicable | Defines the role labels rendered throughout the artifact. |



### sample_comp_narratives.json

Comp-level narrative records used to enrich matchup notes and coaching context.

| Field | Type | Description | Source | Calculation Logic | Notes |
|---|---|---|---|---|---|

| `base_player_name` | string | Name of the primary player in the comp pair. | Comp narrative layer | Not applicable | Combined with `comp_player_name` to form the lookup key. |

| `comp_player_name` | string | Name of the comparison player. | Comp narrative layer | Not applicable | Rendered in the comp card and scouting layers. |

| `similarity_score` | float | Similarity score for the comp pair. | Comp narrative layer | Upstream comp scoring output | Higher values indicate a tighter comp. |

| `edge_dimension` | string | Dimension used to describe the key separation between the two players. | Comp narrative layer | Narrative selection rule | Used in matchup-note framing. |

| `coaching_takeaway` | string | Coach-facing interpretation of the comp pair. | Comp narrative layer | Narrative authoring layer | Feeds the coaching context callout. |



### coaching_implication_templates.json

Role and deployment templates used to create coach-facing interpretation cards.

| Field | Type | Description | Source | Calculation Logic | Notes |
|---|---|---|---|---|---|

| `template_id` | string | Unique identifier for the coaching template. | Coaching template layer | Not applicable | Primary key for the template library. |

| `role_label` | string | Role taxonomy label the template applies to. | Coaching template layer | Not applicable | Aligned to the dashboard role system. |

| `usage_tier` | string | Usage bucket expected for the template. | Coaching template layer | Template rule | Used in template matching. |

| `efficiency_tier` | string | Efficiency bucket expected for the template. | Coaching template layer | Template rule | Used in template matching. |

| `best_used_as` | string | Recommended role or deployment framing. | Coaching template layer | Template authoring | Displayed in the coaching brief block. |

| `primary_caution` | string | Primary caution attached to the role/deployment template. | Coaching template layer | Template authoring | Displayed as the main caution in the coaching layer. |





## Primary Metrics


### Points Per 40

- Definition: Points scored per 40 minutes of playing time.
- Interpretation: Higher values indicate stronger scoring volume independent of raw playing-time totals.

### Rebounds Per 40

- Definition: Total rebounds collected per 40 minutes.
- Interpretation: Higher values indicate stronger possession-ending and second-chance involvement.

### Assists Per 40

- Definition: Assists created per 40 minutes.
- Interpretation: Higher values indicate stronger playmaking and table-setting value.


## Derived Metrics


### Assist-to-Turnover Ratio

- Formula: Assists divided by turnovers.
- Interpretation: Higher values indicate stronger decision-making efficiency and ball security.

### Stocks Per 40

- Formula: Steals per 40 plus blocks per 40.
- Interpretation: Higher values indicate stronger event creation and defensive disruption.

### Effective Field Goal Percentage

- Formula: (FGM + 0.5 * 3PM) / FGA.
- Interpretation: Higher values indicate more efficient shot-making after accounting for three-point value.

### Usage Percentage

- Formula: Embedded derived usage estimate from the source player-intel layer.
- Interpretation: Higher values indicate a player carries more offensive creation burden.
