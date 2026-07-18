from cognit.agent.registry import AgentRegistry
from cognit.agent.models import Agent


class AgentManager:

    def __init__(self):
        self.registry = AgentRegistry()

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

