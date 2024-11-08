class Shop:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @staticmethod
    def small_shop(name, type):
        return Shop(name, type, 10)

    def add_item(self, item_name: str):
        if self.capacity > sum(self.items.values()):
            self.items[item_name] = self.items.get(item_name, 0) + 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items.keys() and amount <= self.items[item_name]:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                self.items.pop(item_name)
            return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
