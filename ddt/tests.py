# -*- coding: utf-8 -*-
"""
Data driven tests
"""
import unittest
from unittest.mock import Mock

from exercises import CITY_DATABASE, Account, scan_barcode, search_city


class TestSearchCity(unittest.TestCase):
    """
    Test cases for search_city
    """

    test_data = [
        ("a", []),
        ("P", []),
        ("Va", ["Valencia", "Vancouver"]),
        ("va", ["Valencia", "Vancouver"]),
        ("VAN", ["Vancouver"]),
        ("ro", ["Rotterdam", "Rome"]),
        ("BUDA", ["Budapest"]),
        ("ape", ["Budapest"]),
        ("ong", ["Hong Kong"]),
        ("city", ["New York City"]),
        ("*", CITY_DATABASE),
        ("Zzz", []),
        ("budas", []),
    ]


def generate_search_test(query, expected_result):
    """
    Generate dinamically a test for search_city
    """

    def test(self):
        self.assertEqual(search_city(query), expected_result)

    return test


for i, (search, expected) in enumerate(TestSearchCity.test_data, start=1):
    test_name = f"test_run_data_driven_{i:02d}_{search.replace('*', 'all')}"
    setattr(TestSearchCity, test_name, generate_search_test(search, expected))


class TestPointOfSale(unittest.TestCase):
    """
    Test cases for the Point of Sale.
    """

    test_data = [
        ("12345", "$7.25"),
        ("23456", "$12.50"),
        ("99999", "Error: barcode not found"),
        ("", "Error: empty barcode"),
        (None, "Error: empty barcode"),
        (["12345", "23456"], "Total: $19.75"),
        (["12345", "99999"], "Error: barcode not found"),
        ([], "Error: empty barcode"),
    ]


def generate_pos_test(value, expected_result):
    """
    Create dinamically a test for scan_barcode
    """

    def test(self):
        self.assertEqual(scan_barcode(value), expected_result)

    return test


for i, (input_value, expected) in enumerate(TestPointOfSale.test_data, start=1):
    test_name = f"test_point_of_sale_{i:02d}"
    setattr(TestPointOfSale, test_name, generate_pos_test(input_value, expected))


class TestBankAccount(unittest.TestCase):
    """
    Tests for Account kata
    """

    def setUp(self):
        """Excutes before each test"""
        self.printer = Mock()
        self.account = Account(self.printer)

    transaction_data = [
        ("deposit", 1000, "01/04/2014", 1000),
        ("withdraw", 100, "02/04/2014", 900),
        ("deposit", 500, "10/04/2014", 1400),
    ]

    def test_transactions_data_driven(self):
        """Tests deposits and take outs"""
        for operation, amount, date, expected_balance in self.transaction_data:
            with self.subTest(operation=operation, amount=amount):
                if operation == "deposit":
                    self.account.deposit(amount, date)
                else:
                    self.account.withdraw(amount, date)
                self.assertEqual(self.account.balance, expected_balance)

    def test_print_statement(self):
        """
        Tests printing account status
        """
        self.account.deposit(1000, "01/04/2014")
        self.account.withdraw(100, "02/04/2014")
        self.account.deposit(500, "10/04/2014")

        self.account.print_statement()

        expected_calls = [
            ("DATE       | AMOUNT  | BALANCE",),
            ("10/04/2014 | 500.00 | 1400.00",),
            ("02/04/2014 | -100.00 | 900.00",),
            ("01/04/2014 | 1000.00 | 1000.00",),
        ]

        actual_calls = [call.args for call in self.printer.print_line.call_args_list]
        self.assertEqual(actual_calls, expected_calls)


if __name__ == "__main__":
    unittest.main()
