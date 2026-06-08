import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    \"\"\"Handles environment variables and API keys.\"\"\"
    # Model API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # Tool API Keys
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    
    # X (Twitter) Credentials
    X_CLIENT_ID = os.getenv("X_CLIENT_ID")
    X_CLIENT_SECRET = os.getenv("X_CLIENT_SECRET")
    X_REDIRECT_URI = os.getenv("X_REDIRECT_URI")

    # Default Model Settings
    DEFAULT_MODEL = "gpt-4o-mini"
    HEAVY_MODEL = "gpt-4o"

    @classmethod
    def validate(cls):
        required = ["OPENAI_API_KEY"]
        missing = [k for k in required if not getattr(cls, k)]
        if missing:
            print(f"Warning: Missing critical configuration for {', '.join(missing)}")
