"""Tests for the tools module."""

from unittest.mock import Mock

from agentforge.tools import FileReaderTool, FileWriterTool, Tool, WebSearchTool


def test_tool_creation():
    tool = Tool(name="echo", description="Echo tool", func=lambda x: f"Echo: {x}")
    assert tool.name == "echo"
    assert tool.description == "Echo tool"


def test_tool_run():
    tool = Tool(name="echo", description="Echo tool", func=lambda x: f"Echo: {x}")
    assert tool.run("hello") == "Echo: hello"


def test_web_search_tool_returns_search_results(monkeypatch):
    response = Mock()
    response.text = (
        '<a class="result__a" href="https://example.com/python">Python &amp; programming</a>'
    )
    request = Mock(return_value=response)
    monkeypatch.setattr("agentforge.tools.requests.get", request)

    response = WebSearchTool.run("AI agents")

    assert "Python & programming" in response
    assert "https://example.com/python" in response
    request.assert_called_once_with(
        "https://html.duckduckgo.com/html/",
        params={"q": "AI agents"},
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10,
    )


def test_web_search_tool_reports_no_results(monkeypatch):
    response = Mock()
    response.text = "<html><body>No results</body></html>"
    monkeypatch.setattr("agentforge.tools.requests.get", Mock(return_value=response))

    result = WebSearchTool.run("unknown query")

    assert "No results found" in result


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
