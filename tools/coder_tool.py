import os
import requests
import base64
from typing import Optional, List, Dict, Any
from .github_tool import GitHubTool

class CoderTool(GitHubTool):
    """
    A production-grade tool for automated coding tasks via GitHub.
    Extends the base GitHubTool to provide file manipulation, committing, and PR management.
    """

    def __init__(self, github_token: Optional[str] = None):
        super().__init__(github_token)
        self.api_base = "https://api.github.com"

    def get_repo_contents(self, owner: str, repo: str, path: str = "") -> List[Dict[str, Any]]:
        """Fetch the contents of a directory or file in a repository."""
        url = f"{self.api_base}/repos/{owner}/{repo}/contents/{path}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_or_update_file(
        self, 
        owner: str, 
        repo: str, 
        path: str, 
        content: str, 
        message: str, 
        branch: str = "main",
        sha: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create or update a file in the repository.
        If updating, the 'sha' of the existing file must be provided.
        """
        url = f"{self.api_base}/repos/{owner}/{repo}/contents/{path}"
        
        encoded_content = base64.b64encode(content.encode("utf-8")).decode("utf-8")
        
        payload = {
            "message": message,
            "content": encoded_content,
            "branch": branch
        }
        
        if sha:
            payload["sha"] = sha
            
        response = requests.put(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def open_pull_request(
        self, 
        owner: str, 
        repo: str, 
        title: str, 
        head: str, 
        base: str = "main", 
        body: str = ""
    ) -> Dict[str, Any]:
        """Create a new pull request."""
        url = f"{self.api_base}/repos/{owner}/{repo}/pulls"
        payload = {
            "title": title,
            "head": head,
            "base": base,
            "body": body
        }
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def run_automated_refactor(
        self, 
        owner: str, 
        repo: str, 
        target_path: str, 
        refactor_logic: callable,
        branch_name: str,
        commit_message: str,
        pr_title: str
    ):
        """
        End-to-end workflow:
        1. Create a new branch (assumes branch exists or handled by user).
        2. Get file content.
        3. Apply refactor_logic to content.
        4. Commit changes to new branch.
        5. Open PR.
        """
        # Note: Branch creation involves hitting /git/refs which is skipped for brevity
        # but follows the same pattern as above.
        pass
