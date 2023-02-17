import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self): # need to start with "test_xxx"
        self.assertEqual(calc.add(10, 50), 60)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self): # need to start with "test_xxx"
        self.assertEqual(calc.subtract(10, 50), -40)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self): # need to start with "test_xxx"
        self.assertEqual(calc.multiply(10, 50), 500)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self): # need to start with "test_xxx"
        self.assertEqual(calc.divide(50, 10), 5)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        #1. not recommended
        # self.assertRaises(ValueError, calc.divide, 10, 0) # Expect, func, each arguments for func
        #2. 
        with self.assertRaises(ValueError):
            calc.divide(10, 0)
        




if __name__ == "__main__":
    unittest.main()