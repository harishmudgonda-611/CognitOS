from cognit.planner.models import Plan, Task


class PlannerService:

    def create_plan(self, mission, task_titles):

        plan = Plan(mission)

        for index, title in enumerate(task_titles, start=1):
            plan.tasks.append(Task(index, title))

        return plan

    def complete_task(self, plan, task_id):

        for task in plan.tasks:
            if task.id == task_id:
                task.status = "Completed"

        return plan

