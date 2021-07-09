# Test the calculator with the examples below

import unittest
from calculator import Calculator

class MyTestCase(unittest.TestCase):

    #errors
    #zero division
    def test_zero_division(self):
        input_text = "0/0"

        c = Calculator(input_text)
        self.assertEqual(c.equal_button(), "ERROR")

    #double decimals
    def test_double_decimals(self):
        input_text = "0..0 + 1"

        c = Calculator(input_text)
        self.assertEqual(c.equal_button(), "ERROR")
    
    def test_double_division(self):
        input_text = "1//20"

        c = Calculator(input_text)
        self.assertEqual(c.equal_button(), "ERROR")
    
    #test with numbers
    def test_positive_number(self):
        input_text = "1+100"

        c = Calculator(input_text)
        self.assertEqual(c.equal_button(), 101)
  
if __name__ == '__main__': 
    unittest.main()
