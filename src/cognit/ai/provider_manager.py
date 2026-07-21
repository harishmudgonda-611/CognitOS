class ProviderManager:
    def __init__(self):
        self.providers = [
            "gemini",
            "groq",
            "huggingface",
            "openrouter"
        ]

    def get_providers(self):
        return self.providers

    def move_to_end(self, provider):
        if provider in self.providers:
            self.providers.remove(provider)
            self.providers.append(provider)
            
