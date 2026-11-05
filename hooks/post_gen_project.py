#!/usr/bin/env python3
"""
Post-generation hook for {{ cookiecutter.project_name }}.

This script runs after the project is generated to:
1. Remove optional files that were not selected
2. Set up additional directories
3. Initialize git repository
4. Create initial commit
"""

import os
import shutil
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
    
    # Read generated names from pre-gen hook
    names_file = Path("generated_names.txt")
    generated_names = {}
    if names_file.exists():
        with open(names_file, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    generated_names[key] = value
        names_file.unlink()  # Clean up temporary file
        print(f"✓ Loaded generated names: {generated_names}")
    
    # Handle BioCypher version if "latest" was selected
    if "{{ cookiecutter.biocypher_version }}" == "latest":
        latest_version = get_latest_biocypher_version()
        print(f"Using latest BioCypher version: {latest_version}")
        
        # Update pyproject.toml with the actual latest version
        pyproject_path = project_dir / "pyproject.toml"
        if pyproject_path.exists():
            content = pyproject_path.read_text()
            # Replace the version in the dependencies
            content = content.replace(
                'biocypher[neo4j]>={{ cookiecutter.biocypher_version }}',
                f'biocypher[neo4j]>={latest_version}'
            )
            pyproject_path.write_text(content)
            print(f"✓ Updated pyproject.toml with BioCypher version {latest_version}")
    
    # Update adapter files with generated names
    if generated_names:
        update_adapter_files(project_dir, generated_names)

    # Remove optional files that were not selected
    if "{{ cookiecutter.include_docker }}" != "y":
        for file_name in ["Dockerfile", "docker-compose.yml", ".dockerignore", "config/biocypher_config.docker.yaml"]:
            (project_dir / file_name).unlink()
        print("✓ Removed Docker files")
    if "{{ cookiecutter.include_tests }}" != "y":
        shutil.rmtree(project_dir / "tests")
        print("✓ Removed tests/")

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
    print(f"\n💡 For the best adaptation experience, use the BioCypher MCP Server:")
    print(f"   https://biocypher.org/BioCypher/llms/")
    print(f"   This provides interactive guidance for customizing your pipeline!")
    print(f"\n⚠ The adapter yields dummy data: data_source_type is only a placeholder and")
    print(f"  {{ cookiecutter.data_source_type }} data is not read yet. Update the adapter for your data source.")
    print(f"\nNext steps:")
    print(f"1. cd {{ cookiecutter.project_name }}")
    print(f"2. pip install -e .  # or uv sync")
    print(f"3. Configure your data source in create_knowledge_graph.py")
    print(f"4. Update config/schema_config.yaml if needed")
    print(f"5. python create_knowledge_graph.py")


def update_adapter_files(project_dir: Path, generated_names: dict):
    """Update adapter files with generated standardized names."""
    adapter_class_name = generated_names.get('adapter_class_name', 'MyResourceAdapter')
    pascal_case_name = generated_names.get('pascal_case_name', 'MyResource')
    snake_case_name = generated_names.get('snake_case_name', 'my_resource')
    
    # Update adapter file
    adapter_file = project_dir / "src" / "{{ cookiecutter.package_name }}" / "adapters" / "{{ cookiecutter.adapter_name }}.py"
    if adapter_file.exists():
        content = adapter_file.read_text()
        # Replace placeholders with actual generated names
        content = content.replace('PLACEHOLDER_ADAPTER_CLASS_NAME', adapter_class_name)
        content = content.replace('PLACEHOLDER_PASCAL_CASE_NAME', pascal_case_name)
        adapter_file.write_text(content)
        print(f"✓ Updated adapter file with {adapter_class_name}")
    
    # Update test file
    test_file = project_dir / "tests" / "test_{{ cookiecutter.adapter_name }}.py"
    if test_file.exists():
        content = test_file.read_text()
        # Replace placeholders with actual generated names
        content = content.replace('PLACEHOLDER_ADAPTER_CLASS_NAME', adapter_class_name)
        content = content.replace('PLACEHOLDER_PASCAL_CASE_NAME', pascal_case_name)
        test_file.write_text(content)
        print(f"✓ Updated test file with {adapter_class_name}")
    
    # Update main script
    main_script = project_dir / "create_knowledge_graph.py"
    if main_script.exists():
        content = main_script.read_text()
        # Replace placeholders with actual generated names
        content = content.replace('PLACEHOLDER_ADAPTER_CLASS_NAME', adapter_class_name)
        content = content.replace('PLACEHOLDER_PASCAL_CASE_NAME', pascal_case_name)
        main_script.write_text(content)
        print(f"✓ Updated main script with {adapter_class_name}")
    
    # Update adapters __init__.py file
    adapters_init_file = project_dir / "src" / "{{ cookiecutter.package_name }}" / "adapters" / "__init__.py"
    if adapters_init_file.exists():
        content = adapters_init_file.read_text()
        # Replace placeholders with actual generated names
        content = content.replace('PLACEHOLDER_ADAPTER_CLASS_NAME', adapter_class_name)
        adapters_init_file.write_text(content)
        print(f"✓ Updated adapters __init__.py with {adapter_class_name}")


def get_latest_biocypher_version():
    """Fetch the latest BioCypher version from PyPI."""
    try:
        import json
        import urllib.request
        url = "https://pypi.org/pypi/biocypher/json"
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            return data["info"]["version"]
    except Exception as e:
        print(f"Warning: Could not fetch latest BioCypher version from PyPI: {e}")
        print("Falling back to version 0.17.0")
        return "0.17.0"


if __name__ == "__main__":
    main()
