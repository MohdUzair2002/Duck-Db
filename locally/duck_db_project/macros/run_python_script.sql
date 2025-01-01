-- macros/run_python_script.sql
{% macro run_python_script() %}
    {% do log('Running Python script...', info=True) %}
    {% set result = run_query('!python3 scripts/run_script.py') %}
    {% do log('Script executed with result: ' ~ result, info=True) %}
{% endmacro %}
