"""Tests for the memory module."""

from agentforge.memory import Memory


def test_memory_creation():
    memory = Memory()
    assert len(memory) == 0


def test_memory_add_and_get():
    memory = Memory()
    memory.add("Hello", role="user")
    memory.add("Hi there", role="assistant")
    entries = memory.get()
    assert len(entries) == 2
    assert entries[0].content == "Hello"
    assert entries[1].content == "Hi there"


def test_memory_context():
    memory = Memory()
    memory.add("Hello", role="user")
    memory.add("Hi there", role="assistant")
    context = memory.get_context()
    assert "User" in context
    assert "Assistant" in context


def test_memory_clear():
    memory = Memory()
    memory.add("Hello")
    memory.clear()
    assert len(memory) == 0


def test_memory_max_limit():
    memory = Memory(max_entries=2)
    memory.add("one")
    memory.add("two")
    memory.add("three")
    assert len(memory) == 2
    assert memory.get()[-1].content == "three"


def test_memory_str():
    memory = Memory()
    memory.add("hello")
    assert "Memory" in str(memory)


__all__ = ["Memory"]

