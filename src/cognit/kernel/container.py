class Container:

    def __init__(self):
        self._services = {}

    def register(self, name, instance):
        self._services[name] = instance

    def resolve(self, name):
        return self._services.get(name)

    def exists(self, name):
        return name in self._services

    def list(self):
        return list(self._services.keys())


