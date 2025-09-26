# Github Utilities

A simple Python toolkit for GitHub repository operations and utilities.

## Features

- Repository information retrieval
- Git clone command generation
- README template generation
- Basic GitHub repository utilities

## Installation

```bash
git clone https://github.com/therakeshjoshi/Github.git
cd Github
```

## Usage

### Command Line Interface

```bash
python3 github_utils.py <owner> <repo>
```

Example:
```bash
python3 github_utils.py therakeshjoshi Github
```

### As a Python Module

```python
from github_utils import GitHubUtils

# Create instance
gh_utils = GitHubUtils("owner", "repository")

# Get repository information
repo_info = gh_utils.get_repo_info()
print(repo_info)

# Generate clone command
clone_cmd = gh_utils.generate_clone_command()
print(clone_cmd)

# Generate README template
readme_template = gh_utils.generate_readme_template()
print(readme_template)
```

## Testing

Run the test suite:

```bash
python3 test_github_utils.py -v
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure everything works
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Submit a pull request

## License

MIT License