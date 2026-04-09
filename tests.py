import unittest
import main

class TestOnlineStore(unittest.TestCase):

    def setUp(self):
        self.user = main.User(1, "denis", "1234")
        self.product1 = main.Product(1, "Laptop", 1000)
        self.product2 = main.Product(2, "Mouse", 50)
        self.order = main.Order(1)

    # 1
    def test_user_registration(self):
        self.assertEqual(self.user.register(), "User denis registered")

    # 2
    def test_login_success(self):
        self.assertTrue(self.user.login("1234"))

    # 3
    def test_login_fail(self):
        self.assertFalse(self.user.login("wrong"))

    # 4
    def test_add_product(self):
        self.order.add_product(self.product1)
        self.assertIn(self.product1, self.order.products)

    # 5
    def test_remove_product(self):
        self.order.add_product(self.product1)
        self.order.remove_product(self.product1)
        self.assertNotIn(self.product1, self.order.products)

    # 6
    def test_calculate_total_single(self):
        self.order.add_product(self.product1)
        self.assertEqual(self.order.calculate_total(), 1000)

    # 7
    def test_calculate_total_multiple(self):
        self.order.add_product(self.product1)
        self.order.add_product(self.product2)
        self.assertEqual(self.order.calculate_total(), 1050)

    # 8
    def test_user_add_order(self):
        self.user.add_order(self.order)
        self.assertIn(self.order, self.user.orders)

    # 9
    def test_user_view_orders(self):
        self.user.add_order(self.order)
        self.assertEqual(self.user.view_orders(), [self.order])

    # 10 (взаємодія)
    def test_user_places_order(self):
        self.order.add_product(self.product1)
        self.user.add_order(self.order)

        self.assertEqual(len(self.user.orders), 1)
        self.assertEqual(self.user.orders[0].calculate_total(), 1000)


if __name__ == "__main__":
    unittest.main()