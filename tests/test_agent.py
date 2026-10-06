"""Tests for the agent module."""

from agentforge import Agent, Tool


def test_agent_creation():
    agent = Agent(name="test-agent")
    assert agent.name == "test-agent"
    assert agent.model == "gpt-4o-mini"
    assert len(agent.tools) == 0
    assert agent.task_count == 0


def test_agent_add_tool():
    agent = Agent(name="test-agent")
    tool = Tool(name="test_tool", description="A test tool", func=lambda x: f"Result: {x}")
    agent.add_tool(tool)
    assert "test_tool" in agent.tools


def test_agent_run():
    agent = Agent(name="test-agent")
    tool = Tool(name="hello_tool", description="Greeting tool", func=lambda x: f"Hello, {x}!")
    agent.add_tool(tool)
    result = agent.run("world")
    assert "task" in result.lower() or "hello" in result.lower()
    assert agent.task_count == 1


def test_agent_remove_tool():
    agent = Agent(name="test-agent")
    tool = Tool(name="test_tool", description="A test tool", func=lambda x: x)
    agent.add_tool(tool)
    assert agent.remove_tool("test_tool") is True
    assert agent.remove_tool("missing") is False


def test_agent_tools_description():
    agent = Agent(name="test-agent")
    description = agent.get_tools_description()
    assert "No tools" in description

    tool = Tool(name="demo_tool", description="Demo tool", func=lambda x: x)
    agent.add_tool(tool)
    description = agent.get_tools_description()
    assert "demo_tool" in description
    assert "Demo tool" in description


def test_memory_summary():
    agent = Agent(name="test-agent")
    _ = agent.run("First task")
    summary = agent.get_memory_summary()
    assert "Tasks completed: 1" in summary
    assert "Memory entries" in summary


def test_agent_string_repr():
    agent = Agent(name="test-agent")
    assert "test-agent" in str(agent)
    assert "gpt-4o-mini" in str(agent)
