from cognit.mission.runner import MissionRunner


def mission():

    runner = MissionRunner()

    mission, plan, workflow = runner.run(
        title="Build Todo App",
        description="Create a simple Todo application",
    )

    print()
    print("Mission :", mission.title)

    print("\nExecution Plan:")

    for task in plan.tasks:
        print(f"{task.id}. {task.title}")
        
