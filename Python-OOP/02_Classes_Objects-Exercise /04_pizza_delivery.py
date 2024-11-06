class PizzaDelivery:

    def __init__(self, name, price, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity * quantity
        else:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif ingredient in self.ingredients and self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= price_per_quantity * quantity

    def make_order(self):
        if not self.ordered:
            self.ordered = True
            text = [f"{key}: {value}" for key, value in self.ingredients.items()]
            return f"You've ordered pizza {self.name} prepared with {', '.join(text)} and the price will be {self.price}lv."
        return f"Pizza {self.name} already prepared, and we can't make any changes!"
