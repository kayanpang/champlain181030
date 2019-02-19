import unittest

from addingMachine import *
class Tests(unittest.TestCase):
    def test_add_integers(self):
        num1 = 2
        num2 = 3
        expectedResult = 5
        result = add(num1, num2)

        """this is act"""
        self.assertEqual(result, expectedResult)
        # use self because we are taking from the class itself

    def test_add_floats(self):
        num1 = 2.0
        num2 = 3.0
        expectedResult = 5.0
        result = add(num1, num2)

        """this is act"""
        self.assertEqual(result, expectedResult)