import io
import unittest
from unittest import mock

from src.day_02 import calcPositionProduct, calcCourseProduct

EXAMPLE_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

class TestDay02(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_02.open', return_value=fake_file, create=True):
            self.assertEqual(150, calcPositionProduct("test.txt"))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_02.open', return_value=fake_file, create=True):
            self.assertEqual(900, calcCourseProduct("test.txt"))