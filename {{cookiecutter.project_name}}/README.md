# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Overview

This BioCypher pipeline processes {{ cookiecutter.data_source_type }} data using the {{ cookiecutter.adapter_name }} to create a knowledge graph.

## Features

- **Data Source**: {{ cookiecutter.data_source_type }} data processing
- **Adapter**: {{ cookiecutter.adapter_name }}
- **Output**: Neo4j knowledge graph
{%- if cookiecutter.include_docker == "y" %}
- **Docker Support**: Containerized deployment
{%- endif %}
{%- if cookiecutter.include_tests == "y" %}
- **Testing**: Comprehensive test suite
{%- endif %}

## Installation

### Prerequisites

- Python {{ cookiecutter.python_version }} or higher
- Neo4j database (local or remote)

### Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd {{ cookiecutter.project_name }}
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

   Or using uv:
   ```bash
   uv sync
   ```

3. Configure your data source in `create_knowledge_graph.py`

4. Update the schema configuration in `config/schema_config.yaml` if needed

## Usage

### Basic Usage

Run the pipeline to create the knowledge graph:

```bash
python create_knowledge_graph.py
```

### Configuration

The pipeline uses two main configuration files:

- `config/biocypher_config.yaml` - BioCypher settings
- `config/schema_config.yaml` - Schema mapping configuration

{%- if cookiecutter.include_docker == "y" %}
### Docker Usage

Build and run with Docker:

```bash
docker-compose up -d
```

This will:
1. Build the BioCypher pipeline
2. Import the data into Neo4j
3. Start the Neo4j instance

Access Neo4j at: http://localhost:7474
{%- endif %}

{%- if cookiecutter.include_tests == "y" %}
## Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov={{ cookiecutter.package_name }} --cov-report=html
```
{%- endif %}

## Project Structure

```
{{ cookiecutter.project_name }}/
├── config/
│   ├── biocypher_config.yaml
│   └── schema_config.yaml
├── src/{{ cookiecutter.package_name }}/
│   └── adapters/
│       └── {{ cookiecutter.adapter_name }}.py
├── create_knowledge_graph.py
{%- if cookiecutter.include_docker == "y" %}
├── docker-compose.yml
├── Dockerfile
{%- endif %}
{%- if cookiecutter.include_tests == "y" %}
├── tests/
│   └── test_{{ cookiecutter.adapter_name }}.py
{%- endif %}
├── pyproject.toml
└── README.md
```

## Development

### Code Style

This project uses:
- **Black** for code formatting
- **isort** for import sorting
- **mypy** for type checking

Format code:
```bash
black .
isort .
```

Type checking:
```bash
mypy src/
```

## License

{{ cookiecutter.license }}

## Author

{{ cookiecutter.author_name }} - {{ cookiecutter.author_email }}
