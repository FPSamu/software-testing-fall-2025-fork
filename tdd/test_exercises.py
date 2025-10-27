# -*- coding: utf-8 -*-

"""
Test Driven Development (TDD) tests.
"""
import unittest

from tdd.exercises import fizzbuzz, password_input_field, string_calculator


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

    def test_unknown_number_of_arguments(self):
        """
        Tests summing more than two numbers.
        """
        # Test con 3 números
        self.assertEqual(string_calculator("1,4,5"), 10)

        # Test con 5 números
        self.assertEqual(string_calculator("1,2,3,4,5"), 15)

        # Test con 4 números (incluyendo cero, para robustez)
        self.assertEqual(string_calculator("10,0,2,8"), 20)

    def test_exactly_2_numbers(self):
        """
        Tests exactly 2 numbers
        """
        self.assertEqual(string_calculator("1,5"), 6)
        self.assertEqual(string_calculator("7,9"), 16)

    def test_exactly_1_number(self):
        """
        Tests input with single number
        """
        self.assertEqual(string_calculator("5"), 5)

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

    def test_empty_number(self):
        """
        Tests no input
        """
        self.assertEqual(string_calculator(""), 0)

    def test_handle_newlines_as_separators(self):
        """
        Tests that the calculator handles newlines as valid separators.
        """
        self.assertEqual(string_calculator("1\n2"), 3)

        self.assertEqual(string_calculator("1,2\n3"), 6)
        self.assertEqual(string_calculator("1\n2\n3"), 6)

    def test_invalid_input_newline_adjacent_to_comma(self):
        """
        Tests the specific invalid input where a newline is adjacent to a comma,
        as defined by the requirement: '2,\n3' is invalid.
        """
        self.assertEqual(
            string_calculator("2,\n3"), "Invalid input. Only numbers accepted"
        )

    def test_separator_at_the_end_is_invalid(self):
        """
        Tests that an input ending with a separator (comma or newline)
        returns an error.
        """
        expected_error = "Invalid input. Only numbers accepted"

        self.assertEqual(string_calculator("1,2,"), expected_error)

        self.assertEqual(string_calculator("1\n2\n"), expected_error)

        self.assertEqual(string_calculator("5,"), expected_error)


class TestPasswordValidator(unittest.TestCase):
    """
    Test cases for test password input field validation kata
    """

    def test_valid_password_all_requirements_met(self):
        """
        Tests a password that meets ALL requirements.
        """
        self.assertEqual(password_input_field("MyP4ssw0rd!"), (True, ""))

    def test_invalid_short_password(self):
        """
        Tests a password shorter than 8 characters, only failing R1.
        """
        self.assertEqual(
            password_input_field("P12!@"),
            (False, "Password must be at least 8 characters"),
        )

    def test_invalid_less_than_two_numbers(self):
        """
        Tests a password with 1 number, only failing R2.
        """
        self.assertEqual(
            password_input_field("LongP4ssword!"),
            (False, "The password must contain at least 2 numbers"),
        )

    def test_invalid_no_capital_letter(self):
        """
        Tests a password with no capital letters, only failing R4.
        """
        self.assertEqual(
            password_input_field("longp4ssw0rd!"),
            (False, "Password must contain at least one capital letter"),
        )

    def test_invalid_no_special_character(self):
        """
        Tests a password with no special characters, only failing R5.
        """
        self.assertEqual(
            password_input_field("LongP4ssw0rd"),
            (False, "Password must contain at least one special character"),
        )

    def test_multiple_errors_length_and_numbers(self):
        """
        Tests a password failing length and numbers.
        """

        expected_length_numbers = (
            "Password must be at least 8 characters\n"
            "The password must contain at least 2 numbers\n"
            "Password must contain at least one special character"
        )
        self.assertEqual(password_input_field("Pa1"), (False, expected_length_numbers))

    def test_all_requirements_fail(self):
        """
        Tests a password that fails all four requirements.
        """
        expected_all_errors = (
            "Password must be at least 8 characters\n"
            "The password must contain at least 2 numbers\n"
            "Password must contain at least one capital letter\n"
            "Password must contain at least one special character"
        )
        self.assertEqual(password_input_field("a"), (False, expected_all_errors))
