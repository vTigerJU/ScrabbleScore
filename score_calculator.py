"""Module to calculate scrabble score"""


class ScoreCalculator():  # pylint: disable = too-few-public-methods
    """Score calculator class"""

    letter_score = {1: {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"},
                   2: {"D", "G"},
                   3: {"B", "C", "M", "P"},
                   4: {"F", "H", "V", "W", "Y"},
                   5: {"K"},
                   8: {"J", "X"},
                   10: {"Q", "Z"}}

    key_values = [1, 2, 3, 4, 5, 8, 10]

    def calculate(self, word):
        """Calculates score of given word"""
        score = 0
        word = word.upper()
        
        for letter in word:
            for key in self.key_values:
                if letter in self.letter_score[key]:
                    score += key
        return score
