class AIRouter:
    """
    Selects which AI model should handle the request.
    """

    def __init__(self):
        self.default_model = "gemini"

    def select(self, task: str):

        task = task.lower()

        if "website" in task:
            return "gemini"

        if "react" in task:
            return "gemini"

        if "python" in task:
            return "qwen"

        if "analysis" in task:
            return "glm"

        return self.default_model
        
