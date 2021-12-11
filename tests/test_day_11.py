import io
import unittest
from unittest import mock

from src.day_11 import countFlashes, countFlashesSingleStep, findFirstFullFlash

EXAMPLE_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


class TestDay11(unittest.TestCase):

    def test_single_step(self):
        grid = [
            [6,5,9,4,2,5,4,3,3,4],
            [3,8,5,6,9,6,5,8,2,2],
            [6,3,7,5,6,6,7,2,8,4],
            [7,2,5,2,4,4,7,2,5,7],
            [7,4,6,8,4,9,6,5,8,9],
            [5,2,7,8,6,3,5,7,5,6],
            [3,2,8,7,9,5,2,8,3,2],
            [7,9,9,3,9,9,2,2,4,5],
            [5,9,5,7,9,5,9,6,6,5],
            [6,3,9,4,8,6,2,6,3,7]
        ]
        self.assertEqual(35, countFlashesSingleStep(grid))
        self.assertEqual([
            [8,8,0,7,4,7,6,5,5,5],
            [5,0,8,9,0,8,7,0,5,4],
            [8,5,9,7,8,8,9,6,0,8],
            [8,4,8,5,7,6,9,6,0,0],
            [8,7,0,0,9,0,8,8,0,0],
            [6,6,0,0,0,8,8,9,8,9],
            [6,8,0,0,0,0,5,9,4,3],
            [0,0,0,0,0,0,7,4,5,6],
            [9,0,0,0,0,0,0,8,7,6],
            [8,7,0,0,0,0,6,8,4,8]
        ], grid)

    def test_first_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_11.open', return_value=fake_file, create=True):
            self.assertEqual(1656, countFlashes("test.txt"))

    def test_second_example(self):
        fake_file = io.StringIO(EXAMPLE_INPUT)
        with mock.patch('src.day_11.open', return_value=fake_file, create=True):
            self.assertEqual(195, findFirstFullFlash("test.txt"))
