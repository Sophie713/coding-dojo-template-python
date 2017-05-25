import unittest
from src.dojo import Dojo

"""
Call "python -m tests.example" while being in parent directory to run tests in this file.
"""


class ExampleTest(unittest.TestCase):
    def setUp(self):
        """ This method will be called *before* each test run. """
        pass

    def tearDown(self):
        """ This method will be called *after* each test run. """
        pass

    def test_example(self):
        dojo = Dojo()
        self.assertEqual(dojo.get_random_number(), 4)

if __name__ == '__main__':
    unittest.main()
