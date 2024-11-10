import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("Test", 10)

    def test_init(self):
        self.assertEqual(self.paint_factory.name, "Test")
        self.assertEqual(self.paint_factory.capacity, 10)
        self.assertEqual(self.paint_factory.ingredients, {})
        self.assertEqual(self.paint_factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_add_ingredient_valid(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual(self.paint_factory.ingredients, {"white": 5})

    def test_add_ingredient_invalid_type(self):
        with self.assertRaises(TypeError) as error:
            self.paint_factory.add_ingredient("purple", 5)
        self.assertEqual(str(error.exception), "Ingredient of type purple not allowed in PaintFactory")

    def test_add_ingredient_invalid_capacity(self):
        with self.assertRaises(ValueError) as error:
            self.paint_factory.add_ingredient("white", 15)
        self.assertEqual(str(error.exception), "Not enough space in factory")

    def test_remove_ingredient_valid(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.remove_ingredient("white", 2)
        self.assertEqual(self.paint_factory.ingredients, {"white": 3})

    def test_remove_ingredient_invalid_type(self):
        with self.assertRaises(KeyError) as error:
            self.paint_factory.remove_ingredient("purple", 5)
        self.assertEqual(str(error.exception), "'No such ingredient in the factory'")

    def test_remove_ingredient_invalid_quantity(self):
        self.paint_factory.add_ingredient("white", 5)
        with self.assertRaises(ValueError) as error:
            self.paint_factory.remove_ingredient("white", 10)
        self.assertEqual(str(error.exception), "Ingredients quantity cannot be less than zero")

    def test_products_property(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual(self.paint_factory.products, {"white": 5})

    def tearDown(self):
        self.paint_factory = None


if __name__ == "__main__":
    unittest.main()
