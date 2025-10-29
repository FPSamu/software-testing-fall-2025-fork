# -*- coding: utf-8 -*-
"""Pruebas de búsqueda de ciudades (data-driven)."""
import unittest

from exercises import CITY_DATABASE, search_city


class TestSearchCity(unittest.TestCase):
    """Clase de pruebas unitarias para la función `search_city`."""

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


def generate_test(query, expected_result):
    """Genera dinámicamente una función de test que comprueba search_city(query)."""

    def test(self):
        self.assertEqual(search_city(query), expected_result)

    return test


for i, (search, expected) in enumerate(TestSearchCity.test_data, start=1):
    test_name = f"test_run_data_driven_{i:02d}_{search.replace('*', 'all')}"
    setattr(TestSearchCity, test_name, generate_test(search, expected))


if __name__ == "__main__":
    unittest.main()
