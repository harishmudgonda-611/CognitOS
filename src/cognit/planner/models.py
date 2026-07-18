from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    id: int
    title: str
    status: str = "Pending"


@dataclass
class Plan:
    mission: str
    tasks: List[Task] = field(default_factory=list)

