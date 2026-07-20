import re


class ContextAnalyzer:

    def analyze(self, prompt: str):

        text = prompt.lower()

        context = {
            "budget": "Unknown",
            "deadline": "Unknown",
            "platform": "Unknown",
            "audience": "General",
            "priority": "Normal",
            "constraints": [],
            "assumptions": [],
            "missing_information": [],
            "risks": []
        }

        # -------------------------
        # Budget
        # -------------------------
        budget = re.search(r"₹\s?[\d,]+", prompt)

        if budget:
            context["budget"] = budget.group()

        # -------------------------
        # Deadline
        # -------------------------
        deadline = re.search(
            r"\d+\s*(day|days|week|weeks|month|months)",
            text
        )

        if deadline:
            context["deadline"] = deadline.group()

        # -------------------------
        # Platform
        # -------------------------
        if "website" in text or "web" in text:
            context["platform"] = "Web"

        elif "android" in text:
            context["platform"] = "Android"

        elif "ios" in text:
            context["platform"] = "iOS"

        elif "desktop" in text:
            context["platform"] = "Desktop"

        # -------------------------
        # Audience
        # -------------------------
        audiences = [
            "students",
            "teachers",
            "doctors",
            "hospitals",
            "developers",
            "businesses",
            "customers"
        ]

        for audience in audiences:
            if audience in text:
                context["audience"] = audience.title()

        # -------------------------
        # Constraints
        # -------------------------
        if context["budget"] != "Unknown":
            context["constraints"].append("Budget")

        if context["deadline"] != "Unknown":
            context["constraints"].append("Deadline")

        # -------------------------
        # Missing Information
        # -------------------------
        if context["budget"] == "Unknown":
            context["missing_information"].append("Budget")

        if context["deadline"] == "Unknown":
            context["missing_information"].append("Deadline")

        if context["platform"] == "Unknown":
            context["missing_information"].append("Platform")

        # -------------------------
        # Risks
        # -------------------------
        if len(context["missing_information"]) > 0:
            context["risks"].append(
                "Insufficient project requirements"
            )

        return context


if __name__ == "__main__":

    analyzer = ContextAnalyzer()

    result = analyzer.analyze(
        "Build an AI healthcare website for hospitals under ₹50000 in 30 days"
    )

    print(result)
    
