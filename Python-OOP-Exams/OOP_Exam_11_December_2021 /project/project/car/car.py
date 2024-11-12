from abc import ABC, abstractmethod


class Car(ABC):
    min_speed_limit: int
    max_speed_limit: int

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        if len(model) < 4:
            raise ValueError("Model {model} is less than 4 symbols!")
        self.speed_limit = speed_limit
        if speed_limit < self.min_speed_limit or speed_limit > self.max_speed_limit:
            raise ValueError("Invalid speed limit! Must be between 100 and 300!")
        self.is_taken = False
