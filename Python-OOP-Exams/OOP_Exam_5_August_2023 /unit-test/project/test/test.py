from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("BMW", "M5", 20000, 50000.0)

    def test_init(self):
        self.assertEqual(self.car.model, "BMW")
        self.assertEqual(self.car.car_type, 'M5')
        self.assertEqual(self.car.mileage, 20000)
        self.assertEqual(self.car.price, 50000.0)
        self.assertEqual(self.car.repairs, [])

    def test_price_setter_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 1.0
        self.assertEqual(str(ex.exception),"Price should be greater than 1.0!")

    def test_mileage_setter_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100
        self.assertEqual(str(ex.exception),"Please, second-hand cars only! Mileage must be greater than 100!")

    def test_set_promotional_price_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(100000)
        self.assertEqual(str(ex.exception),"You are supposed to decrease the price!")

    def test_set_promotional_price_success(self):
        result = self.car.set_promotional_price(15000)
        expected = 'The promotional price has been successfully set.'
        self.assertEqual(result, expected)
        self.assertEqual(self.car.price, 15000.0)

    def test_need_repair_fail_price(self):
        result = self.car.need_repair(30000, "Test Repair")
        expected = 'Repair is impossible!'
        self.assertEqual(result, expected)

    def test_need_repair_success(self):
        result = self.car.need_repair(2000, "Test Repair")
        expected = 'Price has been increased due to repair charges.'
        self.assertEqual(result, expected)
        self.assertEqual(self.car.price, 52000.0)

    def test__gt__1(self):
        self.car2 = SecondHandCar('BMW', 'M3', 10000, 10000.0)
        result = self.car.__gt__(self.car2)
        expected = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(result, expected)

    def test__gt__2(self):
        self.car2 = SecondHandCar('BMW', 'M5', 10000, 40000.0)
        self.assertTrue(self.car.__gt__(self.car2))

    def test__str__(self):
        expected = f"""Model {self.car.model} | Type {self.car.car_type} | Milage {self.car.mileage}km
Current price: {self.car.price:.2f} | Number of Repairs: {len(self.car.repairs)}"""
        result = self.car.__str__()
        self.assertEqual(result, expected)

if __name__ == '__main__':
    main()
