from cognit.builder.website_builder import WebsiteBuilder


class TaskOrchestrator:
    """
    Cognit Task Orchestrator
    """

    def __init__(self):
        self.website_builder = WebsiteBuilder()

    def execute(self, task: str):

        goal = task.strip()

        result = {
            "goal": goal,
            "blueprint": {
                "title": goal,
                "objective": "Analyze and execute the requested task."
            },
            "reasoning": [
                "Understand the user's goal.",
                "Create a solution blueprint.",
                "Generate an execution plan."
            ],
            "plan": [
                "Analyze Request",
                "Design Solution",
                "Generate Output"
            ],
            "status": "completed",
            "files": []
        }

        text = goal.lower()

        if "website" in text:

            files = self.website_builder.build("website")

            result["status"] = "website generated"
            result["files"] = files

        return result
        
