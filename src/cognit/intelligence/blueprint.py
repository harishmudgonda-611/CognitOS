from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any


@dataclass
class ExecutionBlueprint:
    """
    Universal blueprint used by CognitOS.
    Every engine receives and updates this object.
    """

    # Goal
    goal: str = ""
    objective: str = ""

    # Task Information
    artifact: str = ""
    domain: str = ""
    complexity: str = "Unknown"

    # Context
    audience: str = ""
    platform: str = ""
    deadline: str = ""
    budget: str = ""

    # Intelligence
    constraints: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    missing_information: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)

    # Execution
    required_skills: List[str] = field(default_factory=list)
    required_agents: List[str] = field(default_factory=list)
    required_tools: List[str] = field(default_factory=list)
    execution_steps: List[str] = field(default_factory=list)

    # Quality
    success_criteria: List[str] = field(default_factory=list)

    # Metadata
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return asdict(self)

    def summary(self):
        return (
            f"Goal: {self.goal}\n"
            f"Artifact: {self.artifact}\n"
            f"Domain: {self.domain}\n"
            f"Complexity: {self.complexity}"
        )


if __name__ == "__main__":

    blueprint = ExecutionBlueprint(
        goal="Build AI Startup",
        objective="Create production-ready application",
        artifact="Web Application",
        domain="Artificial Intelligence",
        complexity="Medium",
        audience="Developers",
        platform="Web"
    )

    print("=" * 40)
    print("COGNITOS EXECUTION BLUEPRINT")
    print("=" * 40)
    print(blueprint.summary())
    print("=" * 40)
    print(blueprint.to_dict())
    
