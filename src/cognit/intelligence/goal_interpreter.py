from cognit.intelligence.blueprint import ExecutionBlueprint


class GoalInterpreter:

    def interpret(self, prompt: str) -> ExecutionBlueprint:

        text = prompt.lower()

        blueprint = ExecutionBlueprint()
        blueprint.goal = prompt

        # -----------------------------
        # Artifact Detection
        # -----------------------------
        artifacts = {
            "website": "Website",
            "web app": "Web Application",
            "app": "Application",
            "mobile app": "Mobile Application",
            "api": "API",
            "dashboard": "Dashboard",
            "report": "Report",
            "presentation": "Presentation",
            "video": "Video",
            "logo": "Logo",
            "automation": "Automation",
            "agent": "AI Agent"
        }

        blueprint.artifact = "Unknown"

        for keyword, value in artifacts.items():
            if keyword in text:
                blueprint.artifact = value
                break

        # -----------------------------
        # Domain Detection
        # -----------------------------
        domains = {
            "ai": "Artificial Intelligence",
            "hospital": "Healthcare",
            "health": "Healthcare",
            "education": "Education",
            "school": "Education",
            "finance": "Finance",
            "bank": "Finance",
            "ecommerce": "E-Commerce",
            "shop": "E-Commerce",
            "bakery": "Bakery",
            "restaurant": "Restaurant",
            "hotel": "Hospitality",
            "travel": "Travel",
            "youtube": "Content Creation",
            "affiliate": "Affiliate Marketing"
        }

        blueprint.domain = "General"

        for keyword, value in domains.items():
            if keyword in text:
                blueprint.domain = value
                break

        # -----------------------------
        # Complexity
        # -----------------------------
        score = 0

        if blueprint.artifact != "Unknown":
            score += 1

        if blueprint.domain != "General":
            score += 1

        if len(prompt.split()) > 10:
            score += 1

        if "ai" in text:
            score += 1

        if score <= 1:
            blueprint.complexity = "Low"
        elif score == 2:
            blueprint.complexity = "Medium"
        else:
            blueprint.complexity = "High"

        # -----------------------------
        # Skills
        # -----------------------------
        skills = []

        if blueprint.artifact in ["Website", "Web Application"]:
            skills.extend([
                "Frontend Development",
                "UI/UX Design"
            ])

        if blueprint.artifact == "Mobile Application":
            skills.append("Mobile Development")

        if blueprint.domain == "Artificial Intelligence":
            skills.append("AI Engineering")

        if blueprint.domain == "Affiliate Marketing":
            skills.append("Marketing")

        blueprint.required_skills = skills

        # -----------------------------
        # Agents
        # -----------------------------
        blueprint.required_agents = [
            "Planner Agent",
            "Research Agent"
        ]

        if "Development" in " ".join(skills):
            blueprint.required_agents.append("Developer Agent")

        if "Design" in " ".join(skills):
            blueprint.required_agents.append("Designer Agent")

        if "AI Engineering" in skills:
            blueprint.required_agents.append("AI Engineer Agent")

        # -----------------------------
        # Execution Steps
        # -----------------------------
        blueprint.execution_steps = [
            "Understand Goal",
            "Research",
            "Plan",
            "Execute",
            "Verify",
            "Improve"
        ]

        blueprint.success_criteria = [
            "Goal Completed",
            "Quality Verified"
        ]

        return blueprint


if __name__ == "__main__":

    interpreter = GoalInterpreter()

    result = interpreter.interpret(
        "Build an AI startup website with modern UI"
    )

    print(result.to_dict())

    
