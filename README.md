# AgentForge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

AgentForge is an open-source toolkit for building AI agents that can reason, use tools, remember context, and complete complex workflows.

## Why AgentForge?

Most AI demos stop at simple chat. AgentForge helps developers build real AI agents that can:
- 🔍 Search the web for information
- 📁 Read and write files
- 💾 Maintain conversation memory
- ⚙️ Execute tasks and commands
- 🔄 Run multi-step workflows
- 🧩 Extend with custom tools

This project is built for developers who want to prototype AI agents quickly without dealing with heavy boilerplate.

## Features

✅ **Lightweight Agent Core** - Simple, intuitive API for building agents
✅ **Tool Calling System** - Register and execute tools automatically
✅ **Memory Management** - Short-term and conversation history
✅ **Web Search & Fetch** - Built-in web tools
✅ **File Operations** - Read, write, and analyze files
✅ **CLI Support** - Run agents from command line
✅ **Easy Extension** - Add custom tools in seconds
✅ **Local Development** - No cloud dependencies required

## Installation

### From PyPI (coming soon)
```bash
pip install agentforge
```

### From Source
```bash
git clone https://github.com/Tdat10052499/agentforge.git
cd agentforge
pip install -e .
```

## Quick Start

### Simple Example

```python
from agentforge import Agent, Tool

def web_search(query: str) -> str:
    # In real version, this calls a search API
    return f"Search results for: {query}"

# Create an agent
agent = Agent(name="research-agent")

# Add a tool
agent.add_tool(
    Tool(
        name="web_search",
        description="Search the web for information",
        func=web_search
    )
)

# Run the agent
result = agent.run("Find information about AI agents")
print(result)
```

### CLI Usage

```bash
# Run a research agent
python -m agentforge.cli --agent research --task "What are the latest AI trends?"

# Run a file analysis agent
python -m agentforge.cli --agent file-analyzer --task "Summarize README.md"

# Run a workflow agent
python -m agentforge.cli --agent workflow --task "search for Python libraries, then summarize top 3"
```

## Project Structure

```
agentforge/
├── agentforge/
│   ├── __init__.py              # Package exports
│   ├── agent.py                 # Agent core class
│   ├── memory.py                # Memory management
│   ├── tools.py                 # Tool definitions
│   ├── config.py                # Configuration
│   └── cli.py                   # CLI interface
├── examples/
│   ├── 01_research_agent.py     # Web search example
│   ├── 02_file_agent.py         # File analysis example
│   └── 03_workflow_agent.py     # Multi-step workflow example
├── tests/
│   ├── test_agent.py            # Agent tests
│   ├── test_tools.py            # Tool tests
│   └── test_memory.py           # Memory tests
├── README.md                     # This file
├── pyproject.toml               # Project configuration
├── requirements.txt             # Dependencies
└── .gitignore                   # Git ignore rules
```

## Example Agents

### 1. Research Agent
Searches the web and summarizes information.

```bash
python examples/01_research_agent.py
```

### 2. File Analysis Agent
Reads and analyzes files, answers questions about content.

```bash
python examples/02_file_agent.py
```

### 3. Workflow Agent
Performs multi-step tasks with tools.

```bash
python examples/03_workflow_agent.py
```

## How It Works

### Agent Loop

1. **User Input** → Agent receives a task
2. **Thinking** → Agent analyzes the input and decides which tool to use
3. **Tool Selection** → Agent chooses the best tool based on the task
4. **Execution** → Tool runs and returns results
5. **Memory** → Agent saves the interaction
6. **Response** → Agent returns the result to the user

### Built-in Tools

| Tool | Description | Example |
|------|-------------|----------|
| `web_search` | Search the web | "Find latest AI news" |
| `file_reader` | Read and analyze files | "Summarize config.json" |
| `file_writer` | Write content to files | "Save results to output.txt" |
| `command_runner` | Execute system commands | "Run a Python script" |

## API Reference

### Agent

```python
from agentforge import Agent

# Create an agent
agent = Agent(name="my-agent", model="gpt-4o-mini")

# Add tools
agent.add_tool(tool)

# Run the agent
result = agent.run("Your task here")

# Get memory history
history = agent.memory.get()
```

### Tool

```python
from agentforge import Tool

# Create a custom tool
tool = Tool(
    name="my_tool",
    description="What this tool does",
    func=lambda query: f"Result: {query}"
)
```

### Memory

```python
from agentforge import Memory

memory = Memory()
memory.add("User: Hello")
memory.add("Agent: Hi there!")
history = memory.get()
memory.clear()
```

## Roadmap

### v0.1 (Current)
- ✅ Agent core
- ✅ Tool calling system
- ✅ Memory management
- ✅ Basic tools (search, file ops)
- ✅ CLI interface
- ✅ Examples

### v0.2 (Next)
- [ ] OpenAI / Anthropic integration
- [ ] Workflow definition language
- [ ] Better memory (summarization, semantic search)
- [ ] More built-in tools
- [ ] Configuration file support

### v0.3
- [ ] Local LLM support (Ollama)
- [ ] Browser automation
- [ ] API endpoint tool
- [ ] Database integration
- [ ] Agent marketplace

### v1.0
- [ ] Web dashboard
- [ ] Multi-agent collaboration
- [ ] Vector memory / embeddings
- [ ] Production deployment guide
- [ ] Performance optimizations

## Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write tests for new functionality
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

```bash
# Clone the repo
git clone https://github.com/Tdat10052499/agentforge.git
cd agentforge

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run tests
python -m pytest

# Run examples
python examples/01_research_agent.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- 📖 [Documentation](./README.md)
- 💬 [GitHub Discussions](https://github.com/Tdat10052499/agentforge/discussions)
- 🐛 [Issue Tracker](https://github.com/Tdat10052499/agentforge/issues)
- 📧 Email: [Your email]

## Star History

If you find AgentForge useful, please give it a star ⭐ on GitHub!

## Acknowledgments

AgentForge is inspired by:
- AutoGPT and similar agent frameworks
- LangChain's tool calling concepts
- The open-source AI community

## What's Next?

- Add your first tool
- Create your first agent
- Share your agent examples with the community
- Contribute improvements

Happy agent building! 🚀
