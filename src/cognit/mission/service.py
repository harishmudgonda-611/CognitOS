from uuid import uuid4

from cognit.mission.models import Mission


class MissionService:

    def create(self, title, description):

        return Mission(

            id=str(uuid4()),

            title=title,

            description=description,

        )

    def start(self, mission):

        mission.status = "Running"

        return mission

    def complete(self, mission, result):

        mission.status = "Completed"

        mission.result = result

        return mission

