from abc import ABC, abstractmethod

class PlannerInterface(ABC):

    @abstractmethod
    def execute(self):
        pass
