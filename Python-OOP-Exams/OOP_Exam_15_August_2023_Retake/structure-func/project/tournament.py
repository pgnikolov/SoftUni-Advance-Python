from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        if not name.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    def add_equipment(self, equipment_type: str):
        if equipment_type not in ["KneePad", "ElbowPad"]:
            raise Exception("Invalid equipment type!")

        equipment = KneePad() if equipment_type == "KneePad" else ElbowPad()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        if team_type not in ["OutdoorTeam", "IndoorTeam"]:
            raise Exception("Invalid team type!")

        team = OutdoorTeam(team_name, country, advantage) if team_type == "OutdoorTeam" else IndoorTeam(team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = next((e for e in self.equipment if type(e).__name__ == equipment_type), None)
        if not equipment:
            raise Exception(f"No {equipment_type} available!")

        team = next((t for t in self.teams if t.name == team_name), None)
        if not team or team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((t for t in self.teams if t.name == team_name), None)
        if not team:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = sum(1 for e in self.equipment if type(e).__name__ == equipment_type)
        for e in self.equipment:
            if type(e).__name__ == equipment_type:
                e.increase_price()
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next(t for t in self.teams if t.name == team_name1)
        team2 = next(t for t in self.teams if t.name == team_name2)

        if type(team1) is not type(team2):
            raise Exception("Game cannot start! Team types mismatch!")

        team1_score = team1.advantage + sum(e.protection for e in team1.equipment)
        team2_score = team2.advantage + sum(e.protection for e in team2.equipment)

        if team1_score > team2_score:
            team1.win()
            return f"The winner is {team1.name}."
        elif team2_score > team1_score:
            team2.win()
            return f"The winner is {team2.name}."
        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: t.wins, reverse=True)
        result = [f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:"]
        result.extend(t.get_statistics() for t in sorted_teams)
        return "\n".join(result)
