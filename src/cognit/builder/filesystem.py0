from pathlib import Path


class FileSystem:

    @staticmethod
    def ensure_directory(path: Path):
        path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def write_file(path: Path, content: str):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    @staticmethod
    def exists(path: Path):
        return path.exists()

    @staticmethod
    def list_files(path: Path):
        if not path.exists():
            return []

        return sorted(item.name for item in path.iterdir())
