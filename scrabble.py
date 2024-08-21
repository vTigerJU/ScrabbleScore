"""Scrabble game"""

import random
import time
from input_handler import InputHandler
from score_calculator import ScoreCalculator


class Scrabble():
    """Python Scrabble class"""

    input_handler = InputHandler()
    score_calculator = ScoreCalculator()

    def get_bool_from_user(self, statement):
        """Gets yes or no answer from user"""

        while True:
            print(statement, " (y,n)")
            ans = input()
            if ans == "y":
                return True
            if ans == "n":
                return False
            print("Answer y or n")

    def get_word(self, statement, length):
        """Gets word guess from user"""

        correct_input = False
        word = ""
        start_time = time.time()
        end_time = start_time + 15
        while time.time() < end_time and correct_input is not True:
            print(statement)
            word = input()
            correct_input = self.input_handler.is_correct_input(word, length)
            if correct_input is False:
                print("Enter an existing word only using letters")
                word = ""
            if time.time() > end_time:
                print("You answered too slow")
                word = "" 
        word = word.upper()
        return word

    def play_round(self):
        """Play one round of scrabble score"""

        length = random.randrange(2, 8)
        word = self.get_word(f"Write a {length} character long word", length)
        return self.score_calculator.calculate(word)

    def play_game(self):
        """Play complete game of scrabble score"""

        score = 0
        print("Welcome to scrabble! Each round you have 15 seconds to answer")
        for _ in range(10):
            score += self.play_round()
            if self.get_bool_from_user("Play another round?") is False:
                break
        print("Your score is ", score)


if __name__ == "__main__":
    scrabble = Scrabble()
    scrabble.play_game()
