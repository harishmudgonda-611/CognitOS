from fastapi import APIRouter
from pydantic import BaseModel

from cognit.planner.service import PlannerService
from cognit.workflow.adapter import PlanWorkflowAdapter
from cognit.workflow.executor import WorkflowExecutor

router = APIRouter()

planner = PlannerService()
adapter = PlanWorkflowAdapter()
executor = WorkflowExecutor()


class MissionRequest(BaseModel):
    mission: str


@router.post("/plan")
async def create_plan(request: MissionRequest):

    plan = planner.create_plan(request.mission)

    workflow = adapter.convert(plan)

    logs = executor.execute(workflow)

    return {
        "mission": plan.mission,
        "logs": logs,
        "tasks": [
            {
                "id": task.id,
                "title": task.title,
                "status": task.status
            }
            for task in plan.tasks
        ]
    }
    
