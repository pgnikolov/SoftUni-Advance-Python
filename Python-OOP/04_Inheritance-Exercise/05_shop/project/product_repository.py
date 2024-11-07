from project.product import Product
from project.drink import Drink
from project.food import Food


class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for el in self.products:
            if el.name == product_name:
                return el

    def remove(self, product_name: str):
        for product_ in self.products:
            if product_.name == product_name:
                self.products.remove(product_)

    def __repr__(self):
        output = ""
        for el in self.products:
            if el.name not in output:
                output += f"{el.name}: {el.quantity}\n"
        return output.rstrip()

