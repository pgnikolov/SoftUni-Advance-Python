from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    def __init__(self, model, price):
        super().__init__(model, price, 'Wood/Plastic', 'Toys')

    def discount(self):
        self.price *= 0.80
