from cognit.workflow.service import WorkflowService


class PlanWorkflowAdapter:

    def __init__(self):
        self.workflow = WorkflowService()

    def convert(self, plan):

        tasks = []

        for task in plan.tasks:

            title = task.title.lower()

            if "create react project" in title:
                capability = "builder.react"

            elif "install dependencies" in title:
                capability = "builder.dependencies"

            elif "generate components" in title:
                capability = "builder.components"

            elif "run development server" in title:
                capability = "builder.devserver"

            elif "verify build" in title:
                capability = "verifier.build"

            elif "generate html" in title:
                capability = "builder.html"

            elif "generate css" in title:
                capability = "builder.css"

            elif "generate javascript" in title:
                capability = "builder.javascript"

            elif "launch preview" in title:
                capability = "preview.launch"

            elif "verify syntax" in title:
                capability = "verifier.syntax"

            elif "run verification" in title:
                capability = "verifier.test"

            elif "deliver project" in title:
                capability = "output.deliver"

            elif "create project" in title:
                capability = "builder.project"

            else:
                capability = "builder.project"

            tasks.append({
                "title": task.title,
                "capability": capability
            })

        return self.workflow.create(plan.mission, tasks)
        
