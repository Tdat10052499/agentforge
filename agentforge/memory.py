"""Memory management for agents."""

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class MemoryEntry:
    role: str
    content: str
    timestamp: datetime


class Memory:
    """Manages agent conversation history and memory."""

    def __init__(self, max_entries: int = 100):
        self.history: List[MemoryEntry] = []
        self.max_entries = max_entries

    def add(self, message: str, role: str = "assistant"):
        entry = MemoryEntry(role=role, content=message, timestamp=datetime.now())
        self.history.append(entry)
        if len(self.history) > self.max_entries:
            self.history = self.history[-self.max_entries:]

    def get(self):
        return self.history.copy()

    def get_context(self) -> str:
        if not self.history:
            return "No previous context."
        lines = []
        for entry in self.history[-10:]:
            lines.append(f"{entry.role.capitalize()}: {entry.content}")
        return "\n".join(lines)

    def clear(self):
        self.history.clear()

    def __len__(self):
        return len(self.history)

    def __str__(self) -> str:
        return f"Memory({len(self.history)} entries)"


__all__ = ["Memory", "MemoryEntry"]
