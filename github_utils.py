#!/usr/bin/env python3
"""
GitHub Utilities - A simple toolkit for GitHub operations

This module provides basic utilities for interacting with GitHub repositories,
including repository information retrieval and basic operations.
"""

import json
import sys
from typing import Dict, List, Optional


class GitHubUtils:
    """A simple class for GitHub utility operations."""
    
    def __init__(self, owner: str, repo: str):
        """
        Initialize GitHubUtils with repository information.
        
        Args:
            owner (str): The repository owner (username or organization)
            repo (str): The repository name
        """
        self.owner = owner
        self.repo = repo
        self.repo_url = f"https://github.com/{owner}/{repo}"
    
    def get_repo_info(self) -> Dict[str, str]:
        """
        Get basic repository information.
        
        Returns:
            Dict[str, str]: Repository information dictionary
        """
        return {
            "owner": self.owner,
            "repository": self.repo,
            "url": self.repo_url,
            "clone_url": f"{self.repo_url}.git",
            "api_url": f"https://api.github.com/repos/{self.owner}/{self.repo}"
        }
    
    def generate_clone_command(self) -> str:
        """
        Generate git clone command for the repository.
        
        Returns:
            str: Git clone command
        """
        return f"git clone {self.repo_url}.git"
    
    def generate_readme_template(self) -> str:
        """
        Generate a basic README template for the repository.
        
        Returns:
            str: README template content
        """
        return f"""# {self.repo}

A GitHub repository owned by {self.owner}.

## Installation

```bash
{self.generate_clone_command()}
cd {self.repo}
```

## Usage

This repository contains utilities for GitHub operations.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License
"""

def main():
    """Main function to demonstrate GitHubUtils functionality."""
    if len(sys.argv) < 3:
        print("Usage: python github_utils.py <owner> <repo>")
        print("Example: python github_utils.py octocat Hello-World")
        sys.exit(1)
    
    owner = sys.argv[1]
    repo = sys.argv[2]
    
    # Create GitHubUtils instance
    gh_utils = GitHubUtils(owner, repo)
    
    # Display repository information
    print("GitHub Repository Information:")
    print("=" * 40)
    repo_info = gh_utils.get_repo_info()
    for key, value in repo_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "=" * 40)
    print("Clone Command:")
    print(gh_utils.generate_clone_command())
    
    print("\n" + "=" * 40)
    print("README Template:")
    print(gh_utils.generate_readme_template())


if __name__ == "__main__":
    main()