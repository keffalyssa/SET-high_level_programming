#!/usr/bin/python3
"""Defines unittests for models/base.py."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing the Base class."""

    def test_nb_instance(self):
        """Test Base() for assigning automatically an ID."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id(self):
        """Test custom ID assignment."""
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_to_json_string(self):
        """Test to_json_string static method."""
        self.assertEqual(Base.to_json_string(None), "[]")


if __name__ == "__main__":
    unittest.main()
