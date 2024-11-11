from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):

    def setUp(self):
        self.ps = PetShop("PS1")

    def test_init(self):
        self.assertEqual("PS1", self.ps.name)
        self.assertEqual([], self.ps.pets)
        self.assertEqual({}, self.ps.food)

    def test_add_food_fail_quantity_el_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.ps.add_food('apple', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_success(self):
        result = self.ps.add_food('apple', 10)
        self.assertEqual(10, self.ps.food['apple'])
        self.assertEqual("Successfully added 10.00 grams of apple.", result)

    def test_add_pet_success(self):
        result = self.ps.add_pet("Gosho")
        self.assertEqual(["Gosho"], self.ps.pets)
        self.assertEqual("Successfully added Gosho.", result)

    def test_add_pet_fail_pet_exist(self):
        self.ps.pets = ["Gosho"]
        with self.assertRaises(Exception) as ex:
            self.ps.add_pet("Gosho")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_fail_no_pet(self):
        self.ps.food = {"apple": 10}
        with self.assertRaises(Exception) as ex:
            self.ps.feed_pet("apple", "gosho")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_fail_no_food(self):
        self.ps.pets = ["Gosho"]
        self.ps.food = {}
        result = self.ps.feed_pet("orange", "Gosho")
        self.assertEqual("You do not have orange", result)

    def test_feed_pet_fail_under_100(self):
        self.ps.pets = ["Gosho"]
        self.ps.food = {"apple": 10}
        self.assertTrue(self.ps.food["apple"] < 100)
        result = self.ps.feed_pet("apple", "Gosho")
        self.assertTrue(self.ps.food["apple"] == 1010.00)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_success(self):
        self.ps.pets = ["Gosho"]
        self.ps.food = {"apple": 1000}
        self.assertTrue(self.ps.food["apple"] >= 100)
        result = self.ps.feed_pet("apple", "Gosho")
        self.assertTrue(self.ps.food["apple"] == 900.00)
        self.assertEqual("Gosho was successfully fed", result)

    def test_repr(self):
        self.ps.pets = ["Gosho"]
        self.ps.food = {"apple": 1000}
        result = self.ps.__repr__()
        print(result)
        self.assertEqual("Shop PS1:\nPets: Gosho", result)

if __name__ == '__main__':
    main()
