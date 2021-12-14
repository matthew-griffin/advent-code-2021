import io
import unittest
from unittest import mock

from src.day_13 import calcDotsAfterFirstFold, getFoldedOutput

EXAMPLE_INPUT = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


class TestDay13(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_13.open', return_value=fake_file, create=True):
            self.assertEqual(17, calcDotsAfterFirstFold("test.txt"))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_13.open', return_value=fake_file, create=True):
            self.assertEqual("""
#####
#...#
#...#
#...#
#####""", getFoldedOutput("test.txt"))
