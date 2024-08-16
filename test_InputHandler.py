import unittest
from input_handler import InputHandler

class MyTestCase(unittest.TestCase):
    input_handler = InputHandler()

    def test_to_upper(self):
        self.assertEqual("ABBA", self.input_handler.to_upper("abba"))

    def test_is_letters(self):
        self.assertTrue(self.input_handler.is_letters("hejsvejs"))
        self.assertFalse(self.input_handler.is_letters("1"))
        self.assertFalse(self.input_handler.is_letters("&"))
    
    def test_equal_length(self):
        self.assertTrue(self.input_handler.equal_length(3,"abc"))
        self.assertFalse(self.input_handler.equal_length(10,"abc"))

    def test_in_dictionary(self):
        self.assertTrue(self.input_handler.in_dictionary("APE"))
        self.assertFalse(self.input_handler.in_dictionary("aaaaaaaa"))

    def test_is_correct_input(self):
        self.assertTrue(self.input_handler.is_correct_input("hello", length=5))
        self.assertFalse(self.input_handler.is_correct_input("3bla#", length=10))

if __name__ == "__main__":
    unittest.main()
