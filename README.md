# Poke One-to-One Agent Framework

Poke is a modular, event-driven agent framework designed for production-grade personal automation. It bridges the gap between consumer messaging clients (Telegram, Discord) and complex LLM orchestration.

## 🏗 High-Level Architecture

Poke follows a "Cognitive Middleware" pattern, decoupling user interfaces from reasoning logic.

- **Dynamic Arbitration**: The system evaluates task complexity (1-10) to select the optimal execution mode:
    - **Direct**: Standard chat via cost-effective models (GPT-4o-mini).
    - **Single-Agent**: Tool-specific execution.
    - **Multi-Agent DAG**: Complex, parallel workflows for heavy tasks (Claude 3.5 Sonnet / GPT-4o).
- **State Signaling**: Internal turn-lifecycle is tracked via a structured XML-based contract (`<THINKING>`, `<EXECUTING>`, etc.), ensuring clean observability.
- **Confirmation Engine**: A safety-first interception layer classifies actions as "High-Stakes" (e.g., GitHub pushes, emails) to enforce explicit user approval.
- **BYOK (Bring Your Own Key)**: Users can provide their own API keys via the persistent memory system, offloading billing to personal subscriptions.

## 🚀 Quickstart

### 1. Installation
Clone the repo and install dependencies:
```bash
pip install -r requirements.txt
# Core dependencies: requests, python-telegram-bot, discord.py, fastapi, uvicorn, python-dotenv
```

### 2. Configuration
Copy the template and fill in your global API keys:
```bash
cp .env.example .env
```
*Required: `OPENAI_API_KEY`. Optional: `ANTHROPIC_API_KEY`, `XAI_API_KEY`, `GITHUB_TOKEN`, `TELEGRAM_BOT_TOKEN`, `DISCORD_BOT_TOKEN`.*

### 3. Run the Agent

**Interactive CLI:**
```bash
python main.py
```

**Telegram Bot:**
```bash
python platforms/telegram_bot.py
```

**Discord Bot:**
```bash
python platforms/discord_bot.py
```

## 📜 Recipe System

Recipes are modular JSON blueprints for automated workflows.

- **Location**: `/recipes`
- **Schema**: Defined in `recipes/schema.json`

**Example Workflow:**
The `daily_ai_news_briefing.json` recipe automates web searching for AI news, summarizing results, and alerting the user.

## 📂 Project Structure

- `main.py`: CLI entrypoint.
- `agent.py`: Core agent reasoning loop.
- `tools/`:
    - `orchestrator.py`: Arbitration and safety guardrails.
    - `model_router.py`: Multi-model dispatching (incl. Grok).
    - `recipe_parser.py`: JSON workflow execution.
    - `memory_tool.py`: Persistent user context and BYOK.
- `platforms/`: Telegram and Discord connectors.
- `recipes/`: Pre-defined automation JSONs.
