import json


class MemoryPersistence:

    def save(self, storage, filename):

        data = []

        for item in storage.all():
            data.append(item.__dict__)

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load(self, storage, filename):
        pass

