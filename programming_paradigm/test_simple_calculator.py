import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(2, 0), 2)
        self.assertEqual(self.calc.add(-4, -2), -2)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(9, 3), 6)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(2, 0), 2)
        self.assertEqual(self.calc.subtract(4, -2), 6)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(-5. -5), 0)
        self.assertEqual(self.calc.subtract(5, 7), -2)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(3, 0), 0)
        self.assertEqual(self.calc.multiply(-4, 2), -8)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(2, 0), None)
        self.assertEqual(self.calc.divide(-4, -2), 2)
        self.assertEqual(self.calc.divide(-4, 2), -2)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
        # self.assertEqual(self.calc.divide(2, 3), 1.67)
    
