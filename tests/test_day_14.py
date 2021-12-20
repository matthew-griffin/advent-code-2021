import io
import unittest
from unittest import mock

from src.day_14 import calcElementRange

EXAMPLE_INPUT = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


class TestDay14(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_14.open', return_value=fake_file, create=True):
            self.assertEqual(1588, calcElementRange("test.txt", 10))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_14.open', return_value=fake_file, create=True):
            self.assertEqual(2188189693529, calcElementRange("test.txt", 40))
