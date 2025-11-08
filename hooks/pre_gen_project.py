#!/usr/bin/env python3
"""
Pre-generation hook for {{ cookiecutter.project_name }}.

This script runs before the project is generated to:
1. Generate standardized adapter names from the resource name
2. Handle all non-alphanumeric characters properly
3. Create both PascalCase and snake_case versions
"""

import re
import sys
from pathlib import Path


def clean_and_convert_to_pascal_case(name: str) -> str:
    """
    Convert a name to PascalCase by:
    1. Replacing all non-alphanumeric characters with spaces
    2. Splitting on spaces
    3. Capitalizing each word
    4. Joining without spaces
    """
    # Replace all non-alphanumeric characters with spaces
    cleaned = re.sub(r'[^a-zA-Z0-9]', ' ', name)
    
    # Split on spaces and filter out empty strings
    words = [word for word in cleaned.split() if word]
    
    # Capitalize each word and join
    return ''.join(word.capitalize() for word in words)


def clean_and_convert_to_snake_case(name: str) -> str:
    """
    Convert a name to snake_case by:
    1. Replacing all non-alphanumeric characters with underscores
    2. Converting to lowercase
    3. Removing multiple consecutive underscores
    """
    # Replace all non-alphanumeric characters with underscores
    cleaned = re.sub(r'[^a-zA-Z0-9]', '_', name)
    
    # Convert to lowercase
    cleaned = cleaned.lower()
    
    # Remove multiple consecutive underscores
    cleaned = re.sub(r'_+', '_', cleaned)
    
    # Remove leading/trailing underscores
    cleaned = cleaned.strip('_')
    
    return cleaned


def main():
    """Main pre-generation setup."""
    # Get the original adapter name from cookiecutter context
    original_name = "{{ cookiecutter.adapter_name }}"
    
    # Generate standardized names
    pascal_case_name = clean_and_convert_to_pascal_case(original_name)
    snake_case_name = clean_and_convert_to_snake_case(original_name)
    
    # Add "Adapter" suffix to PascalCase name only if it doesn't already end with "Adapter"
    if pascal_case_name.endswith("Adapter"):
        adapter_class_name = pascal_case_name
    else:
        adapter_class_name = f"{pascal_case_name}Adapter"
    
    # Create a temporary file with the generated names
    # This will be read by the post-gen hook to update the generated files
    names_file = Path("generated_names.txt")
    with open(names_file, 'w') as f:
        f.write(f"adapter_class_name={adapter_class_name}\n")
        f.write(f"pascal_case_name={pascal_case_name}\n")
        f.write(f"snake_case_name={snake_case_name}\n")
        f.write(f"original_name={original_name}\n")
    
    print(f"Generated adapter names:")
    print(f"  Original: {original_name}")
    print(f"  PascalCase: {pascal_case_name}")
    print(f"  SnakeCase: {snake_case_name}")
    print(f"  AdapterClass: {adapter_class_name}")


if __name__ == "__main__":
    main()
