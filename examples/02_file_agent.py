#!/usr/bin/env python3
"""Example 2: File Analysis Agent

This example shows how to create an agent that can read and write files.

Usage:
    python examples/02_file_agent.py
"""

from agentforge import Agent, FileReaderTool, FileWriterTool
import os


def main():
    """Run the file analysis agent example."""
    
    print("=" * 60)
    print("AgentForge - File Analysis Agent Example")
    print("=" * 60)
    print()
    
    # Create a file analysis agent
    agent = Agent(name="file-analyzer")
    
    # Add file tools
    agent.add_tool(FileReaderTool)
    agent.add_tool(FileWriterTool)
    
    print(f"Agent created: {agent}")
    print(agent.get_tools_description())
    print()
    
    # Create a sample file for demonstration
    sample_file = "sample_data.txt"
    sample_content = """AgentForge Demo Data
=====================

AgentForge is an open-source toolkit for building AI agents.

Features:
- Tool calling
- Memory management
- Web search
- File operations
- Workflow automation

Version: 0.1.0
License: MIT
"""
    
    # Write sample file
    print(f"Creating sample file: {sample_file}")
    with open(sample_file, 'w') as f:
        f.write(sample_content)
    print(f"✓ File created")
    print()
    
    # Define tasks
    tasks = [
        f"read:{sample_file}",  # Read the file
    ]
    
    # Run tasks
    for i, task in enumerate(tasks, 1):
        print(f"Task {i}: Reading file")
        print("-" * 60)
        
        result = agent.run(task)
        print(result)
        print()
    
    # Save analysis
    print("Saving analysis results...")
    output_file = "analysis_output.txt"
    agent.run(f"write:{output_file}:Analysis complete. AgentForge is working correctly.")
    print()
    
    # Show memory summary
    print("=" * 60)
    print(agent.get_memory_summary())
    print("=" * 60)
    
    # Cleanup
    if os.path.exists(sample_file):
        os.remove(sample_file)
        print(f"\nCleaned up: {sample_file}")


if __name__ == "__main__":
    main()
