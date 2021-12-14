import io
import unittest
from unittest import mock

from src.day_12 import calcNumPaths, calcNumPathsRepeatSmallCave

EXAMPLE_INPUT = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


class TestDay12(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_12.open', return_value=fake_file, create=True):
            self.assertEqual(10, calcNumPaths("test.txt"))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_12.open', return_value=fake_file, create=True):
            self.assertEqual(36, calcNumPathsRepeatSmallCave("test.txt"))
