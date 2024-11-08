from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.budget = budget
        self.animal_capacity = animal_capacity
        self.workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        self.__budget = value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @animal_capacity.setter
    def animal_capacity(self, value):
        self.__animal_capacity = value

    @property
    def workers_capacity(self):
        return self.__workers_capacity

    @workers_capacity.setter
    def workers_capacity(self, value):
        self.__workers_capacity = value

    def add_animal(self, animal: Animal, price):
        if len(self.animals) < self.animal_capacity and self.budget >= price:
            self.animals.append(animal)
            self.budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif len(self.animals) < self.animal_capacity and self.budget < price:
            return f"Not enough budget"
        return f"Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if len(self.workers) < self.workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return f"Not enough space for worker"

    def fire_worker(self, worker_name):
        for el in self.workers:
            if el.name == worker_name:
                self.workers.remove(el)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total = 0
        for el in self.workers:
            total += el.salary
        if self.budget >= total:
            self.budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_cost = 0
        for el in self.animals:
            total_cost += el.money_for_care
        if self.budget >= total_cost:
            self.budget -= total_cost
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.budget += amount

    def animals_status(self):
        stats = {"Cheetah": [], "Tiger": [], "Lion": []}
        for el in self.animals:
            animal_type = el.__class__.__name__
            stats[animal_type].append(str(el))

        total_animals = len(stats['Cheetah']) + len(stats['Tiger']) + len(stats['Lion'])

        output = [
            f"You have {total_animals} animals",
            f"----- {len(stats['Lion'])} Lions:", *stats['Lion'],
            f"----- {len(stats['Tiger'])} Tigers:", *stats['Tiger'],
            f"----- {len(stats['Cheetah'])} Cheetahs:", *stats['Cheetah']
        ]

        return "\n".join(output)

    def workers_status(self):
        stats = {"Keeper": [], "Vet": [], "Caretaker": []}
        for el in self.workers:
            worker_type = el.__class__.__name__
            stats[worker_type].append(str(el))

        total_workers = len(stats['Keeper']) + len(stats['Vet']) + len(stats['Caretaker'])

        output = [
            f"You have {total_workers} workers",
            f"----- {len(stats['Keeper'])} Keepers:", *stats['Keeper'],
            f"----- {len(stats['Caretaker'])} Caretakers:", *stats['Caretaker'],
            f"----- {len(stats['Vet'])} Vets:", *stats['Vet']
        ]

        return "\n".join(output)
