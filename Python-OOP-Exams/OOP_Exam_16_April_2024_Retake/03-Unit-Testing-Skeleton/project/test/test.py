from project.restaurant import Restaurant
from unittest import TestCase, main


class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant('Test', 50)

    def test_valid_restaurant_initialization(self):
        restaurant = Restaurant("Test Restaurant", 5)
        self.assertEqual(restaurant.name, "Test Restaurant")
        self.assertEqual(restaurant.capacity, 5)
        self.assertEqual(restaurant.waiters, [])

    def test_empty_name_initialization(self):
        with self.assertRaises(ValueError) as context:
            Restaurant("   ", 5)
        self.assertEqual(str(context.exception), "Invalid name!")

    def test_set_negative_capacity(self):
        with self.assertRaises(ValueError) as ex:
            Restaurant("Testaurant", -10)
        self.assertEqual(str(ex.exception), "Invalid capacity!")

    def test_add_waiter_when_capacity_not_reached(self):
        restaurant = Restaurant("Testaurant", 5)
        result = restaurant.add_waiter("John")
        self.assertEqual(result, "The waiter John has been added.")
        self.assertIn({'name': 'John'}, restaurant.waiters)

    def test_add_waiter_full_capacity(self):
        restaurant = Restaurant("Testaurant", 1)
        restaurant.add_waiter("John")
        result = restaurant.add_waiter("Jane")
        self.assertEqual(result, "No more places!")

    def test_remove_existing_waiter(self):
        restaurant = Restaurant("Testaurant", 5)
        restaurant.add_waiter("John")
        result = restaurant.remove_waiter("John")
        self.assertEqual(result, "The waiter John has been removed.")
        self.assertNotIn({'name': 'John'}, restaurant.waiters)

    def test_get_filtered_waiters_based_on_earnings(self):
        restaurant = Restaurant("Testaurant", 5)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Jane', 'total_earnings': 200},
            {'name': 'Doe', 'total_earnings': 300}
        ]
        filtered_waiters = restaurant.get_waiters(min_earnings=150, max_earnings=250)
        expected_waiters = [{'name': 'Jane', 'total_earnings': 200}]
        self.assertEqual(filtered_waiters, expected_waiters)

    def test_get_total_earnings(self):
        restaurant = Restaurant("Testaurant", 5)
        restaurant.waiters = [
            {'name': 'John', 'total_earnings': 100},
            {'name': 'Jane', 'total_earnings': 200},
            {'name': 'Doe', 'total_earnings': 300}
        ]
        total_earnings = restaurant.get_total_earnings()
        self.assertEqual(total_earnings, 600)


if __name__ == '__main__':
    main()
