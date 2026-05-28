# Executive Summary: {{ project.title }}

## Project Objective

{{ project.description }}

## Intended Audience

{% for item in project_context.audience %}
- {{ item }}
{% endfor %}

## Key Questions

{% for question in project_context.key_questions %}
- {{ question }}
{% endfor %}

## Decision-Support Value

{{ narrative.decision_support_value }}

## Top Findings

{% for finding in narrative.top_findings %}
{{ loop.index }}. {{ finding }}
{% endfor %}

## Recommended Use Cases

{% for use_case in project_context.use_cases %}
- {{ use_case }}
{% endfor %}

## Limitations

{% for limitation in notes.limitations %}
- {{ limitation }}
{% endfor %}
