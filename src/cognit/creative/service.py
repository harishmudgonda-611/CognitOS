from .models import ProjectPlan
from .design_analyzer import DesignAnalyzer
from .creative_director import CreativeDirector
from .design_system import DesignSystem
from .ux_architect import UXArchitect
from .ui_architect import UIArchitect
from .component_planner import ComponentPlanner
from .animation_planner import AnimationPlanner


class CreativeStudio:

    def __init__(self):
        self.analyzer = DesignAnalyzer()
        self.director = CreativeDirector()
        self.design_system = DesignSystem()
        self.ux = UXArchitect()
        self.ui = UIArchitect()
        self.components = ComponentPlanner()
        self.animations = AnimationPlanner()

    def build(self, prompt: str) -> ProjectPlan:

        profile = self.analyzer.analyze(prompt)

        pages = self.director.plan(profile)

        design_tokens = self.design_system.build(profile)

        ux_flow = self.ux.build(profile)

        ui_layout = self.ui.build(profile)

        component_list = self.components.build(profile)

        animation_plan = self.animations.build(profile)

        return ProjectPlan(
            title=prompt,
            profile=profile,
            pages=pages,
            components=component_list,
            metadata={
                "engine": "Creative Studio v3",
                "status": "planning",
                "version": "0.3",
                "design_system": design_tokens,
                "ux_flow": ux_flow,
                "ui_layout": ui_layout,
                "animation_plan": animation_plan,
            },
        )
        
