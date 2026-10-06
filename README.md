# AgentForge

A polished open-source toolkit for building AI agents with tools, memory, and workflow automation.

## Why AgentForge?

Most AI demos stop at simple chat. AgentForge gives developers the building blocks to create real agents that can:

- Search the web
- Read and write files
- Use memory across tasks
- Run workflows
- Call custom tools
- Run locally or with LLM APIs

This is designed for people who want to prototype agentic apps quickly without heavy boilerplate.

## Project pitch

AgentForge is an open-source framework for building AI agents that can think, call tools, remember context, and complete multi-step tasks.

## Features

- Lightweight agent core
- Tool registry system
- Short-term memory
- Web search tool with live API support
- File read/write tools
- Command execution with safeguards
- Python-first API
- CLI for quick demos
- Extensible architecture for plugins and new tools

## Installation

```bash
git clone https://github.com/Tdat10052499/agentforge.git
cd agentforge
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Required environment variables

Create a `.env` file or export variables in your shell:

```bash
export OPENAI_API_KEY=your-key-here
export AGENTFORGE_MODEL=gpt-4o-mini
export AGENTFORGE_ENABLE_COMMANDS=0
export AGENTFORGE_USE_REAL_SEARCH=1
```

Copy the example file:

```bash
cp .env.example .env
```

## Quick start

```python
from agentforge import Agent, Tool


def web_search(query: str) -> str:
    return f"Search results for: {query}"

agent = Agent(name="research-agent")
agent.add_tool(
    Tool(
        name="web_search",
        description="Search the web for information",
        func=web_search,
    )
)

result = agent.run("Find the latest AI agent frameworks and summarize them.")
print(result)
```

## CLI usage

```bash
python -m agentforge.cli --agent research --task "What are the latest AI agent frameworks?"
python -m agentforge.cli --agent file-analyzer --task "read:README.md"
python -m agentforge.cli --agent workflow --task "Search for AI agent libraries and summarize the best options"
```

## Example agents

- Research agent: searches the web and summarizes results
- File analysis agent: reads files and summarizes content
- Workflow agent: chains several actions together

Examples are included in the `examples/` folder.

## Architecture

```text
agentforge/
├── __init__.py
├── agent.py
├── config.py
├── memory.py
├── tools.py
├── cli.py
├── examples/
├── tests/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
├── CHANGELOG.md
└── README.md
```

## Roadmap

### v0.1
- Agent core
- Memory
- Tool registry
- File tools
- CLI
- Documentation

### v0.2
- OpenAI / Anthropic integration
- Real search support
- Workflow engine
- More built-in tools

### v0.3
- OLLAMA local model support
- Browser tool input/output
- Better memory handling
- More examples and tutorials

### v1.0
- Dashboard or UI
- Multi-agent collaboration
- Production deployment guides
- Better plugin ecosystem

## Contributing

We welcome contributions.

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and contribution guidelines.

## License

MIT License.

## Star this project

If you find AgentForge useful, give it a star and help it grow.

---

This project is still in early alpha, but the goal is to become a clean, practical tool that developers can use and discuss.
