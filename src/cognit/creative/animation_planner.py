from .models import DesignProfile


class AnimationPlanner:
    """
    Creates a motion plan for the website.
    """

    def build(self, profile: DesignProfile):

        animations = {
            "page": "fade-in",
            "hero": "zoom-in",
            "navbar": "slide-down",
            "cards": "stagger-fade",
            "buttons": "hover-scale",
            "sections": "scroll-reveal",
            "footer": "fade-up"
        }

        if profile.style == "luxury":
            animations["hero"] = "cinematic-reveal"
            animations["cards"] = "smooth-float"

        elif profile.style == "minimal":
            animations["hero"] = "simple-fade"
            animations["cards"] = "fade"

        return animations
        
