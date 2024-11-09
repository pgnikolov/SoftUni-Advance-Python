from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS = {"AMD Ryzen 7 5700G": 500, "Intel Core i5-12600K": 600, "Apple M1 Max": 1800}
    MAX_RAM = 128
    PRICE_RAM = 100

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self._ram_exponent = None

    @property
    def processor(self):
        return self._processor

    @processor.setter
    def processor(self, value):
        if value not in self.PROCESSORS:
            raise ValueError(f"{value} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        self._processor = value

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value):
        ram_exponent = self._check_ram_compatibility(value)
        if ram_exponent is None:
            raise ValueError(f"{value}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        self._ram = value
        self._ram_exponent = ram_exponent

    def configure_computer(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price += self.PROCESSORS[self.processor] + self._ram_exponent * self.PRICE_RAM
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."

    @classmethod
    def _check_ram_compatibility(cls, ram):
        exponent = 0
        while (2 ** exponent) <= cls.MAX_RAM:
            if (2 ** exponent) == ram:
                return exponent
            exponent += 1
        return None
