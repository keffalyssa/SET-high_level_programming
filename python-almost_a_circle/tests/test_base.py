#!/usr/bin/python3
"""Defines unittests for models/base.py."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing the Base class methods."""

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None) exists and returns empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test Base.from_json_string("[]") exists."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string(self):
        """Test Base.from_json_string('[{"id": 89}]') exists and returns list."""
        json_str = '[{"id": 89}]'
        res = Base.from_json_string(json_str)
        self.assertIsInstance(res, list)
        self.assertEqual(res, [{"id": 89}])


if __name__ == "__main__":
    unittest.main()
