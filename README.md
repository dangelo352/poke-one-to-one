# Poke One-to-One Agent Framework

... (previous content) ...

## Recipe System (`recipes/`)
The agent now supports Poke-style modular workflows called **Recipes**. These are JSON files that define a sequence of tool calls.

### How to Write a Recipe
Create a JSON file in the `recipes/` directory following the `recipes/schema.json`.

Example (`recipes/market_brief.json`):
```json
{
  "metadata": { "name": "Company Research" },
  "steps": [
    {
      "id": "search",
      "tool": "web_search",
      "args": { "query": "News about {{company}}" }
    }
  ]
}
```

### Loading & Running Recipes
The `RecipeParser` in `tools/recipe_parser.py` handles execution. You can trigger a recipe via the agent loop:
```python
from tools.recipe_parser import RecipeParser
parser = RecipeParser(agent)
parser.execute("recipes/market_brief.json", {"company": "Tesla"})
```

... (remaining content) ...
