from pathlib import Path

from cognit.builder.filesystem import FileSystem
from cognit.builder.templates import ENGINE_TEMPLATES


class Generator:

    def __init__(self):
        self.fs = FileSystem()

    def generate(self, root: Path, name: str):

        engine = root / name.lower()

        self.fs.ensure_directory(engine)

        created = []

        for filename, template in ENGINE_TEMPLATES.items():

            path = engine / filename

            content = template.format(
                name=name.capitalize(),
                lower=name.lower()
            )

            self.fs.write_file(path, content)

            created.append(filename)

        return created

