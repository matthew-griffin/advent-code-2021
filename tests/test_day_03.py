import io
import unittest
from unittest import mock

from src.day_03 import calcPowerUsage, calcLifeSupportRating

EXAMPLE_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

class TestDay03(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_03.open', return_value=fake_file, create=True):
            self.assertEqual(198, calcPowerUsage("test.txt"))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_03.open', return_value=fake_file, create=True):
            self.assertEqual(230, calcLifeSupportRating("test.txt"))