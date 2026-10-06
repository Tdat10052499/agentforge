"""AgentForge - Open-source toolkit for building AI agents with tools, memory, and workflows."""

from .agent import Agent
from .config import AgentConfig
from .memory import Memory
from .tools import (
    CommandRunnerTool,
    FileReaderTool,
    FileWriterTool,
    Tool,
    WebSearchTool,
)

__version__ = "0.2.0"
__author__ = "AgentForge Contributors"
__license__ = "MIT"

__all__ = [
    "Agent",
    "AgentConfig",
    "Memory",
    "Tool",
    "WebSearchTool",
    "FileReaderTool",
    "FileWriterTool",
    "CommandRunnerTool",
]
