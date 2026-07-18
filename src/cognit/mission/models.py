from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Mission:

    id: str

    title: str

    description: str

    status: str = "Created"

    created: datetime = field(default_factory=datetime.now)

    tasks: List[str] = field(default_factory=list)

    result: str = ""

