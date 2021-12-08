import io
import unittest
from unittest import mock

from src.day_05 import countOverlappingPoints

EXAMPLE_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

class TestDay05(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_05.open', return_value=fake_file, create=True):
            self.assertEqual(5, countOverlappingPoints("test.txt", False))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_05.open', return_value=fake_file, create=True):
            self.assertEqual(12, countOverlappingPoints("test.txt", True))
