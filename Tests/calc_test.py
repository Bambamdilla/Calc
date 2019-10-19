import unittest
from calc import Calculator

class CalculatorTest(unittest.TestCase):
    Calculator = Calculator()

    def test_add(self):
        self.assertEqual(4, self.Calculator.add(2, 2))
        self.assertEqual(-2, self.Calculator.add(3, -5))
        self.assertEqual(5.2, self.Calculator.add(3, 2.2))

    def test_multiple(self):
        self.assertEqual(30, self.Calculator.multiple(5, 6))
        self.assertEqual(-30, self.Calculator.multiple(-5, 6))
        self.assertEqual(66.6, self.Calculator.multiple(3, 22.2))

    def test_subtract(self):
        self.assertEqual(2, self.Calculator.subtract(4, 2))
        self.assertEqual(-2, self.Calculator.subtract(2, 4))
        self.assertEqual(6.7, self.Calculator.subtract(10, 3.3))

    def test_divide(self):
        self.assertEqual(3, self.Calculator.divide(9, 3))
        self.assertEqual(-3, self.Calculator.divide(-9, 3))
        self.assertEqual(3.5, self.Calculator.divide(10.5, 3))
        with self.assertRaises(ZeroDivisionError):
            self.Calculator.divide(2,0)

    def test_x_and_y_are_not_numbers(self):
        self.assertRaises(ValueError, self.Calculator.add, 'two', 'three')
        self.assertRaises(ValueError, self.Calculator.add, 'two', 3)
        self.assertRaises(ValueError, self.Calculator.add, 2, 'three')
