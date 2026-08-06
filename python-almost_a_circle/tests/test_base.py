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
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id(self):
        """Test Base(89) saving the ID passed."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])


if __name__ == "__main__":
    unittest.main()
