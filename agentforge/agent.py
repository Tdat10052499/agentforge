"""Core agent implementation."""

from typing import Dict, List, Optional
from .memory import Memory
from .tools import Tool


class Agent:
    """An AI agent that can use tools and maintain memory."""

    def __init__(self, name: str, model: str = "gpt-4o-mini"):
        """Initialize an agent.
        
        Args:
            name: Agent name.
            model: LLM model to use (for future integration).
        """
        self.name = name
        self.model = model
        self.tools: Dict[str, Tool] = {}
        self.memory = Memory()
        self.task_count = 0

    def add_tool(self, tool: Tool) -> None:
        """Add a tool to the agent.
        
        Args:
            tool: Tool to add.
        """
        self.tools[tool.name] = tool

    def remove_tool(self, tool_name: str) -> bool:
        """Remove a tool from the agent.
        
        Args:
            tool_name: Name of tool to remove.
            
        Returns:
            True if tool was removed, False if not found.
        """
        if tool_name in self.tools:
            del self.tools[tool_name]
            return True
        return False

    def get_tools_description(self) -> str:
        """Get descriptions of available tools.
        
        Returns:
            Formatted tool descriptions.
        """
        if not self.tools:
            return "No tools available."
        
        descriptions = ["Available tools:"]
        for tool_name, tool in self.tools.items():
            descriptions.append(f"  - {tool_name}: {tool.description}")
        
        return "\n".join(descriptions)

    def run(self, user_input: str) -> str:
        """Run the agent on a task.
        
        Args:
            user_input: Task or query for the agent.
            
        Returns:
            Agent response.
        """
        self.task_count += 1
        
        # Add to memory
        self.memory.add(user_input, role="user")
        
        # Thinking and tool selection
        response = self._think_and_execute(user_input)
        
        # Add response to memory
        self.memory.add(response, role="assistant")
        
        return response

    def _think_and_execute(self, user_input: str) -> str:
        """Think about the task and execute appropriate tools.
        
        Args:
            user_input: Task input.
            
        Returns:
            Response from the agent.
        """
        lowered = user_input.lower()
        
        # Simple rule-based tool selection
        # In production, this would be more sophisticated
        
        # Check for web search
        if any(keyword in lowered for keyword in ["search", "find", "lookup", "latest", "news"]):
            if "web_search" in self.tools:
                result = self.tools["web_search"].run(user_input)
                return self._format_response("web_search", result)
        
        # Check for file reading
        if any(keyword in lowered for keyword in ["read", "open", "file", "load"]):
            if "file_reader" in self.tools:
                # Extract file path if provided
                if "read:" in user_input:
                    result = self.tools["file_reader"].run(user_input)
                else:
                    result = self.tools["file_reader"].run(f"read:{user_input}")
                return self._format_response("file_reader", result)
        
        # Check for file writing
        if any(keyword in lowered for keyword in ["write", "save", "store", "create file"]):
            if "file_writer" in self.tools:
                if "write:" in user_input:
                    result = self.tools["file_writer"].run(user_input)
                else:
                    result = self.tools["file_writer"].run(f"write:{user_input}")
                return self._format_response("file_writer", result)
        
        # Check for command execution
        if any(keyword in lowered for keyword in ["run", "execute", "command"]):
            if "command_runner" in self.tools:
                result = self.tools["command_runner"].run(user_input)
                return self._format_response("command_runner", result)
        
        # No tool matched - return default response
        return self._default_response(user_input)

    def _format_response(self, tool_name: str, tool_output: str) -> str:
        """Format tool output as agent response.
        
        Args:
            tool_name: Name of the tool used.
            tool_output: Output from the tool.
            
        Returns:
            Formatted response.
        """
        return f"[Using {tool_name}]\n\n{tool_output}"

    def _default_response(self, user_input: str) -> str:
        """Generate default response when no tool matches.
        
        Args:
            user_input: The original user input.
            
        Returns:
            Default response.
        """
        return f"""
Agent '{self.name}' received task: "{user_input}"

I don't have a tool that directly handles this request. 

{self.get_tools_description()}

Try using keywords like:
  - "search" or "find" to use web search
  - "read" to read files
  - "write" or "save" to write files
"""

    def get_memory_summary(self) -> str:
        """Get a summary of agent memory.
        
        Returns:
            Memory summary.
        """
        return f"""
Agent Memory Summary
==================
Agent: {self.name}
Model: {self.model}
Tasks completed: {self.task_count}
Memory entries: {len(self.memory)}
Tools available: {len(self.tools)}
"""

    def __str__(self) -> str:
        """String representation of agent."""
        return f"Agent(name='{self.name}', model='{self.model}', tools={len(self.tools)})"

    def __repr__(self) -> str:
        """Detailed string representation."""
        return self.__str__()
