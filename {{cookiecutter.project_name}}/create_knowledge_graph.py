#!/usr/bin/env python3
"""
{{ cookiecutter.project_name }} - {{ cookiecutter.project_description }}

This script creates a knowledge graph using BioCypher and the {{ cookiecutter.adapter_name }}.
"""

import logging
from pathlib import Path

from biocypher import BioCypher
from {{ cookiecutter.package_name }}.adapters.{{ cookiecutter.adapter_name }} import {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Main function to create the knowledge graph."""
    logger.info("Starting {{ cookiecutter.project_name }} knowledge graph creation")
    
    # Initialize BioCypher
    bc = BioCypher(
        biocypher_config_path="config/biocypher_config.yaml",
        schema_config_path="config/schema_config.yaml"
    )
    
    # Initialize the adapter
    # TODO: Configure your data source path/URL here
    data_source = "path/to/your/data"  # Update this with your actual data source
    
    adapter = {{ cookiecutter.adapter_name.replace('_', '').title() }}Adapter(
        data_source=data_source,
        # Add any additional configuration parameters here
    )
    
    # Add the adapter to BioCypher
    bc.add_adapter(adapter)
    
    # Create the knowledge graph
    logger.info("Creating knowledge graph...")
    bc.write_nodes()
    bc.write_edges()
    
    # Write the graph to Neo4j
    logger.info("Writing to Neo4j...")
    bc.write_to_neo4j()
    
    logger.info("Knowledge graph creation completed successfully!")


if __name__ == "__main__":
    main()
