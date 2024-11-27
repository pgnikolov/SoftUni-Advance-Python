from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    MAX_STRENGTH = 200
    def __init__(self, name):
        super().__init__(name, self.MAX_STRENGTH)

    def can_climb(self):
        if self.strength >= 100:
            return True
        return False

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == 'Extreme':
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5
        self.conquered_peaks.append(peak)
