#!/usr/bin/env python3
"""Example 1: Research Agent

This example shows how to create a simple research agent that can
search the web for information.

Usage:
    python examples/01_research_agent.py
"""

from agentforge import Agent, WebSearchTool


def main():
    """Run the research agent example."""
    
    print("=" * 60)
    print("AgentForge - Research Agent Example")
    print("=" * 60)
    print()
    
    # Create a research agent
    agent = Agent(name="research-agent")
    
    # Add web search tool
    agent.add_tool(WebSearchTool)
    
    print(f"Agent created: {agent}")
    print(agent.get_tools_description())
    print()
    
    # Define research tasks
    tasks = [
        "Search for information about AI agents",
        "Find the latest developments in machine learning",
        "Look up Python web frameworks",
    ]
    
    # Run tasks
    for i, task in enumerate(tasks, 1):
        print(f"Task {i}: {task}")
        print("-" * 60)
        
        result = agent.run(task)
        print(result)
        print()
    
    # Show memory summary
    print("=" * 60)
    print(agent.get_memory_summary())
    print("=" * 60)


if __name__ == "__main__":
    main()
