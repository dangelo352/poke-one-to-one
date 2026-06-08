import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Handles environment variables and API keys."""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    MODEL_NAME = "gpt-4-turbo"

    @classmethod
    def validate(cls):
        missing = [k for k, v in cls.__dict__.items() if not k.startswith("__") and not v]
        if missing:
            print(f"Warning: Missing configuration for {', '.join(missing)}")
