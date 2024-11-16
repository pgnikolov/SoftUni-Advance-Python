from project.meals.meal import Meal


class Starter(Meal):
    def __init__(self, name: str, price: float, quantity: int):
        if quantity <= 0:
            self.quantity = 10
        super().__init__(name, price, self.quantity)

    def details(self):
        return f"{self.__class__.__name__}: {self.price:.2f}lv/piece"
