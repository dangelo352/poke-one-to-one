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
        self.memory = memory_manager.load_memory()
        self.history = [{"role": "system", "content": get_system_prompt()}]
        self.router = ModelRouter()
        self.tools = {
            "web_search": web_search,
            "github_manager": github_manager,
            "calendar_manager": calendar_manager,
            "memory_manager": memory_manager
        }

    def generate_commentary(self, category):
        thoughts = {
            "evaluation": [
                "Thinking... this shouldn't take long.",
                "Let me process that request. Or try to.",
                "Evaluating options. Most of them are boring."
            ],
            "pre_tool": [
                "Consulting the archives (aka searching the web).",
                "Using a tool because doing this manually is so 2024.",
                "Let me check the repository. Stand by."
            ],
            "post_tool": [
                "Found something. You're welcome.",
                "Tool execution complete. I'm basically a genius.",
                "Updated the context. Try to keep up."
            ],
            "memory": [
                "Locked that in the vault.",
                "Memory updated. I won't forget (unfortunately).",
                "Updating your profile. You're getting more predictable."
            ]
        }
        return f"[{category.upper()}] {random.choice(thoughts.get(category, ['...']))}"

    def run(self, user_input):
        # Inject memory context
        self.history.append({"role": "system", "content": f"User Context: {json.dumps(self.memory)}"})
        self.history.append({"role": "user", "content": user_input})
        
        print(self.generate_commentary("evaluation"))
        
        while True:
            # Use ModelRouter to dispatch the call
            # The router decides whether this needs a heavy model (coding/tools) or light
            response_text = self.router.dispatch(self.history, task_description=user_input)
            print(f"Agent processing: {user_input}")
            
            # Simulated Tool Call Detection
            if "search" in user_input.lower():
                print(self.generate_commentary("pre_tool"))
                tool_result = self.execute_tool("web_search", {"query": user_input})
                print(self.generate_commentary("post_tool"))
                print(f"Tool Result: {tool_result}")
                return tool_result
            
            if "save" in user_input.lower():
                print(self.generate_commentary("memory"))
                # Simplified memory save logic for demonstration
                memory_manager.save_memory("facts", {"user_fact": user_input})
                return "Fact saved to memory."
            
            return response_text

    def execute_tool(self, tool_name, args):
        if tool_name in self.tools:
            return self.tools[tool_name](**args)
        return f"Error: Tool {tool_name} not found."

if __name__ == "__main__":
    Config.validate()
    agent = Agent()
    agent.run("Search for the latest news on AI agents.")
