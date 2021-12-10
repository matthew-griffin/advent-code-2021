import io
import unittest
from unittest import mock

from src.day_10 import calcSyntaxErrorScore, calcMiddleCompleteScore

EXAMPLE_INPUT = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


class TestDay10(unittest.TestCase):

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_10.open', return_value=fake_file, create=True):
            self.assertEqual(26397, calcSyntaxErrorScore("test.txt"))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_10.open', return_value=fake_file, create=True):
            self.assertEqual(288957, calcMiddleCompleteScore("test.txt"))
