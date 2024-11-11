from unittest import TestCase, main
from project.train.train import Train

class TrainTests(TestCase):
    def setUp(self):
        self.train = Train("Train", 200)

    def test_train_init(self):
        self.assertEqual("Train", self.train.name)
        self.assertEqual(200, self.train.capacity)
        self.assertEqual(self.train.TRAIN_FULL, "Train is full")
        self.assertEqual(self.train.PASSENGER_NOT_FOUND, "Passenger Not Found")
        self.assertEqual(self.train.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(self.train.PASSENGER_REMOVED, "Removed {}")
        self.assertEqual(self.train.ZERO_CAPACITY, 0)

    def test_train_add_passenger_fail_train_full(self):
        self.train.capacity = 1
        self.train.passengers = ["Peter"]
        self.assertTrue(self.train.capacity==len(self.train.passengers))
        with self.assertRaises(ValueError) as ex:
            self.train.add("George")
        self.assertEqual(self.train.TRAIN_FULL, str(ex.exception))

    def test_train_add_passenger_exists_fail(self):
        self.train.passengers = ["Peter"]
        with self.assertRaises(ValueError) as ex:
            self.train.add("Peter")
        self.assertEqual(self.train.PASSENGER_EXISTS.format("Peter"), str(ex.exception))

    def test_train_add_passenger_success(self):
        result = self.train.add("Peter")
        self.assertEqual(["Peter"], self.train.passengers)
        self.assertEqual("Added passenger Peter", result)

    def test_train_remove_passenger_success(self):
        self.train.passengers = ["Peter"]
        result = self.train.remove("Peter")
        self.assertEqual([], self.train.passengers)
        self.assertEqual(self.train.PASSENGER_REMOVED.format("Peter"), result)

    def test_train_remove_passenger_not_found_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("George")
        self.assertEqual(self.train.PASSENGER_NOT_FOUND, str(ex.exception))


if __name__ == '__main__':
    main()