from cognit.ai.providers.gemini import GeminiProvider


class AIRouter:
    def __init__(self):
        self.providers = [GeminiProvider()]

    def generate(self, prompt):
        last_error = None
        for provider in self.providers:
            try:
                result = provider.generate(prompt)
                if result.get("status") == "success":
                    return result
                last_error = result
            except Exception as exc:
                last_error = {"status": "error", "message": str(exc)}
        return last_error or {"status": "error", "message": "No AI provider available."}
