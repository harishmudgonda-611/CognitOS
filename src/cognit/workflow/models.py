from dataclasses import dataclass, field
from typing import List


@dataclass
class WorkflowTask:
    id: int
    title: str
    capability: str
    status: str = "Pending"


@dataclass
class Workflow:
    name: str
    tasks: List[WorkflowTask] = field(default_factory=list)

