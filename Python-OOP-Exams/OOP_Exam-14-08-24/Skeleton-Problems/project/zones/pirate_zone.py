from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    def __init__(self, code: str):
        super().__init__(code, 8)

    def zone_info(self):
        ships = self.get_ships()
        battleship_names = [ship.name for ship in ships]
        total_ships = len(ships)
        royal_ships_count = sum(1 for ship in ships if type(ship).__name__ == 'RoyalBattleship')

        battleship_names_str = ', '.join(battleship_names)
        if battleship_names_str:
            battleship_names_str = f"#{battleship_names_str}#"

        zone_info_str = (
            "@Royal Zone Statistics@\n"
            f"Code: {self.code}; Volume: {self.volume}\n"
            f"Battleships currently in the Pirate Zone: {total_ships}, {royal_ships_count} out of them are Royal Battleships.\n"
        )

        if battleship_names_str:
            zone_info_str += battleship_names_str
        return zone_info_str
