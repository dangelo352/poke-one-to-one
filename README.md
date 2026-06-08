# Poke One-to-One Agent Framework

A modular, highly-functional open-source agent framework designed for production use.

## Features
- **Core Agent Loop**: Clean `agent.py` implementation with structured tool execution.
- **Snarky Personality**: Pre-configured system prompts in `prompts.py`.
- **Multi-Platform Support**: Ready-to-use boilerplate for Telegram, Discord, and Webhooks.
- **Deep Integrations**:
    - **Search**: Tavily-powered web search.
    - **GitHub**: Repository management and issue tracking.
    - **Coding**: Automated file manipulation and PR management via `tools/coder_tool.py`.
    - **Productivity**: Connectors for Linear, Notion, and Todoist.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install requests python-telegram-bot discord.py fastapi uvicorn`.
3. Configure `config.py` with your API keys.

## Usage
Run the core agent:
```bash
python agent.py
```
Or start a specific platform:
```bash
python platforms/telegram_bot.py
```

## Coder Tool (`tools/coder_tool.py`)
The `CoderTool` allows the agent to:
- Browse repository file structures.
- Read, write, and modify files on specific branches.
- Commit changes with descriptive messages.
- Open Pull Requests for human review.

This enables a "self-improving" or "contributor" agent flow.
