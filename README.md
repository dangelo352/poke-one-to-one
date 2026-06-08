# Poke One-to-One Agent Framework

A complete, highly-functional open-source agent framework designed for modularity and ease of use. This framework implements a core agent loop with structured tool execution, enabling it to perform web searches, manage GitHub repositories, and coordinate calendar events.

## Features

- **Modular Architecture**: Separate logic for core agent loops, configuration, and tool implementations.
- **Robust Tool Executor**: Handles complex tool calls with a structured system/user/assistant message loop.
- **Pre-built Tools**:
  - **Web Search**: Integrated search capabilities.
  - **GitHub**: Interface for repository and issue management.
  - **Calendar**: Management for scheduling and events.

## Setup and Configuration

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dangelo352/poke-one-to-one.git
   cd poke-one-to-one
   ```

2. **Install dependencies**:
   ```bash
   pip install openai requests python-dotenv
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_key
   GITHUB_TOKEN=your_github_token
   TAVILY_API_KEY=your_tavily_key
   ```

## Running the Agent

Run the main agent loop:
```bash
python agent.py
```

## Architecture

- `config.py`: Centralized environment variable management.
- `agent.py`: The heart of the framework, managing the LLM interaction and tool execution cycle.
- `tools/`: A directory containing modular tool definitions.

## Contributing

We welcome contributions! Please submit a PR or open an issue for any improvements.
