import sys
import argparse
from agent import Agent
from tools.orchestrator import Orchestrator
from tools.model_checker import ModelChecker

def main():
    parser = argparse.ArgumentParser(description="Poke One-to-One Agent CLI")
    parser.add_argument("--check", action="store_true", help="Run model connectivity diagnostics")
    args = parser.parse_args()

    # Initialize components
    agent = Agent()
    orchestrator = Orchestrator(agent)

    if args.check:
        checker = ModelChecker(user_keys=agent.user_keys)
        checker.run_diagnostics()
        return

    print("--- Poke One-to-One Interactive CLI ---")
    print("Type 'exit' or 'quit' to stop.")
    print("Type 'check' to run diagnostics.")
    
    while True:
        try:
            user_input = input("\nUser: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                break
            
            if user_input.lower() == "check":
                checker = ModelChecker(user_keys=agent.user_keys)
                checker.run_diagnostics()
                continue

            if not user_input:
                continue

            # Run through orchestrator for arbitration and safety
            response = orchestrator.process_turn(user_input)
            print(f"\nPoke: {response}")

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
