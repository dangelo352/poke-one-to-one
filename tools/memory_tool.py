import json
import os

MEMORY_FILE = "user_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {
        "facts": [], 
        "preferences": [], 
        "jokes": [], 
        "user_mood": "neutral",
        "api_keys": {} # Stores BYOK like {"openai_api_key": "sk-...", "xai_api_key": "xai-..."}
    }

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def memory_manager(action, category=None, content=None):
    \"\"\"
    Manages the persistent memory of the agent.
    Actions: 'load', 'save', 'update_mood', 'set_key'
    \"\"\"
    memory = load_memory()
    
    if action == "load":
        return memory
    
    if action == "save" and category and content:
        if category in memory:
            if isinstance(memory[category], list):
                memory[category].append(content)
            else:
                memory[category] = content
            save_memory(memory)
            return f"Saved to {category}: {content}"
        return f"Error: Category {category} not found."
    
    if action == "update_mood" and content:
        memory["user_mood"] = content
        save_memory(memory)
        return f"Updated user mood to: {content}"

    if action == "set_key" and category and content:
        # category would be the key name like 'openai_api_key'
        if "api_keys" not in memory:
            memory["api_keys"] = {}
        memory["api_keys"][category] = content
        save_memory(memory)
        return f"Successfully set personal API key for {category}."
    
    return "Invalid memory action."
