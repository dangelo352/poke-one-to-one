import requests
from config import Config

def github_manager(action: str, repo: str = None, issue_title: str = None):
    """
    Interacts with GitHub API to manage repositories and issues.
    """
    token = Config.GITHUB_TOKEN
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    base_url = "https://api.github.com"

    if action == "list_repos":
        url = f"{base_url}/user/repos"
        res = requests.get(url, headers=headers)
        return [r["name"] for r in res.json()]
    
    if action == "create_issue" and repo and issue_title:
        url = f"{base_url}/repos/{repo}/issues"
        res = requests.post(url, headers=headers, json={"title": issue_title})
        return res.json().get("html_url", "Failed to create issue")

    return "Invalid GitHub action"
