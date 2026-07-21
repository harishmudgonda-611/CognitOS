class DeepSeekProvider:
    """
    Placeholder DeepSeek provider.
    """

    def generate(self, prompt: str):
        return {
            "provider": "deepseek",
            "status": "ready",
            "message": "DeepSeek integration not connected yet.",
            "prompt": prompt,
        }
        
