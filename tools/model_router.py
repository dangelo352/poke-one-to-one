from config import Config

class ModelRouter:
    """
    Routes requests to different models based on complexity.
    Supports OpenAI, Anthropic, Gemini, and xAI (Grok).
    Supports User-Specific (BYOK) keys.
    """
    def __init__(self, user_keys=None):
        """
        Initialize with optional user-specific keys.
        user_keys: dict containing keys like 'openai_api_key', 'xai_api_key', etc.
        """
        self.user_keys = user_keys or {}
        
        # Priority: User Key > Global Config Key
        self.openai_key = self.user_keys.get("openai_api_key") or Config.OPENAI_API_KEY
        self.anthropic_key = self.user_keys.get("anthropic_api_key") or Config.ANTHROPIC_API_KEY
        self.gemini_key = self.user_keys.get("gemini_api_key") or Config.GEMINI_API_KEY
        self.xai_key = self.user_keys.get("xai_api_key") or Config.XAI_API_KEY

    def get_model(self, task_description, token_estimate=0):
        """
        Heuristic routing with multi-provider support.
        """
        task_lower = task_description.lower()
        
        # Manual Override/Intent
        if "grok" in task_lower and self.xai_key:
            return Config.GROK_MODEL, "xai"
        
        if "gemini" in task_lower and self.gemini_key:
            return "gemini-1.5-flash", "gemini"

        # Complexity Scoring
        heavy_keywords = ["code", "refactor", "complex", "debug", "analyze", "architectural"]
        is_heavy = any(kw in task_lower for kw in heavy_keywords) or token_estimate > 4000

        if is_heavy:
            # Prefer Anthropic for complex reasoning/coding if available
            if self.anthropic_key:
                return "claude-3-5-sonnet-20240620", "anthropic"
            # Fallback to GPT-4o
            return Config.HEAVY_MODEL, "openai"
        
        # Lightweight Default
        # Use Gemini Flash if available for speed/cost, else GPT-4o-mini
        if self.gemini_key:
             return "gemini-1.5-flash", "gemini"
             
        return Config.DEFAULT_MODEL, "openai"

    def dispatch(self, messages, task_description=""):
        model, provider = self.get_model(task_description)
        
        # Determine which key to use
        api_key = getattr(self, f"{provider}_key", None)
        
        # In a real implementation, you'd route to the actual provider client
        print(f"[Router] Dispatching to {model} via {provider} (User Key: {provider in self.user_keys})...")
        return f"Response from {model} for task: {task_description}"
