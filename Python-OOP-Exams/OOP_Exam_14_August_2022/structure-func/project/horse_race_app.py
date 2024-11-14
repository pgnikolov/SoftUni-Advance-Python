from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace
from project.jockey import Jockey


class HorseRaceApp:
    HORSES_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    RACE_TYPES = ["Winter", "Spring", "Autumn", "Summer"]
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_type in self.HORSES_TYPES.keys() and self.check_horse_name(horse_name):
            new_horse = self.HORSES_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."
        elif not self.check_horse_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")


    def add_jockey(self, jockey_name, age):
        if self.check_jockey_name(jockey_name):
            new_jockey = Jockey(jockey_name, age)
            self.jockeys.append(new_jockey)
            return f"Jockey {jockey_name} is added."
        raise Exception(f"Jockey {jockey_name} has been already added!")


    def add_horse_race(self, race_type):
        if race_type in self.RACE_TYPES and self.check_race_type(race_type):
            new_race = HorseRace(race_type)
            self.horse_races.append(new_race)
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        available_horse = next((h for h in reversed(self.horses)
                                if h.__class__.__name__ == horse_type and not h.is_taken), None)
        if not available_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = available_horse
        available_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {available_horse.name}."

    def create_horse_race(self, race_type: str):

        if any(race.race_type == race_type for race in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = next((j for j in self.jockeys if j.name == jockey_name), None)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = next((r for r in self.horse_races if r.race_type == race_type), None)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = max(race.jockeys, key=lambda j: j.horse.speed)
        winner_horse = winner.horse
        return f"The winner of the {race_type} race, with a speed of {winner_horse.speed}km/h is {winner.name}! Winner's horse: {winner_horse.name}."


    def check_race_type(self, value):
        if value in self.RACE_TYPES:
            if not self.horse_races:
                return True
            elif value not in [el.race_type for el in self.horse_races]:
                return True
        raise Exception(f"Race {value} has been already created!")

    def check_jockey_name(self, value):
        if value not in [el.name for el in self.jockeys]:
            return True
        return False

    def check_horse_name(self, value):
        if value not in [el.name for el in self.horses]:
            return True
        return False



horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))