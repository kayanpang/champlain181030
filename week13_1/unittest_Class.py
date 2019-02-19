import unittest
from .addingMachineClass import *
class test_adding_macine(unittest.TestCase):

    def setup(self):

        self.number1 = 2
        self.number2 = 3
        self.adding_machine_instance = AddingMachine(self.number1, self.number2)

    def class_Instantiated(self):
        self.assertIsNotNone(self.adding_machine_instance)

    def test_class_is_instance(self):
        self.assertIsInstance(self.adding_machine_instance, AddingMachine)

    def test_adding_integer(self):

        expected = 5
        result = self.adding_machine_instance.add()
        self.assertEquals(expected, result)