import io
import unittest
from unittest import mock

from src.day_07 import calcMinimumFuel1, calcMinimumFuel2

EXAMPLE_INPUT = """16,1,2,0,4,2,7,1,2,14"""


class TestDay07(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_07.open', return_value=fake_file, create=True):
            self.assertEqual(37, calcMinimumFuel1("test.txt"))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_07.open', return_value=fake_file, create=True):
            self.assertEqual(168, calcMinimumFuel2("test.txt"))
