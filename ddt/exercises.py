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
