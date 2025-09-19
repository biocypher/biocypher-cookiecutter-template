# BioCypher CookieCutter Template

A [Cookiecutter](https://cookiecutter.readthedocs.io/) template for creating BioCypher pipeline projects.

## Features

- **Complete BioCypher Pipeline**: Ready-to-use project structure
- **Multiple Data Source Types**: Support for file, API, database, and custom data sources
- **Docker Support**: Optional containerized deployment
- **Testing Framework**: Optional comprehensive test setup
- **Schema Configuration**: Pre-configured BioCypher schema setup
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
| `adapter_name` | Adapter class name (auto-generated) | Based on package_name |
| `data_source_type` | Type of data source | `file` |
| `include_docker` | Include Docker configuration | `y` |
| `include_tests` | Include test framework | `y` |
| `schema_config` | Include schema configuration | `y` |
| `author_name` | Author name | `BioCypher User` |
| `author_email` | Author email | `user@example.com` |
| `version` | Project version | `0.1.0` |
| `license` | License type | `MIT` |
| `python_version` | Python version requirement | `3.11` |
| `biocypher_version` | BioCypher version | `latest` |

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
│       └── my_biocypher_pipeline_adapter.py
├── tests/
│   ├── __init__.py
│   └── test_my_biocypher_pipeline_adapter.py
├── create_knowledge_graph.py
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
├── README.md
└── .gitignore
```

## Data Source Types

The template supports different data source types with pre-configured adapter templates:

### File-based (`file`)
- JSON, CSV, TSV file processing
- Automatic file type detection
- Example implementations included

### API-based (`api`)
- REST API integration
- Request handling and error management
- JSON response processing

### Database-based (`database`)
- SQLite, PostgreSQL, MySQL support
- Connection management
- Query result processing

### Custom (`custom`)
- Flexible template for custom data sources
- Placeholder implementation
- Easy to extend

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

## Related Projects

- [BioCypher](https://github.com/biocypher/biocypher) - The main BioCypher framework
- [BioCypher MCP](https://github.com/slobentanzer/biocypher-mcp) - MCP server for BioCypher workflows
