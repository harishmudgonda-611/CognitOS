from .models import ProjectPlan


class PromptBuilder:
    """
    Converts a ProjectPlan into a prompt for an AI code generator.
    """

    def build(self, plan: ProjectPlan) -> str:

        sections = []

        for page in plan.pages:
            sections.append(
                f"{page.name}: {', '.join(page.sections)}"
            )

        prompt = f"""
You are a senior frontend engineer.

Create a premium production-quality website.

Project:
{plan.title}

Industry:
{plan.profile.industry}

Style:
{plan.profile.style}

Theme:
{plan.profile.theme}

Framework:
{plan.profile.framework}

CSS:
{plan.profile.css}

Animations:
{", ".join(plan.profile.animations)}

Pages:
{chr(10).join(sections)}

Components:
{", ".join(plan.components)}

Requirements:
- Responsive
- Accessible
- SEO friendly
- Modern UI
- Reusable components
"""

        return prompt.strip()
        
