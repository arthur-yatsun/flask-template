import unittest

from parameterized import parameterized

from exceptions import CustomException
from utils import generate_sign


class TestUtils(unittest.TestCase):
    maxDiff = None

    @parameterized.expand([
        (b"test", "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"),
        (b"10.00:643:5:101qwerty", "a378886a5b81d039bb4e1f2945921d0c4a0b2d19294b7d56dab7bbdfa64fb37d"),
        (b"", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
    ])
    def test_generate_sign(self, input_data, expected):
        result = generate_sign(input_data)
        self.assertEquals(result, expected)

    def test_generate_sign_with_invalid_value(self):
        input_data = "test_value"

        with self.assertRaises(CustomException):
            generate_sign(input_data)

