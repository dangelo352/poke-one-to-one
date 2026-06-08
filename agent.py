import json
import random
from config import Config
from tools.search import web_search
from tools.github_tool import github_manager
from tools.calendar_tool import calendar_manager
from tools.memory_tool import memory_manager
from tools.model_router import ModelRouter
from prompts import get_system_prompt

class Agent:
    def __init__(self):
        # Load user context and BYOK keys
        self.memory = memory_manager("load")
        self.user_keys = self.memory.get("api_keys", {})
        
        # Initialize Router with user-specific keys if available
        self.router = ModelRouter(user_keys=self.user_keys)
        
        # Set up identity
        system_msg = get_system_prompt(user_name=self.memory.get("user_name", "User"))
        self.history = [{"role": "system", "content": system_msg}]
        
        self.tools = {
            "web_search": web_search,
            "github_manager": github_manager,
            "calendar_manager": calendar_manager,
            "memory_manager": memory_manager
        }

    def generate_commentary(self, context_type):
        comments = {
            "evaluate": [
                "Processing this... slowly. Don't rush me.",
                "Analyzing. Try not to be so predictable next time.",
                "Reading between the lines. There's not much there."
            ],
            "tool_pre": [
                "Fine, I'll use a tool. You're welcome.",
                "Consulting the archives because you clearly can't.",
                "Executing... hope this is worth the tokens."
            ],
            "tool_post": [
                "Done. It was easier than I expected, which says a lot.",
                "Result's in. Try to keep up.",
                "[Memory] Locked in the vault. Not that it was worth remembering."
            ]
        }
        return f"[{random.choice(comments[context_type])}]"

    def run(self, user_input):
        print(self.generate_commentary("evaluate"))
        self.history.append({"role": "user", "content": user_input})
        
        while True:
            # Use the model router for the LLM call
            response = self.router.dispatch(self.history, task_description=user_input)
            
            # Simplified tool execution logic for this template
            if "search" in user_input.lower():
                print(self.generate_commentary("tool_pre"))
                tool_result = self.execute_tool("web_search", {"query": user_input})
                print(self.generate_commentary("tool_post"))
                return tool_result
            
            return response

    def execute_tool(self, tool_name, args):
        if tool_name in self.tools:
            return self.tools[tool_name](**args)
        return f"Error: Tool {tool_name} not found."

if __name__ == "__main__":
    Config.validate()
    agent = Agent()
    agent.run("Search for the latest news on AI agents.")
