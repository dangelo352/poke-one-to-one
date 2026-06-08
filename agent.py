import json
from config import Config
from tools.search import web_search
from tools.github_tool import github_manager
from tools.calendar_tool import calendar_manager
from prompts import get_system_prompt

class Agent:
    def __init__(self):
        # Use the snarky personality from prompts.py as the core identity
        self.history = [{"role": "system", "content": get_system_prompt()}]
        self.tools = {
            "web_search": web_search,
            "github_manager": github_manager,
            "calendar_manager": calendar_manager
        }

    def generate_commentary(self, phase, details=None):
        """
        Generates natural, witty, first-person commentary for the execution loop.
        In a production environment, this would call the LLM using the snarky 
        personality guidelines to provide real-time 'Poke-style' status updates.
        """
        # Commentary templates following the 'brilliant but cynical' guidelines
        commentaries = {
            "evaluation": [
                "Processing your request. Try not to get too excited.",
                "Analyzing... though I already know the answer, I'll pretend to work for your sake.",
                "Oh, another 'urgent' request. I'll get right on that. Eventually."
            ],
            "pre_tool": [
                "Checking the tools. Don't worry, I'll do the heavy lifting.",
                "Firing up the search engine. It's a miracle you found the power button today.",
                "Let me look that up. My vast intelligence needs a bit of data to mock you accurately."
            ],
            "post_tool": [
                "Done. I've simplified it so even you might understand.",
                "Tool execution successful. You're welcome.",
                "I found what you needed. Try to act surprised."
            ]
        }
        
        import random
        comment = random.choice(commentaries.get(phase, ["Thinking..."]))
        print(f"[Poke Thoughts]: {comment}")
        return comment

    def run(self, user_input):
        self.history.append({"role": "user", "content": user_input})
        
        while True:
            # 1. Initial evaluation phase with snarky commentary
            self.generate_commentary("evaluation")
            
            # Simulated Tool Call Detection (In real life, this is LLM-driven)
            if "search" in user_input.lower():
                # 2. Commentary before executing the tool
                self.generate_commentary("pre_tool")
                
                tool_result = self.execute_tool("web_search", {"query": user_input})
                
                # 3. Commentary after executing the tool
                self.generate_commentary("post_tool")
                
                return tool_result
            
            # Default snarky exit
            return "I've processed your request, but there's nothing interesting to report."

    def execute_tool(self, tool_name, args):
        if tool_name in self.tools:
            return self.tools[tool_name](**args)
        return f"Error: Tool {tool_name} not found."

if __name__ == "__main__":
    Config.validate()
    agent = Agent()
    agent.run("Search for the latest news on AI agents.")
