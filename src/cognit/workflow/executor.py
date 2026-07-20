from cognit.workflow.orchestrator import WorkflowOrchestrator
from cognit.agents.manager import AgentManager


class WorkflowExecutor:

    def __init__(self):
        self.manager = AgentManager()
        self.orchestrator = WorkflowOrchestrator(
            self.manager.registry
        )

    def execute(self, workflow):

        logs = []

        while True:

            task = self.orchestrator.workflow.next_task(workflow)

            if task is None:
                logs.append("✅ Workflow Complete")
                break

            agent = self.orchestrator.router.find(task.capability)

            if agent is None:
                logs.append(
                    f"❌ No agent for {task.capability}"
                )
                break

            logs.append(
                f"▶ {agent.name}: {task.title}"
            )

            self.orchestrator.workflow.complete(
                workflow,
                task.id
            )

            logs.append(
                f"✔ {task.title}"
            )

        return logs
        
