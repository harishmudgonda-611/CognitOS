from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:

    name: str
    role: str
    capabilities: List[str] = field(default_factory=list)
    status: str = "Idle"

