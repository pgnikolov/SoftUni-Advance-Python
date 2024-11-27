from collections import deque

from project.railway_station import RailwayStation
from unittest import TestCase, main


class TestRailwayStation(TestCase):
    def setUp(self):
        self.rw = RailwayStation('Station')

    def test__init__(self):
        self.assertEqual(self.rw.name, "Station")
        self.assertEqual(self.rw.arrival_trains,deque([]))
        self.assertEqual(self.rw.departure_trains,deque([]))

    def test_name_setter_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.rw.name = "St"
        self.assertEqual(str(ex.exception), "Name should be more than 3 symbols!")

    def test_new_arrival_on_board(self):
        self.rw.new_arrival_on_board('Train1')
        self.assertEqual(self.rw.arrival_trains, deque(['Train1']))

    def test_train_has_arrived_not_first(self):
        self.rw.arrival_trains.append('Train1')
        self.rw.arrival_trains.append('Train2')
        self.assertEqual(self.rw.arrival_trains, deque(['Train1', 'Train2']))
        result = self.rw.train_has_arrived('Train2')
        expected = "There are other trains to arrive before Train2."
        self.assertEqual(result, expected)

    def test_train_has_arrived_will_depart(self):
        self.rw.arrival_trains.append('Train1')
        self.rw.arrival_trains.append('Train2')
        self.assertEqual(self.rw.arrival_trains, deque(['Train1', 'Train2']))
        result = self.rw.train_has_arrived('Train1')
        expected = "Train1 is on the platform and will leave in 5 minutes."
        self.assertEqual(result, expected)
        self.assertEqual(self.rw.departure_trains, deque(['Train1']))
        self.assertEqual(self.rw.arrival_trains, deque(['Train2']))

    def test_train_has_left_false1(self):
        self.assertFalse(self.rw.train_has_left('Train1'), True)

    def test_train_has_left_false2(self):
        self.rw.departure_trains.append('Train1')
        self.rw.departure_trains.append('Train2')
        self.assertEqual(self.rw.departure_trains, deque(['Train1', 'Train2']))
        self.assertFalse(self.rw.train_has_left('Train2'), True)

    def test_train_has_left_true(self):
        self.rw.departure_trains.append('Train1')
        self.rw.departure_trains.append('Train2')
        self.assertEqual(self.rw.departure_trains, deque(['Train1', 'Train2']))
        self.assertTrue(self.rw.train_has_left('Train1'), True)
        self.assertEqual(self.rw.departure_trains, deque(['Train2']))


if __name__ == '__main__':
    main()