# -*- coding: utf-8 -*-

"""
Test Driven Development (TDD) tests.
"""
import unittest

from tdd.exercises import fizzbuzz, string_calculator


class TestFizzBuzz(unittest.TestCase):
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

    def test_fizzbuzz_should_return_number_as_string_when_number_is_not_multiple_of_3_or_5(
        self,
    ):
        """
        Tests that fizzbuzz returns the number as a string for non-multiples of 3 or 5.
        """
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(-2), "-2")

    def test_fizzbuzz_should_return_fizz_when_number_is_multiple_of_three(self):
        """
        Tests that fizzbuzz returns "Fizz" for multiples of three.
        """
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(-9), "Fizz")

    def test_fizzbuzz_should_return_buzz_when_number_is_multiple_of_five(self):
        """
        Tests that fizzbuzz returns "Buzz" for multiples of five.
        """
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")
        self.assertEqual(fizzbuzz(-20), "Buzz")

    def test_fizzbuzz_should_return_fizzbuzz_when_number_is_multiple_of_three_and_five(
        self,
    ):
        """
        Tests that fizzbuzz returns "FizzBuzz" for multiples of both three and five.
        """
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")
        self.assertEqual(fizzbuzz(-45), "FizzBuzz")


class TestStringCalculator(unittest.TestCase):
    """
    Test cases for Kata 2
    """

    def test_more_than_2_numbers(self):
        """
        Tests more than 2 numbers
        """
        self.assertEqual(
            string_calculator("1,4,5"), "To many numbers in the string. Max 2 numbers"
        )

    def test_exactly_2_numbers(self):
        """
        Tests exactly 2 numbers
        """
        self.assertEqual(string_calculator("1,5"), 6)
        self.assertEqual(string_calculator("7,9"), 16)

    def test_zero_as_input(self):
        """
        Test input with zeros
        """
        self.assertEqual(string_calculator("0"), 0)
        self.assertEqual(string_calculator("0,5"), 5)
        self.assertEqual(string_calculator("5,0"), 5)
        self.assertEqual(string_calculator("0,0"), 0)

    def test_spaces_around_comma(self):
        """
        Tests input with spaces
        """
        self.assertEqual(string_calculator(" 1 , 2 "), 3)

    def test_exactly_1_number(self):
        """
        Tests input with single number
        """
        self.assertEqual(string_calculator("5"), 5)

    def test_empty_number(self):
        """
        Tests no input
        """
        self.assertEqual(string_calculator(""), 0)
