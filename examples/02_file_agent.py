#!/usr/bin/env python3
"""Research agent example."""

from agentforge import Agent, WebSearchTool


def main():
    agent = Agent(name="research-agent")
    agent.add_tool(WebSearchTool)

    tasks = [
        "Find the latest AI agent frameworks",
        "Search for open-source AI tools",
    ]

    for task in tasks:
        print(f"Task: {task}")
        print("-" * 60)
        print(agent.run(task))
        print()


if __name__ == "__main__":
    main()

