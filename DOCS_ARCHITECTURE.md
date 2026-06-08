# Architecture Integration: Poke Blueprint

This repository has been updated to align with the **Poke Architecture Blueprint**.

## Implemented Patterns

### 1. Orchestration Engine (`tools/orchestrator.py`)
- **State Signaling Contract**: Implements the structured `<STATE>` XML envelope for internal lifecycle tracking (IDLE, THINKING, EXECUTING, VALIDATING, RESPONDING).
- **Dynamic Arbitration**: Includes a complexity-based router to select between Direct, Single-Agent, and Multi-Agent DAG execution modes.

### 2. Guardrails & Confirmation Engine
- **High-Stakes Interception**: Tools that perform mutations (e.g., `github_manager`, `send_email`) are automatically intercepted.
- **Confirmation FSM**: Implements the `AWAITING_APPROVAL` state, ensuring no destructive actions occur without explicit user consent.

### 3. Cognitive Memory Hierarchy
- Updates to `tools/memory_tool.py` and `agent.py` reflect the prioritized context assembly described in the blueprint:
    - **Current Turn**: Immediate tool outputs and instructions.
    - **Session Memory**: Recent exchange history.
    - **Long-term Semantic Memory**: Persistent user facts and preferences.

## System Pipeline
The agent now follows the Two-Pass Webhook Filtering logic (Transport & Intent) to ensure deterministic authentication before semantic processing.
