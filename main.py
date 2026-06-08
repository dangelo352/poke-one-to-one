import argparse
from tools.orchestrator import Orchestrator
from tools.model_checker import ModelChecker
from tools.model_router import ModelRouter

def interactive_loop():
    orch = Orchestrator()
    print("\nPoke One-to-One Agent CLI")
    print("Type 'exit' to quit, 'check' for diagnostics.")
    
    while True:
        user_input = input("\nUser > ")
        if user_input.lower() in ["exit", "quit"]:
            break
        
        if user_input.lower() == "check":
            checker = ModelChecker(user_keys=orch.agent.user_keys)
            checker.run_diagnostics()
            checker.run_routing_test(orch.agent.router)
            continue
            
        response = orch.process_request(user_input)
        print(f"\nPoke > {response}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Poke One-to-One Agent CLI")
    parser.add_argument("--check", action="store_true", help="Run model connectivity and routing diagnostics")
    args = parser.parse_args()

    if args.check:
        # For simulation purposes, we create a router with dummy keys if none in env
        router = ModelRouter()
        checker = ModelChecker()
        checker.run_diagnostics()
        checker.run_routing_test(router)
    else:
        interactive_loop()
