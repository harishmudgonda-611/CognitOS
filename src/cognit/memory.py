import json
from pathlib import Path


class Memory:
    def __init__(self):
        self.file = Path.home() / ".cognit_memory.json"

        if not self.file.exists():
            self.file.write_text("{}")

    def load(self):
        return json.loads(self.file.read_text())

    def save(self, data):
        self.file.write_text(json.dumps(data, indent=2))

    def set(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)

    def get(self, key, default=None):
        data = self.load()
        return data.get(key, default)

    def delete(self, key):
        data = self.load()

        if key in data:
            del data[key]

        self.save(data)
        
