from abc import ABC, abstractmethod


class BaseZone(ABC):
    @abstractmethod
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    @abstractmethod
    def get_ships(self):
        pass

    @abstractmethod
    def zone_info(self):
        pass
