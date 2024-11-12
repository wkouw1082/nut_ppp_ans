import unittest
from unittest.mock import patch

from user_input import UserInput


class TestUserInputW(unittest.TestCase):
    @patch("builtins.input", side_effect=["w"])
    def test_get_user_input_A_up(self, mock_input):
        expected = (0, -1)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result, f"W: expected: {expected}, result: {result}")

    @patch("builtins.input", side_effect=["a"])
    def test_get_user_input_B_left(self, mock_inpput):
        expected = (-1, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result, f"A: expected: {expected}, result: {result}")

    @patch("builtins.input", side_effect=["s"])
    def test_get_user_input_C_down(self, mock_input):
        expected = (0, 1)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["d"])
    def test_get_user_input_D_right(self, mock_input):
        expected = (1, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=[" "])
    def test_get_user_input_F_invalid(self, mock_input):
        expected = (0, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
