from .models import DesignProfile


class DesignSystem:
    """
    Generates design tokens from a DesignProfile.
    """

    def build(self, profile: DesignProfile):

        colors = {
            "background": "#0F172A",
            "surface": "#111827",
            "primary": "#7C3AED",
            "secondary": "#22D3EE",
            "text": "#FFFFFF"
        }

        if profile.theme == "light":
            colors = {
                "background": "#FFFFFF",
                "surface": "#F8FAFC",
                "primary": "#4F46E5",
                "secondary": "#0EA5E9",
                "text": "#111827"
            }

        typography = {
            "heading": "Space Grotesk",
            "body": "Inter"
        }

        spacing = {
            "section": 96,
            "container": 1280,
            "radius": 16
        }

        return {
            "colors": colors,
            "typography": typography,
            "spacing": spacing
        }
        
