import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest
from unittest import TestCase


class TestWorker(TestCase):
    def test_init_worker(self):
        w = Worker('Test', 1000, 1000)
        self.assertEqual('Test', w.name)
        self.assertEqual(1000, w.salary)
        self.assertEqual(1000, w.energy)
        self.assertEqual(0, w.money)

    def test_rest_worker(self):
        w = Worker('Test', 1000, 0)
        self.assertEqual('Test', w.name)
        self.assertEqual(1000, w.salary)
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)
        w.rest()
        self.assertEqual(1, w.energy)

    def test_work_worker_does_not_have_enery_raises(self):
        w = Worker('Test', 0, 0)
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)

    def test_work_worker_success(self):
        w = Worker('Test', 100, 100)
        self.assertEqual('Test', w.name)
        self.assertEqual(100, w.salary)
        self.assertEqual(100, w.energy)
        self.assertEqual(0, w.money)
        w.work()
        self.assertEqual('Test', w.name)
        self.assertEqual(100, w.salary)
        self.assertEqual(99, w.energy)
        self.assertEqual(100, w.money)

    def test_get_info(self):
        w = Worker('Test', 100, 100)
        result = w.get_info()
        expected = 'Test has saved 0 money.'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
