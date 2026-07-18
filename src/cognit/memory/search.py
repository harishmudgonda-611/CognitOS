class MemorySearch:

    def __init__(self, storage):
        self.storage = storage

    def find(self, text):
        result = []

        for item in self.storage.all():
            if (
                text.lower() in item.key.lower()
                or text.lower() in item.value.lower()
            ):
                result.append(item)

        return result
