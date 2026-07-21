from .models import DesignProfile


class UIArchitect:
    """
    Creates the visual layout plan for each page.
    """

    def build(self, profile: DesignProfile):

        layout = {
            "header": "Sticky Navbar",
            "hero": "Fullscreen Hero",
            "sections": [],
            "footer": "Multi-column Footer"
        }

        if profile.industry == "Portfolio":

            layout["sections"] = [
                "About",
                "Projects Grid",
                "Skills",
                "Experience",
                "Contact"
            ]

        elif profile.industry == "Restaurant":

            layout["sections"] = [
                "Menu",
                "Gallery",
                "Chef",
                "Reservations",
                "Testimonials",
                "Map"
            ]

        else:

            layout["sections"] = [
                "Features",
                "About",
                "Pricing",
                "Testimonials",
                "FAQ",
                "CTA"
            ]

        return layout
        
