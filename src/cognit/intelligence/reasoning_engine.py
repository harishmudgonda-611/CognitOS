from __future__ import annotations

from pprint import pprint

from cognit.intelligence.blueprint_builder import BlueprintBuilder


class ReasoningEngine:
    """Reasoning engine for CognitOS."""

    def reason(self, prompt: str):
        blueprint = BlueprintBuilder().build(prompt)

        reasoning = {
            "goal": blueprint.goal,
            "thinking": [],
            "research_required": False,
            "clarification_required": False,
            "recommended_next_action": "",
        }

        reasoning["thinking"].append(
            f"Goal detected: {blueprint.artifact}"
        )

        if blueprint.domain != "General":
            reasoning["research_required"] = True
            reasoning["thinking"].append(
                f"Research required for {blueprint.domain}"
            )

        if blueprint.missing_information:
            reasoning["clarification_required"] = True
            reasoning["thinking"].append("User input is incomplete.")

            for item in blueprint.missing_information:
                reasoning["thinking"].append(f"Missing: {item}")

        if blueprint.risks:
            for risk in blueprint.risks:
                reasoning["thinking"].append(f"Risk: {risk}")

        if reasoning["clarification_required"]:
            reasoning["recommended_next_action"] = (
                "Ask user for missing information."
            )
        elif reasoning["research_required"]:
            reasoning["recommended_next_action"] = (
                "Perform research before execution."
            )
        else:
            reasoning["recommended_next_action"] = (
                "Start execution."
            )

        return reasoning


if __name__ == "__main__":
    engine = ReasoningEngine()

    result = engine.reason(
        "Build an AI healthcare website for hospitals under ₹50000 in 30 days"
    )

    pprint(result)
    
