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
    Create a simple calculator that takes a String and returns a integer
    """
    result = ""
    error = None

    if not nums:
        parts = []
    else:
        cleaned_nums = nums.replace(" ", "")
        parts = cleaned_nums.split(",")

    if len(parts) == 0:
        result = "0"
    else:
        if len(parts) > 2:
            error = "To many numbers in the string. Max 2 numbers"
        else:
            parsed_numbers = []
            for part in parts:
                if not part:
                    error = "Invalid input. Only numbers accepted"
                    break

                if not re.fullmatch(r"\d+", part):
                    error = "Invalid input. Only numbers accepted"
                    break

                parsed_numbers.append(int(part))

            if error is None:
                if len(parsed_numbers) == 0:
                    error = "Invalid input. Only numbers accepted"
                elif len(parsed_numbers) == 1:
                    result = str(parsed_numbers[0])
                else:
                    result = str(sum(parsed_numbers))

    final = error if error is not None else result
    return final
