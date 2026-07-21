from .ai_router import AIRouter
from .prompt_builder import PromptBuilder
from .models import ProjectPlan


class CodeGenerator:
    """
    Creates a generation request for an AI model.
    """

    def __init__(self):
        self.router = AIRouter()
        self.builder = PromptBuilder()

    def generate(self, plan: ProjectPlan):

        prompt = self.builder.build(plan)

        model = self.router.select(plan.title)

        return {
            "status": "ready",
            "model": model,
            "framework": plan.profile.framework,
            "css": plan.profile.css,
            "animations": plan.profile.animations,
            "project_name": plan.title,
            "prompt": prompt,
            "output_directory": "output/generated_site"
        }
        
