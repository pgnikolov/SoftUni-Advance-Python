class Driver:
    def __init__(self, name: str):
        self.name = name
        if name == "" or name.isspace():
            raise ValueError("Name should contain at least one character!")
        self.car = None
        self.number_of_wins = 0
