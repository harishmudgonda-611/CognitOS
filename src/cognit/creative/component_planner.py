from .models import DesignProfile


class ComponentPlanner:
    """
    Plans reusable UI components for the project.
    """

    def build(self, profile: DesignProfile):

        common = [
            "Navbar",
            "Footer",
            "Button",
            "Section",
            "Container",
        ]

        if profile.industry == "Portfolio":
            specific = [
                "Hero",
                "ProjectCard",
                "SkillCard",
                "Timeline",
                "ContactForm",
            ]

        elif profile.industry == "Restaurant":
            specific = [
                "Hero",
                "MenuCard",
                "Gallery",
                "ReservationForm",
                "Map",
            ]

        else:
            specific = [
                "Hero",
                "FeatureCard",
                "PricingCard",
                "TestimonialCard",
                "FAQ",
                "CTA",
            ]

        return common + specific
        
