# -*- coding: utf-8 -*-
"""Functions and data"""

from datetime import datetime

CITY_DATABASE = [
    "Paris",
    "Budapest",
    "Skopje",
    "Rotterdam",
    "Valencia",
    "Vancouver",
    "Amsterdam",
    "Vienna",
    "Sydney",
    "New York City",
    "London",
    "Bangkok",
    "Hong Kong",
    "Dubai",
    "Rome",
    "Istanbul",
]


def search_city(search_text: str) -> list[str]:
    """
    Look for cities
    """
    if search_text == "*":
        return list(CITY_DATABASE)

    if len(search_text) < 2:
        return []

    normalized_search = search_text.lower()

    results = []

    for city in CITY_DATABASE:
        normalized_city = city.lower()
        if normalized_search in normalized_city:
            results.append(city)

    return results


PRODUCT_DATABASE = {"12345": 7.25, "23456": 12.50}


def scan_barcode(barcodes):
    """
    Scan one or more bar codees and returns the price or total
    """
    if not barcodes:
        return "Error: empty barcode"

    if isinstance(barcodes, str):
        return _scan_single(barcodes)

    total = 0
    for code in barcodes:
        result = _scan_single(code)
        if "Error" in result:
            return result
        total += float(result.replace("$", ""))
    return f"Total: ${total:.2f}"


def _scan_single(barcode):
    """
    Scan an unique bars code
    """
    if not barcode:
        return "Error: empty barcode"

    if barcode not in PRODUCT_DATABASE:
        return "Error: barcode not found"

    price = PRODUCT_DATABASE[barcode]
    return f"${price:.2f}"


class Account:
    """
    Class for Kata 6
    """

    def __init__(self, printer):
        """
        Initialize the account with a balance and empty history
        """
        self.transactions = []
        self.balance = 0
        self.printer = printer

    def deposit(self, amount, date=None):
        """
        Make a deposit
        """
        date = date or datetime.now().strftime("%d/%m/%Y")
        self.balance += amount
        self.transactions.append((date, amount, self.balance))

    def withdraw(self, amount, date=None):
        """
        Take out money
        """
        date = date or datetime.now().strftime("%d/%m/%Y")
        self.balance -= amount
        self.transactions.append((date, -amount, self.balance))

    def print_statement(self):
        """
        Print the account final state
        """
        self.printer.print_line("DATE       | AMOUNT  | BALANCE")
        for date, amount, balance in reversed(self.transactions):
            self.printer.print_line(f"{date} | {amount:.2f} | {balance:.2f}")
