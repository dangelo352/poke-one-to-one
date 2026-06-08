# Poke One-to-One Agent Framework

A modular, highly-functional open-source agent framework designed for production use, built with an intuitive "brilliant but cynical" personality inspired by Poke.

## Features
- **Intelligent Core Loop**: A clean `agent.py` implementation with structured tool execution and first-person "thinking" commentary.
- **Dynamic Multi-Model Routing**: Automatically routes tasks between OpenAI (GPT-4o/mini), Anthropic (Claude 3.5 Sonnet), and xAI (Grok) based on task complexity.
- **Persistent Memory**: A local JSON-based long-term memory system that tracks user preferences, facts, and emotional context across sessions.
- **BYOK (Bring Your Own Key)**: Support for user-specific API keys stored in encrypted memory, allowing the agent to use personal subscriptions.
- **Advanced Recipe Engine**: Define complex multi-step workflows in JSON blueprints (`recipes/`) that can be executed sequentially or conditionally.

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install requests python-dotenv python-telegram-bot discord.py fastapi uvicorn
   ```
3. Create a `.env` file based on the config requirements and add your keys (OpenAI, GitHub, etc.).

## Usage
Run the core agent:
```bash
python agent.py
```
Or start a specific platform bot:
```bash
python platforms/telegram_bot.py
```

## Integrations
The framework includes built-in support for:
- **Slack & Discord**: Direct messaging and channel management.
- **GitHub**: Repository management, automated coding, and PR reviews via `tools/coder_tool.py`.
- **Communications**: Twilio for SMS/Calling and Resend for style-matched emails.
- **Payments**: Stripe integration for managing customer subscriptions and billing.
- **Dev Tools**: Vercel, Sentry, Linear, PostHog, and Supabase for full-stack observability.

## Recipe System (`recipes/`)
Recipes are modular blueprints that allow you to automate repetitive workflows. Each recipe defines metadata, required parameters, and a sequence of tool steps.

### Example: Market Research
```json
{
  "metadata": { "name": "Market Intelligence", "trigger": { "type": "manual" } },
  "steps": [
    { "id": "search", "tool": "web_search", "args": { "query": "News about {{company}}" } },
    { "id": "save", "tool": "memory_manager", "args": { "action": "save", "category": "facts", "content": "{{search.output}}" } }
  ]
}
```

Documentation on writing custom recipes can be found in `recipes/schema.json`.
