#!/usr/python3
"""Unit tests for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset Base nb_objects before each test if necessary."""
        Base._Base__nb_objects = 0

    def test_id_automatic(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_manual(self):
        """Test manual ID assignment."""
        b3 = Base(98)
        self.assertEqual(b3.id, 98)

    def test_to_json_string(self):
        """Test to_json_string static method."""
        d = [{"id": 1, "width": 2, "height": 3, "x": 0, "y": 0}]
        json_str = Base.to_json_string(d)
        self.assertEqual(type(json_str), str)
