"""
CognitOS Agent Manager

Creates and manages AI agents.
"""

from __future__ import annotations

from typing import Any


class AgentManager:
    """Manages AI agents."""

    def __init__(self) -> None:
        self._agents: dict[str, Any] = {}

    def register(self, name: str, agent: Any) -> None:
        if name in self._agents:
            raise ValueError(f"Agent '{name}' already exists.")

        self._agents[name] = agent

    def unregister(self, name: str) -> None:
        self._agents.pop(name, None)

    def get(self, name: str) -> Any:
        return self._agents.get(name)

    def exists(self, name: str) -> bool:
        return name in self._agents

    def list(self) -> list[str]:
        return sorted(self._agents.keys())

    def count(self) -> int:
        return len(self._agents)

    def execute(self, name: str, task: Any) -> Any:
        agent = self.get(name)

        if agent is None:
            raise ValueError(f"Agent '{name}' not found.")

        if not hasattr(agent, "execute"):
            raise TypeError(f"Agent '{name}' has no execute() method.")

        return agent.execute(task)


class DummyAgent:

    def execute(self, task: Any) -> dict:
        return {
            "status": "success",
            "task": task,
        }


if __name__ == "__main__":

    manager = AgentManager()

    manager.register("dummy", DummyAgent())

    print(manager.execute("dummy", "Build AI Website"))

    print("Agents:", manager.list())
    
