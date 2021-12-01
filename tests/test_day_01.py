import io
import unittest
from unittest import mock

from day_01.day_01 import countWindowedIncreases

EXAMPLE_INPUT = """199
200
208
210
200
207
240
269
260
263"""

class TestDay01(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('day_01.day_01.open', return_value=fake_file, create=True):
            self.assertEqual(7, countWindowedIncreases("test.txt", 1))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('day_01.day_01.open', return_value=fake_file, create=True):
            self.assertEqual(5, countWindowedIncreases("test.txt", 3))