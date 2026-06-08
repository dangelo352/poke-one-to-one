import json
import os

MEMORY_FILE = "user_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"facts": [], "preferences": [], "jokes": [], "user_mood": "neutral"}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def memory_manager(action, category=None, content=None):
    """
    Manages the persistent memory of the agent.
    Actions: 'load', 'save', 'update_mood'
    """
    memory = load_memory()
    
    if action == "load":
        return memory
    
    if action == "save" and category and content:
        if category in memory:
            memory[category].append(content)
            save_memory(memory)
            return f"Saved to {category}: {content}"
        return f"Error: Category {category} not found."
    
    if action == "update_mood" and content:
        memory["user_mood"] = content
        save_memory(memory)
        return f"Updated user mood to: {content}"
    
    return "Invalid memory action."
