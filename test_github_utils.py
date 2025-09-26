#!/usr/bin/env python3
"""
Tests for GitHub Utilities

Simple test suite to validate the GitHubUtils functionality.
"""

import unittest
from github_utils import GitHubUtils


class TestGitHubUtils(unittest.TestCase):
    """Test cases for GitHubUtils class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.gh_utils = GitHubUtils("testowner", "testrepo")
    
    def test_initialization(self):
        """Test GitHubUtils initialization."""
        self.assertEqual(self.gh_utils.owner, "testowner")
        self.assertEqual(self.gh_utils.repo, "testrepo")
        self.assertEqual(self.gh_utils.repo_url, "https://github.com/testowner/testrepo")
    
    def test_get_repo_info(self):
        """Test get_repo_info method."""
        repo_info = self.gh_utils.get_repo_info()
        
        expected_keys = ["owner", "repository", "url", "clone_url", "api_url"]
        for key in expected_keys:
            self.assertIn(key, repo_info)
        
        self.assertEqual(repo_info["owner"], "testowner")
        self.assertEqual(repo_info["repository"], "testrepo")
        self.assertEqual(repo_info["url"], "https://github.com/testowner/testrepo")
        self.assertEqual(repo_info["clone_url"], "https://github.com/testowner/testrepo.git")
        self.assertEqual(repo_info["api_url"], "https://api.github.com/repos/testowner/testrepo")
    
    def test_generate_clone_command(self):
        """Test generate_clone_command method."""
        clone_cmd = self.gh_utils.generate_clone_command()
        expected_cmd = "git clone https://github.com/testowner/testrepo.git"
        self.assertEqual(clone_cmd, expected_cmd)
    
    def test_generate_readme_template(self):
        """Test generate_readme_template method."""
        readme = self.gh_utils.generate_readme_template()
        
        # Check if essential elements are present
        self.assertIn("# testrepo", readme)
        self.assertIn("testowner", readme)
        self.assertIn("git clone", readme)
        self.assertIn("## Installation", readme)
        self.assertIn("## Usage", readme)
        self.assertIn("## Contributing", readme)
        self.assertIn("## License", readme)


if __name__ == "__main__":
    unittest.main()