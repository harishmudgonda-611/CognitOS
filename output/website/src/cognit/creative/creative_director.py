"""
Cognit Creative Director

Creates a creative brief from the user's request.
This is the first stage of the premium website generation pipeline.
"""


class CreativeDirector:

    def create_brief(self, prompt: str):

        prompt = prompt.strip()

        return {
            "project": prompt,
            "style": "Premium Modern",
            "theme": "Dark",
            "quality": "Awwwards",
            "animation": True,
            "responsive": True,
            "framework": "Next.js + Tailwind",
            "motion": "GSAP + Framer Motion",
            "threejs": False,
            "pages": [
                "Home"
            ],
            "sections": [
                "Hero",
                "Features",
                "About",
                "Gallery",
                "Testimonials",
                "Pricing",
                "FAQ",
                "Contact",
                "Footer"
            ],
            "design": {
                "spacing": "Luxury",
                "typography": "Bold Modern",
                "border_radius": "Large",
                "shadow": "Soft",
                "glassmorphism": True,
                "gradients": True
            }
        }
        
