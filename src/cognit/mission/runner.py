from cognit.mission.service import MissionService
from cognit.planner.service import PlannerService
from cognit.workflow.adapter import PlanWorkflowAdapter
from cognit.workflow.orchestrator import WorkflowOrchestrator
from cognit.agents.registry import AgentRegistry
from cognit.agents.models import Agent


class MissionRunner:

    def __init__(self):
        self.mission_service = MissionService()
        self.planner = PlannerService()
        self.adapter = PlanWorkflowAdapter()

        self.registry = AgentRegistry()

        self.registry.register(
            Agent(
                name="React Builder",
                role="Builder",
                capabilities=[
                    "builder.react",
                    "builder.ui",
                ],
            )
        )

        self.orchestrator = WorkflowOrchestrator(self.registry)

    def run(self, title, description):

        mission = self.mission_service.create(title, description)
        mission = self.mission_service.start(mission)

        plan = self.planner.create_plan(mission.title)

        workflow = self.adapter.convert(plan)

        self.orchestrator.run(workflow)

        return mission, plan, workflow
        
