"""
Adapters for {{ cookiecutter.project_name }}.
"""

from .{{ cookiecutter.adapter_name }} import {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter

__all__ = ["{{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter"]
