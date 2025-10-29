# -*- coding: utf-8 -*-
"""
Data driven tests
"""
# pylint: disable=import-error, missing-function-docstring, missing-class-docstring, unused-import

import unittest
from unittest.mock import Mock

from exercises import CITY_DATABASE, Account, scan_barcode, search_city

from ddt import data, ddt, unpack


@ddt
class TestSearchCity(unittest.TestCase):
    """
    Test cases for search_city
    """

    @data(
        ("Pa", ["Paris"]),
        ("par", ["Paris"]),
        ("V", []),
        ("va", ["Valencia", "Vancouver"]),
        ("xyz", []),
        ("*", CITY_DATABASE),
    )
    @unpack
    def test_search_city(self, search_text, expected_result):
        """
        Tests for search city function
        """
        result = search_city(search_text)
        self.assertEqual(sorted(result), sorted(expected_result))


@ddt
class TestScanBarcode(unittest.TestCase):
    """
    Test cases for the ScanBarcode.
    """

    @data(
        ("12345", "$7.25"),
        ("23456", "$12.50"),
        ("99999", "Error: barcode not found"),
        ("", "Error: empty barcode"),
        (None, "Error: empty barcode"),
    )
    @unpack
    def test_single_barcode(self, barcode, expected):
        """
        test single barcode
        """
        result = scan_barcode(barcode)
        self.assertEqual(result, expected)

    @data(
        (["12345", "23456"], "Total: $19.75"),
        (["23456", "12345", "12345"], "Total: $27.00"),
        (["12345", "99999"], "Error: barcode not found"),
        (["", "12345"], "Error: empty barcode"),
        ([], "Error: empty barcode"),
    )
    @unpack
    def test_multiple_barcodes(self, barcodes, expected):
        """
        test multiple barcodes
        """
        result = scan_barcode(barcodes)
        self.assertEqual(result, expected)


@ddt
class TestAccount(unittest.TestCase):

    def setUp(self):
        self.mock_printer = Mock()
        self.account = Account(self.mock_printer)

    @data(
        # deposit
        ([(1000, "10/01/2023")], [], 1000),
        # deposit and withdrawal
        ([(1000, "10/01/2023")], [(500, "14/01/2023")], 500),
        # many movements
        ([(1000, "10/01/2023"), (2000, "13/01/2023")], [(500, "14/01/2023")], 2500),
    )
    @unpack
    def test_balance_after_transactions(self, deposits, withdrawals, expected_balance):
        """
        test balance
        """
        # deposits
        for amount, date in deposits:
            self.account.deposit(amount, date)

        # withdrawals
        for amount, date in withdrawals:
            self.account.withdraw(amount, date)

        self.assertEqual(self.account.balance, expected_balance)

    def test_transactions_are_recorded_correctly(self):
        """
        test recording
        """
        self.account.deposit(1000, "10/01/2023")
        self.account.withdraw(200, "11/01/2023")

        expected = [
            ("10/01/2023", 1000, 1000),
            ("11/01/2023", -200, 800),
        ]
        self.assertEqual(self.account.transactions, expected)

    def test_print_statement_format(self):
        """
        test print
        """
        self.account.deposit(1000, "10/01/2023")
        self.account.deposit(2000, "13/01/2023")
        self.account.withdraw(500, "14/01/2023")

        self.account.print_statement()

        self.mock_printer.print_line.assert_any_call("DATE       | AMOUNT  | BALANCE")

        expected_calls = [
            ("14/01/2023 | -500.00 | 2500.00",),
            ("13/01/2023 | 2000.00 | 3000.00",),
            ("10/01/2023 | 1000.00 | 1000.00",),
        ]
        self.mock_printer.print_line.assert_has_calls(
            [unittest.mock.call(*args) for args in expected_calls], any_order=False
        )


if __name__ == "__main__":
    unittest.main()
