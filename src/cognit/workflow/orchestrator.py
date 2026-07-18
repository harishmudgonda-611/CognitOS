from cognit.workflow.service import WorkflowService
from cognit.agents.router import AgentRouter


class WorkflowOrchestrator:

    def __init__(self, registry):
        self.workflow = WorkflowService()
        self.router = AgentRouter(registry)

    def run(self, workflow):

        while True:

            task = self.workflow.next_task(workflow)

            if task is None:
                print("✅ Workflow Complete")
                break

            agent = self.router.find(task.capability)

            if agent is None:
                print(f"No agent found for {task.capability}")
                break

            print(f"{agent.name} -> {task.title}")

            self.workflow.complete(workflow, task.id)

