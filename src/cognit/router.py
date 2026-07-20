from dataclasses import dataclass


@dataclass
class Model:
    name: str
    provider: str
    strengths: list[str]


class ModelRouter:
    def __init__(self):
        self.models = [
            Model(
                name="gemini",
                provider="Google",
                strengths=["general", "coding", "reasoning"],
            ),
            Model(
                name="claude",
                provider="Anthropic",
                strengths=["coding", "writing", "analysis"],
            ),
            Model(
                name="qwen",
                provider="Alibaba",
                strengths=["coding", "multilingual"],
            ),
        ]

    def choose(self, task: str) -> Model:
        task = task.lower()

        keywords = {
            "claude": ["code", "python", "react", "build", "debug"],
            "gemini": ["write", "article", "email", "summary"],
            "qwen": ["translate", "multilingual", "chinese"],
        }

        for model in self.models:
            for keyword in keywords.get(model.name, []):
                if keyword in task:
                    return model

        return self.models[0]

        
