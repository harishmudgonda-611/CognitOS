from pathlib import Path
import json
import os


class ConfigManager:
    def __init__(self):
        self.root = Path.cwd()
        self.config_dir = self.root / ".cognit"
        self.config_file = self.config_dir / "config.json"

        self.defaults = {
            "environment": "development",
            "log_level": "INFO",
            "plugins": True,
            "debug": False
        }

        self.config = {}
        self.load()

    def load(self):
        self.config_dir.mkdir(exist_ok=True)

        if self.config_file.exists():
            with open(self.config_file, "r") as f:
                self.config = json.load(f)
        else:
            self.config = self.defaults.copy()
            self.save()

    def save(self):
        with open(self.config_file, "w") as f:
            json.dump(self.config, f, indent=4)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save()

