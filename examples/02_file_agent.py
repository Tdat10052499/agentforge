#!/usr/bin/env python3
"""File analysis agent example."""

from agentforge import Agent, FileReaderTool, FileWriterTool


def main():
    agent = Agent(name="file-analyzer")
    agent.add_tool(FileReaderTool)
    agent.add_tool(FileWriterTool)

    print("Creating demo file...")
    agent.run("write:demo.txt:AgentForge is a tool for building AI agents.")
    print("Reading the created file...")
    print(agent.run("read:demo.txt"))


if __name__ == "__main__":
    main()
