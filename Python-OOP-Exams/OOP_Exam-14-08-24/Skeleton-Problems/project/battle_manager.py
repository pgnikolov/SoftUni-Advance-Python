from project.battleships.base_battleship import BaseBattleship
from project.zones.base_zone import BaseZone
from project.zones.royal_zone import RoyalZone
from project.zones.pirate_zone import PirateZone
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship


class BattleManager:
    def __init__(self):
        self.zones = []
        self.ships = []

    def add_zone(self, zone_type: str, zone_code: str):
        pass

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        pass

    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        pass

    def remove_battleship(self, ship_name: str):
        pass

    def start_battle(self, zone: BaseZone):
        pass

    def get_statistics(self):
        pass
