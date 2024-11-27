from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.summit_peak import SummitPeak
from project.peaks.arctic_peak import ArcticPeak


class SummitQuestManagerApp:
    PEAK_TYPES = {'SummitPeak': SummitPeak, 'ArcticPeak': ArcticPeak}
    CLIMBER_TYPES = {'ArcticClimber': ArcticClimber, 'SummitClimber': SummitClimber}
    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES.keys():
            return f"{climber_type} doesn't exist in our register."
        if self._get_climber_by_name(climber_name):
            return f"{climber_name} has been already registered."

        new_climber = self.CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPES.keys():
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.PEAK_TYPES[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        p = self._get_peak_by_name(peak_name)
        required_gear = set(p.get_recommended_gear())
        if required_gear == set(gear):
            return f"{climber_name} is prepared to climb {peak_name}."

        c = self._get_obj_climber_by_name(climber_name)
        c.is_prepared = False
        missing_items = required_gear - set(gear)
        sorted_missing_items = sorted(missing_items)
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_missing_items)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        c = self._get_obj_climber_by_name(climber_name)
        if not c:
            return f"Climber {climber_name} is not registered yet."

        p = self._get_peak_by_name(peak_name)
        if not p:
            return f"Peak {peak_name} is not part of the wish list."

        if c.can_climb() and c.is_prepared:
            c.conquered_peaks.append(peak_name)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {p.calculate_difficulty_level()}."

        if not c.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        # Sort climbers based on the number of conquered peaks and their names
        sorted_climbers = sorted(
            [climber for climber in self.climbers if climber.conquered_peaks],
            key=lambda climber: (-len(climber.conquered_peaks), climber.name)
        )

        # Prepare the result lines
        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]

        # Append climber statistics to the result
        climber_statistics = "\n".join(str(c) for c in sorted_climbers)
        if climber_statistics:  # Only add climber statistics if available
            result.append(climber_statistics)

        # Return the result as a single string
        return "\n".join(result)

    def _get_climber_by_name(self, climber_name: str):
        for climber in self.climbers:
            if climber_name == climber.name:
                return True
        return False

    def _get_peak_by_name(self, peak_name: str):
        for peak in self.peaks:
            if peak_name == peak.name:
                return peak
        return None


    def _get_obj_climber_by_name(self, climber_name: str):
        for climber in self.climbers:
            if climber_name == climber.name:
                return climber
        return None


# Create an instance of SummitQuestManagerApp
climbing_app = SummitQuestManagerApp()

# Register climbers
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("ExtremeClimber", "Dave"))
print(climbing_app.register_climber("ArcticClimber", "Charlie"))
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Eve"))
print(climbing_app.register_climber("SummitClimber", "Frank"))

# Add peaks to the wish list
print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

# Prepare climbers for climbing
print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))
#
# Perform climbing
print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))
#
# Get statistics
print(climbing_app.get_statistics())
