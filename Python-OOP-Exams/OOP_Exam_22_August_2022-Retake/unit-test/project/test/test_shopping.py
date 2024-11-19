from project.shopping_cart import ShoppingCart
from unittest import TestCase, main

class ShoppingCartTests(TestCase):

    def setUp(self) -> None:
        self.cart_empty = ShoppingCart("EmptyCart", 100.2)
        self.cart_with_removals = ShoppingCart("RemovalCart", 100.2)
        self.cart_with_items = ShoppingCart("ItemCart", 1220.2)
        self.cart_with_items.add_to_cart("Apple", 10.34)
        self.cart_with_items.add_to_cart("ZebraToy", 50.322)
        self.cart_with_removals.add_to_cart("Apple", 27.34)
        self.cart_with_removals.add_to_cart("Apple", 37.34)
        self.cart_with_removals.add_to_cart("EnergyDrink", 99.99999999999)
        self.combined_cart = self.cart_with_removals + self.cart_with_items

    def test_initialization(self):
        self.assertEqual(100.2, self.cart_empty.budget)
        self.assertEqual("EmptyCart", self.cart_empty.shop_name)
        self.assertEqual({}, self.cart_empty.products)

    def test_invalid_shop_name_start(self):
        with self.assertRaises(ValueError) as exc:
            ShoppingCart("invalid", 10)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(exc.exception))

    def test_invalid_shop_name_non_alpha(self):
        with self.assertRaises(ValueError) as exc:
            ShoppingCart("Shop123", 10)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(exc.exception))

    def test_invalid_shop_name_spaces(self):
        with self.assertRaises(ValueError) as exc:
            ShoppingCart("My Shop", 10)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(exc.exception))

    def test_adding_items_to_cart(self):
        msg1 = self.cart_empty.add_to_cart("Apple", 27.34)
        self.assertEqual({'Apple': 27.34}, self.cart_empty.products)
        msg2 = self.cart_empty.add_to_cart("Apple", 37.34)
        msg3 = self.cart_empty.add_to_cart("EnergyDrink", 99.99999999999)
        self.assertEqual("Apple product was successfully added to the cart!", msg1)
        self.assertEqual("Apple product was successfully added to the cart!", msg2)
        self.assertEqual("EnergyDrink product was successfully added to the cart!", msg3)
        self.assertEqual({'Apple': 37.34, 'EnergyDrink': 99.99999999999}, self.cart_empty.products)

    def test_adding_expensive_item(self):
        with self.assertRaises(ValueError) as exc:
            self.cart_empty.add_to_cart("LuxuryGift", 200)
        self.assertEqual("Product LuxuryGift cost too much!", str(exc.exception))

    def test_removing_nonexistent_item(self):
        with self.assertRaises(ValueError) as exc:
            self.cart_empty.remove_from_cart("Apple")
        self.assertEqual("No product with name Apple in the cart!", str(exc.exception))

    def test_removing_item_correctly(self):
        self.assertEqual({'Apple': 37.34, 'EnergyDrink': 99.99999999999}, self.cart_with_removals.products)
        msg1 = self.cart_with_removals.remove_from_cart("EnergyDrink")
        self.assertEqual({'Apple': 37.34}, self.cart_with_removals.products)
        self.assertEqual("Product EnergyDrink was successfully removed from the cart!", msg1)
        msg2 = self.cart_with_removals.remove_from_cart("Apple")
        self.assertEqual({}, self.cart_with_removals.products)
        self.assertEqual("Product Apple was successfully removed from the cart!", msg2)

    def test_combining_carts(self):
        merged_cart = self.cart_with_removals + self.cart_with_items
        self.assertEqual("RemovalCartItemCart", merged_cart.shop_name)
        self.assertEqual(1320.4, merged_cart.budget)
        self.assertEqual({'Apple': 10.34, 'EnergyDrink': 99.99999999999, 'ZebraToy': 50.322}, merged_cart.products)

    def test_buying_items(self):
        msg1 = self.cart_empty.buy_products()
        msg2 = self.combined_cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 0.00lv.", msg1)
        self.assertEqual("Products were successfully bought! Total cost: 160.66lv.", msg2)

    def test_buying_over_budget(self):
        with self.assertRaises(ValueError) as exc:
            self.cart_with_removals.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 37.14lv!", str(exc.exception))

if __name__ == '__main__':
    main()