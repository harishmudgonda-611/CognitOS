"""
CognitOS Kernel Interfaces

Defines the abstract interfaces that every Engine, Agent,
Skill, Tool, and Plugin must implement.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class KernelComponent(ABC):
    """Base class for every CognitOS component."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique component name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def version(self) -> str:
        """Component version."""
        raise NotImplementedError

    @abstractmethod
    def initialize(self) -> None:
        """Initialize component resources."""
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """Release component resources."""
        raise NotImplementedError


class Engine(KernelComponent):
    """Base interface for all intelligence engines."""

    @abstractmethod
    def execute(self, context: Any) -> Any:
        """Execute engine logic."""
        raise NotImplementedError


class Agent(KernelComponent):
    """Base interface for autonomous agents."""

    @abstractmethod
    def execute(self, task: Any) -> Any:
        """Execute a task."""
        raise NotImplementedError


class Skill(KernelComponent):
    """Base interface for reusable skills."""

    @abstractmethod
    def execute(self, data: Any) -> Any:
        """Run the skill."""
        raise NotImplementedError


class Tool(KernelComponent):
    """Base interface for external tools."""

    @abstractmethod
    def execute(self, command: Any) -> Any:
        """Execute the tool."""
        raise NotImplementedError


class Plugin(KernelComponent):
    """Base interface for CognitOS plugins."""

    @abstractmethod
    def register(self, registry: Any) -> None:
        """Register with the kernel registry."""
        raise NotImplementedError
    
