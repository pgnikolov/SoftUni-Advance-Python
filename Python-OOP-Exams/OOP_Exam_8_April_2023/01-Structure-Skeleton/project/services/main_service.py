from project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name):
        super().__init__(name, 30)

    def details(self):
        return f"{self.name} Main Service:\n" \
               f"Robots: {'none' if not self.robots else ' '.join([robot.name for robot in self.robots])}"
