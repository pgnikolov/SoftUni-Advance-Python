from project.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):

    def drive(self, kilometers):
        if kilometers * CrossMotorcycle.DEFAULT_FUEL_CONSUMPTION <= self.fuel:
            self.fuel -= kilometers * CrossMotorcycle.DEFAULT_FUEL_CONSUMPTION
