from .models import DesignProfile, PagePlan


class CreativeDirector:
    """
    Plans the website structure based on the design profile.
    """

    def plan(self, profile: DesignProfile):

        pages = []

        if profile.industry == "Portfolio":
            pages.append(
                PagePlan(
                    name="Home",
                    sections=[
                        "Hero",
                        "About",
                        "Projects",
                        "Skills",
                        "Experience",
                        "Contact",
                        "Footer"
                    ]
                )
            )

        elif profile.industry == "Restaurant":
            pages.append(
                PagePlan(
                    name="Home",
                    sections=[
                        "Hero",
                        "Menu",
                        "Gallery",
                        "Reservations",
                        "Testimonials",
                        "Location",
                        "Footer"
                    ]
                )
            )

        else:
            pages.append(
                PagePlan(
                    name="Home",
                    sections=[
                        "Hero",
                        "Features",
                        "About",
                        "Pricing",
                        "Testimonials",
                        "FAQ",
                        "CTA",
                        "Footer"
                    ]
                )
            )

        return pages
        
