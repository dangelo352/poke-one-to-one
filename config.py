import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    \"\"\"Handles environment variables and API keys.\"\"\"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    XAI_API_KEY = os.getenv("XAI_API_KEY")
    
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    
    # X (Twitter) Credentials
    X_CLIENT_ID = os.getenv("X_CLIENT_ID")
    X_CLIENT_SECRET = os.getenv("X_CLIENT_SECRET")
    
    DEFAULT_MODEL = "gpt-4o-mini"
    HEAVY_MODEL = "gpt-4o"
    GROK_MODEL = "grok-beta"

    @classmethod
    def validate(cls):
        required = ["OPENAI_API_KEY"]
        missing = [k for k in required if not getattr(cls, k)]
        if missing:
            print(f"Warning: Missing required configuration for {', '.join(missing)}")
