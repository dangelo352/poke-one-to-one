import sys
from agent import Agent
from tools.orchestrator import Orchestrator
from tools.memory_tool import memory_manager

def main():
    print("--- Poke One-to-One Agent CLI ---")
    print("Initializing components...")
    
    agent = Agent()
    orchestrator = Orchestrator(agent)
    
    user_name = memory_manager("load").get("user_name", "User")
    print(f"Welcome back, {user_name}. (Type 'exit' to quit)")

    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                break
            
            # Use Orchestrator to handle arbitration and state signaling
            response = orchestrator.handle_request(user_input)
            
            # The orchestrator handles the internal logic; 
            # for the CLI we just display the final response.
            print(f"\n{response}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
