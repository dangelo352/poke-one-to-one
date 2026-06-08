import json
import re

class RecipeParser:
    """
    Loads and executes Poke-style recipes (JSON workflows).
    """
    def __init__(self, agent):
        self.agent = agent
        self.context = {}

    def load_recipe(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

    def _resolve_variables(self, data, params):
        """Recursively resolve {{variable}} placeholders."""
        if isinstance(data, str):
            # Resolve parameters
            for k, v in params.items():
                data = data.replace(f"{{{{{k}}}}}", str(v))
            # Resolve step outputs (e.g., {{step_id.output}})
            for step_id, result in self.context.items():
                data = data.replace(f"{{{{{step_id}.output}}}}", str(result))
            return data
        elif isinstance(data, dict):
            return {k: self._resolve_variables(v, params) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._resolve_variables(v, params) for v in data]
        return data

    def execute(self, recipe_path, input_params=None):
        recipe = self.load_recipe(recipe_path)
        metadata = recipe.get("metadata", {})
        steps = recipe.get("steps", [])
        
        # Merge default params with provided inputs
        params = {k: v.get("default") for k, v in recipe.get("parameters", {}).items()}
        if input_params:
            params.update(input_params)

        print(f"[Recipe] Starting execution: {metadata.get('name')}")
        
        for step in steps:
            step_id = step.get("id")
            tool_name = step.get("tool")
            args = self._resolve_variables(step.get("args", {}), params)
            
            # Simple condition check (mock implementation)
            if "condition" in step:
                cond = self._resolve_variables(step["condition"], params)
                if not eval(cond): # Caution: in production use a safer eval
                    print(f"[Recipe] Skipping step {step_id} due to condition.")
                    continue

            print(f"[Recipe] Executing tool: {tool_name} with args: {args}")
            
            # Use the agent's existing tool execution logic
            result = self.agent.execute_tool(tool_name, args)
            
            if step_id:
                self.context[step_id] = result

        print(f"[Recipe] Completed: {metadata.get('name')}")
        return self.context
