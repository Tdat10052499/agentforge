"""Tests for the tools module."""

from agentforge.tools import Tool, WebSearchTool, FileReaderTool, FileWriterTool


def test_tool_creation():
    tool = Tool(name="echo", description="Echo tool", func=lambda x: f"Echo: {x}")
    assert tool.name == "echo"
    assert tool.description == "Echo tool"


def test_tool_run():
    tool = Tool(name="echo", description="Echo tool", func=lambda x: f"Echo: {x}")
    assert tool.run("hello") == "Echo: hello"


def test_web_search_tool():
    response = WebSearchTool.run("AI agents")
    assert isinstance(response, str)
    assert len(response) > 0


def test_file_reader_tool_usage_message():
    response = FileReaderTool.run("hello")
    assert "Usage" in response


def test_file_writer_tool_usage_message():
    response = FileWriterTool.run("hello")
    assert "Usage" in response


def test_tool_error_handling():
    def bad_func(_):
        raise ValueError("explode")

    tool = Tool(name="bad", description="bad", func=bad_func)
    result = tool.run("x")
    assert "Tool error" in result
    assert "ValueError" in result
