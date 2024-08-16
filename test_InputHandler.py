import unittest
from InputHandler import InputHandler

class MyTestCase(unittest.TestCase):
    inputHandler = InputHandler()

    def test_toUpper(self):
        self.assertEqual("ABBA", inputHandler.toUpper("abba"))

    def test_isLetter(self):
        self.assertTrue(inputHandler.isLetter("hejsvejs"))
        self.assertFalse(inputHandler.isLetter("1"))
        self.assertFalse(inputHandler.isLetter("&"))
    
    def test_equalLength(self):
        self.assertTrue(inputHandler.equalLength(3,"abc"))
        self.assertFalse(inputHandler.equalLength(10,"abc"))

    def test_inDictionary(self):
        self.assertTrue(inputHandler.inDictionary("ape"))
        self.assertFalse(inputHandler.inDictionary("aaaaaaaa"))

    def test_isCorrectInput(self):
        self.assertTrue(inputHandler.isCorrectInput("hello", length=5))
        self.assertFalse(inputHandler.isCorrectInput("3bla#", length=10))

if __name__ == "__main__":
    unittest.main()
