"""Tests for the agent module."""

import pytest
from agentforge import Agent, Tool, Memory


def test_agent_creation():
    """Test agent creation."""
    agent = Agent(name="test-agent")
    assert agent.name == "test-agent"
    assert agent.model == "gpt-4o-mini"
    assert len(agent.tools) == 0
    assert agent.task_count == 0


def test_agent_add_tool():
    """Test adding a tool to agent."""
    agent = Agent(name="test-agent")
    
    tool = Tool(
        name="test_tool",
        description="A test tool",
        func=lambda x: f"Result: {x}"
    )
    
    agent.add_tool(tool)
    assert "test_tool" in agent.tools
    assert agent.tools["test_tool"] == tool


def test_agent_remove_tool():
    """Test removing a tool from agent."""
    agent = Agent(name="test-agent")
    
    tool = Tool(
        name="test_tool",
        description="A test tool",
        func=lambda x: f"Result: {x}"
    )
    
    agent.add_tool(tool)
    assert agent.remove_tool("test_tool")
    assert "test_tool" not in agent.tools
    assert not agent.remove_tool("nonexistent")


def test_agent_run():
    """Test running agent with a tool."""
    agent = Agent(name="test-agent")
    
    # Add a simple tool
    tool = Tool(
        name="hello_tool",
        description="A greeting tool",
        func=lambda x: f"Hello, {x}!"
    )
    agent.add_tool(tool)
    
    # Run the agent
    result = agent.run("world")
    
    # Check memory
    assert len(agent.memory) == 2  # user input + agent response
    assert agent.task_count == 1


def test_agent_memory():
    """Test agent memory functionality."""
    agent = Agent(name="test-agent")
    
    result1 = agent.run("First task")
    result2 = agent.run("Second task")
    
    assert agent.task_count == 2
    assert len(agent.memory) == 4  # 2 user inputs + 2 agent responses


def test_agent_tools_description():
    """Test getting tool descriptions."""
    agent = Agent(name="test-agent")
    
    # No tools
    description = agent.get_tools_description()
    assert "No tools" in description
    
    # Add a tool
    tool = Tool(
        name="test_tool",
        description="A test tool",
        func=lambda x: x
    )
    agent.add_tool(tool)
    
    description = agent.get_tools_description()
    assert "test_tool" in description
    assert "A test tool" in description


def test_agent_string_representation():
    """Test agent string representation."""
    agent = Agent(name="test-agent", model="test-model")
    
    str_repr = str(agent)
    assert "test-agent" in str_repr
    assert "test-model" in str_repr
