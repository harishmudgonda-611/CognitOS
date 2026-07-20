from dataclasses import dataclass, asdict


@dataclass
class ProjectBlueprint:
    project_type: str
    industry: str
    style: str


class PromptAnalyzer:

    def analyze(self, prompt: str):
        text = prompt.lower()

        industry = "general"
        if "bakery" in text:
            industry = "bakery"
        elif "restaurant" in text:
            industry = "restaurant"
        elif "portfolio" in text:
            industry = "portfolio"

        style = "modern"
        if "premium" in text or "luxury" in text:
            style = "luxury"

        return ProjectBlueprint(
            project_type="website",
            industry=industry,
            style=style,
        )


if __name__ == "__main__":
    analyzer = PromptAnalyzer()

    result = analyzer.analyze(
        "Build a premium bakery website"
    )

    print(asdict(result))
