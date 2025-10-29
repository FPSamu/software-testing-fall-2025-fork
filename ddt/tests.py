# -*- coding: utf-8 -*-
"""
Data driven tests
"""
import unittest

from exercises import CITY_DATABASE, scan_barcode, search_city


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


if __name__ == "__main__":
    unittest.main()
