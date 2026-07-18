from cognit.kernel.config import ConfigManager
from cognit.kernel.logger import CognitLogger
from cognit.kernel.events import EventBus
from cognit.kernel.registry import ServiceRegistry
from cognit.kernel.container import Container
from cognit.kernel.plugin_loader import PluginLoader
from cognit.kernel.runtime import Runtime


class CognitKernel:

    def __init__(self):
        self.config = ConfigManager()
        self.logger = CognitLogger()
        self.events = EventBus()
        self.registry = ServiceRegistry()
        self.container = Container()
        self.plugins = PluginLoader()
        self.runtime = Runtime()

    def boot(self):
        self.logger.info("Booting Cognit OS...")

        self.container.register("config", self.config)
        self.container.register("logger", self.logger)
        self.container.register("events", self.events)
        self.container.register("registry", self.registry)
        self.container.register("plugins", self.plugins)
        self.container.register("runtime", self.runtime)

        self.runtime.start()

        self.logger.info("Cognit OS Boot Complete")

    def status(self):
        return {
            "runtime": self.runtime.status(),
            "services": self.container.list(),
            "plugins": self.plugins.list(),
        }
