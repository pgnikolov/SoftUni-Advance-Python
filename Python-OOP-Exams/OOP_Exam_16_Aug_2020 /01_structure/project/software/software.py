from abc import ABC, abstractmethod

class Software(ABC):
    def __init__(self, name, software_type, capacity_consumption, memory_consumption):
        self.name = name
        self.software_type = software_type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption
