from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.robot = Robot("Rob", 'Military', 20, 100)

    def test_init(self):
        self.assertEqual(self.robot.robot_id, 'Rob')
        self.assertEqual(self.robot.category, 'Military')
        self.assertEqual(self.robot.available_capacity, 20)
        self.assertEqual(self.robot.price, 100)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_category_setter_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = 'Military1'
        self.assertEqual(str(ex.exception),"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_price_setter_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -1
        self.assertEqual(str(ex.exception),"Price cannot be negative!")

    def test_hardware_upgrades_fail_(self):
        self.robot.hardware_upgrades = ['test']
        result = self.robot.upgrade('test', 20)
        expected = "Robot Rob was not upgraded."
        self.assertEqual(result, expected)

    def test_upgrade_success(self):
        result = self.robot.upgrade('test', 20)
        expected = "Robot Rob was upgraded with test."
        self.assertEqual(result, expected)
        self.assertEqual(self.robot.price, 130.0)
        self.assertEqual(self.robot.hardware_upgrades, ['test'])

    def test_update_fail_version_old(self):
        self.robot.software_updates = [1.01]
        result = self.robot.update(1.01, 10)
        expected = 'Robot Rob was not updated.'
        self.assertEqual(result, expected)

    def test_update_fail_not_enough_capacity(self):
        result = self.robot.update(1.01, 21)
        expected = 'Robot Rob was not updated.'
        self.assertEqual(result, expected)

    def test_update_success(self):
        result = self.robot.update(1.01, 10)
        expected = 'Robot Rob was updated to version 1.01.'
        self.assertEqual(result, expected)
        self.assertEqual(self.robot.software_updates, [1.01])
        self.assertEqual(self.robot.available_capacity, 10.0)

    def test__gt__1(self):
        self.robot2 = Robot('r2', 'Education', 20, 80)
        result = self.robot.__gt__(self.robot2)
        expected = 'Robot with ID Rob is more expensive than Robot with ID r2.'
        self.assertEqual(result, expected)

    def test__gt__2(self):
        self.robot2 = Robot('r2', 'Education', 20, 100)
        result = self.robot.__gt__(self.robot2)
        expected = 'Robot with ID Rob costs equal to Robot with ID r2.'
        self.assertEqual(result, expected)

    def test__gt__3(self):
        self.robot2 = Robot('r2', 'Education', 20, 120)
        result = self.robot.__gt__(self.robot2)
        expected = 'Robot with ID Rob is cheaper than Robot with ID r2.'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
