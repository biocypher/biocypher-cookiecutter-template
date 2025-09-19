#!/usr/bin/env python3
"""
Post-generation hook for {{ cookiecutter.project_name }}.

This script runs after the project is generated to:
1. Initialize git repository
2. Create initial commit
3. Set up additional directories
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, cwd=None):
    """Run a shell command and return success status."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {command} failed: {e.stderr}")
        return False


def main():
    """Main post-generation setup."""
    # The hook runs in the generated project directory
    project_dir = Path(".")
    
    print(f"Setting up {{ cookiecutter.project_name }}...")
    
    # Create additional directories
    additional_dirs = ["logs", "output", "data"]
    for dir_name in additional_dirs:
        dir_path = project_dir / dir_name
        dir_path.mkdir(exist_ok=True)
        print(f"✓ Created directory: {dir_name}/")
    
    # Initialize git repository
    if run_command("git init"):
        if run_command("git add ."):
            run_command(f'git commit -m "Initial commit: {{ cookiecutter.project_name }}"')
    
    print(f"\n🎉 {{ cookiecutter.project_name }} setup complete!")
    print(f"\nNext steps:")
    print(f"1. cd {{ cookiecutter.project_name }}")
    print(f"2. pip install -e .  # or uv sync")
    print(f"3. Configure your data source in create_knowledge_graph.py")
    print(f"4. Update config/schema_config.yaml if needed")
    print(f"5. python create_knowledge_graph.py")


if __name__ == "__main__":
    main()
