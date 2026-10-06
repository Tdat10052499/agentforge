#!/usr/bin/env python3
"""Example 3: Workflow Agent

This example shows how to create an agent that can execute
multi-step workflows using different tools.

Usage:
    python examples/03_workflow_agent.py
"""

from agentforge import Agent
from agentforge.tools import DEFAULT_TOOLS


def main():
    """Run the workflow agent example."""
    
    print("=" * 60)
    print("AgentForge - Workflow Agent Example")
    print("=" * 60)
    print()
    
    # Create a workflow agent
    agent = Agent(name="workflow-agent")
    
    # Add all available tools
    for tool_name, tool in DEFAULT_TOOLS.items():
        agent.add_tool(tool)
    
    print(f"Agent created: {agent}")
    print(agent.get_tools_description())
    print()
    
    # Define workflow tasks
    workflow_tasks = [
        "Search for information about AI agents and save it",
        "Read a configuration file and analyze it",
        "Generate a report and save it to results.txt",
    ]
    
    # Run workflow tasks
    for i, task in enumerate(workflow_tasks, 1):
        print(f"Workflow Step {i}: {task}")
        print("-" * 60)
        
        result = agent.run(task)
        print(result)
        print()
    
    # Show memory context
    print("=" * 60)
    print("Workflow Execution Summary")
    print("=" * 60)
    print(agent.get_memory_summary())
    print()
    print("Memory Context:")
    print("-" * 60)
    print(agent.memory.get_context())
    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
