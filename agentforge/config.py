"""Configuration management for agents."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class AgentConfig:
    """Configuration for an agent."""
    name: str
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_tokens: int = 2000
    tools: List[str] = field(default_factory=list)
    system_prompt: Optional[str] = None
    memory_size: int = 100

    def to_dict(self) -> Dict:
        """Convert config to dictionary.
        
        Returns:
            Dictionary representation.
        """
        return {
            "name": self.name,
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "tools": self.tools,
            "system_prompt": self.system_prompt,
            "memory_size": self.memory_size,
        }

    @classmethod
    def from_dict(cls, config_dict: Dict) -> "AgentConfig":
        """Create config from dictionary.
        
        Args:
            config_dict: Dictionary with config values.
            
        Returns:
            AgentConfig instance.
        """
        return cls(**config_dict)
