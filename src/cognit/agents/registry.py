from cognit.agents.models import Agent


class AgentRegistry:

    def __init__(self):
        self.agents = {}

    def register(self, agent: Agent):
        self.agents[agent.name] = agent

    def get(self, name):
        return self.agents.get(name)

    def list(self):
        return list(self.agents.keys())

    def exists(self, name):
        return name in self.agents

