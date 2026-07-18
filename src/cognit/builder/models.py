from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class BuilderRequest:
    kind: str
    name: str
    root: Path


@dataclass
class BuilderResult:
    success: bool
    name: str
    path: Path
    created_files: list[str] = field(default_factory=list)
    message: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
