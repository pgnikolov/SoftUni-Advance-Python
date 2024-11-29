from collections import defaultdict

from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.toy_store import ToyStore
from project.stores.furniture_store import FurnitureStore
from project.stores.base_store import BaseStore
from project.products.base_product import BaseProduct

class FactoryManager:
    PRODUCT_TYPES = {'Chair': Chair, 'HobbyHorse': HobbyHorse}
    STORE_TYPES = {'ToyStore': ToyStore, 'FurnitureStore': FurnitureStore}

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in ["Chair", "HobbyHorse"]:
            raise Exception("Invalid product type!")

        product = None
        if product_type == "Chair":
            product = Chair(model, price)
        else:
            product = HobbyHorse(model, price)

        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in ['FurnitureStore', 'ToyStore']:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = None
        if store_type == 'FurnitureStore':
            store = FurnitureStore(name, location)
        else:
            store = ToyStore(name, location)

        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store, *products):
        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        matching_products = []
        for product in products:
            if ((store.store_type == "FurnitureStore" and product.sub_type == "Furniture") or
                    (store.store_type == "ToyStore" and product.sub_type == "Toys")):
                matching_products.append(product)

        if not matching_products:
            return "Products do not match in type. Nothing sold."

        for product in matching_products:
            store.products.append(product)
            self.products.remove(product)
            self.income += product.price

        store.capacity -= len(matching_products)
        return f"Store {store.name} successfully purchased {len(matching_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store.name}, location: {store.location}."

    def discount_products(self, product_model: str):
        matching_products = [p for p in self.products if p.model == product_model]
        for product in matching_products:
            product.discount()
        return f"Discount applied to {len(matching_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"
        return store.store_stats()

    def statistics(self):
        model_counts = defaultdict(int)
        total_price = 0
        for product in self.products:
            model_counts[product.model] += 1
            total_price += product.price

        model_info = [f"{model}: {count}" for model, count in sorted(model_counts.items())]
        store_names = sorted(store.name for store in self.stores)

        return (f"Factory: {self.name}\n"
                f"Income: {self.income:.2f}\n"
                f"***Products Statistics***\n"
                f"Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}\n" +
                "\n".join(model_info) + "\n"
                                        f"***Partner Stores: {len(self.stores)}***\n" +
                "\n".join(store_names))

