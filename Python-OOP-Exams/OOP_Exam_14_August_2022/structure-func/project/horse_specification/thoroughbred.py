from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    TRAIN_AMOUNT = 3

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.TRAIN_AMOUNT <= self.MAX_SPEED:
            self.speed += self.TRAIN_AMOUNT
