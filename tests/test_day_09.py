import io
import unittest
from unittest import mock

from src.day_09 import sumRiskLevels, calcBasinAreaProduct

EXAMPLE_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678"""


class TestDay09(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_09.open', return_value=fake_file, create=True):
            self.assertEqual(15, sumRiskLevels("test.txt"))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_09.open', return_value=fake_file, create=True):
            self.assertEqual(1134, calcBasinAreaProduct("test.txt"))
