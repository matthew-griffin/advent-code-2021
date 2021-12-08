import io
import unittest
from unittest import mock

from src.day_06 import calcNumFish

EXAMPLE_INPUT = """3,4,3,1,2"""

class TestDay06(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_06.open', return_value=fake_file, create=True):
            self.assertEqual(26, calcNumFish("test.txt", 18))

        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_06.open', return_value=fake_file, create=True):
            self.assertEqual(5934, calcNumFish("test.txt", 80))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_06.open', return_value=fake_file, create=True):
            self.assertEqual(26984457539, calcNumFish("test.txt", 256))
