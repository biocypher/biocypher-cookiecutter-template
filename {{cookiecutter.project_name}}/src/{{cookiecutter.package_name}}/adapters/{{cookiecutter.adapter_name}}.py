"""
{{ cookiecutter.adapter_name.replace('_', ' ').title() }} Adapter

This adapter handles {{ cookiecutter.data_source_type }} data source for BioCypher.
"""

import logging
from typing import Any, Dict, List, Optional, Union
from pathlib import Path

logger = logging.getLogger(__name__)


class {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter:
    """
    Adapter for {{ cookiecutter.adapter_name.replace('_', ' ') }} data source.
    
    This adapter implements the BioCypher adapter interface for {{ cookiecutter.data_source_type }} data.
    """
    
    def __init__(self, data_source: Union[str, Path], **kwargs):
        """
        Initialize the adapter.
        
        Args:
            data_source: Path or URL to the data source
            **kwargs: Additional configuration parameters
        """
        self.data_source = data_source
        self.config = kwargs
        logger.info(f"Initialized {{ cookiecutter.adapter_name }} with data source: {data_source}")
        
    def get_nodes(self) -> List[Dict[str, Any]]:
        """
        Extract nodes from the data source.
        
        Returns:
            List of node dictionaries
        """
        logger.info("Extracting nodes from {{ cookiecutter.data_source_type }} data source")
        nodes = []
        
        # TODO: Implement node extraction based on your {{ cookiecutter.data_source_type }} data source
        # Example implementation for different data source types:
        
        {%- if cookiecutter.data_source_type == "file" %}
        # File-based data source
        if isinstance(self.data_source, (str, Path)):
            data_path = Path(self.data_source)
            if data_path.exists():
                # Process file based on extension
                if data_path.suffix == '.json':
                    import json
                    with open(data_path, 'r') as f:
                        data = json.load(f)
                        # Process JSON data and create nodes
                        for item in data:
                            nodes.append({
                                'id': item.get('id'),
                                'label': item.get('type', 'Unknown'),
                                'properties': item
                            })
                elif data_path.suffix in ['.csv', '.tsv']:
                    import pandas as pd
                    df = pd.read_csv(data_path)
                    # Process CSV data and create nodes
                    for _, row in df.iterrows():
                        nodes.append({
                            'id': str(row.get('id', '')),
                            'label': 'DataNode',
                            'properties': row.to_dict()
                        })
        {%- elif cookiecutter.data_source_type == "api" %}
        # API-based data source
        import requests
        
        try:
            response = requests.get(self.data_source)
            response.raise_for_status()
            data = response.json()
            
            # Process API response and create nodes
            for item in data:
                nodes.append({
                    'id': item.get('id'),
                    'label': item.get('type', 'APINode'),
                    'properties': item
                })
        except requests.RequestException as e:
            logger.error(f"Failed to fetch data from API: {e}")
        {%- elif cookiecutter.data_source_type == "database" %}
        # Database-based data source
        # TODO: Implement database connection and querying
        # Example with SQLite:
        import sqlite3
        
        try:
            conn = sqlite3.connect(self.data_source)
            cursor = conn.cursor()
            
            # Example query - customize based on your database schema
            cursor.execute("SELECT * FROM your_table")
            rows = cursor.fetchall()
            
            for row in rows:
                nodes.append({
                    'id': str(row[0]),  # Assuming first column is ID
                    'label': 'DatabaseNode',
                    'properties': dict(zip([desc[0] for desc in cursor.description], row))
                })
            
            conn.close()
        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
        {%- else %}
        # Custom data source
        # TODO: Implement custom data processing logic
        logger.warning("Custom data source type - implement your own processing logic")
        {%- endif %}
        
        logger.info(f"Extracted {len(nodes)} nodes")
        return nodes
    
    def get_edges(self) -> List[Dict[str, Any]]:
        """
        Extract edges from the data source.
        
        Returns:
            List of edge dictionaries
        """
        logger.info("Extracting edges from {{ cookiecutter.data_source_type }} data source")
        edges = []
        
        # TODO: Implement edge extraction based on your data source
        # This is where you would identify relationships between nodes
        
        # Example: If your data contains relationship information
        # Process your data to identify relationships and create edge dictionaries
        
        logger.info(f"Extracted {len(edges)} edges")
        return edges
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get metadata about the data source.
        
        Returns:
            Dictionary containing metadata
        """
        return {
            'name': '{{ cookiecutter.adapter_name }}',
            'data_source': str(self.data_source),
            'data_type': '{{ cookiecutter.data_source_type }}',
            'version': '{{ cookiecutter.version }}',
            'adapter_class': '{{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter'
        }
    
    def validate_data_source(self) -> bool:
        """
        Validate that the data source is accessible and properly formatted.
        
        Returns:
            True if data source is valid, False otherwise
        """
        try:
            {%- if cookiecutter.data_source_type == "file" %}
            # Validate file-based data source
            data_path = Path(self.data_source)
            return data_path.exists() and data_path.is_file()
            {%- elif cookiecutter.data_source_type == "api" %}
            # Validate API-based data source
            import requests
            response = requests.head(self.data_source, timeout=10)
            return response.status_code == 200
            {%- elif cookiecutter.data_source_type == "database" %}
            # Validate database-based data source
            import sqlite3
            conn = sqlite3.connect(self.data_source)
            conn.close()
            return True
            {%- else %}
            # Custom validation
            return True
            {%- endif %}
        except Exception as e:
            logger.error(f"Data source validation failed: {e}")
            return False
