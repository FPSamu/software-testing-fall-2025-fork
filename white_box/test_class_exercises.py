# -*- coding: utf-8 -*-
"""
White-box unit testing examples.
"""
import sys
import unittest
from io import StringIO

from white_box.class_exercises import (
    BankAccount,
    BankingSystem,
    Product,
    ShoppingCart,
    TrafficLight,
    divide,
    get_grade,
    is_even,
    is_triangle,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    def test_is_triangle_no_2(self):
        """
        Checks the three inputs can't form a triangle when B is greater or equal than A + C.
        """
        self.assertEqual(is_triangle(2, 3, 1), "No, it's not a triangle.")

    def test_is_triangle_no_3(self):
        """
        Checks the three inputs can't form a triangle when A is greater or equal than B + C.
        """
        self.assertEqual(is_triangle(2, 1, 1), "No, it's not a triangle.")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        """
        Set up a new TrafficLight instance for each test.
        """
        self.traffic_light = TrafficLight()

    def test_get_state(self):
        """
        Checks if the get_current_state function works correctly.
        """
        state = self.traffic_light.get_current_state()
        self.assertEqual(state, "Red")

    def test_change_from_red(self):
        """
        Checks if the state changes from red to green correctly.
        """
        self.traffic_light.change_state()
        state = self.traffic_light.get_current_state()
        self.assertEqual(state, "Green")

    def test_change_from_green(self):
        """
        Checks if the state changes from green to yellow correctly.
        """
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        state = self.traffic_light.get_current_state()
        self.assertEqual(state, "Yellow")

    def test_change_from_yellow(self):
        """
        Checks if the state changes from yellow to red correctly.
        """
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        state = self.traffic_light.get_current_state()
        self.assertEqual(state, "Red")


class TestBankingSystem(unittest.TestCase):
    """White box test cases to test BankAccount and BankingSystem classes"""

    def setUp(self):
        self.bank = BankingSystem()
        self.bank_account = BankAccount("user123", 5000)

    def test_auth_user_valid(self):
        """Tests that a valid user with correct credentials can authenticate successfully."""
        output = StringIO()
        sys.stdout = output
        result = self.bank.authenticate("user123", "pass123")
        sys.stdout = sys.__stdout__
        self.assertEqual(
            output.getvalue(), "User user123 authenticated successfully.\n"
        )
        self.assertEqual(result, True)

    def test_auth_user_invalid_email(self):
        """Tests that authentication fails when an invalid username is provided."""
        output = StringIO()
        sys.stdout = output
        result = self.bank.authenticate("usernotvalid", "pass123")
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Authentication failed.\n")
        self.assertEqual(result, False)

    def test_auth_user_wrong_password(self):
        """Tests that authentication fails when a wrong password is provided."""
        output = StringIO()
        sys.stdout = output
        result = self.bank.authenticate("user123", "notthepassword")
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Authentication failed.\n")
        self.assertEqual(result, False)

    def test_auth_user_already_logged_in(self):
        """Tests that authentication fails when user is already logged in."""
        self.bank.authenticate("user123", "pass123")

        output = StringIO()
        sys.stdout = output
        result = self.bank.authenticate("user123", "pass123")
        sys.stdout = sys.__stdout__

        self.assertEqual(output.getvalue(), "User already logged in.\n")
        self.assertEqual(result, False)

    def test_transfer_money_sender_not_authenticated(self):
        """Tests that money transfer fails when sender is not authenticated."""
        self.assertEqual(
            self.bank.transfer_money("user123", "user2", 1000, "regular"), False
        )

    def test_transfer_money_sender_wrong_transaction_type(self):
        """Tests that money transfer fails with invalid transaction type."""
        self.bank.authenticate("user123", "pass123")
        result = self.bank.transfer_money("user123", "user2", 1000, "not valid")
        self.assertEqual(result, False)

    def test_transfer_money_sender_type_regular(self):
        """Tests successful money transfer with regular transaction type."""
        self.bank.authenticate("user123", "pass123")
        self.assertEqual(
            self.bank.transfer_money("user123", "user2", 900, "regular"), True
        )

    def test_transfer_money_sender_type_express(self):
        """Tests successful money transfer with express transaction type."""
        self.bank.authenticate("user123", "pass123")
        self.assertTrue(self.bank.transfer_money("user123", "user2", 900, "express"))

    def test_transfer_money_sender_type_scheduled(self):
        """Tests successful money transfer with scheduled transaction type."""
        self.bank.authenticate("user123", "pass123")
        self.assertTrue(self.bank.transfer_money("user123", "user2", 990, "scheduled"))

    def test_transfer_money_insufficient_funds_regular(self):
        """Tests that regular transfer fails when sender has insufficient funds."""
        self.bank.authenticate("user123", "pass123")
        self.assertFalse(self.bank.transfer_money("user123", "user2", 1000, "regular"))

    def test_transfer_money_insufficient_funds_express(self):
        """Tests that express transfer fails when sender has insufficient funds including fees."""
        self.bank.authenticate("user123", "pass123")
        self.assertFalse(
            self.bank.transfer_money("user123", "user2", 980, "express")
        )  # 980 + 49 = 1029 > 1000

    def test_transfer_money_insufficient_funds_scheduled(self):
        """Tests that scheduled transfer fails when sender has insufficient funds including fees."""
        self.bank.authenticate("user123", "pass123")
        self.assertFalse(
            self.bank.transfer_money("user123", "user2", 995, "scheduled")
        )  # 995 + 9.95 = 1004.95 > 1000

    def test_bank_account_view_account(self):
        """Tests that view_account displays correct account information."""
        output = StringIO()
        sys.stdout = output
        self.bank_account.view_account()
        sys.stdout = sys.__stdout__
        acc_number = self.bank_account.account_number
        balance = self.bank_account.balance
        self.assertEqual(
            output.getvalue(),
            f"The account {acc_number} has a balance of {balance}\n",
        )


class TestWhiteBoxProduct(unittest.TestCase):
    """White-box tests for the Product class methods."""

    def test_product_initialization(self):
        """Checks if the Product object is initialized correctly."""
        product = Product("Laptop", 1200.00)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 1200.00)

    def test_view_product(self):
        """Checks the output message of the view_product method."""
        product = Product("Keyboard", 75.50)
        expected_msg = "The product Keyboard has a price of 75.5"
        self.assertEqual(product.view_product(), expected_msg)


class TestWhiteBoxShoppingCart(unittest.TestCase):
    """White-box tests for the ShoppingCart class, focusing on state and logic."""

    def setUp(self):
        """Set up a new ShoppingCart and Products before each test."""
        self.cart = ShoppingCart()
        self.product_a = Product("Shirt", 50.00)
        self.product_b = Product("Pants", 80.00)

    def test_cart_initialization(self):
        """Checks if the shopping cart is initialized with an empty item list."""
        self.assertEqual(self.cart.items, [])

    def test_add_product_new_item(self):
        """Checks adding a new product to the cart."""
        self.cart.add_product(self.product_a, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product_a)
        self.assertEqual(self.cart.items[0]["quantity"], 2)

    def test_add_product_existing_item(self):
        """Checks adding a product that already exists in the cart updates the quantity."""
        self.cart.add_product(self.product_a, 1)
        self.cart.add_product(self.product_a, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 4)

    def test_add_product_multiple_items(self):
        """Checks adding multiple different products to the cart."""
        self.cart.add_product(self.product_a, 1)
        self.cart.add_product(self.product_b, 2)
        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.items[0]["product"], self.product_a)
        self.assertEqual(self.cart.items[1]["product"], self.product_b)

    def test_remove_product_reduce_quantity(self):
        """Checks removing a product reduces its quantity."""
        self.cart.add_product(self.product_a, 5)
        self.cart.remove_product(self.product_a, 2)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_exact_quantity(self):
        """Checks removing a product with exact quantity removes it from the cart."""
        self.cart.add_product(self.product_a, 3)
        self.cart.remove_product(self.product_a, 3)
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_exceeding_quantity(self):
        """Checks removing more than existing quantity removes the product from the cart."""
        self.cart.add_product(self.product_a, 2)
        self.cart.remove_product(self.product_a, 5)
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_not_in_cart(self):
        """Checks removing a product not in the cart does nothing."""
        self.cart.add_product(self.product_a, 2)
        self.cart.remove_product(self.product_b, 1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product_a)

    def test_remove_product_invalid_quantity(self):
        """Checks removing a product with zero or negative quantity does nothing."""
        self.cart.add_product(self.product_a, 2)
        self.cart.remove_product(self.product_a, 0)
        self.assertEqual(len(self.cart.items), 1)
        self.cart.remove_product(self.product_a, -3)
        self.assertEqual(len(self.cart.items), 1)

    def test_view_cart_empty(self):
        """Checks the output message of view_cart when the cart is empty."""
        captured = StringIO()
        sys.stdout = captured
        self.cart.view_cart()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue().strip(), "")

    def test_view_cart_with_items(self):
        """Checks the output message of view_cart with items in the cart."""
        self.cart.add_product(self.product_a, 2)
        self.cart.add_product(self.product_b, 1)
        expected_msg = "2 x Shirt - $100.0\n1 x Pants - $80.0"
        captured = StringIO()
        sys.stdout = captured
        self.cart.view_cart()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue().strip(), expected_msg)
