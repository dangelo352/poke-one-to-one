import requests
import json
from config import Config

class LinearIntegration:
    """Integration for Linear workspace management."""
    def __init__(self):
        self.api_key = Config.LINEAR_API_KEY
        self.url = "https://api.linear.app/api"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": self.api_key
        }

    def create_issue(self, team_id, title, description):
        query = """
        mutation CreateIssue($teamId: String!, $title: String!, $description: String) {
            issueCreate(input: { teamId: $teamId, title: $title, description: $description }) {
                success
                issue { id title }
            }
        }
        """
        variables = {"teamId": team_id, "title": title, "description": description}
        response = requests.post(self.url, headers=self.headers, json={"query": query, "variables": variables})
        return response.json()

class NotionIntegration:
    """Integration for Notion databases."""
    def __init__(self):
        self.api_key = Config.NOTION_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def add_page_to_database(self, database_id, properties):
        url = "https://api.notion.com/v1/pages"
        data = {"parent": {"database_id": database_id}, "properties": properties}
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

class TodoistIntegration:
    """Integration for Todoist task management."""
    def __init__(self):
        self.api_key = Config.TODOIST_API_KEY
        self.url = "https://api.todoist.com/rest/v2/tasks"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def create_task(self, content, description=None):
        data = {"content": content, "description": description}
        response = requests.post(self.url, headers=self.headers, json=data)
        return response.json()

class SlackIntegration:
    """Integration for Slack messaging and webhooks."""
    def __init__(self):
        self.bot_token = Config.SLACK_BOT_TOKEN
        self.webhook_url = Config.SLACK_WEBHOOK_URL
        self.headers = {"Authorization": f"Bearer {self.bot_token}", "Content-Type": "application/json"}

    def send_webhook_message(self, text):
        """Send a message via an Incoming Webhook."""
        if not self.webhook_url:
            return {"error": "No webhook URL configured"}
        response = requests.post(self.webhook_url, json={"text": text})
        return response.status_code

    def post_message(self, channel, text, blocks=None):
        """Send a message using the Web API (chat.postMessage)."""
        url = "https://slack.com/api/chat.postMessage"
        payload = {"channel": channel, "text": text}
        if blocks:
            payload["blocks"] = blocks
        response = requests.post(url, headers=self.headers, json=payload)
        return response.json()

class TwilioIntegration:
    """Integration for Twilio SMS messaging."""
    def __init__(self):
        self.account_sid = Config.TWILIO_ACCOUNT_SID
        self.auth_token = Config.TWILIO_AUTH_TOKEN
        self.from_number = Config.TWILIO_FROM_NUMBER
        self.base_url = f"https://api.twilio.com/2010-04-01/Accounts/{self.account_sid}/Messages.json"

    def send_sms(self, to_number, body):
        """Send an SMS message to a specific number."""
        auth = (self.account_sid, self.auth_token)
        data = {
            "To": to_number,
            "From": self.from_number,
            "Body": body
        }
        response = requests.post(self.base_url, data=data, auth=auth)
        return response.json()

class StripeIntegration:
    """Integration for Stripe payment and subscription management."""
    def __init__(self):
        self.api_key = Config.STRIPE_API_KEY
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        self.url = "https://api.stripe.com/v1"

    def list_customers(self, limit=10):
        """List Stripe customers."""
        response = requests.get(f"{self.url}/customers", headers=self.headers, params={"limit": limit})
        return response.json()

    def create_checkout_session(self, customer_id, price_id, success_url, cancel_url):
        """Create a hosted checkout session."""
        data = {
            "customer": customer_id,
            "payment_method_types[]": "card",
            "line_items[0][price]": price_id,
            "line_items[0][quantity]": 1,
            "mode": "subscription",
            "success_url": success_url,
            "cancel_url": cancel_url
        }
        response = requests.post(f"{self.url}/checkout/sessions", headers=self.headers, data=data)
        return response.json()
