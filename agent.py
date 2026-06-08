import json
from config import Config
from tools.search import web_search
from tools.github_tool import github_manager
from tools.calendar_tool import calendar_manager

class Agent:
    def __init__(self):
        self.history = [{"role": "system", "content": "You are a highly capable AI assistant with access to tools."}]
        self.tools = {
            "web_search": web_search,
            "github_manager": github_manager,
            "calendar_manager": calendar_manager
        }

    def run(self, user_input):
        self.history.append({"role": "user", "content": user_input})
        
        while True:
            # This is a mock of the LLM call logic
            # In a real implementation, you would call OpenAI/Anthropic here
            print(f"Agent processing: {user_input}")
            
            # Simulated Tool Call Detection
            # For demonstration, we'll assume the LLM wants to search if the input contains 'search'
            if "search" in user_input.lower():
                tool_result = self.execute_tool("web_search", {"query": user_input})
                print(f"Tool Result: {tool_result}")
                return tool_result
            
            break

    def execute_tool(self, tool_name, args):
        if tool_name in self.tools:
            return self.tools[tool_name](**args)
        return f"Error: Tool {tool_name} not found."

if __name__ == "__main__":
    Config.validate()
    agent = Agent()
    agent.run("Search for the latest news on AI agents.")
