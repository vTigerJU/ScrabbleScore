"""Unit test module for scrabble"""
import unittest
from unittest.mock import patch
import tkinter as tk
from scrabble import Scrabble


class MyTestCase(unittest.TestCase):
    """Unit test class"""
    def setUp(self):
        """Sets up application"""
        self.root = tk.Tk()
        self.game = Scrabble(self.root)

    def tearDown(self):
        """Closes application"""
        self.root.destroy()

    def test_intial_state(self):
        """Test pre game state"""
        self.assertEqual(0, self.game.score)
        self.assertFalse(self.game.timer_running)
        self.assertFalse(self.game.playing_game)

    def test_update_score(self):
        """Test update the displayed score"""
        self.assertEqual(0, self.game.score)
        self.game.update_score(10)
        self.assertEqual(10, self.game.score)

    @patch('tkinter.messagebox.showwarning')
    def test_check_word(self, mock_showwarning):
        """Test checking user input"""
        self.game.score = 0
        self.game.entry.insert(0, "Hello")
        self.game.amount_characters = 5
        self.game.check_word()
        self.assertEqual("", self.game.entry.get())
        self.assertEqual(8, self.game.score)
        self.game.entry.insert(0, "He")
        self.game.amount_characters = 5
        self.game.check_word()
        self.assertEqual(8, self.game.score)
        mock_showwarning.return_value = "ok"

    def test_reset_timer(self):
        """Test reset timer"""
        self.game.time_left = 10
        self.game.reset_timer()
        self.assertEqual(15, self.game.time_left)

    @patch('tkinter.messagebox.showinfo')
    def test_finish_game(self, mock_showinfo):
        """Test finished game"""
        self.game.score = 60
        self.game.round = 10
        self.game.finish_game()
        mock_showinfo.return_value = "ok"
        self.assertEqual(0, self.game.score)
        self.assertEqual(0, self.game.round)
        self.assertFalse(self.game.playing_game)


if __name__ == "__main__":
    unittest.main()
