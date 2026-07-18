from cognit.agents.registry import AgentRegistry


class AgentRouter:

    def __init__(self, registry: AgentRegistry):
        self.registry = registry

    def find(self, capability):

        for agent in self.registry.agents.values():

            if capability in agent.capabilities:
                return agent

        return None

