# Methodology: {{ project.title }}

## Data Sources

{% for source in methodology.data_sources %}
### {{ source.name }}

- URL: {{ source.url }}
- Notes: {{ source.notes }}
{% endfor %}

## Cleaning Steps

{% for step in methodology.cleaning_steps %}
- {{ step }}
{% endfor %}

## Feature Engineering

{% for item in methodology.feature_engineering %}
- {{ item }}
{% endfor %}

{% if methodology.embedded_layers %}
## Embedded Artifact Layers

{% for item in methodology.embedded_layers %}
- {{ item }}
{% endfor %}
{% endif %}

## Metrics

### Primary Metrics

{% for metric in metrics.primary_metrics %}
- **{{ metric.name }}**: {{ metric.definition }}
  - Interpretation: {{ metric.interpretation }}
{% endfor %}

### Derived Metrics

{% for metric in metrics.derived_metrics %}
- **{{ metric.name }}**: {{ metric.formula }}
  - Interpretation: {{ metric.interpretation }}
{% endfor %}

## Modeling Approach

{{ methodology.modeling_approach }}

## Validation Checks

{% for check in methodology.validation_checks %}
- {{ check }}
{% endfor %}

{% if methodology.excluded_files %}
## Excluded Support Files

{% for item in methodology.excluded_files %}
- {{ item }}
{% endfor %}
{% endif %}

## Reproducibility Notes

This project uses a config-driven documentation workflow. Update `project_config.yml`, then regenerate docs using:

```bash
python scripts/generate_docs.py
python scripts/generate_readme.py
```
