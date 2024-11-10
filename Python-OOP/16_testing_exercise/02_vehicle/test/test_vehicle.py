from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.v = Vehicle(50, 118)

    def test_init(self):
        self.assertEqual(self.v.fuel, 50)
        self.assertEqual(self.v.horse_power, 118)
        self.assertEqual(self.v.fuel, self.v.capacity)
        self.assertEqual(self.v.fuel_consumption, self.v.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_success(self):
        self.v.drive(10)
        result = self.v.fuel
        expected = 37.50
        self.assertEqual(result, expected)

    def test_drive_fail(self):
        with self.assertRaises(Exception) as ex:
            self.v.drive(41)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_refuel_success(self):
        self.v.capacity = 50
        self.v.fuel = 40
        self.v.refuel(10)
        result = self.v.fuel
        expected = 50
        self.assertEqual(result, expected)

    def test_refuel_fail(self):
        self.v.capacity = 50
        self.v.fuel = 40
        with self.assertRaises(Exception) as ex:
            self.v.refuel(11)

        self.assertEqual(str(ex.exception), "Too much fuel")

    def test_str(self):
        expected = f"The vehicle has {self.v.horse_power} " \
               f"horse power with {self.v.fuel} fuel left and {self.v.fuel_consumption} fuel consumption"
        result = self.v.__str__()

        self.assertEqual(result, expected)

if __name__ == '__main__':
    main()
