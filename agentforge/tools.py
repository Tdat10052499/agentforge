"""Tool definitions for agents."""

import os
import subprocess
from dataclasses import dataclass
from typing import Callable

import requests


@dataclass
class Tool:
    """A tool that an agent can use."""
    name: str
    description: str
    func: Callable[[str], str]

    def run(self, input_text: str) -> str:
        try:
            return self.func(input_text)
        except Exception as exc:  # pragma: no cover - defensive branch
            return f"Tool error: {type(exc).__name__}: {exc}"


# Built-in tool implementations

def web_search_func(query: str) -> str:
    """Search the web using DuckDuckGo's public API."""
    if not query or not query.strip():
        return "Web search requires a valid query."

    normalized = query.strip()
    
    try:
        response = requests.get(
            "https://api.duckduckgo.com/",
            params={
                "q": normalized,
                "format": "json",
                "no_html": 1,
                "skip_disambig": 1,
            },
            timeout=10,
        )
        response.raise_for_status()
        payload = response.json()

        # Thử lấy Abstract trước
        abstract = payload.get("AbstractText", "").strip()
        if abstract:
            result_lines = [f"Search results for: '{normalized}'", "", abstract]
            abstract_url = payload.get("AbstractURL")
            if abstract_url:
                result_lines.append(f"Source: {abstract_url}")
            return "\n".join(result_lines)

        # Nếu không có Abstract, dùng RelatedTopics
        related_topics = payload.get("RelatedTopics", [])
        if related_topics:
            result_lines = [f"Search results for: '{normalized}'", ""]
            count = 0
            for topic in related_topics:
                # Skip categories
                if "Topics" in topic:
                    continue
                
                text = topic.get("Text", "").strip()
                first_url = topic.get("FirstURL", "")
                
                if text:
                    result_lines.append(f"• {text}")
                    if first_url:
                        result_lines.append(f"  Link: {first_url}")
                    count += 1
                    
                if count >= 5:  # Giới hạn 5 kết quả
                    break
            
            if count > 0:
                return "\n".join(result_lines)

        return f"No results found for '{normalized}'. Try a different search term."
        
    except Exception as exc:
        return (
            f"Web search failed: {type(exc).__name__}: {exc}\n"
            "This might be a network issue. Try again later."
        )


def file_reader_func(query: str) -> str:
    """Read a file from the local filesystem."""
    if not query.startswith("read:"):
        return "Usage: read:/path/to/file.txt"

    file_path = query.replace("read:", "", 1).strip()
    if not file_path:
        return "No file path was provided."

    try:
        with open(file_path, "r", encoding="utf-8") as file_handle:
            content = file_handle.read()
        return f"File contents of {file_path}:\n\n{content}"
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as exc:  # pragma: no cover - defensive branch
        return f"Failed to read file: {file_path} ({type(exc).__name__}: {exc})"


def file_writer_func(query: str) -> str:
    """Write content to a file."""
    if not query.startswith("write:"):
        return "Usage: write:/path/to/file.txt:content"

    payload = query.replace("write:", "", 1)
    if ":" not in payload:
        return "Usage: write:/path/to/file.txt:content"

    file_path, content = payload.split(":", 1)
    file_path = file_path.strip()
    content = content.strip()

    if not file_path:
        return "No file path was provided."

    try:
        with open(file_path, "w", encoding="utf-8") as file_handle:
            file_handle.write(content)
        return f"Successfully wrote {len(content)} characters to {file_path}"
    except Exception as exc:  # pragma: no cover - defensive branch
        return f"Failed to write file: {file_path} ({type(exc).__name__}: {exc})"


def command_runner_func(query: str) -> str:
    """Run a secure, restricted system command."""
    if os.getenv("AGENTFORGE_ENABLE_COMMANDS", "0") != "1":
        return (
            "Command execution is disabled in this version. "
            "Set AGENTFORGE_ENABLE_COMMANDS=1 to allow it in a controlled environment."
        )

    allowed = ["echo", "python", "python3", "ls", "pwd"]
    command = query.strip()
    if not command:
        return "No command was provided."

    executable = command.split()[0]
    if executable not in allowed:
        return f"Command '{executable}' is not allowed by the whitelist."

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            capture_output=True,
            text=True,
        )
        output = result.stdout.strip() or result.stderr.strip() or "Command returned no output."
        return f"Command output:\n{output}"
    except Exception as exc:  # pragma: no cover - defensive branch
        return f"Command execution failed: {type(exc).__name__}: {exc}"


WebSearchTool = Tool(
    name="web_search",
    description="Search the web for information",
    func=web_search_func,
)

FileReaderTool = Tool(
    name="file_reader",
    description="Read and analyze a file. Example: read:/path/to/file.txt",
    func=file_reader_func,
)

FileWriterTool = Tool(
    name="file_writer",
    description="Write content to a file. Example: write:/path/to/file.txt:content",
    func=file_writer_func,
)

CommandRunnerTool = Tool(
    name="command_runner",
    description="Run a restricted system command",
    func=command_runner_func,
)

DEFAULT_TOOLS = {
    "web_search": WebSearchTool,
    "file_reader": FileReaderTool,
    "file_writer": FileWriterTool,
    "command_runner": CommandRunnerTool,
}

__all__ = [
    "Tool",
    "WebSearchTool",
    "FileReaderTool",
    "FileWriterTool",
    "CommandRunnerTool",
    "DEFAULT_TOOLS",
]
