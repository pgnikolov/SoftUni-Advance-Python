from project.software.software import Software
from math import floor

class LightSoftware(Software):
    def __init__(self, name, software_type, capacity_consumption, memory_consumption):
        adjusted_capacity = floor(capacity_consumption * 1.5)
        adjusted_memory = floor(memory_consumption * 0.5)
        super().__init__(name, software_type, adjusted_capacity, adjusted_memory)
