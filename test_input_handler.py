"""Unit Test for input_handler"""

import unittest
from input_handler import InputHandler


class MyTestCase(unittest.TestCase):
    """Unit Test class"""
    input_handler = InputHandler()

    def test_is_letters(self):
        """Test is letter function"""
        self.assertTrue(self.input_handler.is_letters("hejsvejs"))
        self.assertFalse(self.input_handler.is_letters("1"))
        self.assertFalse(self.input_handler.is_letters("&"))

    def test_equal_length(self):
        """Test equal length function"""
        self.assertTrue(self.input_handler.equal_length(3, "abc"))
        self.assertFalse(self.input_handler.equal_length(10, "abc"))

    def test_in_dictionary(self):
        """Test if word is in dictionary function"""
        self.assertTrue(self.input_handler.in_dictionary("APE"))
        self.assertFalse(self.input_handler.in_dictionary("aaaaaaaa"))

    def test_is_correct_input(self):
        """Test check correct input function"""
        self.assertTrue(self.input_handler.is_correct_input("hello", 5))
        self.assertFalse(self.input_handler.is_correct_input("3bla#", 10))


if __name__ == "__main__":
    unittest.main()
