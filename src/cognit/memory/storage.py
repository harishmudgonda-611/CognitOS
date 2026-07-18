from cognit.memory.models import MemoryItem


class MemoryStorage:

    def __init__(self):
        self.data = {}

    def save(self, item: MemoryItem):
        self.data[item.key] = item

    def get(self, key):
        return self.data.get(key)

    def all(self):
        return list(self.data.values())

    def delete(self, key):
        if key in self.data:
            del self.data[key]
