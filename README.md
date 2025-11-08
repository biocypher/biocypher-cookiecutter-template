# BioCypher CookieCutter Template

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for creating BioCypher pipeline projects.

## Features

- **Complete BioCypher Pipeline**: Ready-to-use project structure
- **Multiple Data Source Types**: Support for file, API, database, and custom data sources
- **Docker Support**: Optional containerized deployment
- **Testing Framework**: Optional comprehensive test setup
- **Schema Configuration**: Pre-configured BioCypher schema setup (included by default)
- **Git Integration**: Automatic git repository initialization

## Usage

### Via MCP Tool (Recommended)

Use the BioCypher MCP tool in Cursor or other MCP clients:

```python
create_biocypher_pipeline(
    project_name="my-protein-pipeline",
    project_description="Pipeline for protein data analysis",
    template_method="cookiecutter",
    data_source_type="api"
)
```

### Direct CookieCutter Usage

```bash
# Install cookiecutter
pip install cookiecutter

# Generate project from template
cookiecutter https://github.com/biocypher/biocypher-cookiecutter-template.git
```

## Template Variables

The template uses the following variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `project_name` | Name of the project | `my-biocypher-pipeline` |
| `project_description` | Project description | `A BioCypher pipeline for biological data integration` |
| `package_name` | Python package name (auto-generated) | Based on project_name |
| `adapter_name` | Adapter class name | `my_resource_adapter` |
| `data_source_type` | Type of data source | `csv` |
| `include_docker` | Include Docker configuration | `y` |
| `include_tests` | Include test framework | `y` |
| `author_name` | Author name | `BioCypher User` |
| `author_email` | Author email | `user@example.com` |
| `version` | Project version | `0.1.0` |
| `license` | License type | `MIT` |
| `python_version` | Python version requirement | `3.11` |
| `biocypher_version` | BioCypher version | `latest` (fetched from PyPI) |

## Generated Project Structure

```
my-biocypher-pipeline/
├── config/
│   ├── biocypher_config.yaml
│   └── schema_config.yaml
├── src/my_biocypher_pipeline/
│   ├── __init__.py
│   └── adapters/
│       ├── __init__.py
│       └── my_resource_adapter.py
├── tests/
│   ├── __init__.py
│   └── test_my_resource_adapter.py
├── create_knowledge_graph.py
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
└── .gitignore
```

## Data Source

The template is configured for **CSV data sources** by default:

### CSV Processing
- **Pandas-based**: Uses pandas for robust CSV reading and processing
- **Flexible**: Handles various CSV formats and structures
- **Simple**: Straightforward implementation that users can easily customize
- **Extensible**: Easy to modify for specific data requirements

The adapter assumes CSV input and provides a clean foundation that users (or the BioCypher MCP copilot) can adapt for their specific data sources and processing needs.

## Post-Generation Setup

After project generation, the template automatically:

1. Creates additional directories (`logs/`, `output/`, `data/`)
2. Initializes git repository
3. Creates initial commit
4. Provides next steps instructions

## Development

### Testing the Template

```bash
# Test the template locally
cookiecutter . --no-input

# Test with custom values
cookiecutter . --no-input project_name="test-pipeline" data_source_type="api"
```

### Contributing

1. Fork the repository
2. Make your changes
3. Test the template
4. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Next Steps: Adapting Your Pipeline

The best way to adapt your BioCypher pipeline to your specific needs is through the **BioCypher MCP Server** available at https://mcp.biocypher.org. This MCP server provides:

- **Interactive Guidance**: Step-by-step assistance for adapter creation
- **Schema Configuration**: Help with BioCypher schema setup and customization
- **Implementation Patterns**: Best practices for different data source types
- **Resource Management**: Guidance on data download and caching strategies
- **Decision Support**: Recommendations based on your data characteristics

### Using the BioCypher MCP Server

1. **Install MCP Client**: Use Cursor or another MCP-compatible client
2. **Connect to Server**: Add the BioCypher MCP server at https://mcp.biocypher.org
3. **Get Guidance**: Use the interactive tools to customize your pipeline
4. **Implement**: Follow the provided patterns and recommendations

## Related Projects

- [BioCypher](https://github.com/biocypher/biocypher) - The main BioCypher framework
- [BioCypher MCP](https://biocypher.org/BioCypher/llms/) - Interactive MCP server for BioCypher workflows
