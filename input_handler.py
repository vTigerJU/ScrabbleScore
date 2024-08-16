"""Module to verify user input"""
import enchant


class InputHandler():
    """Input handler class"""
    dictionary = enchant.Dict("en_US")

    def to_upper(self, word):
        """Transforms string into uppercase"""
        return word.upper()

    def is_letters(self, word):
        """Checks that string is all letters"""
        return word.isalpha()

    def equal_length(self, length, word):
        """Compares length of given word to given int"""
        return length == len(word)

    def in_dictionary(self, word):
        """Checks that string is in the english dictionary"""
        return self.dictionary.check(word)

    def is_correct_input(self, word, length):
        """Runs string throu all other methods"""
        word = self.to_upper(word)
        return (self.is_letters(word) and self.in_dictionary(word) and
                self.equal_length(length, word))
