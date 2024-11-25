from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    MAX_OXYGEN = 540
    def __init__(self, name):
        super().__init__(name, oxygen_level=self.MAX_OXYGEN)

    def miss(self, time_to_catch: int):
        rounded_value = round(time_to_catch * 0.6)
        if self.oxygen_level < rounded_value:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= rounded_value

    def renew_oxy(self):
        self.oxygen_level = self.MAX_OXYGEN
