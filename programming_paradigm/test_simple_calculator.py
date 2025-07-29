# test_simple_calculator.py
"""
Unit tests for the SimpleCalculator class.

Run with:
    python -m unittest test_simple_calculator.py
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Comprehensive tests for all SimpleCalculator operations."""

    def setUp(self):
        """Create a fresh calculator for each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition ----------
    def test_addition_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 4), 3)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
        self.assertAlmostEqual(self.calc.add(-1.2, -3.8), -5.0)

    # ---------- Subtraction ----------
    def test_subtraction_integers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(-2, -3), 1)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # ---------- Multiplication ----------
    def test_multiplication_integers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(0, 99), 0)

    def test_multiplication_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)

    # ---------- Division ----------
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(5, 0))

    def test_division_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_negative(self):
        self.assertEqual(self.calc.divide(-8, -2), 4)
        self.assertEqual(self.calc.divide(-8, 2), -4)


if __name__ == "__main__":
    unittest.main()
