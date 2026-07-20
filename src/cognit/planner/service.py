from cognit.planner.models import Plan, Task


class PlannerService:

    def create_plan(self, mission):

        plan = Plan(mission)

        title = mission.lower()

        if "react" in title:
            task_titles = [
                "Create React Project",
                "Install Dependencies",
                "Generate Components",
                "Run Development Server",
                "Verify Build"
            ]

        elif "python" in title or "calculator" in title:
            task_titles = [
                "Create Project",
                "Generate Source Code",
                "Create README",
                "Verify Syntax",
                "Deliver Project"
            ]

        elif "website" in title:
            task_titles = [
                "Create Project",
                "Generate HTML",
                "Generate CSS",
                "Generate JavaScript",
                "Launch Preview"
            ]

        else:
            task_titles = [
                "Analyze Request",
                "Create Project",
                "Generate Files",
                "Run Verification",
                "Deliver Result"
            ]

        for index, task in enumerate(task_titles, start=1):
            plan.tasks.append(Task(index, task))

        return plan

    def complete_task(self, plan, task_id):

        for task in plan.tasks:
            if task.id == task_id:
                task.status = "Completed"

        return plan
        
