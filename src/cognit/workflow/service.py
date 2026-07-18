from cognit.workflow.models import Workflow, WorkflowTask


class WorkflowService:

    def create(self, name, tasks):
        workflow = Workflow(name)

        for index, task in enumerate(tasks, start=1):
            workflow.tasks.append(
                WorkflowTask(
                    id=index,
                    title=task["title"],
                    capability=task["capability"]
                )
            )

        return workflow

    def next_task(self, workflow):
        for task in workflow.tasks:
            if task.status == "Pending":
                return task
        return None

    def complete(self, workflow, task_id):
        for task in workflow.tasks:
            if task.id == task_id:
                task.status = "Completed"
                return task

        return None

