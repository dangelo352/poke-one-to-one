import json
import random
from config import Config
from tools.search import web_search
from tools.github_tool import github_manager
from tools.calendar_tool import calendar_manager
from tools.memory_tool import memory_manager
from prompts import get_system_prompt

class Agent:
    def __init__(self):
        # Load memory at initialization
        self.memory = memory_manager("load")
        user_context = json.dumps(self.memory)
        
        self.history = [{"role": "system", "content": get_system_prompt(user_context=user_context)}]
        self.tools = {
            "web_search": web_search,
            "github_manager": github_manager,
            "calendar_manager": calendar_manager,
            "memory_manager": memory_manager
        }

    def generate_commentary(self, stage):
        commentaries = {
            "evaluating": [
                "Scanning your brain... wait, that's just the request. Processing.",
                "I see what you're doing here. Clever.",
                "Analyzing this. Give me a second to look smart."
            ],
            "executing": [
                "Consulting the archives (aka the internet).",
                "Doing the heavy lifting for you, as usual.",
                "Tapping into the matrix for this one."
            ],
            "finished": [
                "And... voila. I'm basically a magician.",
                "There you go. Don't say I never did anything for you.",
                "Task complete. I'll take my payment in digital headpats."
            ]
        }
        return random.choice(commentaries.get(stage, ["Processing..."]))

    def run(self, user_input):
        # Refresh memory for every run to ensure up-to-date context
        self.memory = memory_manager("load")
        
        self.history.append({"role": "user", "content": user_input})
        
        # 1. Evaluation Phase
        print(f"[Thought] {self.generate_commentary('evaluating')}")
        
        while True:
            # Simulated logic to detect tool use or memory updates
            # In a real setup, the LLM would decide which tool to call.
            
            if "search" in user_input.lower():
                print(f"[Action] {self.generate_commentary('executing')}")
                tool_result = self.execute_tool("web_search", {"query": user_input})
                print(f"[Status] {self.generate_commentary('finished')}")
                return tool_result
            
            # Example of the agent deciding to save a memory
            if "remember" in user_input.lower():
                fact = user_input.replace("remember that", "").strip()
                res = self.execute_tool("memory_manager", {"action": "save", "category": "facts", "content": fact})
                print(f"[Memory] {res}")
                return "Got it. Locked in the vault."
            
            break

    def execute_tool(self, tool_name, args):
        if tool_name in self.tools:
            return self.tools[tool_name](**args)
        return f"Error: Tool {tool_name} not found."

if __name__ == "__main__":
    Config.validate()
    agent = Agent()
    # Test memory persistence
    agent.run("Remember that I love dark roast coffee.")
    agent.run("Search for the best dark roast beans.")
