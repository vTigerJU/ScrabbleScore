from scrabble import Scrabble
import unittest
from unittest import mock


class MyTestCase(unittest.TestCase):
    scrabble = Scrabble()

    @mock.patch('scrabble.input', create=True)
    def test_get_bool_from_user(self, mocked_input):
        mocked_input.side_effect = ["y","aaa","n"]
        self.assertTrue(self.scrabble.get_bool_from_user("txt"))
        self.assertFalse(self.scrabble.get_bool_from_user("txt"))

   
if __name__ == "__main__":
    unittest.main()
