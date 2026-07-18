from pathlib import Path

from cognit.builder.generator import Generator


class BuilderService:

    def __init__(self):
        self.generator = Generator()

    def create_engine(self, name: str):
        return self.generator.generate(
            Path("src/cognit"),
            name
        )

