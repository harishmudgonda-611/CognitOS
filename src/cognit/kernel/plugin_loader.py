class PluginLoader:

    def __init__(self):
        self.plugins = {}

    def load(self, name, plugin):
        self.plugins[name] = plugin

    def unload(self, name):
        if name in self.plugins:
            del self.plugins[name]

    def get(self, name):
        return self.plugins.get(name)

    def list(self):
        return list(self.plugins.keys())
