from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV


class Room:
    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if float(value) < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for el_list in args:
            for el in el_list:
                total_expenses += el.get_monthly_expense()
        self.expenses = total_expenses

    @staticmethod
    def add_tv():
        return TV()

    @staticmethod
    def add_fridge():
        return Fridge()

    @staticmethod
    def add_laptop():
        return Laptop()

    @staticmethod
    def add_stove():
        return Stove()
