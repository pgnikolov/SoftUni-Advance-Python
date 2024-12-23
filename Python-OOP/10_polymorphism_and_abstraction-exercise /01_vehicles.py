from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity
        self.__air_conditioners_consumptions = 0.9

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + self.__air_conditioners_consumptions)
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity
        self.__air_conditioners_consumptions = 1.6
        self.__fuel_tank_leak = 0.95

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + self.__air_conditioners_consumptions)
        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.__fuel_tank_leak
