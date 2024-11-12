from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car_types = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}
        if not car_type in car_types:
            return
        new_car_type = car_types[car_type]
        if model in [el.model for el in self.cars]:
            return f"Car {model} already created."

        new_car = new_car_type(model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [el.name for el in self.drivers if el.name == driver_name]:
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [el.name for el in self.races if el.name == race_name]:
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        selected_driver = next((d for d in self.drivers if d.name == driver_name), None)
        if not selected_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        selected_car = next((el for el in reversed(self.cars) if type(el).__name__ == car_type and not el.is_taken), None)
        if not selected_car:
            raise Exception(f"Car {car_type} could not be found!")

        if selected_driver.car is None:
            selected_driver.car = selected_car
            selected_car.is_taken = True
            return f"Driver {driver_name} chose the car {selected_car.model}."

        older_car = selected_driver.car
        selected_driver.car = selected_car
        older_car.is_taken = False
        selected_car.is_taken = True
        return f"Driver {driver_name} changed his car from {type(older_car).__name__} to {car_type}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = next((el for el in self.races if el.name == race_name), None)
        driver = next((d for d in self.drivers if d.name == driver_name), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = next((el for el in self.races if el.name == race_name), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(race.drivers, key=lambda driver: driver.car.speed_limit, reverse=True)[:3]

        final_results = []
        for winner in winners:
            winner.number_of_wins += 1
            final_results.append(f"The winner is {winner.name} with total speed {winner.car.speed_limit}.")
        return '\n'.join(final_results)


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]