import unittest
from unittest.mock import patch
from user_input import UserInput


class TestUserInput(unittest.TestCase):

    @patch("builtins.input", side_effect=["w"])
    def test_get_user_input_up(self, mock_input):
        expected = (0, -1)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["a"])
    def test_get_user_input_left(self, mock_input):
        expected = (-1, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["s"])
    def test_get_user_input_down(self, mock_input):
        expected = (0, 1)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["d"])
    def test_get_user_input_right(self, mock_input):
        expected = (1, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["x"])
    def test_get_user_input_invalid(self, mock_input):
        expected = (0, 0)
        result = UserInput.get_user_input()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
