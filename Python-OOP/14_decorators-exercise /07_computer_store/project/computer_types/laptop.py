from project.computer_types.computer import Computer

class Laptop(Computer):
    PROCESSORS = {"AMD Ryzen 9 5950X": 900, "Intel Core i9-11900H": 1050, "Apple M1 Pro": 1200}
    MAX_RAM = 64
    PRICE_RAM = 100

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, value):
        if value not in self.PROCESSORS:
            raise ValueError(f"{value} is not compatible with laptop {self.manufacturer} {self.model}!")
        self._processor = value

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value):
        ram_exponent = self._get_ram_exponent(value)
        if ram_exponent is None:
            raise ValueError(f"{value}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self._ram = value
        self._ram_exponent = ram_exponent

    def configure_computer(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price += self.PROCESSORS[self.processor] + (self._ram_exponent * self.PRICE_RAM)
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    @classmethod
    def _get_ram_exponent(cls, ram):
        exponent = 0
        while (2 ** exponent) <= cls.MAX_RAM:
            if (2 ** exponent) == ram:
                return exponent
            exponent += 1
        return None
