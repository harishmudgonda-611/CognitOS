from .models import DesignProfile


class UXArchitect:
    """
    Creates a user journey based on the project type.
    """

    def build(self, profile: DesignProfile):

        if profile.industry == "Portfolio":
            return [
                "Landing",
                "Discover Projects",
                "View Skills",
                "Contact"
            ]

        elif profile.industry == "Restaurant":
            return [
                "Landing",
                "Browse Menu",
                "Reserve Table",
                "Visit Location"
            ]

        return [
            "Landing",
            "Learn Product",
            "Explore Features",
            "Compare Pricing",
            "Read Testimonials",
            "Call To Action"
        ]
        
