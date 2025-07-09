# Cookiecutter Python Package Template

A modern [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python packages that follows best practices, including the src/ layout pattern.

## Features

- Modern `src/` layout (better for testing and deployment)
- Configured with `pyproject.toml` and `setup.cfg`
- Ready-to-use testing setup with pytest
- MIT License by default
- Python package best practices
- Pre-configured development dependencies
- Comprehensive `.gitignore` for Python projects

## Requirements

- Python 3.8+
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter)

## Usage

1. Install Cookiecutter if you haven't already:
   ```bash
   pip install cookiecutter
   ```

2. Generate a Python package project:
   ```bash
   cookiecutter https://github.com/hariharandata/cookiecutter-python-package-template
   ```

3. You'll be prompted for these values:
   - `project_name`: The display name of your project
   - `package_name`: The Python package name (automatically generated from project_name)
   - `author_name`: Your name
   - `description`: A short description of your project
   - `version`: The initial version (defaults to 0.1.0)

## Project Structure

The generated project will have this structure:

```
{{cookiecutter.package_name}}/
├── README.md
├── LICENSE
├── Makefile
├── pyproject.toml
├── pytest.ini
├── ruff.toml
├── setup.cfg
├── .gitignore
├── .pylintrc
├── .pre-commit-config.yaml
├── src/
│   └── {{cookiecutter.package_name}}/
│       ├── __init__.py
│       ├── main.py
│       └── logger/
│           ├── __init__.py
│           ├── log_config.py
│           └── logging_config.yaml
└── tests/
   ├── __init__.py
   └── test_{{cookiecutter.package_name}}.py
```

## Development

After generating your project:

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

2. Install the package in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

3. Run tests:
   ```bash
   pytest
   ```

## Features in Detail

### Source Layout (`src/`)
- Uses the `src/` layout pattern
- Better separation of source and tests
- Prevents implicit imports during testing

### Configuration Files
- `pyproject.toml`: Modern Python packaging configuration
- `setup.cfg`: Package metadata and additional configuration
- Pre-configured test settings with pytest

### Development Tools
Includes development dependencies for:
- pytest for testing
- black for code formatting
- flake8 for linting
- mypy for type checking

## License

This template is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a Pull Request.