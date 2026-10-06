"""Tool definitions for agents."""

from typing import Callable, Any
from dataclasses import dataclass


@dataclass
class Tool:
    """A tool that an agent can use."""
    name: str
    description: str
    func: Callable[[str], str]

    def run(self, input_text: str) -> str:
        """Execute the tool.
        
        Args:
            input_text: Input to the tool.
            
        Returns:
            Tool output.
        """
        try:
            return self.func(input_text)
        except Exception as e:
            return f"Tool error: {str(e)}"

    def __repr__(self) -> str:
        return f"Tool(name='{self.name}')"


# Built-in tool implementations

def web_search_func(query: str) -> str:
    """Search the web for information.
    
    Args:
        query: Search query.
        
    Returns:
        Search results.
    """
    # Placeholder implementation
    # In production, integrate with Google Search API, DuckDuckGo, or similar
    return f"""
    Web Search Results for: '{query}'
    
    Note: This is a placeholder. To enable real web search:
    1. Install: pip install requests beautifulsoup4
    2. Add API keys for search service
    3. Implement actual search logic
    
    Example results that would appear:
    - Result 1: ...
    - Result 2: ...
    - Result 3: ...
    """


def file_reader_func(query: str) -> str:
    """Read and analyze files.
    
    Args:
        query: File path or analysis request.
        
    Returns:
        File contents or analysis.
    """
    try:
        # Try to parse as file path
        if query.startswith('read:'):
            file_path = query.replace('read:', '').strip()
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return f"File contents of {file_path}:\n\n{content}"
        else:
            return f"File reader: Query '{query}' does not match expected format. Use 'read:/path/to/file'"
    except FileNotFoundError:
        return f"Error: File not found. Please check the path and try again."
    except Exception as e:
        return f"Error reading file: {str(e)}"


def file_writer_func(query: str) -> str:
    """Write content to files.
    
    Args:
        query: Write command in format 'write:/path/to/file:content'.
        
    Returns:
        Confirmation message.
    """
    try:
        if query.startswith('write:'):
            parts = query.replace('write:', '').split(':', 1)
            if len(parts) == 2:
                file_path, content = parts
                file_path = file_path.strip()
                content = content.strip()
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return f"Successfully wrote {len(content)} characters to {file_path}"
        return "File writer: Query must be in format 'write:/path/to/file:content'"
    except Exception as e:
        return f"Error writing file: {str(e)}"


def command_runner_func(query: str) -> str:
    """Execute system commands.
    
    Args:
        query: Command to execute.
        
    Returns:
        Command output.
    """
    # Placeholder for security - actual implementation should have restrictions
    return f"""
    Command Runner: Received command '{query}'
    
    Note: Command execution is disabled in this version for security.
    To enable command execution:
    1. Review security implications
    2. Add command whitelist
    3. Implement proper sandboxing
    4. Add audit logging
    """


# Create built-in tool instances

WebSearchTool = Tool(
    name="web_search",
    description="Search the web for information",
    func=web_search_func
)

FileReaderTool = Tool(
    name="file_reader",
    description="Read and analyze files. Usage: 'read:/path/to/file'",
    func=file_reader_func
)

FileWriterTool = Tool(
    name="file_writer",
    description="Write content to files. Usage: 'write:/path/to/file:content'",
    func=file_writer_func
)

CommandRunnerTool = Tool(
    name="command_runner",
    description="Execute system commands (restricted)",
    func=command_runner_func
)

# Tool registry
DEFAULT_TOOLS = {
    "web_search": WebSearchTool,
    "file_reader": FileReaderTool,
    "file_writer": FileWriterTool,
    "command_runner": CommandRunnerTool,
}
