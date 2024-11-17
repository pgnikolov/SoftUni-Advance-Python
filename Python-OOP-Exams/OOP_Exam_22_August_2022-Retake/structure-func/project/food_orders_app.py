from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter
from project.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients = []

    def register_client(self, client_phone_number):
        if [cl for cl in self.clients if cl.phone_number == client_phone_number]:
            raise Exception("The client has already been registered!")
        self.clients.append(Client(client_phone_number))

    def add_meals_to_menu(self, *meals: Meal):
