"""Tests for the tools module."""

import pytest
from agentforge.tools import Tool, WebSearchTool, FileReaderTool, FileWriterTool


def test_tool_creation():
    """Test tool creation."""
    tool = Tool(
        name="test_tool",
        description="A test tool",
        func=lambda x: f"Result: {x}"
    )
    
    assert tool.name == "test_tool"
    assert tool.description == "A test tool"
    assert callable(tool.func)


def test_tool_run():
    """Test running a tool."""
    tool = Tool(
        name="echo_tool",
        description="Echo tool",
        func=lambda x: f"Echo: {x}"
    )
    
    result = tool.run("hello")
    assert "Echo" in result
    assert "hello" in result


def test_tool_run_with_error():
    """Test tool error handling."""
    def failing_func(x):
        raise ValueError("Tool error")
    
    tool = Tool(
        name="failing_tool",
        description="A tool that fails",
        func=failing_func
    )
    
    result = tool.run("test")
    assert "Tool error" in result
    assert "ValueError" in result


def test_builtin_web_search_tool():
    """Test built-in web search tool."""
    result = WebSearchTool.run("test query")
    assert "test query" in result
    assert isinstance(result, str)


def test_builtin_file_reader_tool():
    """Test built-in file reader tool."""
    result = FileReaderTool.run("read:/path/to/file.txt")
    assert isinstance(result, str)


def test_builtin_file_writer_tool():
    """Test built-in file writer tool."""
    result = FileWriterTool.run("write:/path/to/file.txt:content")
    assert isinstance(result, str)


def test_tool_repr():
    """Test tool string representation."""
    tool = Tool(
        name="test_tool",
        description="A test tool",
        func=lambda x: x
    )
    
    assert "test_tool" in repr(tool)
