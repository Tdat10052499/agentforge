"""Memory management for agents."""

from typing import List
from dataclasses import dataclass
from datetime import datetime


@dataclass
class MemoryEntry:
    """A single memory entry."""
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime


class Memory:
    """Manages agent conversation history and memory."""

    def __init__(self, max_entries: int = 100):
        """Initialize memory.
        
        Args:
            max_entries: Maximum number of entries to keep in memory.
        """
        self.history: List[MemoryEntry] = []
        self.max_entries = max_entries

    def add(self, message: str, role: str = "assistant"):
        """Add a message to memory.
        
        Args:
            message: The message content.
            role: "user" or "assistant".
        """
        entry = MemoryEntry(
            role=role,
            content=message,
            timestamp=datetime.now()
        )
        self.history.append(entry)
        
        # Keep memory size manageable
        if len(self.history) > self.max_entries:
            self.history = self.history[-self.max_entries:]

    def get(self) -> List[MemoryEntry]:
        """Get all memory entries.
        
        Returns:
            List of memory entries.
        """
        return self.history.copy()

    def get_context(self) -> str:
        """Get formatted context for the agent.
        
        Returns:
            Formatted context string.
        """
        if not self.history:
            return "No previous context."
        
        context_lines = []
        for entry in self.history[-10:]:  # Last 10 entries
            context_lines.append(f"{entry.role.capitalize()}: {entry.content}")
        
        return "\n".join(context_lines)

    def clear(self):
        """Clear all memory."""
        self.history.clear()

    def __len__(self) -> int:
        """Get number of entries in memory."""
        return len(self.history)

    def __str__(self) -> str:
        """Get string representation of memory."""
        return f"Memory({len(self.history)} entries)"
