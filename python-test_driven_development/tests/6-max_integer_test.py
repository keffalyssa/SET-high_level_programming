#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer(list=[])."""

    def test_regular_list(self):
        """Test with a normal list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max value is at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test when the list is empty."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a list containing only one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with a list containing negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of positive and negative numbers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_string(self):
        """Test with a string (treated as a list of characters)."""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["abc", "def", "xyz"]), "xyz")
