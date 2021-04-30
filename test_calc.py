import unittest
import calc

class testCaseAdd(unittest.TestCase):
    def test_add(self);
        self.assertEqual(calc.add(10,5), 15)

    def test_add_2(self);
        self.assertEqual(calc.add(1,5), 6)

class testCaseSubtract(unittest.TestCase):
    def test_sub(self);
        self.assertEqual(calc.subtract(10,5), 10)

    def test_sub_2(self);
        self.assertEqual(calc.subtract((1,5), -4)

class testCaseDivide(unittest.TestCase):
    def test_divide(self);
        self.assertEqual(calc.divide(10,5), 2)

    def test_divide_2(self);
        self.assertEqual(calc.divide((6,2), 3)

class testCaseMultiply(unittest.TestCase):
    def test_mult(self);
        self.assertEqual(calc.multiply(10,5), 50)

    def test_mult_2(self);
        self.assertEqual(calc.multiply(((1,5), 5)

if __name__ == '__main__':
    unittest.main()