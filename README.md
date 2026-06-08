# Poke One-to-One Agent Framework

A modular, highly-functional, and anthropomorphic open-source agent framework. Designed to be more than just a chatbot, Poke One-to-One is a "brilliant but cynical best friend" that lives where you do.

## 🚀 Key Features

### 🧠 Advanced Core & Personality
- **Anthropomorphic Execution**: The agent doesn't just return results; it provides natural, witty, first-person commentary on its own "thoughts" and tool executions, mimicking the status updates of the Poke platform.
- **Dynamic Personality**: Powered by `prompts.py`, the agent mirrors user vibes (formality, casing, emoji usage) while maintaining a helpful, slightly snarky attitude.
- **Persistent Memory**: Uses a local JSON-based memory system (`tools/memory_tool.py`) to track user preferences, ongoing jokes, and emotional context across sessions.

### 🤖 Intelligent Model Routing
- **Multi-Model Support**: Integrated `ModelRouter` supports OpenAI, Anthropic, Gemini, and **xAI (Grok)**.
- **Smart Dispatch**: Automatically routes simple chats to fast "mini" models (e.g., GPT-4o-mini) and complex coding or reasoning tasks to "heavy" models (e.g., Claude 3.5 Sonnet).
- **BYOK (Bring Your Own Key)**: Users can store their personal OpenAI or xAI API keys in their memory profile. The agent will prioritize personal keys over global host keys.

### 🛠 Deep Integrations
- **Social & Auth**: Native support for **X (Twitter) OAuth 2.0** flows and session management.
- **Developer Tools**: Full GitHub integration for managing repos, issues, and PRs.
- **Productivity**: Connectors for Slack, Twilio, Stripe, Linear, and Notion.
- **Search**: Real-time web search powered by Tavily.

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dangelo352/poke-one-to-one.git
   cd poke-one-to-one
   ```

2. **Install Dependencies**:
   ```bash
   pip install requests python-telegram-bot discord.py fastapi uvicorn openai anthropic
   ```

3. **Configure Environment**:
   Create a `.env` file (see `.env.example`) and add your keys:
   - `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `XAI_API_KEY`
   - `X_CLIENT_ID`, `X_CLIENT_SECRET` (for X OAuth)
   - `TAVILY_API_KEY` (for search)

## 🎮 How to Use

### Run the Core Agent
Test the agent directly in your terminal:
```bash
python agent.py
```

### Launch a Platform
Connect your agent to a messaging service:
```bash
# For Telegram
python platforms/telegram_bot.py

# For Discord
python platforms/discord_bot.py
```

### "Bring Your Own Key" (BYOK)
To use your own subscription key, tell the agent:
> "Hey, save my OpenAI key: sk-proj-..."
The agent will save it to your persistent memory and use it for all future reasoning tasks.

## 🔧 Project Structure
- `agent.py`: The heart of the execution loop and commentary engine.
- `prompts.py`: Personality guidelines and vibe-matching instructions.
- `tools/`:
    - `model_router.py`: Logic for multi-model dispatch and Grok integration.
    - `memory_tool.py`: Persistent user-fact and preference storage.
    - `auth_manager.py`: OAuth templates for external service integration.
- `platforms/`: Entry points for various messaging and webhook interfaces.

## 🤝 Contributing
Poke One-to-One is built to be self-improving. You can use the `CoderTool` within the agent itself to propose changes to this repository!
