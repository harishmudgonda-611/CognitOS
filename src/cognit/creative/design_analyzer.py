from .models import DesignProfile


class DesignAnalyzer:
    """
    Analyzes the user's prompt and creates a design profile.
    """

    def analyze(self, prompt: str) -> DesignProfile:

        text = prompt.lower()

        profile = DesignProfile()

        # Industry
        if "ai" in text:
            profile.industry = "AI"

        elif "portfolio" in text:
            profile.industry = "Portfolio"

        elif "restaurant" in text:
            profile.industry = "Restaurant"

        elif "agency" in text:
            profile.industry = "Agency"

        elif "ecommerce" in text or "shop" in text:
            profile.industry = "E-Commerce"

        # Theme
        if "light" in text:
            profile.theme = "light"
        else:
            profile.theme = "dark"

        # Style
        if "minimal" in text:
            profile.style = "minimal"

        elif "luxury" in text:
            profile.style = "luxury"

        else:
            profile.style = "modern"

        profile.framework = "nextjs"
        profile.css = "tailwind"

        profile.animations = [
            "gsap",
            "framer-motion"
        ]

        return profile
        
