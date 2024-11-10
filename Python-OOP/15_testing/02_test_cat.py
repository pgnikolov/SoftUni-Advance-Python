class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest
from unittest import TestCase


class TestCat(TestCase):
    def test_init_cat(self):
        c = Cat('cat')
        self.assertEqual(c.name, 'cat')
        self.assertEqual(c.fed, False)
        self.assertEqual(c.sleepy, False)
        self.assertEqual(c.size, 0)

    def test_size_increase_after_eat(self):
        c = Cat('cat')
        self.assertEqual(c.size, 0)
        self.assertFalse(c.fed)
        self.assertFalse(c.sleepy)
        c.eat()
        self.assertEqual(c.size, 1)
        self.assertTrue(c.fed)
        self.assertTrue(c.sleepy)

    def test_fed_after_eat(self):
        c = Cat('cat')
        c.fed = True
        with self.assertRaises(Exception) as ex:
            c.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_sleep_not_fed(self):
        c = Cat('cat')
        with self.assertRaises(Exception) as ex:
            c.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_sleep_after_sleep(self):
        c = Cat('cat')
        c.sleepy = True
        c.fed = True
        c.sleep()
        self.assertFalse(c.sleepy)


if __name__ == '__main__':
    unittest.main()
