import json
from pathlib import Path

REGISTRY_DIR = Path(".cognit/registry")

class Registry:

    def __init__(self, name):
        self.file = REGISTRY_DIR / f"{name}.json"

        if not self.file.exists():
            self.file.write_text("{}")

    def load(self):
        return json.loads(self.file.read_text())

    def save(self, data):
        self.file.write_text(json.dumps(data, indent=2))

    def register(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)

    def list(self):
        return self.load()
