from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, software_type, capacity_consumption, memory_consumption):
        adjusted_memory = memory_consumption * 2
        super().__init__(name, software_type,capacity_consumption, adjusted_memory)
