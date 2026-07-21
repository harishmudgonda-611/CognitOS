class GLMProvider:
    """
    Placeholder GLM provider.
    """

    def generate(self, prompt: str):
        return {
            "provider": "glm",
            "status": "ready",
            "message": "GLM integration not connected yet.",
            "prompt": prompt,
        }
        
