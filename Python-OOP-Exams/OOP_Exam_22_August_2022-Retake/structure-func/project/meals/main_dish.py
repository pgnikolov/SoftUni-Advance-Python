from project.meals.meal import Meal


class MainDish(Meal):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        if self.quantity == 0:
            self.quantity = 50

    def details(self):
        return f"{self.__class__.__name__}: {self.price:.2f}lv/piece"
