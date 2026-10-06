"""Command-line interface for AgentForge."""

import argparse
import sys
from typing import Optional

from .agent import Agent
from .tools import DEFAULT_TOOLS


def create_research_agent() -> Agent:
    """Create a research agent.
    
    Returns:
        Configured research agent.
    """
    agent = Agent(name="research-agent")
    agent.add_tool(DEFAULT_TOOLS["web_search"])
    return agent


def create_file_agent() -> Agent:
    """Create a file analysis agent.
    
    Returns:
        Configured file agent.
    """
    agent = Agent(name="file-analyzer")
    agent.add_tool(DEFAULT_TOOLS["file_reader"])
    agent.add_tool(DEFAULT_TOOLS["file_writer"])
    return agent


def create_workflow_agent() -> Agent:
    """Create a workflow execution agent.
    
    Returns:
        Configured workflow agent.
    """
    agent = Agent(name="workflow-agent")
    for tool in DEFAULT_TOOLS.values():
        agent.add_tool(tool)
    return agent


def main(args: Optional[list] = None) -> int:
    """Main CLI entry point.
    
    Args:
        args: Command-line arguments.
        
    Returns:
        Exit code.
    """
    parser = argparse.ArgumentParser(
        description="AgentForge - AI Agent Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m agentforge.cli --agent research --task "What are AI agents?"
  python -m agentforge.cli --agent file-analyzer --task "read:/path/to/file.txt"
  python -m agentforge.cli --agent workflow --task "Search for Python and summarize"
        """
    )
    
    parser.add_argument(
        "--agent",
        type=str,
        choices=["research", "file-analyzer", "workflow"],
        default="research",
        help="Type of agent to run"
    )
    
    parser.add_argument(
        "--task",
        type=str,
        required=True,
        help="Task for the agent to perform"
    )
    
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    parsed_args = parser.parse_args(args)
    
    # Create appropriate agent
    if parsed_args.agent == "research":
        agent = create_research_agent()
    elif parsed_args.agent == "file-analyzer":
        agent = create_file_agent()
    else:  # workflow
        agent = create_workflow_agent()
    
    if parsed_args.verbose:
        print(f"Agent: {agent}")
        print(agent.get_tools_description())
        print()
    
    # Run the agent
    print(f"Task: {parsed_args.task}")
    print()
    
    result = agent.run(parsed_args.task)
    print(result)
    
    if parsed_args.verbose:
        print()
        print(agent.get_memory_summary())
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
