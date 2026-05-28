# Data Dictionary: {{ project.title }}

## Overview

This document defines key fields used in the project datasets.

{% if data.included_files %}
## Included Files

{% for item in data.included_files %}
- `{{ item.path }}`: {{ item.description }}{% if item.notes %} {{ item.notes }}{% endif %}
{% endfor %}
{% endif %}

{% if data.file_catalog %}
## Key Fields By File

{% for catalog in data.file_catalog %}
### {{ catalog.file }}

{{ catalog.description }}

| Field | Type | Description | Source | Calculation Logic | Notes |
|---|---|---|---|---|---|
{% for field in catalog.fields %}
| `{{ field.name }}` | {{ field.type }} | {{ field.description }} | {{ field.source }} | {{ field.calculation }} | {{ field.notes }} |
{% endfor %}

{% endfor %}
{% endif %}

## Primary Metrics

{% for metric in metrics.primary_metrics %}
### {{ metric.name }}

- Definition: {{ metric.definition }}
- Interpretation: {{ metric.interpretation }}
{% endfor %}

## Derived Metrics

{% for metric in metrics.derived_metrics %}
### {{ metric.name }}

- Formula: {{ metric.formula }}
- Interpretation: {{ metric.interpretation }}
{% endfor %}
