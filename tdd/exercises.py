# -*- coding: utf-8 -*-

"""
Test Driven Development (TDD) exercises.
"""

import re


def fizzbuzz(num):
    """
    Kata 1 - FizzBuzz
    FizzBuzz is one of the most famous coding exercises for beginners.
    It is a simple exercise but an excellent one to start learning the TDD flow with.

    Requirements
    1. Write a “fizzBuzz” method that accepts a number as input and returns it as a String.

    Notes:

    start with the minimal failing solution
    keep the three rules in mind and always write just sufficient enough code
    do not forget to refactor your code after each passing test
    write your assertions relating to the exact requirements
    2. For multiples of three return “Fizz” instead of the number

    3. For the multiples of five return “Buzz”

    4. For numbers that are multiples of both three and five return “FizzBuzz”.
    """
    output = ""

    if num % 3 == 0:
        output += "Fizz"

    if num % 5 == 0:
        output += "Buzz"

    if output == "":
        output = str(num)

    return output


def string_calculator(nums):
    """
    2. Allow the add method to handle an unknown number of arguments
    """
    if not nums:
        return 0

    cleaned_nums = nums.replace(" ", "")
    parts = cleaned_nums.split(",")

    parsed_numbers = []

    for part in parts:
        if not part or not re.fullmatch(r"\d+", part):
            return "Invalid input. Only numbers accepted"

        parsed_numbers.append(int(part))
    return sum(parsed_numbers)
