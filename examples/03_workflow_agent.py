#!/usr/bin/env python3
"""Workflow example."""

from agentforge import Agent
from agentforge.tools import DEFAULT_TOOLS


def main():
    agent = Agent(name="workflow-agent")
    for tool in DEFAULT_TOOLS.values():
        agent.add_tool(tool)

    tasks = [
        "Search for AI agent frameworks",
        "Read demo.txt if it exists",
    ]

    for task in tasks:
        print(f"Task: {task}")
        print("-" * 60)
        print(agent.run(task))
        print()


if __name__ == "__main__":
    main()
