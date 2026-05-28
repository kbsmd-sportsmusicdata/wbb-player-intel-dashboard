# {{ project.title }}

**{{ project.subtitle }}**

{{ project.description }}

{% if project_context.repo_usage_steps %}
## How To Use This Repo

{% for step in project_context.repo_usage_steps %}
{{ loop.index }}. {{ step }}
{% endfor %}
{% endif %}

## Live Project

- HTML Notebook: {{ links.github_pages }}
- Portfolio Page: {{ links.portfolio_page }}
- Tableau Public: {{ links.tableau_public }}

## Project Status

{{ project.status }}

## Why This Project Matters

{{ project_context.problem_statement | default("Add project problem statement.") }}

## Key Questions

{% for question in project_context.key_questions %}
- {{ question }}
{% endfor %}

## Audience

{% for item in project_context.audience %}
- {{ item }}
{% endfor %}

## Evidence Bundle

{% for item in data.included_files %}
- `{{ item.path }}` ({{ item.classification }}): {{ item.description }}
{% if item.notes %}  Notes: {{ item.notes }}
{% endif %}
{% endfor %}

{% if methodology.excluded_files %}
## Excluded From Initial Public Bundle

{% for item in methodology.excluded_files %}
- {{ item }}
{% endfor %}
{% endif %}

## Project Outputs

- Primary deliverable: {{ outputs.primary_deliverable }}
- Notebook path: `{{ outputs.notebook_path }}`
- Report path: `{{ outputs.report_path }}`

## Data Sources

{% for source in methodology.data_sources %}
- {{ source.name }}{% if source.url %}: {{ source.url }}{% endif %}{% if source.notes %} — {{ source.notes }}{% endif %}
{% endfor %}

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

{% for step in notes.next_steps %}
- {{ step }}
{% endfor %}
