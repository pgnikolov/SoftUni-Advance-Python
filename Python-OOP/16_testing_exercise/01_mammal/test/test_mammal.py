from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('Larry', 'dog', 'woof')

    def test_mammal_init(self):
        self.assertEqual(self.mammal.name, 'Larry')
        self.assertEqual(self.mammal.type, 'dog')
        self.assertEqual(self.mammal.sound, 'woof')
        self.assertEqual(self.mammal._Mammal__kingdom, 'animals')

    def test_mammal_make_sound(self):
        result = self.mammal.make_sound()
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        self.assertEqual(expected, result)

    def test_mammal_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_mammal_info(self):
        result = self.mammal.info()
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
