from player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player not in self.players and player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player is self.players and player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated" and player.guild != self.name:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for member in self.players:
            if member.name == player_name:
                member.guild = "Unaffiliated"
                self.players.remove(member)
                return f"Player {player_name} has been removed from the guild."
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        output = [f"Guild: {self.name}"]
        for player in self.players:
            output.append(player.player_info())
        return "\n".join(output)


player = Player("George", 50, 100)

print(player.add_skill("Shield Break", 20))

print(player.player_info())

guild = Guild("UGT")

print(guild.assign_player(player))

print(guild.guild_info())
