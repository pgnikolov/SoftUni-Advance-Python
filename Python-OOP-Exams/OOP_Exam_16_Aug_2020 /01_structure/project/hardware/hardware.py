from abc import ABC, abstractmethod

from project.software.software import Software


class Hardware(ABC):
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @abstractmethod
    def install(self, software: Software):
        curent_used_cap = sum([el.capacity_consumption for el in self.software_components])
        curent_used_mem = sum([el.memory_consumption for el in self.software_components])
        if software.capacity_consumption <= self.capacity - curent_used_cap and software.memory_consumption <= self.memory - curent_used_mem:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    @abstractmethod
    def uninstall(self, software: Software):
        self.software_components.remove(software)
