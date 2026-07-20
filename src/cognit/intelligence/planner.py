"""
CognitOS Planner

Creates an execution plan from the reasoning output.
"""

from __future__ import annotations

from typing import Any


class Planner:
    """Simple execution planner."""

    def create_plan(self, reasoning: dict[str, Any]) -> dict[str, Any]:
        plan = {
            "goal": reasoning.get("goal"),
            "steps": [],
            "status": "ready",
        }

        if reasoning.get("research_required"):
            plan["steps"].append("Research")

        if reasoning.get("clarification_required"):
            plan["steps"].append("Ask User")

        plan["steps"].append("Execute")
        plan["steps"].append("Verify")

        return plan


if __name__ == "__main__":
    sample = {
        "goal": "Build an AI website",
        "research_required": True,
        "clarification_required": False,
    }

    planner = Planner()
    print(planner.create_plan(sample))
    
