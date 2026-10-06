# Contributing to AgentForge

We welcome contributions from the community! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/Tdat10052499/agentforge/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Python version and OS

### Suggesting Features

1. Check [Issues](https://github.com/Tdat10052499/agentforge/issues) and [Discussions](https://github.com/Tdat10052499/agentforge/discussions)
2. Create a new issue with:
   - Clear title
   - Detailed description of the feature
   - Use cases and examples
   - Why this would be useful

### Code Contributions

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Write or update tests
5. Run tests: `python -m pytest`
6. Commit with clear messages: `git commit -m "Add feature description"`
7. Push: `git push origin feature/your-feature-name`
8. Create a Pull Request with:
   - Clear title
   - Description of changes
   - Related issues
   - Screenshots if applicable

## Development Setup

```bash
# Clone repository
git clone https://github.com/Tdat10052499/agentforge.git
cd agentforge

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest

# Run with verbose output
python -m pytest -v

# Run with coverage
python -m pytest --cov=agentforge
```

## Code Style

- Follow PEP 8
- Use type hints
- Write docstrings for functions and classes
- Format with black: `black agentforge/`
- Lint with ruff: `ruff check agentforge/`

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Aim for good code coverage
- Test both happy path and error cases

## Documentation

- Update README.md for user-facing changes
- Add docstrings to new code
- Include examples for new features
- Update CHANGELOG.md

## Pull Request Process

1. Ensure tests pass
2. Update documentation
3. Add entry to CHANGELOG.md
4. Submit PR with clear description
5. Respond to review feedback
6. Maintainer will merge when ready

## Areas for Contribution

- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🧪 Additional tests
- 🎨 Code quality improvements
- 🔌 New tools and integrations
- 📱 Examples and tutorials

## Questions?

- Open a [Discussion](https://github.com/Tdat10052499/agentforge/discussions)
- Check existing documentation
- Look at examples

Thank you for contributing! 🎉
