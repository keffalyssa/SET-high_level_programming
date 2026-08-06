#!/usr/bin/python3
"""Defines unittests for models/base.py."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing the Base class."""

    def test_id(self):
        """Test automatic and manual ID assignments."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

        b4 = Base(89)
        self.assertEqual(b4.id, 89)

        b5 = Base()
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()
