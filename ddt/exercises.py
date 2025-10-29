# -*- coding: utf-8 -*-
"""Functions and data"""

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
