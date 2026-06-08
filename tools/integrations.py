import requests
from config import Config

class IntegrationTools:
    """
    Skeletons for popular productivity tool integrations.
    Requires relevant API keys in config.py.
    """

    @staticmethod
    def create_linear_issue(title, description, team_id):
        """Creates an issue in Linear."""
        # Implementation skeleton using Linear GraphQL API
        url = "https://api.linear.app/graphql"
        headers = {"Authorization": Config.LINEAR_API_KEY, "Content-Type": "application/json"}
        query = f"""
        mutation {{
          issueCreate(input: {{ title: "{title}", description: "{description}", teamId: "{team_id}" }}) {{
            success
            issue {{ id title }}
          }}
        }}
        """
        # response = requests.post(url, json={'query': query}, headers=headers)
        return f"Mock: Created Linear issue '{title}'"

    @staticmethod
    def add_notion_page(database_id, properties):
        """Adds a page to a Notion database."""
        # Implementation skeleton using Notion API
        url = f"https://api.notion.com/v1/pages"
        headers = {
            "Authorization": f"Bearer {Config.NOTION_TOKEN}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }
        # response = requests.post(url, json={"parent": {"database_id": database_id}, "properties": properties}, headers=headers)
        return "Mock: Added page to Notion"

    @staticmethod
    def create_todoist_task(content, due_string="today"):
        """Creates a task in Todoist."""
        # Implementation skeleton using Todoist REST API
        url = "https://api.todoist.com/rest/v2/tasks"
        headers = {"Authorization": f"Bearer {Config.TODOIST_API_KEY}"}
        # response = requests.post(url, json={"content": content, "due_string": due_string}, headers=headers)
        return f"Mock: Created Todoist task '{content}'"
