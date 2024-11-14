from project.horse_specification.horse import Horse



class Appaloosa(Horse):
    MAX_SPEED = 120
    TRAIN_AMOUNT = 2

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.TRAIN_AMOUNT <= self.MAX_SPEED:
            self.speed += self.TRAIN_AMOUNT
        else:
            self.speed = self.MAX_SPEED
