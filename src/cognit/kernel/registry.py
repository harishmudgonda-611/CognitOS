"""
CognitOS Service Registry

Central registry for all kernel components.
"""

from __future__ import annotations

from typing import Any


class ServiceRegistry:
    """Central registry for CognitOS components."""

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        """Register a component."""
        if name in self._services:
            raise ValueError(f"Service '{name}' is already registered.")
        self._services[name] = service

    def unregister(self, name: str) -> None:
        """Remove a component."""
        self._services.pop(name, None)

    def get(self, name: str) -> Any:
        """Get a component by name."""
        return self._services.get(name)

    def exists(self, name: str) -> bool:
        """Check whether a component exists."""
        return name in self._services

    def list(self) -> list[str]:
        """Return all registered component names."""
        return sorted(self._services.keys())

    def clear(self) -> None:
        """Remove all registered components."""
        self._services.clear()

    def count(self) -> int:
        """Return the number of registered components."""
        return len(self._services)
        
