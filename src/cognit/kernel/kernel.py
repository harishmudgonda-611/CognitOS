"""
CognitOS Kernel

Bootstraps and manages the core services of CognitOS.
"""

from __future__ import annotations

from cognit.kernel.config import ConfigManager
from cognit.kernel.container import Container
from cognit.kernel.events import EventBus
from cognit.kernel.logger import CognitLogger
from cognit.kernel.plugin_loader import PluginLoader
from cognit.kernel.registry import ServiceRegistry
from cognit.kernel.runtime import Runtime

from cognit.intelligence.reasoning_engine import ReasoningEngine
from cognit.intelligence.blueprint_builder import BlueprintBuilder


class CognitKernel:
    """Main kernel responsible for managing CognitOS."""

    def __init__(self) -> None:
        self.config = ConfigManager()
        self.logger = CognitLogger()
        self.events = EventBus()
        self.registry = ServiceRegistry()
        self.container = Container()
        self.plugins = PluginLoader()
        self.runtime = Runtime()

    def initialize(self) -> None:
        """Initialize kernel services."""

        # Core Services
        self.container.register("config", self.config)
        self.container.register("logger", self.logger)
        self.container.register("events", self.events)
        self.container.register("registry", self.registry)
        self.container.register("plugins", self.plugins)
        self.container.register("runtime", self.runtime)

        self.registry.register("config", self.config)
        self.registry.register("logger", self.logger)
        self.registry.register("events", self.events)
        self.registry.register("plugins", self.plugins)
        self.registry.register("runtime", self.runtime)

        # Intelligence Components
        reasoning_engine = ReasoningEngine()
        blueprint_builder = BlueprintBuilder()

        self.container.register("reasoning_engine", reasoning_engine)
        self.container.register("blueprint_builder", blueprint_builder)

        self.registry.register("reasoning_engine", reasoning_engine)
        self.registry.register("blueprint_builder", blueprint_builder)

        self.logger.logger.info("Kernel initialized.")

    def start(self) -> None:
        """Start CognitOS."""
        self.runtime.start()
        self.logger.logger.info("Kernel started.")

    def stop(self) -> None:
        """Stop CognitOS."""
        self.runtime.stop()
        self.logger.logger.info("Kernel stopped.")

    def status(self) -> dict:
        """Return kernel status."""
        return {
            "runtime": self.runtime.status(),
            "services": self.registry.count(),
            "registered": self.registry.list(),
        }


if __name__ == "__main__":
    kernel = CognitKernel()
    kernel.initialize()
    kernel.start()

    print(kernel.status())

    kernel.stop()
    
