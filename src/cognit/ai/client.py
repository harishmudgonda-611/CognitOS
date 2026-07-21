from cognit.ai.router import AIRouter


class AIClient:

    def __init__(self):
        self.router = AIRouter()

    def generate(self, provider=None, prompt=""):
        """
        provider parameter is kept for backward compatibility.
        The router automatically selects the best provider.
        """
        return self.router.generate(prompt)
        
