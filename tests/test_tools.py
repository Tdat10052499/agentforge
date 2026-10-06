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


def test_web_search_tool_uses_instant_answer_and_cleans_query_prefix(monkeypatch):
    response = Mock()
    response.json.return_value = {
        "AbstractText": "Python is a general-purpose programming language.",
        "AbstractURL": "https://example.com/python",
    }
    request = Mock(return_value=response)
    monkeypatch.setattr("agentforge.tools.requests.get", request)

    result = WebSearchTool.run("search for Python programming")

    assert "Python is a general-purpose programming language." in result
    assert "https://example.com/python" in result
    request.assert_called_once_with(
        "https://api.duckduckgo.com/",
        params={
            "q": "Python programming",
            "format": "json",
            "no_html": 1,
            "skip_disambig": 1,
        },
        timeout=10,
    )


def test_web_search_tool_returns_search_results(monkeypatch):
    api_response = Mock()
    api_response.json.return_value = {}
    html_response = Mock()
    html_response.text = (
        '<a class="result__a" href="https://example.com/python">Python &amp; programming</a>'
    )
    request = Mock(side_effect=[api_response, html_response])
    monkeypatch.setattr("agentforge.tools.requests.get", request)

    response = WebSearchTool.run("AI agents")

    assert "Python & programming" in response
    assert "https://example.com/python" in response
    assert request.call_args_list[1].args == (
        "https://html.duckduckgo.com/html/",
    )
    assert request.call_args_list[1].kwargs == {
        "params": {"q": "AI agents"},
        "headers": {"User-Agent": "Mozilla/5.0"},
        "timeout": 10,
    }


def test_web_search_tool_reports_no_results(monkeypatch):
    api_response = Mock()
    api_response.json.return_value = {}
    html_response = Mock()
    html_response.text = "<html><body>No results</body></html>"
    monkeypatch.setattr(
        "agentforge.tools.requests.get",
        Mock(side_effect=[api_response, html_response]),
    )

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
