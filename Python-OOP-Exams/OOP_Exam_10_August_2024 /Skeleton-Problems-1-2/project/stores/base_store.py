from abc import ABC, abstractmethod


class BaseStore(ABC):
    @abstractmethod
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value.strip()) < 3 or len(value.strip()) > 3:
            raise ValueError( "Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        products_value = 0
        for product in self.products:
            products_value += product.price
        return f"Estimated future profit for {len(self.products)} products is {(products_value * 0.10):.2f}"

    @property
    def store_type(self):
        return self.__class__.__name__

    @abstractmethod
    def store_stats(self):
        pass
