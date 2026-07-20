from __future__ import annotations

from cognit.intelligence.blueprint import ExecutionBlueprint
from cognit.intelligence.goal_interpreter import GoalInterpreter
from cognit.intelligence.context_analyzer import ContextAnalyzer


class BlueprintBuilder:
    """Builds an ExecutionBlueprint from a user prompt."""

    def __init__(self) -> None:
        self.goal_interpreter = GoalInterpreter()
        self.context_analyzer = ContextAnalyzer()

    def build(self, prompt: str) -> ExecutionBlueprint:
        blueprint = self.goal_interpreter.interpret(prompt)

        context = self.context_analyzer.analyze(prompt)

        blueprint.budget = context.get("budget")
        blueprint.deadline = context.get("deadline")
        blueprint.platform = context.get("platform")
        blueprint.audience = context.get("audience")
        blueprint.constraints = context.get("constraints", [])
        blueprint.assumptions = context.get("assumptions", [])
        blueprint.missing_information = context.get("missing_information", [])
        blueprint.risks = context.get("risks", [])

        return blueprint
        
