import unittest

from .validate_pw_complexity import *

class test_PW_Function(unittest.TestCase):
    def test_pw_long_enough_min(self):
        sample_pass = "abcd"
        expected_result = False

        result = validate_pw_complexity(sample_pass)
        self.assertEqual(expected_result, result)

    def test_pw_just_long_enough(self):
        sample_pass = "abcd"
        expected_result = False

        result = validate_pw_complexity(sample_pass)
        self.assertEqual(expected_result, result)