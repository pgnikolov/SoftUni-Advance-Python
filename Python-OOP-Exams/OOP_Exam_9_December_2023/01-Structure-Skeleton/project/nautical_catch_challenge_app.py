from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {'FreeDiver': FreeDiver, 'ScubaDiver': ScubaDiver}
    FISH_TYPES = {'PredatoryFish': PredatoryFish, 'DeepSeaFish': DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES.keys():
            return f"{diver_type} is not allowed in our competition."
        for d in self.divers:
            if d.name == diver_name:
                return f"{diver_name} is already a participant."
        new_diver = self.DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES.keys():
            return f"{fish_type} is forbidden for chasing in our competition."
        for f in self.fish_list:
            if f.name == fish_name:
                return f"{fish_name} is already permitted."
        new_fish = self.FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver_ = self._diver_validation(diver_name)
        if not diver_:
            return f"{diver_name} is not registered for the competition."

        fish_ = self._fish_validation(fish_name)
        if not fish_:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver_.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver_.oxygen_level < fish_.time_to_catch:
            diver_.miss(fish_.time_to_catch)
            if diver_.oxygen_level == 0:
                diver_.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        elif diver_.oxygen_level == fish_.time_to_catch:
            if is_lucky:
                diver_.hit(fish_)
                if diver_.oxygen_level == 0:
                    diver_.update_health_status()
                return f"{diver_name} hits a {fish_.points:.1f}pt. {fish_name}."
            else:
                diver_.miss(fish_.time_to_catch)
                if diver_.oxygen_level == 0:
                    diver_.update_health_status()
                return f"{diver_name} missed a good {fish_name}."

        else:
            diver_.hit(fish_)
            if diver_.oxygen_level == 0:
                diver_.update_health_status()
            return f"{diver_name} hits a {fish_.points:.1f}pt. {fish_name}."


    def health_recovery(self):
        counter = 0
        for d in self.divers:
            if d.has_health_issue:
                d.update_health_status()
                d.renew_oxy()
                counter += 1
        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name: str):
        diver_ = self._diver_validation(diver_name)
        fish_details = [fish.fish_details() for fish in diver_.catch]

        catch_report = '\n'.join(fish_details)
        return f"**{diver_name} Catch Report**\n{catch_report}"

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in sorted_divers)
        return result

    def _diver_validation(self, diver_name):
        for d in self.divers:
            if d.name == diver_name:
                return d

    def _fish_validation(self, fish_name):
        for f in self.fish_list:
            if f.name == fish_name:
                return f

nautical_catch_challenge = NauticalCatchChallengeApp()

# Dive into competition
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

# Swim into competition
print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))
#
# Check health recovery
print(nautical_catch_challenge.health_recovery())

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# View catch reports
print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))

# View competition statistics
print(nautical_catch_challenge.competition_statistics())

