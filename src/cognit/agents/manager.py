from cognit.agents.registry import AgentRegistry
from cognit.agents.models import Agent


class AgentManager:

    def __init__(self):
        self.registry = AgentRegistry()
        self._register_default_agents()

    def _register_default_agents(self):

        self.add(
            Agent(
                name="Builder",
                role="Project Builder",
                capabilities=[
                    "builder.project",
                    "builder.react",
                    "builder.html",
                    "builder.css",
                    "builder.javascript",
                    "builder.components",
                    "builder.dependencies",
                    "builder.devserver",
                ],
            )
        )

        self.add(
            Agent(
                name="Verifier",
                role="Verification",
                capabilities=[
                    "verifier.test",
                    "verifier.syntax",
                    "verifier.build",
                ],
            )
        )

        self.add(
            Agent(
                name="Preview",
                role="Preview",
                capabilities=[
                    "preview.launch",
                ],
            )
        )

        self.add(
            Agent(
                name="Output",
                role="Output",
                capabilities=[
                    "output.deliver",
                ],
            )
        )

    def add(self, agent: Agent):
        self.registry.register(agent)

    def start(self, name):
        agent = self.registry.get(name)

        if agent:
            agent.status = "Running"

    def stop(self, name):
        agent = self.registry.get(name)

        if agent:
            agent.status = "Stopped"

    def status(self):
        return {
            agent.name: agent.status
            for agent in self.registry.agents.values()
        }
