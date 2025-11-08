"""
Tests for PLACEHOLDER_ADAPTER_CLASS_NAME.
"""

import pytest
from pathlib import Path
import tempfile
import pandas as pd

from {{ cookiecutter.package_name }}.adapters.{{ cookiecutter.adapter_name }} import PLACEHOLDER_ADAPTER_CLASS_NAME


class TestPLACEHOLDER_ADAPTER_CLASS_NAME:
    """Test the PLACEHOLDER_ADAPTER_CLASS_NAME."""
    
    def test_adapter_initialization(self):
        """Test that the adapter initializes correctly."""
        adapter = PLACEHOLDER_ADAPTER_CLASS_NAME("test_data_source.csv")
        
        assert adapter.data_source == "test_data_source.csv"
        assert adapter.config == {}
    
    def test_adapter_initialization_with_config(self):
        """Test that the adapter initializes with additional config."""
        config = {"param1": "value1", "param2": "value2"}
        adapter = PLACEHOLDER_ADAPTER_CLASS_NAME("test_data_source.csv", **config)
        
        assert adapter.data_source == "test_data_source.csv"
        assert adapter.config == config
    
    def test_get_metadata(self):
        """Test that metadata is returned correctly."""
        adapter = PLACEHOLDER_ADAPTER_CLASS_NAME("test_data_source.csv")
        metadata = adapter.get_metadata()
        
        assert metadata["name"] == "PLACEHOLDER_ADAPTER_CLASS_NAME"
        assert metadata["data_source"] == "test_data_source.csv"
        assert metadata["data_type"] == "csv"
        assert metadata["version"] == "{{ cookiecutter.version }}"
        assert metadata["adapter_class"] == "PLACEHOLDER_ADAPTER_CLASS_NAME"
    
    def test_get_nodes_with_csv_file(self):
        """Test node extraction from CSV file."""
        # Create a temporary CSV file
        test_data = pd.DataFrame({
            'id': ['1', '2', '3'],
            'name': ['Protein A', 'Gene B', 'Compound C'],
            'type': ['protein', 'gene', 'compound']
        })
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            test_data.to_csv(f, index=False)
            temp_file = f.name
        
        try:
            adapter = PLACEHOLDER_ADAPTER_CLASS_NAME(temp_file)
            nodes = adapter.get_nodes()
            
            assert len(nodes) == 3
            assert nodes[0]["id"] == "1"
            assert nodes[0]["label"] == "DataNode"
            assert "name" in nodes[0]["properties"]
            assert nodes[0]["properties"]["name"] == "Protein A"
        finally:
            Path(temp_file).unlink()
    
    def test_validate_data_source_with_existing_csv(self):
        """Test data source validation with existing CSV file."""
        # Create a temporary CSV file
        test_data = pd.DataFrame({'id': ['1'], 'name': ['test']})
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            test_data.to_csv(f, index=False)
            temp_file = f.name
        
        try:
            adapter = PLACEHOLDER_ADAPTER_CLASS_NAME(temp_file)
            assert adapter.validate_data_source() is True
        finally:
            Path(temp_file).unlink()
    
    def test_validate_data_source_with_nonexistent_file(self):
        """Test data source validation with non-existent file."""
        adapter = PLACEHOLDER_ADAPTER_CLASS_NAME("nonexistent_file.csv")
        assert adapter.validate_data_source() is False
    
    def test_get_edges_empty(self):
        """Test that edges are returned (empty by default)."""
        adapter = PLACEHOLDER_ADAPTER_CLASS_NAME("test_data_source.csv")
        edges = adapter.get_edges()
        
        assert isinstance(edges, list)
        # By default, edges list is empty - implement your own edge extraction logic
        assert len(edges) == 0
