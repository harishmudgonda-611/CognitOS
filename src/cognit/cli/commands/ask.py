import sys

from cognit.router import ModelRouter
from cognit.memory.service import MemoryService


def ask():
    if len(sys.argv) < 3:
        print("Usage: cognit ask <your task>")
        return

    task = " ".join(sys.argv[2:])

    router = ModelRouter()
    memory = MemoryService()

    model = router.choose(task)

    memory.set("last_task", task)
    memory.set("last_model", model.name)
    memory.set("last_provider", model.provider)

    print("=" * 40)
    print("          COGNIT ASK")
    print("=" * 40)
    print(f"Task     : {task}")
    print(f"Model    : {model.name}")
    print(f"Provider : {model.provider}")
    print(f"Strength : {', '.join(model.strengths)}")
    print("=" * 40)
    print("✓ Task saved to memory")

