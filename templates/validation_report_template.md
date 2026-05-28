# Validation Report: {{ project.title }}

## Validation Status

Generated validation results will appear here after running:

```bash
python scripts/validate_data.py
```

## Planned Validation Checks

{% for check in methodology.validation_checks %}
- {{ check }}
{% endfor %}

## Latest Validation Summary

See `reports/validation_summary.md` for the latest generated validation output.
