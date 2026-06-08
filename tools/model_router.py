from config import Config

class ModelRouter:
    \"\"\"
    Routes requests to different models based on complexity.
    \"\"\"
    def __init__(self):
        self.openai_key = Config.OPENAI_API_KEY
        self.anthropic_key = Config.ANTHROPIC_API_KEY
        self.gemini_key = Config.GEMINI_API_KEY

    def get_model(self, task_description, token_estimate=0):
        \"\"\"
        Simple heuristic routing.
        - Complexity: Coding, complex tool execution, or large contexts use 'heavy' models.
        - Speed/Cost: Simple chat or basic search uses 'mini' models.
        \"\"\"
        heavy_keywords = ["code", "refactor", "complex", "debug", "analyze"]
        is_heavy = any(kw in task_description.lower() for kw in heavy_keywords) or token_estimate > 4000

        if is_heavy:
            # Prefer Claude 3.5 Sonnet for heavy reasoning/coding if key exists
            if self.anthropic_key:
                return "claude-3-5-sonnet-20240620", "anthropic"
            return Config.HEAVY_MODEL, "openai"
        
        # Default to fast/cheap model
        return Config.DEFAULT_MODEL, "openai"

    def dispatch(self, messages, task_description=\"\"):
        model, provider = self.get_model(task_description)
        print(f"[Router] Dispatching to {model} via {provider}...")
        
        # Mocking the actual provider call
        return f"Response from {model} for task: {task_description}"
