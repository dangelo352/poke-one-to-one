import json
import os
from typing import Dict, Any, List

class Orchestrator:
    """
    Implements the Orchestration Engine from the Architecture Blueprint.
    Manages task decomposition, state signaling, and confirmation guardrails.
    """
    STATES = ["IDLE", "THINKING", "EXECUTING", "VALIDATING", "RESPONDING"]

    def __init__(self, agent):
        self.agent = agent
        self.current_state = "IDLE"
        self.pending_action = None

    def set_state(self, state: str):
        if state in self.STATES:
            self.current_state = state
            print(f"[State] {state}")
        else:
            raise ValueError(f"Invalid state: {state}")

    def arbitrate(self, request: str) -> str:
        """
        Arbitration Logic: Decides between Direct, Single-Agent, or Multi-Agent modes.
        Matches the Blueprint's 'Dynamic Agent-Arbitration Engine'.
        """
        self.set_state("THINKING")
        
        # Complexity heuristic
        complexity = len(request.split())
        if complexity < 5:
            mode = "DIRECT"
        elif "and" in request.lower() or "then" in request.lower():
            mode = "MULTI_AGENT_DAG"
        else:
            mode = "SINGLE_AGENT"
            
        return mode

    def handle_tool_call(self, tool_name: str, args: Dict[str, Any]):
        """
        Implements Section 4: Guardrails and Confirmation Engine.
        Intercepts high-stakes actions.
        """
        self.set_state("VALIDATING")
        
        high_stakes_tools = ["github_manager", "delete_file", "send_email"]
        
        if tool_name in high_stakes_tools:
            self.set_state("AWAITING_APPROVAL")
            self.pending_action = {"tool": tool_name, "args": args}
            return {
                "status": "PAUSE",
                "message": f"High-stakes action detected: {tool_name}. Approval required.",
                "preview": args
            }
        
        self.set_state("EXECUTING")
        return {"status": "PROCEED"}

    def signal_state(self, message: str) -> str:
        """
        Implements Section 1.5: State Signaling Contract.
        Wraps response in XML tags for internal lifecycle tracking.
        """
        return f"<{self.current_state}>{message}</{self.current_state}>"
