"""
Tests for {{ cookiecutter.adapter_name }}.
"""

import pytest
from pathlib import Path
import tempfile
import json

from {{ cookiecutter.package_name }}.adapters.{{ cookiecutter.adapter_name }} import {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter


class Test{{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter:
    """Test the {{ cookiecutter.adapter_name }} adapter."""
    
    def test_adapter_initialization(self):
        """Test that the adapter initializes correctly."""
        adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter("test_data_source")
        
        assert adapter.data_source == "test_data_source"
        assert adapter.config == {}
    
    def test_adapter_initialization_with_config(self):
        """Test that the adapter initializes with additional config."""
        config = {"param1": "value1", "param2": "value2"}
        adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter("test_data_source", **config)
        
        assert adapter.data_source == "test_data_source"
        assert adapter.config == config
    
    def test_get_metadata(self):
        """Test that metadata is returned correctly."""
        adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter("test_data_source")
        metadata = adapter.get_metadata()
        
        assert metadata["name"] == "{{ cookiecutter.adapter_name }}"
        assert metadata["data_source"] == "test_data_source"
        assert metadata["data_type"] == "{{ cookiecutter.data_source_type }}"
        assert metadata["version"] == "{{ cookiecutter.version }}"
        assert metadata["adapter_class"] == "{{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter"
    
    {%- if cookiecutter.data_source_type == "file" %}
    def test_get_nodes_with_json_file(self):
        """Test node extraction from JSON file."""
        # Create a temporary JSON file
        test_data = [
            {"id": "1", "type": "protein", "name": "Protein A"},
            {"id": "2", "type": "gene", "name": "Gene B"}
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(test_data, f)
            temp_file = f.name
        
        try:
            adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter(temp_file)
            nodes = adapter.get_nodes()
            
            assert len(nodes) == 2
            assert nodes[0]["id"] == "1"
            assert nodes[0]["label"] == "protein"
            assert nodes[1]["id"] == "2"
            assert nodes[1]["label"] == "gene"
        finally:
            Path(temp_file).unlink()
    
    def test_validate_data_source_with_existing_file(self):
        """Test data source validation with existing file."""
        with tempfile.NamedTemporaryFile(delete=False) as f:
            temp_file = f.name
        
        try:
            adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter(temp_file)
            assert adapter.validate_data_source() is True
        finally:
            Path(temp_file).unlink()
    
    def test_validate_data_source_with_nonexistent_file(self):
        """Test data source validation with non-existent file."""
        adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter("nonexistent_file.json")
        assert adapter.validate_data_source() is False
    {%- elif cookiecutter.data_source_type == "api" %}
    def test_validate_data_source_with_valid_url(self):
        """Test data source validation with valid URL."""
        # Mock a valid URL (this would need proper mocking in real tests)
        adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter("https://httpbin.org/status/200")
        # Note: This test would need proper mocking to avoid actual HTTP requests
        # assert adapter.validate_data_source() is True
    {%- endif %}
    
    def test_get_edges_empty(self):
        """Test that edges are returned (empty by default)."""
        adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter("test_data_source")
        edges = adapter.get_edges()
        
        assert isinstance(edges, list)
        # By default, edges list is empty - implement your own edge extraction logic
        assert len(edges) == 0
