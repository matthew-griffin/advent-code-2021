import unittest

from src.timer import formatTime


class TestDay02(unittest.TestCase):

    def test_format_time_seconds(self):
        self.assertEqual("1.0 seconds", formatTime(1.0))

    def test_format_time_milliseconds(self):
        self.assertEqual("1.0 milliseconds", formatTime(0.001))

    def test_format_time_microsecond(self):
        self.assertEqual("1.0 microseconds", formatTime(0.000001))

    def test_second_rounding(self):
        self.assertEqual("0.5 seconds", formatTime(0.5))
        self.assertEqual("490.0 milliseconds", formatTime(0.49))

    def test_millisecond_rounding(self):
        self.assertEqual("0.5 milliseconds", formatTime(0.0005))
        self.assertEqual("490.0 microseconds", formatTime(0.00049))